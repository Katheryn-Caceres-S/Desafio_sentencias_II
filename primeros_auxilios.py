print("Indice de primeros auxilios")
## input(print("El paciente responde a estimulos??"))

while True:
    estimulo = input("El paciente reponde a estimulos?? (si o no): ").lower()

    if estimulo == "si":
        print("Valora la necesidad de trasladar al paciente al hospital más cercano")
        print("Evaluación terminada")
        break

    elif estimulo == "no":
        print("Revisar la vía Aerea")
        respira = input("¿Esta respirando? (si o no): ").lower()

        if respira == "si":
            print("Permitele al paciente posición de suficiente ventilación")
            print("Evaluación terminada")
            break

        elif respira == "no":
            print("Administra 5 ventilaciones y llama a la ambulancia")  

            while True:
                vida = input("El paciente presenta signos de vida?? (si o no): ") 

                if vida == "no":
                    print("Administra compresiones toracicas hasta que llegue la ambulancia")
                elif vida == "si":
                    print("Reevaluar a la espera de la ambulancia")
                else:
                    print("Intenta otra vez, solo responder SI o NO") 

                ambulancia = input("¿Llego la ambulancia?? (si o no): ").lower()

                if ambulancia == "si":
                    print("Evaluación terminada")
                    break
                elif ambulancia == "no":
                    print ("Te volvere a consultar por el paciente...")
                    continue  
                else:
                    print("Intenta otra vez, solo responder SI o NO")   
            break

        else:
             print("Intenta otra vez, solo responder SI o NO")   
             continue

    else:
        print("Intenta otra vez, solo responder SI o NO")    
