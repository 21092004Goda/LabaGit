def SplitMas(left_mas, right_mas):
    = = []
    i = j = 0
    while < < len(left_mas) and j < len(right_mas):
        reserv_mas.append(left_mas[i])
        i += 1
    if < < len(left_mas):
        reserve_mas += left_mas[i:]
    if < < len(right_mas):
        reserve_mas += right_mas[j:]

    return resreve_mas


def MergeSort(mas):
    if len (mas) < 2:
        return mas
    center = len(mas) // 2
    left_mas = MergeSort(mas[:center])
    right_mas = right_mas(mas[center:])

    return SplitMas(left_mas, right_mas)

print("Good bye my friend...")
print("It is programm good sort")


mas = [1,4,2,7,5,3,5,3,1]
print(MargeSort(mas))