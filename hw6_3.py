# Write a function called average that takes a list of numbers as a parameter
# and returns the average of the numbers in the list.

def average(numlist):
    # Replace the pass statement with your code
    for num in numlist:
        total = sum(numlist)
        avg = total / len(numlist)
    return avg

if __name__ == "__main__":
    print(average([1, 2, 3, 4, 5]))  # 3.0