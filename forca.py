import consumo_api

# Retorna se o jogo acabou
def jogo_acabou(acertos_forca):
    for acerto in acertos_forca:
        if(acerto == False):
            return False

    return True

def chutar_letra(palavra_forca):
    chute_letra = input("Chute uma Letra de A ~ Z\n").upper()
    print("Você chutou a letra: {}".format(chute_letra))


    for x in range(0, len(palavra_forca)):
        letra = palavra_forca[x]
        if(letra == chute_letra):            
            acertos_palavra_forca[x] = True        

    for x in range(0, len(palavra_forca)):
        if(acertos_palavra_forca[x]):
            print("{} ".format(palavra_forca[x]), end=" ")        
        else:            
            print("_ ", end=" ")

    print("")

print("*************************")
print("***** Jogo da Forca *****")
print("*************************")

print("Adivinha a palavra:")

#palavra_forca = list("BOLA")

palavra_api = consumo_api.pega_palavra()
palavra_forca = list(palavra_api) 
acertos_palavra_forca = []

for x in range(0, len(palavra_forca)):
    acertos_palavra_forca.append(False)
    print("_", end=" ")

print(" ")

while(jogo_acabou(acertos_palavra_forca) == False):
    chutar_letra(palavra_forca)

print("Acertou, muito bom!")