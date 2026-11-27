score = 0

print("--- Quiz Game ---")

print("\n1. What is the capital of India?")
print("a. Mumbai")
print("b. Delhi")
print("c. Kolkata")
print("d. Chennai")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n2. Which language are we learning?")
print("a. Python")
print("b. Java")
print("c. C++")
print("d. PHP")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n3. How many days are there in a week?")
print("a. 5")
print("b. 6")
print("c. 7")
print("d. 8")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n4. Which device is used to type text?")
print("a. Monitor")
print("b. Keyboard")
print("c. Speaker")
print("d. Printer")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n5. What is 5 + 5?")
print("a. 8")
print("b. 9")
print("c. 10")
print("d. 11")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n--- Quiz Completed ---")
print("Your Score:", score, "/ 5")