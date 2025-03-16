name = input('Original Text:')#anirachmingkhwan #thequickbrownfoxjumppower
i = 0
a = 1
b = 3
while i < len(name):
    if i == a:
        print(name[i].lower(),end='')
        a += b
        b += 1
    else:
        print(name[i].upper(),end='')
    i = i+1