records = {'6506022620052':['Kainapat Suwannachote', 'guy26466@gmail.com', '0944828221']}

print(records)

id = records['6506022620052']
print(id)
def main():
    again = 'y'   
    person = {}
    person['id'] = int(input('ID: '))
    person['name'] = input('Name: ')
    person['email'] = input('Email: ')
    person['phone_number'] = int(input('Phone number: '))
    print(person)
    del person['id']
    print(person)
    while again.lower() == 'y':
        again = input('Enter more data? (y/n): ')
main()