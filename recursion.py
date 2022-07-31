
def look_for_key(box):
    """псевдокод поиска ключа в коробке:"""
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print('found the key!')


def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)


def fact(x):
    """рекурсивыный вызов факториала"""
    if x == 1:
        return 1
    return x * fact(x-1)

