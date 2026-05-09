score = 0

print("Welcome to my quiz game!")
print()

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("correct!")
    score += 1
else:
    print("wrong!")

print()

answer = input("2. Which language is used for python files? ")

if answer.lower() == "python":
    print("correct!")
    score += 1
else:
    print("wrong!")

print()

answer = input("3. 5 + 7 = ? ")

if answer == "12":
    print("correct!")
    score += 1
else:
    print("wrong!")

print()
print("Your final score is:", score)