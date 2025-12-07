numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = numbers.copy()
numbers_without_none.remove(None)

average = sum(numbers_without_none) / len(numbers)

missing_index = numbers.index(None)

numbers[missing_index] = average

print("Измененный список:", numbers)
