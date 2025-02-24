import random
while True:
    input("Press enter to toss:")
    result="Heads" if random.randint(0,1)==0 else "Tails"
    print(result)
