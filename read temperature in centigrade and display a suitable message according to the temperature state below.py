tmp = float(input("Enter the temperature : "))
   
if(tmp<0):
   {
     print("\nFreezing weather.")
   }         
elif(tmp>0 and tmp<=10):
   {
     print("\nVery cold weather.")
   }        
elif(tmp>10 and tmp<=20):
   {
     print("\nCold weather.")
   }                    
elif(tmp>20 and tmp<=30):
   {
     print("\nNormal in temp.")
   }                           
elif(tmp>30 and tmp<=40):
   {
     print("\nIts Hot.")
   }                                     
else:
   {
     print("\nIts very hot.")
   }
   
