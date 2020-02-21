def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Incorrect input!")
        return False


amount = input()
while not is_int(amount):
    amount = input()
amount = int(amount)
fi_numbers = [0, 1]
i = len(fi_numbers)
while i < amount:
    new_element = fi_numbers[i - 1] + fi_numbers[i - 2]
    fi_numbers.append(new_element)
    i += 1
print(fi_numbers)
