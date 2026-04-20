questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. HTML", "D. All"],
        "answer": "D"
    },
    {
        "question": "2 + 2 * 2 = ?",
        "options": ["A. 6", "B. 8", "C. 4", "D. 2"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")
