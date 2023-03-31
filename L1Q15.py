def main():
  lista = []
  x, y = 0,0
  max = int(input("Quantidade de Números: "))
  
  while True:
    numero = int(input("Número {}: ".format(x+1)))
    lista.append(numero)
    x += 1
    if x == max:
      break
  print("Os Números menores que cinco são:")
  while True:
    if lista[y] < 5:
      print("•", lista[y])
    y += 1
    if y == max:
      break

if __name__ == "__main__":
  main()