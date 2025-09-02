def run_quiz(questions):
    score = 0
    for q_data in questions:
        print(f"\nQuestion: {q_data['question']}")
        for i, option in enumerate(q_data['options']):
            print(f"{chr(65 + i)}. {option}") # A, B, C, D...

        user_answer = input("Your answer (A, B, C, etc.): ").upper()

        if user_answer == q_data['answer']:
            print("Correct!")
            score += 4
        else:
            score -=2
            print(f"Incorrect. The correct answer was {q_data['answer']}.")

    print(f"\nQuiz finished! You scored {score} out of {len(questions)*4}.")

# Define your quiz questions
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Berlin", "Madrid", "Paris", "Rome"],
        'answer': "C"
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Earth", "Mars", "Jupiter", "Venus"],
        'answer': "B"
    },
    {
        'question': "What is 2 + 2?",
        'options': ["3", "4", "5", "6"],
        'answer': "B"
    },
    {
        'question': "Who painted the Mona Lisa?",
        'options': ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        'answer': "C"
    },
    {
        'question': "What is the largest ocean on Earth?",
        'options': ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        'answer': "D"
    },
    {
        'question': "Which animal lays eggs?",
        'options': ["Dog", "Chicken", "Cat", "Cow"],
        'answer': "B"
    },
    {
        'question': "What is the chemical symbol for water?",
        'options': ["O2", "H2O", "CO2", "NaCl"],
        'answer': "B"
    },
    {
        'question': "How many continents are there?",
        'options': ["5", "6", "7", "8"],
        'answer': "C"
    },
    {
        'question': "What is the smallest prime number?",
        'options': ["0", "1", "2", "3"],
        'answer': "C"
    },
    {
        'question': "Which gas do plants absorb from the atmosphere?",
        'options': ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        'answer': "C"
    },
    {
        'question': "What is the currency of Japan?",
        'options': ["Yuan", "Won", "Euro", "Yen"],
        'answer': "D"
    },
    {
        'question': "What is the highest mountain in the world?",
        'options': ["Mount Kilimanjaro", "Mount Everest", "K2", "Matterhorn"],
        'answer': "B"
    },
    {
        'question': "Which famous scientist developed the theory of relativity?",
        'options': ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        'answer': "C"
    },
    {
        'question': "What is the capital of Australia?",
        'options': ["Sydney", "Melbourne", "Canberra", "Perth"],
        'answer': "C"
    },
    {
        'question': "What is the main ingredient in guacamole?",
        'options': ["Tomato", "Onion", "Avocado", "Lime"],
        'answer': "C"
    },
    {
        'question': "How many sides does a triangle have?",
        'options': ["2", "3", "4", "5"],
        'answer': "B"
    },
    {
        'question': "Which organ pumps blood throughout the body?",
        'options': ["Lungs", "Brain", "Heart", "Liver"],
        'answer': "C"
    },
    {
        'question': "What is the largest land animal?",
        'options': ["Giraffe", "Elephant", "Rhinoceros", "Hippopotamus"],
        'answer': "B"
    },
    {
        'question': "What is the freezing point of water in Celsius?",
        'options': ["-10°C", "0°C", "10°C", "100°C"],
        'answer': "B"
    },
    {
        'question': "Which country is known as the 'Land of the Rising Sun'?",
        'options': ["China", "South Korea", "Japan", "Thailand"],
        'answer': "C"
    }
]

# Run the quiz
run_quiz(quiz_questions)
