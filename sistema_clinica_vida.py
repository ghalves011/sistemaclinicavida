#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lista para armazenar o cadastro dos pacientes
pacientes = []

def cadastrar_paciente():
  
    # Nome
    while True:
        nome = input("Digite o nome do paciente: ").strip()
        if nome.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido! Digite apenas letras.")

    # Idade
    while True:
        idade = input("Digite a idade do paciente: ")
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("Idade inválida! Digite apenas números.")

    # Telefone
    while True:
        telefone = input("Digite o telefone do paciente (apenas números, ex: 19999999999): ")
        if telefone.isdigit() and len(telefone) == 11:  # 2 dígitos do DDD + 9 dígitos
            telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            break
        else:
            print("Telefone inválido! Digite 11 números, incluindo o DDD.")

    # Cria o dicionário do paciente e adiciona na lista
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone_formatado
    }
    pacientes.append(paciente)
    print(f"Paciente {nome} cadastrado com sucesso!\n")

# Função para gerar estatísticas

def estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    idade_media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print("=== Estatísticas dos Pacientes ===")
    print(f"Número total de pacientes: {total}")
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")

# Função para buscar paciente
def buscar_paciente():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    termo = input("Digite o nome ou parte do nome do paciente: ").strip().lower()
    resultados = []

    for paciente in pacientes:
        if termo in paciente["nome"].lower():  # busca ignorando maiúsculas/minúsculas
            resultados.append(paciente)

    if resultados:
        print("Pacientes encontrados:")
        for i, paciente in enumerate(resultados, start=1):
            print(f"{i}. Nome: {paciente['nome']}, Idade: {paciente['idade']}, Telefone: {paciente['telefone']}")
    else:
        print("Nenhum paciente encontrado com esse nome.")
    print()  # linha em branco

# Função para listar pacientes
def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    print("Lista de pacientes:")
    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {paciente['nome']}, Idade: {paciente['idade']}, Telefone: {paciente['telefone']}")
    print()  # linha em branco

# Menu principal
def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar pacientes")
        print("4. Listar pacientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Executa o menu
menu()


# In[ ]:




