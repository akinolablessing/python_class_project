def func(number:list)->list:
    number.sort()
    reverse = number.reverse()
    decrease = number[: : -1]
    print(decrease)
    print(number)
    print(reverse)


func([5,3,4,2,1])