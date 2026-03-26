# StudyTask CLI

Um gerenciador simples de tarefas feito em Python usando linha de comando (CLI).

## Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Salvar tarefas em arquivo JSON
- Testes automáticos com unittest

## Como executar o projeto

No terminal, execute:

python src/main.py

## Como executar os testes

No terminal, execute:

python -m unittest discover tests

## Estrutura do projeto

study-task-cli/
│
├── src/
│   ├── main.py
│   ├── task.py
│   └── storage.py
│
├── tests/
│   └── test_task.py
│
├── tasks.json
└── README.md

## Tecnologias utilizadas

- Python 3
- JSON
- unittest

## Autor

Projeto desenvolvido como prática de programação em Python.