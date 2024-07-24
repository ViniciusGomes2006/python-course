from contact import contactEntity

contactList = [contactEntity("Vinicius", "12345")]

def main():

  comands = {
    "1": "Adicionar contato",
    "2": "Editar informações extras ao contato",
    "3": "Editar contato",
    "4": "Marcar contato como favorito",
    "5": "Listar contatos",
    "6": "Sair"
  }

  global mainCommand
  mainCommand = True

  if mainCommand:
    for key, value in comands.items():
      print(f"{key}: {value}")

    command = input(f"\nDigite o comando: ")

    if command == "1":
      name = str(input("Digite o nome do contato: ", ))
      phone = str(input("Digite o telefone do contato: "))
      email = str(input("Digite o email do contato: "))

      newContact = contactEntity(name, phone, email)

      contactList.append(newContact)
    if command == "2":
      phone = str(input("Digite o telefone do contato: "))
      print("Buscando informações...")      

      for contact in contactList:
        if contact.phone == phone:
          image_url = str(input(f"Digite a url da imagem (Caso queira manter, não digite nada):"))
          notes = str(input(f"Digite a notas (Caso queira manter, não digite nada):"))

          contact.add_extra_data(image_url, notes)
    if command == "3":
      phoneCheck = input("Digite o telefone do contato para buscar as informações: ")
      print("Buscando informações...")
      for contact in contactList:
        if contact.phone == phoneCheck:
          name = input("Digite o nome do contato: ")
          phone = input("Digite o telefone do contato: ")
          email = input("Digite o email do contato: ")

          contact.edit_contact(name, phone, email)
    if command == "4":
      phoneCheck = input("Digite o telefone do contato para buscar as informações: ")
      print("Buscando informações...")
      
      for contact in contactList:
        if contact.phone == phoneCheck:
          isFavorite = contact.isFavorite
          
          contact.set_favorite(not isFavorite)
    if command == "5":
      print(f"\n5Contatos favoritos:\n")
      for contact in contactList:
        if contact.isFavorite:
          print(contact)
          
      print(f"\nTodos os contatos:\n")
      for contact in contactList:
        print(contact)
    if command == "6":
      mainCommand = False
      print("Saindo...")
      exit()

while True:
  main()
  if mainCommand == False:
    break