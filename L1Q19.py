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
  lista.sort()    
  print("Números em ordem Crescente: ", lista)

if __name__ == "__main__":
  main()