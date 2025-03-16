name = input('Enter your name = ')
print('Types of Photo','\n'
'1. One inch','\n'
'2. Two inch','\n'
'3. Polaroid')
select = int(input('Select type = '))
amount = int(input('Enter amount = '))
if select == 1:
    selection = 'One inch'
    if amount >= 3:
        fullcost_str = str(65)+str('*')+str(amount)
        fullcost = 65*amount
        ans = 65*amount*(95/100)
        discount = fullcost-ans
    else:
        fullcost_str = str(65)+str('*')+str(amount)
        fullcost = 65*amount
        ans = fullcost
        discount = 0
if select == 2:
    selection = 'Two inch'
    if amount >= 3:
        fullcost_str = str(80)+str('*')+str(amount)
        fullcost = 80*amount
        ans = 80*amount*(95/100)
        discount = fullcost-ans
    else:
        fullcost_str = str(80)+str('*')+str(amount)
        fullcost = 80*amount
        ans = fullcost
        discount = 0
if select == 3:
    selection = 'Polaroid'
    fullcost_str = str(70)+str('*')+str(amount)
    fullcost = 70*amount
    ans = fullcost
    discount = 0
print('---------------------------------------------------')
print('Show Details','\n'
'Your name is ',name,'\n'
'Type of photo is',selection,'\n'
'Amount is ',amount,'\n'
'Total price is',fullcost_str,'=',fullcost,'\n'
'Discount =',int(discount),'\n'
'Net price =',int(ans))