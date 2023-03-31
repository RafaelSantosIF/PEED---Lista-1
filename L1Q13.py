def main():
  lista = []
  x, y = 0,0
  max = int(input("Quantidade de Palavras: "))
  
  while True:
    palavra = input("Palavra {}: ".format(x+1))
    lista.append(palavra)
    x += 1
    if x == max:
      break
  print("As Palavras que começam com a letra A são:")
  while True:
    if lista[y][0] == "a" or lista[y][0] == "A":
      print("•", lista[y])
    y += 1
    if y == max:
      break

if __name__ == "__main__":
  main()