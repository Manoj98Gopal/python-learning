import sys
from termcolor import colored, cprint


questions = [
    {
        'question': """
Question 1: What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome""",
        'answer': "c"
    },
    {
        'question': """
Question 2: Which planet is known as the Red Planet?
A. Earth
B. Mars
C. Jupiter
D. Venus""",
        'answer': "b"
    },
    {
        'question': """
Question 3: Who developed Python programming language?
A. James Gosling
B. Guido van Rossum
C. Dennis Ritchie
D. Bjarne Stroustrup""",
        'answer': "b"
    }

]


def print_color_text(text, color="white"):
    cprint(text, color, attrs=["bold"], file=sys.stderr)
    



def start_game():
    user_score = 0
    for x in range(3):
        question = questions[x]
        print(question["question"])
        user_choice = input("Your answer: ").lower()
        if question['answer'] == user_choice:
            user_score += 1
            print_color_text("Correct!", "green")
        else:
            print_color_text(
                f"Wrong! The correct answer is {question['answer']}", "red")

    print(f"Quiz over! Your final score is {user_score} out of 3")


start_game()
