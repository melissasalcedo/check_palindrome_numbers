# Check if the numbers is palindrome
# Pseudocode
# Function
def palindrome(number):
    orig_num = number

    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
    return orig_num == reverse_num

# Numbers
number1 = 12345
number2 = 899898
number3 = 1010101

result1 = palindrome(number1)
print(f"{number1} is a palindrome: {result1}")

result2 = palindrome(number2)
print(f"{number2} is a palindrome: {result2}")

result3 = palindrome(number3)
print(f"{number1} is a palindrome: {result3}")

