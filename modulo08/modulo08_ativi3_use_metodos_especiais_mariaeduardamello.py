class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        info_base = super().__str__()
        return f"{info_base} | Autonomia: {self.autonomia_bateria}km"


# Exemplo de uso:
meu_carro = CarroEletrico("BYD", "Dolphin", "600")
print(meu_carro)