def clcm(x,y):
     
     if x < y:  
        smaller = x  
     else:
        smaller = y  
    
     for i in range(1,smaller+1):
         if((x%i==0) and (y%i==0)):
             hcf=i 
     return hcf

clcm(54,24)
print(clcm(54,24))  