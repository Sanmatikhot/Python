number = input("enter a number")
palindrome = True
for i in range(len(number) // 2):
    if number[i] != number[-i -1]:
        palindrome = False
        break
if palindrome:
    print(f"{number} is palindrome")
else:
    print(f"{number} is not a palindrome")