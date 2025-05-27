
import json
import os
import datetime

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas(nome_arquivo):
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(nome_arquivo):
        return []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)

        for tarefa in tarefas:
            if 'id' in tarefa:
                tarefa['id'] = int(tarefa['id'])
        return tarefas
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar tarefas: {e}. Iniciando com lista vazia.")
        return []

def salvar_tarefas(tarefas, nome_arquivo):
    """Salva a lista de tarefas no arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(tarefas, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar tarefas: {e}")

def obter_proximo_id(tarefas):
    """Calcula o próximo ID disponível."""
    if not tarefas:
        return 1

    return max(tarefa.get('id', 0) for tarefa in tarefas) + 1

def limpar_terminal():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    limpar_terminal()
    print("--- Adicionar Nova Tarefa ---")
    descricao = input("Digite a descrição da tarefa: ")
    if not descricao:
        print("Descrição não pode ser vazia.")
        input("Pressione Enter para continuar...")
        return

    nova_tarefa = {
        "id": obter_proximo_id(tarefas),
        "descricao": descricao,
        "concluida": False,
        "data_criacao": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")
    input("Pressione Enter para continuar...")

def listar_tarefas(tarefas):
    """Lista todas as tarefas."""
    limpar_terminal()
    print("--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in sorted(tarefas, key=lambda t: t.get('id', 0)):
            status = "[X]" if tarefa.get('concluida', False) else "[ ]"
            print(f"{tarefa.get('id', 'N/A'):>3} {status} {tarefa.get('descricao', 'Sem descrição')}")
    print("-----------------------")
    input("Pressione Enter para continuar...")

def marcar_concluida(tarefas):
    """Marca uma tarefa como concluída ou pendente."""
    limpar_terminal()
    print("--- Marcar Tarefa como Concluída/Pendente ---")
    listar_tarefas_simples(tarefas)
    if not tarefas:
         input("Nenhuma tarefa para marcar. Pressione Enter para continuar...")
         return

    try:
        id_tarefa = int(input("Digite o ID da tarefa para alterar o status: "))
        encontrada = False
        for tarefa in tarefas:
            if tarefa.get('id') == id_tarefa:
                tarefa['concluida'] = not tarefa.get('concluida', False)
                status_str = "concluída" if tarefa['concluida'] else "pendente"
                print(f"Tarefa {id_tarefa} marcada como {status_str}.")
                encontrada = True
                break
        if not encontrada:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
    input("Pressione Enter para continuar...")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista."""
    limpar_terminal()
    print("--- Remover Tarefa ---")
    listar_tarefas_simples(tarefas)
    if not tarefas:
         input("Nenhuma tarefa para remover. Pressione Enter para continuar...")
         return

    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
        tarefa_original_len = len(tarefas)
        tarefas[:] = [tarefa for tarefa in tarefas if tarefa.get('id') != id_tarefa]

        if len(tarefas) < tarefa_original_len:
            print(f"Tarefa {id_tarefa} removida com sucesso.")
        else:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
    input("Pressione Enter para continuar...")

def listar_tarefas_simples(tarefas):
     """Função auxiliar para listar tarefas sem limpar a tela ou pausar."""
     print("\nTarefas Atuais:")
     if not tarefas:
        print("Nenhuma tarefa cadastrada.")
     else:
        for tarefa in sorted(tarefas, key=lambda t: t.get('id', 0)):
            status = "[X]" if tarefa.get('concluida', False) else "[ ]"
            print(f"{tarefa.get('id', 'N/A'):>3} {status} {tarefa.get('descricao', 'Sem descrição')}")
     print("-----------------------")

def exibir_menu():
    """Exibe o menu de opções."""
    limpar_terminal()
    print("--- Gerenciador de Tarefas Simples ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída/Pendente")
    print("4. Remover Tarefa")
    print("0. Sair")
    print("-------------------------------------")

if __name__ == "__main__":
    lista_de_tarefas = carregar_tarefas(ARQUIVO_TAREFAS)

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tarefa(lista_de_tarefas)
            salvar_tarefas(lista_de_tarefas, ARQUIVO_TAREFAS)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            marcar_concluida(lista_de_tarefas)
            salvar_tarefas(lista_de_tarefas, ARQUIVO_TAREFAS)
        elif escolha == '4':
            remover_tarefa(lista_de_tarefas)
            salvar_tarefas(lista_de_tarefas, ARQUIVO_TAREFAS)
        elif escolha == '0':
            print("Saindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

