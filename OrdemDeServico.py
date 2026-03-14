class OrdemDeServico:
    def __init__(self, id, veiculo, descricao, valor, status):
        self.id = id
        self.veiculo = veiculo
        self.descricao = descricao
        self.valor = valor
        self.status = status

    def mostrar_dados(self):
        print(f"ID: {self.id}")
        print(f"Veículo: {self.veiculo.modelo}")
        print(f"Serviço: {self.descricao}")
        print(f"Valor: {self.valor}")
        print(f"Status: {self.status}")


        