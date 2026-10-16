# Comandos Essenciais - Selenium + Behave (Gherkin)

## Instalação completa

```bash
pip install -r requirements.txt
```

## Rodar todos os testes Pytest

```bash
pytest tests/ -v
```

## Rodar todos os testes BDD (Behave)

```bash
behave
```

## Rodar somente um arquivo de teste Pytest

```bash
pytest tests/test_portfolio.py -v
```

## Rodar somente um arquivo .feature

```bash
behave features/portfolio.feature
```

## Rodar somente um cenário (pelo nome)

```bash
behave features/portfolio.feature --name "FT-001"
```

## Rodar somente um cenário (por tag, se adicionar tags)

```bash
behave --tags=@smoke
```

## Limpar e reinstalar

```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```
