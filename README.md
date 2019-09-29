# Jogo da Forca em Python


Objetivo do repo é fazer um Jogo da forca:
Ps: Nunca vi Python na minha vida.

Ex:
Output
```shell
Adivinha a palavra: (No caso BOLA)
_ _ _ _ 

Chute uma Letra de A  ~ Z
```

Entrada do usuario:
```
B
```

```
B _ _ _ 
```


Ideia, criar um conjunto a partir de todas as letras (BOLA)
```
#[
    #0 => false
    #1 => false
    #2 => false
    #3 => false
#]
```

E ao ir acertando, ex: "B", adicionar true no chave-valor
```
#[
    #0 => true
    #1 => false
    #2 => false
    #3 => false
#]
```
