sexo = input("Ingrese su sexo: ")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su Estatura: "))

if edad >= 18:
    print("Es mayor de edad")

if sexo == "femenino" and altura > 1.70:
    print("Es una mujer alta")
elif sexo == "masculino" and altura > 1.80:
    print("Es un hombre alto")
gi