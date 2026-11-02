# exercise_1
def apply_to_all(numbers, action):
    result = []
    for num in numbers:
         result.append(action(num))
    return result

def double(num):
    return num * 2


print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))


# exercise_2

prices = [20, 75, 120, 45, 90]
over_fifty=list(filter(lambda p:p >50 ,prices))
add=list(map(lambda p:p +10 , over_fifty))
print(over_fifty)
print(add)


# exercise_3
words = ["banana", "fig", "aherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
sorted_len=(sorted(words, key=len))
print(sorted_len)
print(max(sorted_len,key=len))
best= max(students, key=lambda s:s [1])
print(best)

