import os
from random import shuffle
from sets import sets


def main():
    try:
        # Repeat until the user inputs a valid grade
        grade = 0
        while grade < 1 or grade > len(sets):
            clear_screen()

            # Print the options
            for set in sets:
                print(f"[{set['grade']}] Grade {set['grade']}")
            
            # Get the grade from the user
            try:
                grade = int(input("\nSelect a grade: "))
            except ValueError:
                pass
        
        # Get question subsets
        questions = sets[grade - 1]["questions"]
        qsets = []
        if grade == 3:
            qsets = [questions[0:143], questions[144:287]]
        else:
            for i in range(int(len(questions)/50)):
                qsets.append(questions[i*50:(i+1)*50-1])
        
        # Get question set
        num = 0
        while num < 1 or num > len(qsets):
            clear_screen()

            # Print the options
            for i in range(len(qsets)):
                print(f"[{i + 1}] Question set {i + 1}")

            # Get the number from the user
            try:
                num = int(input("\nSelect a question set: "))
            except ValueError:
                pass
        
        
            

    except KeyboardInterrupt:
        clear_screen()
        pass


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
