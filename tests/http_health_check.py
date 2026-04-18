import requests


def run_healthcheck(base_url: str = "http://127.0.0.1:8051") -> None:
    response = requests.get(f"{base_url}/health", timeout=5)
    if response.status_code != 200 or response.text.strip() != "OK":
        raise RuntimeError(
            f"Healthcheck inválido: status={response.status_code}, body={response.text!r}"
        )


if __name__ == "__main__":
    run_healthcheck()
