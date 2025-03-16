def main():
    emps_file = open('employees.txt', 'r')

    for line in emps_file:
        amount = line
        print(line)
        

    emps_file.close()

    

main()
