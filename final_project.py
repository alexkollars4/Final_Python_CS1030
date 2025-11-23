import random

#Quiz Questions
questions = [
    { 'question': 'What is the derivative of x^2?',
        'options': ['2x', 'x', 'x^2', '1'],
        'answer': '2x'
    }, 
]

#Function for operating the quiz
def display_quiz(question):
    print(question['question'])
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")

#Function to Recive User Answer
def get_user_answer():
    while True:
        try:
            choice = int(input("Enter the number of your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice - 1 
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Running Quiz Logic
def run_quiz():
    score = 0 
    total_questions = len(questions)
    
    random.shuffle(questions)

    for question in questions:
        display_quiz(question)
        user_choice = get_user_answer()

        if question['options'][user_choice] == question['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")

        print()

        print(f"Quiz Over! Your final score is {score} out of {total_questions}.")
        percentage = (score / total_questions) * 100
        print(f"That's {percentage:.2f}% correct.")

#Main Game Loop
def main():
    while True:
        print("Welcome to the Derivative Quiz!")
        run_quiz()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
    