from banco import cursor, conexao

def agendar():
    cliente = input("Digite o nome do cliente: ")
    data = input("Digite a data (dd/mm/aaaa): ")
    horario = input("Digite o horário: ")

    cursor.execute(
        "SELECT * FROM agendamentos WHERE data = ? AND horario = ?",
        (data, horario)
    )

    horario_existente = cursor.fetchone()

    if horario_existente:
        print("Esse horário já está ocupado.")
        return

    cursor.execute(
        "INSERT INTO agendamentos (cliente, data, horario) VALUES (?, ?, ?)",
        (cliente, data, horario)
    )

    conexao.commit()

    print("Agendamento realizado com sucesso!")


def listar_agendamentos():
    cursor.execute("SELECT * FROM agendamentos")

    agendamentos = cursor.fetchall()

    if len(agendamentos) == 0:
        print("Nenhum agendamento encontrado.")
        return

    for agendamento in agendamentos:
        print(agendamento)


def cancelar_agendamento():
    id_agendamento = int(input("Digite o ID do agendamento: "))

    cursor.execute(
        "DELETE FROM agendamentos WHERE id = ?",
        (id_agendamento,)
    )

    conexao.commit()

    print("Agendamento cancelado com sucesso!")


while True:
    print("\n=== SISTEMA DE AGENDAMENTO ===")
    print("1 - Novo agendamento")
    print("2 - Listar agendamentos")
    print("3 - Cancelar agendamento")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        agendar()

    elif opcao == "2":
        listar_agendamentos()

    elif opcao == "3":
        cancelar_agendamento()

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")