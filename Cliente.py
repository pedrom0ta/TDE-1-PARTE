class Cliente:
    def __init__(self, id, nome, cpf, telefone):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def mostrar_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Cpf: {self.cpf}")
        print(f"ID: {self.id}")

        