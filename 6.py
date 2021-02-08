def int_func(word):
    return word[0].upper() + word[1:]


for item in input().split():
    print(int_func(item), end=' ')
