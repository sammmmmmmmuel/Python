select = 0

while (select != 6) :

    menu = '''
    [1] Coke
    [2] Diet Coke
    [3] 7up
    [4] Brisk
    [5] Sprite
    [6] exit
    '''     # ''' : string

    print(menu)

    select = float(input("SELECT DRINK : "))

    if select == 1 :
        drink = 'Coke'
    elif select == 2 : 
        drink = 'Diet Coke'
    elif select == 3 : 
        drink = '7up'
    elif select == 4 : 
        drink = 'Brisk'
    elif select == 5 : 
        drink = 'Sprite'
    elif select == 6 : 
        break
    else:
        drink = "Nothing"

    print(f'Your Choice : {drink}')