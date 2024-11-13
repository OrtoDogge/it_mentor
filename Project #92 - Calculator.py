def main(input: str):
    l = input.split()
    if len(l) != 3:
        print('Неверный формат ввода')
        raise Exception
    if False in (l[0].isdigit(), l[2].isdigit()) or int(l[0]) > 10 or int(l[0]) < 1 or int(l[2]) < 1 or int(l[2]) > 10:
        print('Используйте только числа от 1 до 10 включительно')
        raise Exception
    if l[1] not in '-+/*':
        print('Разрешены только операции сложения, вычитания, умножения и деления')
        raise Exception
    return int(eval(input))

while True:
    x = input()
    print(main(x))
