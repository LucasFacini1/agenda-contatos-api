import json
from datetime import datetime

ARQUIVO_CONTATOS = "contatos.json"

# --- Classe Contato ---
class Contato:
    def __init__(self, nome, celular, email, data_nascimento, mensagem_aniversario):
        self.nome = nome
        self.celular = celular
        self.email = email
        self.data_nascimento = data_nascimento
        self.mensagem_aniversario = mensagem_aniversario

# --- Persistência ---
def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as arquivo:
        json.dump([c.__dict__ for c in contatos], arquivo, indent=4)
    print("\033[92m✅ Contatos salvos com sucesso!\033[0m\n")

def carregar_contatos():
    try:
        with open(ARQUIVO_CONTATOS, "r") as arquivo:
            contatos_json = json.load(arquivo)
            return [Contato(**dados) for dados in contatos_json]
    except FileNotFoundError:
        return []

# --- Funções de CRUD ---
def adicionar_contato(contatos):
    print("\n--- Adicionar Contato ---")
    nome = input("Nome: ")
    celular = input("Celular: ")
    email = input("Email: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    mensagem_aniversario = input("Mensagem de aniversário: ")
    contatos.append(Contato(nome, celular, email, data_nascimento, mensagem_aniversario))
    print(f"\033[92m✅ Contato '{nome}' adicionado!\033[0m\n")

def listar_contatos(contatos):
    if not contatos:
        print("\033[93m⚠️ Nenhum contato cadastrado.\033[0m\n")
        return
    print("\n--- Lista de Contatos ---")
    for i, c in enumerate(contatos):
        print(f"{i+1}. {c.nome} | {c.celular} | {c.email} | {c.data_nascimento} | {c.mensagem_aniversario}")
    print()

def editar_contato(contatos):
    listar_contatos(contatos)
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato que deseja editar: ")) - 1
        if 0 <= indice < len(contatos):
            c = contatos[indice]
            print("\nPressione Enter para manter o valor atual.\n")
            c.nome = input(f"Nome ({c.nome}): ") or c.nome
            c.celular = input(f"Celular ({c.celular}): ") or c.celular
            c.email = input(f"Email ({c.email}): ") or c.email
            c.data_nascimento = input(f"Data de nascimento ({c.data_nascimento}): ") or c.data_nascimento
            c.mensagem_aniversario = input(f"Mensagem de aniversário ({c.mensagem_aniversario}): ") or c.mensagem_aniversario
            print(f"\033[92m✅ Contato '{c.nome}' atualizado!\033[0m\n")
        else:
            print("\033[91m❌ Contato inválido!\033[0m\n")
    except ValueError:
        print("\033[91m❌ Entrada inválida!\033[0m\n")

def remover_contato(contatos):
    listar_contatos(contatos)
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato que deseja remover: ")) - 1
        if 0 <= indice < len(contatos):
            confirm = input(f"Tem certeza que deseja remover '{contatos[indice].nome}'? (s/n): ").lower()
            if confirm == 's':
                removido = contatos.pop(indice)
                print(f"\033[92m✅ Contato '{removido.nome}' removido!\033[0m\n")
            else:
                print("\033[93m❌ Remoção cancelada.\033[0m\n")
        else:
            print("\033[91m❌ Contato inválido!\033[0m\n")
    except ValueError:
        print("\033[91m❌ Entrada inválida!\033[0m\n")

# --- Busca ---
def buscar_contato(contatos):
    if not contatos:
        print("\033[93m⚠️ Nenhum contato cadastrado.\033[0m\n")
        return
    termo = input("Digite o nome ou email para buscar: ").lower()
    resultados = [c for c in contatos if termo in c.nome.lower() or termo in c.email.lower()]
    if resultados:
        print("\n--- Resultados da busca ---")
        for c in resultados:
            print(f"{c.nome} | {c.celular} | {c.email} | {c.data_nascimento} | {c.mensagem_aniversario}")
        print()
    else:
        print("\033[91m❌ Nenhum contato encontrado.\033[0m\n")

# --- Aniversariantes do dia ---
def aniversariantes_do_dia(contatos):
    hoje = datetime.today().strftime("%m-%d")
    aniversariantes = [c for c in contatos if c.data_nascimento[5:] == hoje]
    if aniversariantes:
        print("\n🎉 Aniversariantes de hoje:")
        for c in aniversariantes:
            print(f"{c.nome} - {c.mensagem_aniversario}")
        print()
    else:
        print("\nNenhum aniversariante hoje.\n")

# --- Menu Principal ---
def menu():
    contatos = carregar_contatos()
    aniversariantes_do_dia(contatos)
    while True:
        print("=== Agenda de Contatos ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Remover contato")
        print("5. Sair")
        print("6. Buscar contato")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            listar_contatos(contatos)
        elif escolha == "3":
            editar_contato(contatos)
        elif escolha == "4":
            remover_contato(contatos)
        elif escolha == "5":
            salvar_contatos(contatos)
            print("👋 Saindo da agenda...")
            break
        elif escolha == "6":
            buscar_contato(contatos)
        else:
            print("\033[91m❌ Opção inválida! Tente novamente.\033[0m\n")

if __name__ == "__main__":
    menu()
