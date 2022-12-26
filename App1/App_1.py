 #Скрипт для нахождения факториала 
def factorial(n):
      # Вычесление факториала    
    if n<2:        
        return 1
        return n * factorial(n-1)

if __name__=="__main__":
    n = int(input())
    print(factorial(n))   
    

  
    
    
     
    