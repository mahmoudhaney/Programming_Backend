import Calculations as Calculations

def pick_choice():
    while True:
        try:
            Menu()
            choice = int(input("Choose a process: "))
            if choice in [1, 2, 3, 4]:
                calc(choice)
            elif choice == 5:
                print("<3 <3 Thank You <3 <3")
                break
            else:
                print("Oops!! - Unknown Choice")
        except ValueError:
            print("!! Invalid Choice !!")

def Menu():
    print("--------------CHOOSE--------------")
    print("1- Summation\n2- Subtraction\n3- Multiplication\n4- Division\n5- Exit")
    print("----------------------------------")

def calc(choice):
    values = list(map(float, input("Enter the values: ").split())) 
    match choice:
        case 1:
            print("<== The Result:", Calculations.Summation(values), "==>")
        case 2:
            print("<== The Result:", Calculations.Subtraction(values), "==>")
        case 3:
            print("<== The Result:", Calculations.Multiplication(values), "==>")
        case 4:
            print("<== The Result:", Calculations.Division(values), "==>")
        case _:
            print("Unknown Choice")

def main():
    pick_choice()

if __name__ == "__main__":
    main()