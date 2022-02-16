# Напишите функцию, которая переворачивает строку. Входная строка задается в виде массива таких символов.
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_string(ls):
    if len(ls) == 1:
        return ls
    else:
        return [ls.pop()] + reverse_string(ls)


ls = ["h"]
print(reverse_string(ls))
ls = ["h", "e", "l", "l", "o"]
print(reverse_string(ls))
