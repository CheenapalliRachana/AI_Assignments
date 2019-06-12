num=0
nearest_square = 0
finalValue =0
while(num <100):
    nearest_square = num
    nearest_square=nearest_square*nearest_square
    if(nearest_square<40):
        finalValue = nearest_square
        num+=1
    else:
        print(finalValue)
        break 
    
    
