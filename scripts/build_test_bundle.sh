#!/usr/bin/env bash
set -euo pipefail

OUTPUT_NAME="${1:-COVID-19-dash-ajustado-com-testes.zip}"

zip -r "${OUTPUT_NAME}" . \
  -x '.git/*' \
     '__pycache__/*' \
     '*.pyc' \
     '.pytest_cache/*' \
     'artifacts/*' \
     'dist/*' \
     "${OUTPUT_NAME}"

echo "Bundle gerado: ${OUTPUT_NAME}"
sha256sum "${OUTPUT_NAME}"
