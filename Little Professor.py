import random


def main():
    x = get_level()
    score = generate_integer(x)
    print("Score: " + str(score))


def get_level():
    while True:
        x = input("Level: ")
        if x.isdigit():
            x = int(x)
            if x == 1 or x == 2 or x == 3:
                return x


def generate_integer(level):
    score = 0
    if level == 1:
        num1 = 0
        num2 = 9

    elif level == 2:
        num1 = 10
        num2 = 99

    else:
        num1 = 100
        num2 = 999

    for _ in range(10):
        a = random.randint(num1, num2)
        b = random.randint(num1, num2)
        c = a + b
        answer = input(f"{a} + {b} = ")
        if answer.isdigit():
            if int(answer) == c:
                score += 1
                continue

        print("EEE")
        for _ in range(2):
            answer = input(f"{a} + {b} = ")
            if answer.isdigit():
                if int(answer) == c:
                    break
                else:
                    print("EEE")

        print(f"{a} + {b} = {c}")

    return score


if __name__ == "__main__":
    main()
