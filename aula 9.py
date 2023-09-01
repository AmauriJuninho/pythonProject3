lista=[1,2,3,4,2,3]
dupla=(1,2,3,4,2,3)
dicionario={"um":1,"dois":2,"tres":3}
conjunto={1,2,3,4,2,3}


print(f"lista: {lista}")
print(f"dupla: {dupla}")
print(f"dicionario: {dicionario}")
print(f"conjunto: {conjunto}")

tamanho=len(conjunto)

conjunto.add(4)
if len(conjunto)==tamanho:
    print("login ja existe!")

xsgf