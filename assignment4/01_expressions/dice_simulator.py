import random  
NUM_SIDES = 6  
def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Each die is a random number between 1 and NUM_SIDES.
    """
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)  
    total = die1 + die2  
    print("Total of two dice:", total)  

def main():
    die1 = 10  
    print("die1 in main() starts as: " + str(die1))  
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))  

if __name__ == '__main__':
    main()
