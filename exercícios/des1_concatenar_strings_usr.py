string = str(input("Digite uma string qualquer: "))

tres_primeiros_caracteres = string[:3]
tres_ultimos_caracteres = string[-3:]

print(f"Três primeiros caracteres: {tres_primeiros_caracteres}")
print(f"Três últimos caracteres: {tres_ultimos_caracteres}")

concatenado = tres_primeiros_caracteres + tres_ultimos_caracteres

print(f"Concatenado: {concatenado}")