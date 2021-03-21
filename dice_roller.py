import random

def roll(sides=6, die_count=1):
    rolls = 0
    for roll in range(die_count):
        rolls += random.randint(1,sides)
    return rolls

def get_stats(rolls):
    count = {}
    sequence = {}
    previous_roll = None
    current_run = 1
    first_run = True
    for roll in rolls:
        if roll in count.keys():
            count[roll] = count[roll] + 1
        else:
            count[roll] = 1
        if not first_run:
            if previous_roll == roll:
                current_run += 1
            else:
                if previous_roll in sequence.keys() and current_run > sequence[previous_roll]:
                    sequence[previous_roll] = current_run
                elif previous_roll not in sequence.keys():
                    sequence[previous_roll] = current_run
                current_run = 1
        first_run = False
        previous_roll = roll

    if previous_roll in sequence.keys() and current_run > sequence[previous_roll]:
        sequence[previous_roll] = current_run
    elif previous_roll not in sequence.keys():
        sequence[previous_roll] = current_run
        
    statistics = {}
    statistics['count'] = count
    statistics['sequence'] = sequence
    statistics['average'] = sum(rolls) / len(rolls)
    return statistics

def test(die_count=1, sides=6, roll_count=1):
    rolls = []
    for die_roll in range(roll_count):
        rolls.append(roll(sides, die_count))
    return rolls

def main():
    rolling = True
    while rolling:
        roll_again = input("Roll the Dice? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            sides = int(input("How many sides do these dice have?"))
            die_count = int(input("How many dice do we have to roll?"))
            roll_count = int(input("How many times would you like to roll?"))
            rolls = test(die_count, sides, roll_count)
            print("You rolled the following: ", rolls)
            print("Here are some stats about that set: ")
            print(get_stats(rolls))
        else:
            rolling = False
            
main()
