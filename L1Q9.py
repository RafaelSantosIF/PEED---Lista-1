def main():
  lista = []
  x, menor,tam = 0, 0, 999999999
  max = int(input("Quantidade de Números: "))
  
  while True:
    numero = int(input("Número {}: ".format(x+1)))
    lista.append(numero)
    if lista[x] < tam:
      menor = x
      tam = lista[x]
    x += 1
    if x == max:
      break
  print("O Menor número é {}".format(lista[menor]))

if __name__ == "__main__":
  main()