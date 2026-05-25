import time

print("Typing Speed Test")
print("------------------")

sentence = "Python is a powerful programming language"

input("Press Enter to start...")

start_time = time.time()

typed_text = input("\nType this sentence:\n" + sentence + "\n\n")

end_time = time.time()

time_taken = end_time - start_time

words = len(sentence.split())
wpm = (words / time_taken) * 60

print("\nTime Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(wpm, 2), "WPM")

if typed_text == sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Incorrect typing")