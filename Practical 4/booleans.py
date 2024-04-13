X=1<2
Y=1>2
W=(X or Y) and not (X and Y)
print(W)
#time table:
#A True B True: False
#A True B false: True
#A false B true: True
#A false B false: False
# When there are one true and one false, X or Y is true, X and Y is false, not (X and Y) is true, so (X or Y) and not (X and Y) is true
#When there are two trues, X or Y is true, but not (X and Y) is false, (X or Y) and not (X and Y) is false
#When there are two falses, X or Y is false, not (X and Y) is true, so () and () is false