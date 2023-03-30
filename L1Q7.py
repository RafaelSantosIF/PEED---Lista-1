def main():
  lista = []
  x, maior,tam = 0, 0, 0
  max = int(input("Quantidade de Palavras: "))
  
  while True:
    palavra = input("Palavra {}: ".format(x+1))
    lista.append(palavra)
    if len(lista[x]) > tam:
      maior = x
      tam = len(lista[x])
    x += 1
    if x == max:
      break
  print("A Maior palavra é {}, com {} letras.".format(lista[maior], tam))

if __name__ == "__main__":
  main()