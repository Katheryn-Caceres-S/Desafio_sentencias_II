from string import ascii_lowercase
import getpass

intentos = 0
adivinada = ""

clave = input("Ingrese la contraseña: ").lower()

for letra_clave in clave:
    for letra in ascii_lowercase:
        intentos += 1
        if letra == letra_clave:
            adivinada += letra
            break

print(f"La clave fue forzada en {intentos} intentos.")


#while clave != "gato":
 #   print("Clave incorrecta. Inténtalo de nuevo.")
  #  clave = getpass.getpass("clave: ")

# print("Clave correcta")


 #   caracter = 'b'
  #  if caracter in string.ascii_lowercase:
   #     print(f"{caracter} es una letra minúscula")