import requests
from task import Task
from storage import save_tasks, load_tasks


def show_menu():
    print("\n=== StudyTask CLI ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("6 - Buscar endereço por CEP")


def add_task(tasks):
    title = input("Digite o título da tarefa: ").strip()

    if title == "":
        print("Título não pode ser vazio.")
        return

    task = Task(title)

    tasks.append(task)

    save_tasks(tasks)

    print("Tarefa adicionada com sucesso!")


def list_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print("\nLista de tarefas:")

    for i, task in enumerate(tasks):
        status = "✔" if task.completed else "✘"
        print(f"{i + 1}. {task.title} [{status}]")
        

def complete_task(tasks):
    if not tasks:
        print("Nenhuma tarefa para concluir.")
        return

    list_tasks(tasks)

    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index].completed = True
            save_tasks(tasks)

            print("Tarefa marcada como concluída!")

        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")
        
        
def remove_task(tasks):
    if not tasks:
        print("Nenhuma tarefa para remover.")
        return

    list_tasks(tasks)

    try:
        index = int(input("Digite o número da tarefa para remover: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)

            save_tasks(tasks)

            print(f"Tarefa '{removed.title}' removida com sucesso!")

        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")

def buscar_cep():
    cep = input("Digite o CEP: ")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        print("\n=== Endereço ===")
        print("Rua:", dados.get("logradouro"))
        print("Bairro:", dados.get("bairro"))
        print("Cidade:", dados.get("localidade"))
        print("Estado:", dados.get("uf"))
    else:
        print("Erro ao buscar CEP.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)
            
        elif choice == "4" :
            remove_task(tasks)
            
        elif choice == "5" :
            print("saindo...")
            break
        elif choice == "6":
            buscar_cep()

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()