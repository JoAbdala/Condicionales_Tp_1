nombre = input("Ingrese su nombre completo: ")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

if imc <= 15:
    print("Su Condiciòn Fìsica es :Delgadez muy severa")
elif imc <= 15.9:
    print("Su Condiciòn Fìsica es: Delgadez severa")
elif imc <= 18.4:
    print("Su Condiciòn Fìsica es: Delgadez")
elif imc <= 24.9:
    print("Su Condiciòn Fìsica es: Peso Saludable")
elif imc <= 29.9:
    print("Su Condiciòn Fìsica es: Sobrepeso")
elif imc <= 34.9:
    print("Su Condiciòn Fìsica es: Obesidad moderada")
elif imc <= 39.9:
    print("Su Condiciòn Fìsica es: Obesidad severa")
else:
    print("Su Condiciòn Fìsica es: Obesidad muy severa (Obesidad morbida)")


