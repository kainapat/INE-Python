def main():
    infile = open('cities.txt', 'r')
    cities = infile.readline()
    infile.close()

    index = 0 
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print(cities)
main()