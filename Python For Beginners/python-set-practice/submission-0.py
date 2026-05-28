from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_list = set(words)
    if len(my_list)==len(words):
        return "False"
    else:
        return "True"


    pass

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
