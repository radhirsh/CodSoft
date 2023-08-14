import random
quiz_data = [
    {
        "question": "Which of the following is the use of id() function in Python?",
        "options": ["Every object doesn’t have a unique id", "Id returns the identity of the object", "All of the mentioned", "None of the mentioned"],
        "correct_answer": 1
    },
    {
        "question": "Is Python case sensitive when dealing with identifiers?",
        "options": ["yes", "no"],
        "correct_answer": 0
    },
    {
        "question": "All keywords in Python are written in ..................",
        "options": ["UPPER CASE", "lower case", "Capitalized", "None of the mentioned"],
        "correct_answer": 1
    },
]

def display_welcome_message():
    print("Welcome to the Python Quiz!")
    print("Answer multiple-choice questions on Python.")
    print("Let's get started!")

def present_quiz_question(question_data):
    print(question_data["question"])
    for index, option in enumerate(question_data["options"], start=1):
        print(f"{index}. {option}")
    user_answer_index = int(input("Enter the number of your answer: ")) - 1  # Convert to zero-based index
    return user_answer_index

def evaluate_user_answer(user_answer_index, correct_answer_index):
    return user_answer_index == correct_answer_index

def play_quiz_game():
    display_welcome_message()
    score = 0
    
    random.shuffle(quiz_data)
    
    for question_data in quiz_data:
        user_answer_index = present_quiz_question(question_data)
        if evaluate_user_answer(user_answer_index, question_data["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            correct_option = question_data["options"][question_data["correct_answer"]]
            print(f"The correct answer is: {correct_option}")
    
    print("\nQuiz completed!")
    print(f"Your final score is: {score}/{len(quiz_data)}")
    
    if score == len(quiz_data):
        print("Congratulations! You answered all questions correctly.")
    elif score == 2:
        print("Well done! You got 2 out of 3 questions correct. Keep it up!")
    elif score == 1:
        print("Nice try! You got 1 out of 3 questions correct. Keep learning!")
    else:
        print("Don't give up! Keep practicing and you'll improve.")

    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

def main():
    play_again = True
    while play_again:
        play_again = play_quiz_game()

if __name__ == "__main__":
    main()
