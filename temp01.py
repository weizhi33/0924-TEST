students = [
{'id': 1, 'name': 'Alice', 'major': 'Computer Science'},
# ± ?×/¯
# ³  Copilot ov¯×O/¯
]{'id': 2, 'name': 'Bob', 'major': 'Mathematics'},  
{'id': 3, 'name': 'Charlie', 'major': 'Physics'}
]   

#寫一個函式，接收一個數字串列，回傳該串列中的最大值
def find_maximum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

#寫一個程式，從1印到100，但3的倍數印"Fizz"，5的倍數印"Buzz"，3和5的倍數印"FizzBuzz"，其他情況則印出數字本身
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)