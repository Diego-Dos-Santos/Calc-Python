# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eJQFAQS_GxVjgNClvHydd7n5BufoqYHH

**CALCULADORA UTILIZANDO FUNCIONES**
"""

def sumar():
  x = a + b
  print(("Resultado"), (x))
def restar():
  x = a - b 
  print(("Resultado"), (x))
def multiplicar():
  x = a * b
  print(("Resultado"), (x))
def dividir():
  x = a / b
  print(("Resultado"), (x))

while True:
  try:
    a = int(input("Ingresar el primeiro numero: \n"))
    b = int(input("Ingresar el segundo numero: \n"))
    print(("que calculo quieres realizar entre"), (a), ("y"),(b), ("? \n"))
    op = str(input(""" #Ofrecemos las opciones de calculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))

    if op == '1':
      sumar()
      break 
    elif op == '2':
      restar()
      break
    elif op == '3':
      multiplicar()
      break 
    elif op == '4':
      dividir()
      break 
    else:
      print("elija una opción o intente otra vez")
  except:
    print("Error")
    op = '?'

  finally:
    print("Gracias por utilizar nuestra calculadora")