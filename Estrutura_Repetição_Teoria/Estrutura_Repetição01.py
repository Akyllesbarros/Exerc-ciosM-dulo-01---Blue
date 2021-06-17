  
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
for c in vogais :
  frase = frase.replace(c, "")
print(frase)