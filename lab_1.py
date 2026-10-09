import sys

def is_float(value):
    cleaned = value.lstrip('-').replace('.', '', 1)
    return cleaned.isdigit()


def get_coefficients():
    a, b, c = None, None, None

    if len(sys.argv) == 4:
        if is_float(sys.argv[1]) and float(sys.argv[1]) != 0:
            a = float(sys.argv[1])
        else:
            print("Параметр CLI 'a' некорректен (должен быть числом не равным 0). Он будет запрошен с клавиатуры.")

        if is_float(sys.argv[2]):
            b = float(sys.argv[2])
        else:
            print("Параметр CLI 'b' некорректен. Он будет запрошен с клавиатуры.")

        if is_float(sys.argv[3]):
            c = float(sys.argv[3])
        else:
            print("Параметр CLI 'c' некорректен. Он будет запрошен с клавиатуры.")

    if a is None:
        while True:
            input_a = input("Введите коэффициент a (не равен 0): ")
            if is_float(input_a) and float(input_a) != 0:
                a = float(input_a)
                break
            print("Пожалуйста, введите корректное число (не 0).")

    if b is None:
        while True:
            input_b = input("Введите коэффициент b: ")
            if is_float(input_b):
                b = float(input_b)
                break
            print("Пожалуйста, введите число.")

    if c is None:
        while True:
            input_c = input("Введите коэффициент c: ")
            if is_float(input_c):
                c = float(input_c)
                break
            print("Пожалуйста, введите число.")

    print(f"Коэффициенты загружены: a={a}, b={b}, c={c}")
    return a, b, c


def discriminant_calculating(a, b, c):
    return b ** 2 - 4 * a * c


def calculating(a, b, c):
    answer = set()
    d = discriminant_calculating(a, b, c)
    if d < 0:
        print('Действительных корней нет!')
        return answer
    t_1 = (-b + d ** 0.5) / (2 * a)
    t_2 = (-b - d ** 0.5) / (2 * a)
    if t_1 >= 0:
        answer.add(t_1 ** 0.5)
        answer.add(-(t_1 ** 0.5))
    if t_2 >= 0:
        answer.add(t_2 ** 0.5)
        answer.add(-(t_2 ** 0.5))
    if not answer:
        print('Действительных корней нет!')
    else:
        print('Корни уравнения:', sorted(answer))
    return answer


if __name__ == "__main__":
    a, b, c = get_coefficients()
    calculating(a, b, c)
