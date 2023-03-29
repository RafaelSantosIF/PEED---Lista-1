def main():
  while True:
    numo = int(input("Número: "))
    if numo == 0:
      break
    elif numo%2 == 0:
      print("Par\n")
    else:
      print("Ímpar\n")
    
if __name__ == "__main__":
  main()