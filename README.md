# Testes Automatizados com Selenium - Patrick Ataíde Portfolio

## Objetivo

Projeto de testes funcionais automatizados para o site [https://www.patrickataide.com.br/](https://www.patrickataide.com.br/) utilizando Selenium + Pytest.

Este repositório faz parte de uma série de projetos de demonstração de ferramentas de teste (Cypress, Playwright, Selenium, Robot Framework e BDD com Cucumber).

## Tecnologias

- [Selenium](https://www.selenium.dev/)
- Python + Pytest
- GitHub Actions (CI/CD)

## Plano de Testes

O plano de testes funcionais está disponível em `plano-testes.csv`.

## Como executar localmente

### Pré-requisitos

- Python 3.11+
- pip

### Instalação

```bash
pip install -r requirements.txt
```

### Executar testes

```bash
pytest tests/ -v
```

## CI/CD

Os testes são executados automaticamente via GitHub Actions.

## Autor

Patrick Ataíde - [patrickataide.com.br](https://www.patrickataide.com.br/)
