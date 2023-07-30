def Summation(args):
    try:
        sum = 0
        for number in args:
            sum += number
        return sum
    except ArithmeticError:
        return "Oops - Arithmetic Error"

def Subtraction(args):
    try:
        sub = args[0]
        for number in range(1, len(args) ):
            sub -= args[number]
        return sub
    except ArithmeticError:
        return "Oops - Arithmetic Error"

def Multiplication(args):
    try:
        mul = 1
        for number in args:
            mul *= number
        return mul
    except ArithmeticError:
        return "Oops - Arithmetic Error"

def Division(args):
    try:
        div = args[0]
        for number in range(1, len(args)):
            div /= args[number]
        return div
    except ZeroDivisionError:
        return "Oops - Division by zero is not possible"
    except ArithmeticError:
        return "Oops - Arithmetic Error"