def remove_fourth_character(word: str) -> str:
    before_fourth_char = word[0:3]
    after_fourth_char = word[4:]

    word = before_fourth_char + after_fourth_char
    return word
    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
