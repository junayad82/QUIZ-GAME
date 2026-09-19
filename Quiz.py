import random

questions = [
    {
        "question": "What is the output of 2 + 3?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "func", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()"
    }
]

results = []


# Start Quiz
def start_quiz():
    score = 0

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    for question in quiz_questions:

        print("\n" + question["question"])

        for index, option in enumerate(question["options"], 1):
            print(f"{index}. {option}")

        answer = input("Enter your answer: ")

        if answer.isdigit():
            answer = int(answer)

            if 1 <= answer <= len(question["options"]):
                selected_answer = question["options"][answer - 1]

                if selected_answer == question["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {question['answer']}")
            else:
                print("Invalid option!")
        else:
            print("Please enter a number!")

    print("\n====== QUIZ RESULT ======")
    print(f"Your score: {score}/{len(quiz_questions)}")

    results.append(score)

    return score


# View Questions
def view_questions():
    if len(questions) == 0:
        print("No questions found!")

    else:
        print("\n====== QUESTIONS ======")

        for index, question in enumerate(questions, 1):
            print(f"{index}. {question['question']}")

            for option in question["options"]:
                print(f"- {option}")

            print(f"Answer: {question['answer']}")
            print("----------------------")


# Add Question
def add_question():
    question_text = input("Enter question: ")

    options = []

    for i in range(4):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)

    answer = input("Enter correct answer: ")

    question = {
        "question": question_text,
        "options": options,
        "answer": answer
    }

    questions.append(question)

    print("Question added successfully!")


# Search Question
def search_question():
    search = input("Enter keyword: ")
    found = False

    for question in questions:
        if search.lower() in question["question"].lower():
            print("\nQuestion found!")
            print(question["question"])

            for option in question["options"]:
                print(f"- {option}")

            found = True

    if not found:
        print("Question not found!")


# View Result
def view_result():
    if len(results) == 0:
        print("No result found!")

    else:
        print("\n====== RESULTS ======")

        for index, score in enumerate(results, 1):
            print(f"Quiz {index}: {score}/{len(questions)}")


# Save Result
def save_result():
    with open("quiz_result.txt", "w") as file:

        for index, score in enumerate(results, 1):
            file.write(
                f"Quiz {index}: {score}/{len(questions)}\n"
            )

    print("Result saved successfully!")


# Main Menu
while True:

    print("\n====== QUIZ EXAM SYSTEM ======")
    print("1. Start Quiz")
    print("2. View Questions")
    print("3. Add Question")
    print("4. Search Question")
    print("5. View Result")
    print("6. Save Result")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        view_questions()

    elif choice == "3":
        add_question()

    elif choice == "4":
        search_question()

    elif choice == "5":
        view_result()

    elif choice == "6":
        save_result()

    elif choice == "7":
        print("Thank you for using Quiz Exam System!")
        break

    else:
        print("Invalid choice!")