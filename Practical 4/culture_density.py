n=0.05 
#use n as a symbol to indicate density
max=0.9
#the value when density get max
i=1
#days
while n<max: 
#judge whether the density reaches 90%
    i+=1 
#record days
    n*=2
#change density
print(i)
#count days