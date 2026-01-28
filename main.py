limite = 1000
contador = 1
while contador <= limite: 
    if contador % 3 ==0 and contador % 5 ==0:
        print("Fizzbuzz")
    elif contador % 3 ==0: 
        print("Fizz")   
    elif contador % 5 ==0:
        print("Buzz")    
    else:
        print(contador)    
    contador = contador + 1