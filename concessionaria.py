motocicletas = []
clientes = []
vendas = []

def criar_cliente(nome, idade, cep, genero, cpf):
  # Criar cliente a partir de um dicionario
  if clientes != []:
    for cliente in clientes:
      if cliente["cpf"] == cpf:
        print("O cpf já foi cadastrado, delete ou atualize o cliente")
      else:
        cliente = {"nome": nome, "idade": idade, "cep": cep, "genero": genero, "cpf": cpf}
        clientes.append(cliente)
  else:
    cliente = {"nome": nome, "idade": idade, "cep": cep, "genero": genero, "cpf": cpf}
    clientes.append(cliente)


def ler_cliente(cpf):
  # Percorrer o array para achar o cliente com o mesmo cpf de busca
  for cliente in clientes:
    if cliente["cpf"] == cpf:
      print(f"O cliente é {cliente}")

def deletar_cliente(cpf):
  # Usando remove para deletar o elemento cliente do array clientes a partir do cpf
  for cliente in clientes:
    if cliente["cpf"] == cpf:
      clientes.remove(cliente)

def atualizar_cliente(cpf):
  # O usuario vai entrar com a chave a ser alterado e o valor para a mesma
  print("Digite nome se quer att o nome do cliente")
  print("Digite idade se quer att o idade do cliente")
  print("Digite cep se quer att o cep do cliente")
  print("Digite genero se quer att o genero do cliente")
  print("Digite cpf se quer att o cpf do cliente")
  chave = input("Entre com a chave:")
  valor = input("Entre com o valor:")
  for cliente in clientes:
    if cliente["cpf"] == cpf:
      cliente[chave] = valor

def criar_moto(modelo, ano):
  # Criar moto a partir de um dicionario
  # Verificar se o array é diferente de vazio senao criar a primeira moto
  if motocicletas != []:
    for moto in motocicletas:
      # Percorrer o array procurando o mesmo modelo e ano, se tiver atualizar a qntd de unidades
      if moto["modelo"] == modelo and moto["ano"] == ano:
        moto["unidades"] = moto["unidades"] + 1
      # Senao criar a primeira moto do modelo e ano passado
      else:
        moto = {"modelo": modelo, "ano": ano, "unidades": 1}
        motocicletas.append(moto)
  else:
    moto = {"modelo": modelo, "ano": ano, "unidades": 1}
    motocicletas.append(moto)


def ler_moto(modelo, ano):
  # Percorrer o array para achar a moto com o mesmo modelo e ano
  for moto in motocicletas:
    if moto["modelo"] == modelo and moto["ano"] == ano:
      print(f"A Moto é {moto}")

def deletar_moto(modelo, ano):
  # Usando remove para deletar o elemento moto se a quantidade for igual a zero
  for moto in motocicletas:
    if moto["modelo"] == modelo and moto["ano"] == ano:
      moto["quantidades"] = moto["quantidades"] - 1
      if moto["quantidades"] == 0:
        motocicletas.remove(moto)

def atualizar_moto(modelo, ano):
  # O usuario vai entrar com a chave a ser alterado e o valor para a mesma
  print("Digite modelo se quer att o modelo da moto")
  print("Digite ano se quer att o ano da moto")
  print("Digite unidades se quer att o numero de unidades da moto")
  chave = input("Entre com a chave:")
  valor = input("Entre com o valor:")
  for moto in motocicletas:
    if moto["modelo"] == modelo and moto["ano"] == ano:
      moto[chave] = valor

def main():
  sair = True
  while sair != False:
    print("Digite 1 para criar cliente")
    print("Digite 2 para ler cliente")
    print("Digite 3 para atualizar cliente")
    print("Digite 4 para deletar cliente")
    print("Digite 5 para criar moto")
    print("Digite 6 para ler moto")
    print("Digite 7 para atualizar moto")
    print("Digite 8 para deletar moto")
    print("Digite 9 para realizar uma venda")
    print("Digite 10 para ver todas as vendas")
    print("Digite 11 para pesquisar uma venda especifica")
    

    