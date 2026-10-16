# Testes Automatizados com Selenium + Behave (Gherkin) - Patrick Ataíde Portfolio

## Objetivo

Projeto de testes funcionais automatizados (incluindo BDD com Gherkin) para o site [https://www.patrickataide.com.br/](https://www.patrickataide.com.br/) utilizando Selenium + Pytest + Behave.

## Tecnologias

- [Selenium](https://www.selenium.dev/)
- [Behave](https://behave.readthedocs.io/) (BDD/Gherkin)
- Python + Pytest
- GitHub Actions (CI/CD)

## Plano de Testes

O plano de testes funcionais está disponível em `plano-testes.csv`.
Arquivos Gherkin: `features/*.feature`

## Como executar localmente

```bash
pip install -r requirements.txt
pytest tests/ -v     # testes Pytest
behave               # testes BDD/Gherkin
```

## CI/CD

Os testes (incluindo BDD) são executados automaticamente via GitHub Actions.

## Autor

Patrick Ataíde - [patrickataide.com.br](https://www.patrickataide.com.br/)
