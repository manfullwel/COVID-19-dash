# Roteiro de resolução de conflitos do PR (`README.md` e `tests/http_health_check.py`)

Este roteiro preserva as alterações críticas de validação profissional (smoke + health + E2E/CI).

## 1) Atualize sua branch local

```bash
git checkout <sua-branch-do-pr>
git fetch origin
git rebase origin/main
```

> Se preferir merge:
> `git merge origin/main`

## 2) Resolva conflito em `README.md`

### Manter (do PR):
- Seção **Validação rápida (smoke test)**.
- Seção **Validação profissional (HTTP + E2E Playwright)**.
- Seção **CI automatizada (GitHub Actions)**.

### Ação recomendada:
1. Abra o arquivo com conflito.
2. Remova os marcadores `<<<<<<<`, `=======`, `>>>>>>>`.
3. Preserve o bloco de validação entre as linhas da seção de desenvolvimento local e antes de “Dados e Metodologia”.

Arquivo de referência neste branch:
- `README.md` (linhas 102 a 143).

## 3) Resolva conflito em `tests/http_health_check.py`

### Manter (crítico):
- Função `run_healthcheck(...)` com:
  - `timeout_seconds`,
  - `retry_interval_seconds`,
  - loop com retry até timeout.
- Condição de sucesso:
  - status `200`
  - body `OK`.

Arquivo de referência neste branch:
- `tests/http_health_check.py` (linhas 6 a 30).

## 4) Marque conflitos como resolvidos e continue

```bash
git add README.md tests/http_health_check.py
git rebase --continue
```

> Se estiver usando merge, faça commit normal:
> `git commit`

## 5) Valide localmente antes do push

```bash
python -m unittest tests/test_dashboard_smoke.py
PORT=8051 python dashboard.py > /tmp/dashboard_ci.log 2>&1 & echo $! > /tmp/dashboard_ci.pid
python tests/http_health_check.py
kill $(cat /tmp/dashboard_ci.pid) || true
```

## 6) Envie a branch atualizada

```bash
git push --force-with-lease
```

## 7) Confirmar no GitHub

Após o push:
1. Verifique se o PR ficou sem conflitos.
2. Confira o check **dashboard-ci / Health Gate (/health)**.
3. Confira o check **dashboard-ci / E2E Gate (Playwright)** e os artifacts.
