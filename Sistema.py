from Cliente import Cliente
from OrdemDeServico import OrdemDeServico
from Veiculo import Veiculo

class Sistema:

    def __init__(self):
        self.clientes = []
        self.veiculos = []
        self.ordemdeservico = []
    
    #Cadastrar Clientes
    def cadastrar_cliente(self):
        
        id = int(input("\nID do Cliente: "))
        nome = input("Nome: ")
        cpf = input("Cpf: ")
        telefone = input("Telefone: ")

        cliente = Cliente(id, nome, cpf, telefone)
        
        self.clientes.append(cliente)

        print("\nCliente cadastrado!\n")
    
    #Cadastrar Veiculos
    def cadastrar_veiculo(self):

        id = int(input("\nID do Veículo: "))
        modelo = input("Modelo: ")
        placa = input("Placa: ")
        ano = int(input("Ano do Veículo: "))

        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return
        
        veiculo = Veiculo(id, modelo, placa, ano)

        self.veiculos.append(veiculo)

        print("\nVeículo cadastrado!\n")

    #Cadastrar Serviços
    def cadastrar_servico(self):

        id = int(input("\nID do Veículo: "))
        veiculo = input("Veículo: ")
        descricao = input("Descrição do Serviço: ")
        valor = float(input("Valor do Serviço: "))
        status = input("Status: ")

        servico = OrdemDeServico(id, veiculo, descricao, valor, status)

        self.ordemdeservico.append(servico)

        print("\nServiço cadastrado!\n")

    #Listar Clientes
    def listar_clientes(self):

        if not self.clientes:
            print("\nNenhum cliente cadastrado!\n")
            return
        
        print("\n-=- Lista de Clientes -=-\n")

        for cliente in self.clientes:
            cliente.mostrar_dados()
            print("----------------")
    
    #Listar Veiculos
    def listar_veiculos(self):

        if not self.veiculos:
            print("\nNenhum veículo cadastrado!\n")
            return
        
        print("\n-=- Lista de Veículos -=-\n")

        for veiculo in self.veiculos:
            veiculo.mostrar_dados()
            print("----------------")
    
    #Listar Serviços
    def listar_ordem(self):

        if not self.ordemdeservico:
            print("\nNenhum serviço cadastrado!\n")
            return
        
        print("\n-=- Lista de Serviços -=-\n")

        for servicos in self.ordemdeservico:
            servicos.mostrar_dados()
            print("----------------")
        