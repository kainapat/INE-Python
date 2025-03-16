def main():
    emps_file = open('employees.txt', 'r')
    line = emps_file.readline().rstrip('\n')
    while line != '':
        print('Name:', line)
        line = emps_file.readline().rstrip('\n')
        print('ID:', line)
        line = emps_file.readline().rstrip('\n')
        print('Dept:', line)
        line = emps_file.readline().rstrip('\n')
        print()
    emps_file.close()
main()
