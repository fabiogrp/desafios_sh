class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def apresentar_carro(self):
        print(f"Carro:\n  - Marca:{self.marca}\n  - Modelo:{self.modelo}\n  - Ano:  {self.ano}")

meu_carro = Carro("Chevrolet", "Celta", 2020)

meu_carro.apresentar_carro()