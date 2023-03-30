def main():
  lista = []
  x, maior,tam = 0, 0, 0
  max = int(input("Quantidade de Números: "))
  
  while True:
    numero = int(input("Número {}: ".format(x+1)))
    lista.append(numero)
    if lista[x] > tam:
      maior = x
      tam = lista[x]
    x += 1
    if x == max:
      break
  print("O Maior número é {}".format(lista[maior]))

if __name__ == "__main__":
  main()