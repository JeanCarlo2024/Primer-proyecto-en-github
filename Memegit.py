for i in range(5):
    meme_dict = {
                "XD": "Una respuesta de algo gracioso",
                "POSSER": "fan por moda",
                "CHAMBA": "significa trabajo",
                "FANBOY": "es un fan ciengo"
                }
                
    word = input("que palabra quieres saber el significado?").upper()


    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no tenemos esa palabra en el diccionario")
