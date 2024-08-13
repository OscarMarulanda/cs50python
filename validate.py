import re

email = input("what's your email? ").strip()

if re.search(".+@.+\.com", email):
    print("valid")
else:
    print("invalid")
