from os import system

# Main
unidades = [
    "Zero",
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dez",
    "Onze",
    "Doze",
    "Treze",
    "Catorze",
    "Quinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
]

dezenas = [
    "",
    "Dez",
    "Vinte",
    "Trinta",
    "Quarenta",
    "Cinquenta",
    "Sessenta",
    "Setenta",
    "Oitenta",
    "Noventa",
]
centenas = [
    "",
    "Cem",
    "Duzentos",
    "Trezentos",
    "Quatrocentos",
    "Quinhentos",
    "Seiscentos",
    "Setecentos",
    "Oitocentos",
    "Novecentos",
]


def remove_casas(numero, extenso, unidades, dezenas):
    # remove casa da centena
    numero -= (numero // 100) * 100

    if 0 < numero <= 19:
        extenso += unidades[numero]
    else:
        extenso += dezenas[numero // 10]

        # remove casa dezena
        numero -= (numero // 10) * 10
        if numero > 0:
            extenso += " e " + unidades[numero]

    cls(extenso)


def cls(extenso):
    f"Voce digitou {extenso.capitalize()}"


numero = 0
while numero <= 999:
    while True:
        try:
            numero = int(input("Digite um numero entre 0 e 999: "))
            break
        except ValueError:
            system("cls")
            print("Por favor digite um numero válido")

    extenso = "Zero" if numero == 0 else ""

    if 200 > numero > 100:
        extenso += "Cento e "
    elif numero >= 200 or numero == 100:
        extenso += centenas[numero // 100]
        if numero - (numero // 100) * 100 > 0:
            extenso += " e "

    remove_casas(numero, extenso, unidades, dezenas)
