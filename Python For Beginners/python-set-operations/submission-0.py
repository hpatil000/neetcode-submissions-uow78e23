from typing import List

def count_unique_words(words: List[str]) -> int:
    my_list = set(words)
    # print(my_list)
    count = 0
    for i in my_list:
        count +=1
    return count

    pass

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
