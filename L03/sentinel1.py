keep_going = "y"

while keep_going == 'y':
        wholesale = int(input("Enter the item's wholesale cost: "))
        retail_price = wholesale * 2.5
        print("Retail price", retail_price)
        keep_going = input("Do you have another item?" + \
                       "(Enter y for yes): ")