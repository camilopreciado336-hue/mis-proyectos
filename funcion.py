def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 4)

print("El área es:", resultado)


def calcular_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro

resultado2 = calcular_perimetro_rectangulo(5, 4)

print("El perímetro es:", resultado2)