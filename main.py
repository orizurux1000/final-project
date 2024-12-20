import os
from random import shuffle
from sets import sets
from fractions import Fraction


def main():
    try:
        flag = 0

        # Iterate through the sets of problems
        for set in sets:
            shuffle(set["questions"])

            # Iterate through the questions in each set
            for question in set["questions"]:
                clear_screen()

                # Print the heading
                print(f"Grade {set['grade']}")

                # Print the note, if there is one
                try:
                    print(set["note"])
                except KeyError:
                    pass

                # Add a new line
                print("")

                # Ask the question
                print(f"Question: {question['question']}")
                answer = input("Answer: ")

                # Verify the answer
                if answer != question["answer"]:
                    # Update a flag so that the outer loop breaks
                    flag = 1
                    break

            # Break if the user inputed the incorrect answer
            if flag == 1:
                break

        # You
        clear_screen()
        if flag == 0:
            print("Good job. You won.")
        elif flag == 1:
            print("Wrong answer. Good bye.\n")

    except KeyboardInterrupt:
        clear_screen()
        print(Fraction(3,4))


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
