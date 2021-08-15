  
def PrimeChecker(a):  
     
    if a > 1:  
          
        for j in range(2, int(a/2) + 1):  
           
            if (a % j) == 0:  
                return False  
                break  
        
        else:  
            return True 
  
    else:  
        return False  

