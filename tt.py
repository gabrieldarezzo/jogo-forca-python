array_result = [True, True, False, True]


def jogo_acabou(acertos_forca):
    for acerto in acertos_forca:
        if(acerto == False):
            print("X ")
        else: 
            print("_ ")        
print(jogo_acabou(array_result))