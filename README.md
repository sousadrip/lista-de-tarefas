# ✅ Lista de Tarefas via Terminal (To-Do CLI)

Uma aplicação de linha de comando (CLI) em Python para gerenciamento de tarefas pessoais, com interface simples, interativa e **persistência de dados em JSON**.

## 🎯 Objetivo

Permitir que o usuário controle suas tarefas diretamente pelo terminal, com funcionalidades como adicionar, listar, concluir e remover tarefas — tudo salvo automaticamente.

## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `json` – Para salvar e carregar tarefas em formato `.json`
  - `os` – Para limpar o terminal e melhorar a usabilidade
  - `datetime` – Para registrar data e hora de criação das tarefas

## ✨ Funcionalidades

- **Menu interativo via terminal**
- **Adicionar tarefa:** com ID único e data/hora automática
- **Listar tarefas:** com ID, status e descrição
- **Alterar status:** marcar como concluída `[X]` ou pendente `[ ]`
- **Remover tarefa:** exclui a tarefa informando seu ID
- **Persistência de dados:** tudo salvo no arquivo `tarefas.json`
- **Carregamento automático:** tarefas salvas são recuperadas ao iniciar
- **Geração automática de IDs**
- **Limpeza de tela:** para melhor experiência no terminal

## 📂 Estrutura esperada

├── todo.py # Código principal da aplicação
├── tarefas.json # Arquivo gerado com as tarefas
└── README.md # Este arquivo

## ▶️ Como Executar

1. **Clone o repositório (ou baixe os arquivos):**
   ```bash
   git clone https://github.com/sousadrip/lista-de-tarefas
   cd lista-de-tarefas
   python todo_list_app.py
