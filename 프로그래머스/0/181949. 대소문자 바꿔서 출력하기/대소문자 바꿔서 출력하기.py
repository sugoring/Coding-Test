str = input()
modified_str = ""

for char in str:
    if char.isupper():
        modified_str += char.lower()
    else:
        modified_str += char.upper()

print(modified_str)