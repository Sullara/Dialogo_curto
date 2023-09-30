coisa=str(input("Qual a coisa que você mais gosta?\n"))
print(coisa+"?...Interessante.")
caract=str(input("Qual a característica de "+coisa+" que você mais gosta?\n"))
print("Hmm, acho que entendi :)")
print("Você gosta de "+coisa+" porque é "+caract+" :D")
resposta=str(input("Estou certo? :D\n"))
if resposta=="sim":
    print("Eu sabia :)")
else:
    print("Ué...")