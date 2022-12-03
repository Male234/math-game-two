while True:
    user_name = str(input("Enter your name: "))
    correct_answers = 0
    incorrect_answers = 0

    print(f"Hello, {user_name}!")
    import time

    time.sleep(1)

    print("You woke up")
    time.sleep(5)
    print("You go to school")
    time.sleep(1.5)
    print("Oh no! There's a math test!")
    time.sleep(3.2)
    print("The question is : ")
    print("What is 6+2?")
    correct_answer = 6 + 2
    answer = int(input("Answer: \n "))
    if answer == correct_answer:
        print("You thing you got that correct.")
        correct_answers += correct_answers + 1
    else:
        print("You thing you got that incorrect.")
        incorrect_answers += incorrect_answers + 1
    time.sleep(0.5)
    print("The next question is: \n What is 3/2")
    correct_answer = 3 / 2
    answer = float(input("You answer: \n"))
    if answer == correct_answer:
        print("You thing you got that correct.")
        correct_answers += correct_answers + 1
    else:
        print("You thing you got that incorrect.")
        incorrect_answers += incorrect_answers + 1
    time.sleep(0.5)
    print("The next question is: \n What is 9*2")
    correct_answer = 9 * 2
    answer = int(input("Your answer: \n "))
    if answer == correct_answer:
        print("You think you got that correct.")
        correct_answers += correct_answer + 1
    else:
        print("You think you got that wrong.")
        incorrect_answers += incorrect_answers + 1
    time.sleep(10)
    print("The teacher checked the tests.")
    if correct_answers > incorrect_answers:
        print("You passed!")
    elif incorrect_answers > correct_answers:
        print("You failed...")
    else:
        print("What.. happened?")
    print(f"You had {str(incorrect_answers)} of incorrect answers and you got {str(correct_answers)} correct answers.")

    replay = input("Replay?: ")
    if replay == 'Y' or 'Yes' or 'yea':
        pass
    elif replay == 'N' or 'No' or 'nein' or 'Nein' or 'n':
        break
        exit
    else:
        break
        exit