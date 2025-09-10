echo "# Agenda de Contatos CLI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Uma aplicação de console (CLI) em Python para gerenciar contatos, com persistência em JSON.

O projeto permite adicionar, listar, editar, remover e buscar contatos, além de exibir os aniversariantes do dia automaticamente.

## Funcionalidades

- ✅ CRUD completo: adicionar, listar, editar e remover contatos
- ✅ Persistência de contatos em arquivo JSON (\`contatos.json\`)
- ✅ Busca de contatos por nome ou email
- ✅ Exibição de aniversariantes do dia ao iniciar
- ✅ Mensagens coloridas para sucesso, erro e alerta
- ✅ Estrutura simples e fácil de usar

## Estrutura do Projeto

\`\`\`
agenda-contatos-api/
│
├─ venv/                 # Ambiente virtual do Python
├─ src/
│   ├─ agenda.py          # Código principal da agenda
│   └─ main.py            # Ponto de entrada que chama menu()
└─ contatos.json          # Arquivo que armazena os contatos (gerado automaticamente)
\`\`\`

## Como rodar

1. Ative o ambiente virtual:

Windows CMD/PowerShell:
\`\`\`
venv\\Scripts\\activate
\`\`\`

Linux/macOS:
\`\`\`
source venv/bin/activate
\`\`\`

2. Rode o programa:
\`\`\`
python src/main.py
\`\`\`

3. Ao sair, os contatos serão salvos automaticamente no arquivo \`contatos.json\`.

4. Para sair do ambiente virtual:
\`\`\`
deactivate
\`\`\`

## Dependências

- Python 3.x  
- Bibliotecas padrão do Python (\`json\`, \`datetime\`)

## Próximos passos possíveis

- Transformar em aplicação web (Flask/Django)
- Criar interface interativa com cores e alertas avançados
- Enviar notificações de aniversário automaticamente
- Migrar a persistência de JSON para banco de dados (SQLite, PostgreSQL)

## Autor

Lucas Facini

## Licença

Este projeto está licenciado sob a licença MIT.  
" > README.md
