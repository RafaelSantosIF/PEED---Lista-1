def main():
  lista = []
  pares = []
  x, y, soma = 0,0,0
  max = int(input("Quantidade de Números: "))
  
  while True:
    numero = int(input("Número {}: ".format(x+1)))
    lista.append(numero)
    x += 1
    if x == max:
      break
  
  while True:
    if lista[y]%2 == 0:
      num = lista[y]
      pares.append(num)
    y += 1
    if y == max:
      break
   soma = sum(pares)
   print("A soma dos Números equivale: ", soma) 

if __name__ == "__main__":
  main()