import random

Heads = 1
Tails = 2
Tosses = 10

def main():
    for toss in range(Tosses):
        if random.randint(Heads, Tails) == Heads:
            print('Heads')
        else:
            print('Tails')

main()