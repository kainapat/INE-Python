proid = str(input('Enter your code product: '))
price = int(input('Enter your price for product: '))
qty = int(input('Enter your piece of product: '))

if (proid[1]=='1'):
    result = price*qty
    discount1 = result*0.03
    print(result-discount1)
if (proid[1]=='2'):
    result1 = price*qty
    discount2 = result1*0.03
    discount3 = result1*0.05
    if (qty <=3):
        print (result1-discount2)
    if (qty >=5):
        print (result1-discount3)
if(proid[1]!='1 ,2 '):
    result2 = price*qty
    print(result2)