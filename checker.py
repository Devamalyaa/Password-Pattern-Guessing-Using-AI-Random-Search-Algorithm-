import random
import string
import time

target = "AI"
characters = string.ascii_uppercase + string.digits

start_time = time.time()
attempts = 0
guess = ""

max_attempts = 500  

while guess != target and attempts < max_attempts:
    guess = ''.join(random.choice(characters) for _ in range(len(target)))
    attempts += 1
    print("Trying:", guess)

end_time = time.time()
elapsed = round(end_time - start_time, 2)

print("\n--- RESULT ---")
if guess == target:
    print("Password Matched Successfully!")
else:
    print("Password Not Found within limit.")
print("Target Password:", target)
print("Total Attempts:", attempts)
print("Time Taken:", elapsed, "seconds")


