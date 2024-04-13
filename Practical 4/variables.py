a=40
#define time cost before training
b=36
#define time cost after only running training
c=30
#define time cost after running and strength training
d=a-b
#d is the improvement from running training
e=b-c
#e is the improvement from running and strength training
if d>e:
     print("The improvement from running training only is greater than that from both running and strength training")
else:
     print("The improvement from running and strength training is greater than that from running training only")
#running and strength training had a greater effect on the 5 km