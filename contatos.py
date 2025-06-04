def cadastrar_novo_contato(nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(f"Contato {nome} cadastrado com sucesso!")
    return

def visualizar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favorito"] else "〇"
        print(f"{indice}. {favorito} {contato['nome']} - {contato['telefone']} - {contato['email']} ")
    return

def atualizar_contato(indice, nome, telefone, email):
    indice_contato_ajustado = int(indice) - 1
    indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos)
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if not nome:
            nome = contatos[indice_contato_ajustado]["nome"]  # Mantém o nome atual se não for fornecido um novo  
        if not telefone:
            telefone = contatos[indice_contato_ajustado]["telefone"]  # Mantém o telefone atual se não for fornecido um novo
        if not email:
            email = contatos[indice_contato_ajustado]["email"]  # Mantém o email atual se não for fornecido um novo
        contatos[indice_contato_ajustado]["nome"] = nome    
        contatos[indice_contato_ajustado]["telefone"] = telefone
        contatos[indice_contato_ajustado]["email"] = email
        print(f"Contato {indice + 1} atualizado com sucesso!")
    else:
        print("Índice inválido.") 
    return

def marcar_contato_favorito(indice):
    indice_contato_ajustado = int(indice) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice + 1} marcado como favorito.")
    else:
        print("Índice inválido.")
    return

def desmarcar_contato_favorito(indice):
    indice_contato_ajustado = int(indice) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice + 1} desmarcado como favorito.")
    else:
        print("Índice inválido.")
    return

def ver_contatos_favoritos():
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(favoritos, start=1):
        print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    return

def deletar_contato(indice):
    indice_contato_ajustado = int(indice) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato_removido['nome']} deletado com sucesso!")
    else:
        print("Índice inválido.")
    return


contatos = []
while True:
  print("\nLista de contatos cadastrados:")
  print("1. Cadastrar novo contato")
  print("2. Visualizar Contatos")
  print("3. Editar Contato")
  print("4. Marcar um contato favorito")
  print("5. Desmarcar um contato favorito")
  print("6. Ver contatos favoritos")
  print("7. Deletar Contato")
  print("8. Sair")

  escolha = input("Digite o número da sua escolha: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    cadastrar_novo_contato(nome, telefone, email)

  elif escolha == "2":
    visualizar_contatos()

  elif escolha == "3":
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
    nome = input("Digite o novo nome do contato (deixe em branco para manter o atual): ")
    telefone = input("Digite o novo telefone do contato (deixe em branco para manter o atual): ")
    email = input("Digite o novo email do contato (deixe em branco para manter o atual): ")
    atualizar_contato(indice, nome, telefone, email)

  elif escolha == "4":
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja marcar como favorito: ")) - 1
    marcar_contato_favorito(indice)

  elif escolha == "5":
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja desmarcar como favorito: ")) - 1
    desmarcar_contato_favorito(indice)

  elif escolha == "6":
    ver_contatos_favoritos()

  elif escolha == "7":
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja deletar: ")) - 1
    deletar_contato(indice)

  elif escolha == "8":
    break

print("Progrma finalizado. Até a proxima!")