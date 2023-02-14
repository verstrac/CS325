#Caleb Verstraete
# 2/9/23
# CS 325

def main():
    print(feedDog([1,3,2], [2,1,4,6]))

def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    dogs_fed = 0
    dog_to_feed = 0

    for biscuit in biscuit_size:
        if biscuit >= hunger_level[dog_to_feed]:
            dogs_fed += 1
            dog_to_feed += 1
        if dogs_fed == len(hunger_level):
            break

    return dogs_fed


if __name__ == '__main__':
    main()