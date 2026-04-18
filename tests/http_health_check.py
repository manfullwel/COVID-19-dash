import time

import requests


def run_healthcheck(
    base_url: str = "http://127.0.0.1:8051",
    timeout_seconds: int = 30,
    retry_interval_seconds: float = 1.0,
) -> None:
    deadline = time.time() + timeout_seconds
    last_error = None

    while time.time() < deadline:
        try:
            response = requests.get(f"{base_url}/health", timeout=5)
            if response.status_code == 200 and response.text.strip() == "OK":
                return
            last_error = RuntimeError(
                f"Healthcheck inválido: status={response.status_code}, body={response.text!r}"
            )
        except requests.RequestException as exc:
            last_error = exc
        time.sleep(retry_interval_seconds)

    raise RuntimeError(f"Falha no healthcheck após {timeout_seconds}s: {last_error}")


if __name__ == "__main__":
    run_healthcheck()
