    #stores the amount of change collected
    money = change
    #stores all money values up to 5 dollars
    Coins = [0.05,0.10,0.25,0.50,1.00,2.00,5.00]
    Rturn = [0,0,0,0,0,0,0]
    #counter in while Loop
    counter = 7
    reverse = -1
    #counter2
    remainder = 0
    #loop choosing the amout of coins
    while(money > 0.05):
        counter -= 1
        reverse += 1
        Rturn[reverse] = int(money/Coins[counter])
        remainder = money % Coins[counter]
        money =  remainder
    print(Coins)
    print(Rturn)


changeCheck(500)
