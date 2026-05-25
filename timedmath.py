import random
import time

def generate_question():
    op = random.choice(['+', '-', '*'])
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b

    question = f"{a} {op} {b}"
    return question, answer


def math_challenge(num_questions=5, time_limit=10):
    print("\nWelcome to timed math challenge!")
    print(f"You have {time_limit} seconds per question.\n")

    score = 0

    for i in range(num_questions):
        question, correct_answer = generate_question()

        print(f"Q{i+1}: {question} = ?")
        start_time = time.time()

        try:
            user_input = input("your answer: ")
            if time.time() - start_time > time_limit:
                print("Time's up!\n")
                continue
            user_answer = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {correct_answer}.\n")

    print(f"Your score: {score}/{num_questions}")


if __name__ == "__main__":
    math_challenge()