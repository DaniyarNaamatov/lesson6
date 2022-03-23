import time

#декоратор бенчмарк
def bench(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('{}'.format(end - start))
    return wrapper

#генерируем список
def gen_list():
    big_list = []
    x = 1
    while len(big_list) != 1000000000:
        big_list.append(x)
        x += 1
    return big_list

#время нахождение методом индекс
@bench
def search_index():
    big_list = gen_list()
    dx = big_list.index(5000001)
    return dx

#время нахождения бинарным поиском
@bench
def binary_search():
    low = 0
    high = len(gen_list()) - 1
    l = list(gen_list())

    while low <= high:
        mid = (low + high)
        guess = l[mid]
        if guess == 5000001:
            return mid
        elif guess > 5000001:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    print('')
    print('простой поиск по индексу:')
    search_index()
    print('*' * 20)
    print('бинарный поиск:')
    binary_search()

main()
