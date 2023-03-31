class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f'Nome: {self.nome} // Tipo: {self.tipo}'


antonioPokemon = Pokemon("charmander", "fogo")

print(antonioPokemon)
