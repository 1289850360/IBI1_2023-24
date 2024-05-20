def chocolate_calculate(total_money,price):
    number=total_money//price#we can get the bar number
    rest_money=total_money%price#we can get rest money
    print(f'You can buy {number} bar. And have {rest_money} money left')
    return number,rest_money
total_money=int(input("All money you have"))
price=int(input("Price of one bar"))
chocolate_calculate(total_money,price)
