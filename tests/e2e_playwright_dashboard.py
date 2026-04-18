import os
import subprocess
import time
from pathlib import Path

import requests
from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:8051"
SCREENSHOT_PATH = Path("artifacts/dashboard-e2e.png")


def wait_for_health(timeout_seconds: int = 60) -> None:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=2)
            if response.status_code == 200 and response.text.strip() == "OK":
                return
        except requests.RequestException:
            pass
        time.sleep(1)
    raise RuntimeError("Servidor não ficou saudável em /health dentro do tempo limite.")


def run_e2e() -> None:
    SCREENSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["PORT"] = "8051"

    server = subprocess.Popen(
        ["python", "dashboard.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
    )

    try:
        wait_for_health()

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(BASE_URL, wait_until="networkidle", timeout=120000)

            # Aguarda os gráficos principais ficarem disponíveis.
            page.wait_for_selector("#choropleth-map .js-plotly-plot", timeout=120000)
            page.wait_for_selector("#bar-chart .js-plotly-plot", timeout=120000)
            page.wait_for_selector("#mortality-chart .js-plotly-plot", timeout=120000)
            page.wait_for_selector("#line-graph .js-plotly-plot", timeout=120000)

            # Aplica filtro de UF (ex.: SP) no dcc.Dropdown.
            page.click("#location-button", timeout=30000)
            page.fill("#location-button input", "SP")
            page.keyboard.press("Enter")

            # Aguarda callback atualizar gráficos após filtro.
            page.wait_for_timeout(2500)

            # Verifica renderização de todos os gráficos após interação.
            figure_sizes = page.evaluate(
                """
                () => {
                  const ids = ["choropleth-map", "bar-chart", "mortality-chart", "line-graph"];
                  const result = {};
                  for (const id of ids) {
                    const container = document.getElementById(id);
                    const plot = container ? container.querySelector(".js-plotly-plot") : null;
                    const dataLength = plot && plot.data ? plot.data.length : 0;
                    result[id] = dataLength;
                  }
                  return result;
                }
                """
            )

            for graph_id, data_length in figure_sizes.items():
                if data_length < 1:
                    raise RuntimeError(f"Gráfico '{graph_id}' sem dados renderizados após interação E2E.")

            page.screenshot(path=str(SCREENSHOT_PATH), full_page=True)
            browser.close()
    finally:
        server.terminate()
        try:
            server.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    run_e2e()
