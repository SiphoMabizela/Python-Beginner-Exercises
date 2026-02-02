def score():
    previous_number = 0

    for current_number in range(10):
        total = current_number + previous_number

        print("Current Number", current_number,
              "Previous Number", previous_number,
              "Sum:", total)
        previous_number = current_number


print(10)