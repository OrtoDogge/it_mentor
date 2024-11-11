def main(input: str):
    l = input.split()
    if len(l) != 3 or False in (l[0].isdigit(), l[2].isdigit()) or int(l[0]) > 10 or int(l[0]) < 1 or int(l[2]) < 1 or int(l[2]) > 10 or l[1] not in '-+/*':
            raise Exception
    return int(eval(input))

while True:
    x = input()
    print(main(x))
