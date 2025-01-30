quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"}
]

current_question_index = 0
score = 0

def load_question():
    global current_question_index
    question = quiz_data[current_question_index]
    print("\n" + question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

def check_answer(user_input):
    global current_question_index, score
    correct_answer = quiz_data[current_question_index]["answer"]
    if quiz_data[current_question_index]["options"][user_input - 1] == correct_answer:
        print("Correct! 🎉")
        score += 1
    else:
        print(f"Wrong! 😢 The correct answer is {correct_answer}.")

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(quiz_data):
        load_question()
    else:
        print(f"\nQuiz Completed! Final Score: {score}/{len(quiz_data)}")

def quiz():
    load_question()
    while current_question_index < len(quiz_data):
        try:
            user_input = int(input("Enter the number of your answer: "))
            if 1 <= user_input <= 4:
                check_answer(user_input)
                next_question()
            else:
                print("Please enter a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    quiz()
