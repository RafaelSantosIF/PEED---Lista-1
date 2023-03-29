def main():
  max = int(input("Tamanho da Lista: "))
  lista = []
  x = 0
  
  while True:
    valor = int(input("Valor {}: ".format(x+1)))
    lista.append(valor)
    x = x+1
    if x == max:
      break
  soma = sum(lista)
  
  print("Soma Total: ", soma)
  
if __name__ == "__main__":
  main()