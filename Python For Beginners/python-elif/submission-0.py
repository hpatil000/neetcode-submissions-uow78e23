def check_range(num: int) -> str:
    if num < 0:
        return "negative"
        #print("negative")
    elif num == 0:
        return "zero"
        print("zero")
    elif num > 0 and num < 10:
        return "positive single digit"
        print("positive single digit")
    else:
        return "positive multi digit"
        print("positive multi digit")

  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
