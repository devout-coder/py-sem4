def count_occurrences(list, number):
    count = 0
    for element in list:
        if element == number:
            count += 1
    return count

numbers = [1, 2, 3, 4, 1, 2, 3, 1]
search_number = 1
occurrences = count_occurrences(numbers, search_number)
print(f"The number {search_number} occurs {occurrences} times in the list.")
