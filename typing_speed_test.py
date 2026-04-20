import time

sentence = "The quick brown fox jumps over the lazy dog"

print("Typing Speed Test")
print("\nType this sentence as fast and accurately as you can:")
print("\n", sentence)
print("\nPress Enter when ready...")
input()

start_time = time.time()

typed = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

word_count = len(typed.split())
wpm = (word_count / time_taken) * 60

accuracy = sum(1 for a, b in zip(typed, sentence) if a == b) / len(sentence) * 100

print("\n--- Results ---")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Words per minute (WPM): {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
