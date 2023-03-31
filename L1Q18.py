import numpy
def main():
  lista = []
  x = 0
  max = int(input("Quantidade de Números: "))
  
  while True:
    numero = int(input("Número {}: ".format(x+1)))
    lista.append(numero)
    x += 1
    if x == max:
      break
  produto = numpy.prod(lista)    
  print("O produto desses números é: ", produto)

if __name__ == "__main__":
  main()