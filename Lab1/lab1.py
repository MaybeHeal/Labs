from random import randint


def task1():
    print('Task 1: ')
    q1 = [i for i in range(10, 2)]
    for i in q1:
        print(i)


def task2():
    print('Task 2: ')
    q2 = [0, 1, 2, 3, 4]
    print(q2[2:5])


def task3and4():
    print('Task 3: ')
    q34 = [randint(1, 10) for i in range(10)]
    print(q34)
    print('Task4:')
    q34.clear()
    print(q34)


def task5():
    print('Task 5: ')
    s = input('Input sting: ')
    q5 = list(s)
    letters = ['a', 'e', 'o']
    for i in q5[::-1]:
        if i in letters:
            q5.remove(i)
    print(q5)


def task6():
    print('Task 6: ')
    a = [1, 3, 4, 5]
    b = [4, 5, 6, 7]
    for i in b[::-1]:
        if i in a:
            b.remove(i)
    print(b)


def task7_8_9_10():
    print('Task 7: ')
    q7 = [randint(1, 10) for g in range(randint(1, 15))]
    print(q7)
    print(max(q7))
    print('Task 8: ')
    print(min(q7))
    print('Task 9: ')
    print(sum(q7))
    print('Task 10: ')
    print(sum(q7) / len(q7))


if __name__ == '__main__':
    task1()
    task2()
    task3and4()
    task5()
    task6()
    task7_8_9_10()
