# program to print alphabate A usiing star


# Function to display alphabet pattern
def print_pattern(n):
    # Outer for loop for number of lines(rows)
    for i in range(n):

        # Inner for loop for printing *'s and  &nbsp's(columns)
        for j in range((n // 2) + 1):

            # prints two column lines
            if ((j == 0 or j == n // 2) and i != 0 or

                    # print first line of alphabet
                    i == 0 and j != 0 and j != n // 2 or

                    # prints middle line
                    i == n // 2):
                print("*", end="")
            else:
                print(" ", end="")

        print()

# Size of the letter
num = int(input("Enter the size:> "))

if num > 7:
    print_pattern(num)
else:
    print("Enter a size minumin of 8")