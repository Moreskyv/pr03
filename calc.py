
def calculator():
    print("калькулятор (для выхода введите 'выход')")
    
    while True:
        try:
            a_input = input("Введите первое число: ").strip()
            if a_input.lower() in ('выход', 'exit', 'quit'):
                print("выход")
                break

            a = float(a_input)

            op = input("введите оператор (+, -, *, /): ").strip()
            if op.lower() in ('выход', 'exit', 'quit'):
                print("выход")
                break
            if op not in ('+', '-', '*', '/'):
                print("Неверный оператор. Допустимые: +, -, *, /")
                continue

            b_input = input("Введите второе число: ").strip()
            if b_input.lower() in ('выход', 'exit', 'quit'):
                print("выход")
                break

            b = float(b_input)

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("ошибка: деление на ноль!")
                    continue
                result = a / b

            if result == int(result):
                result = int(result)
            print(f"результат: {result}")

        except ValueError:
            print("ошибка: введите корректное число.")
        except OverflowError:
            print("ошибка: число слишком велико для обработки.")

calculator()