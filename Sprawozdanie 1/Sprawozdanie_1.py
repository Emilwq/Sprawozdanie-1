def dodawanie(a,b):  
      print("Wynik dodawania wynosi: ") 
      return a+b

def odejmowanie(a,b):
      print("Wynik odejmowania wynosi: ")
      return a-b

def mnozenie(a,b):  
       print("Wynik mnozenia wynosi: ") 
       return a*b

def dzielenie(a, b):  
       print("Wynik dzielenia wynosi: ") 
       return a/b

def potegowanie(a, b):  
       print("Wynik potegowania wynosi: ") 
       return a**b

print("Wybierz działanie")  
print("1 - dodawanie")  
print("2 - odejmowanie")  
print("3 - mnozenie")  
print("4 - dzielenie")
print("5 - potegowanie")

while True:  

  c = int(input())  

  if c == 1:  
      print("Podaj pierwsza liczbe")  
      a = int(input()) 
      print("Podaj druga liczbe")
      b = int(input())  
      print(dodawanie(a,b))  

  if c == 2:  
      print("Podaj pierwsza liczbe")  
      a = int(input()) 
      print("Podaj druga liczbe")
      b = int(input())  
      print(odejmowanie(a,b))  

  if c == 3:  
      print("Podaj pierwsza liczbe")  
      a = int(input()) 
      print("Podaj druga liczbe")
      b = int(input())  
      print(mnozenie(a,b))  

  if c == 4:  
      print("Podaj pierwsza liczbe")  
      a = int(input()) 
      print("Podaj druga liczbe")
      b = int(input())  
      print(dzielenie(a,b))  

  if c == 5:  
      print("Podaj pierwsza liczbe")  
      a = int(input()) 
      print("Podaj druga liczbe")
      b = int(input())  
      print(potegowanie(a,b))

  else :  
      print("Podaj liczbę od 1 do 5")
