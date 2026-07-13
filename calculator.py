while True:
    print("\n=========Simple Calculator=========")
    print("Addition : +")
    print("Subtraction : -")
    print("Multiplication : *")
    print("Division : /")

    try:
    
        num1 = int(input("please enter the first number :__"))
        num2 = int(input("please enter the second number :__"))

        choice = input("please enter your choice like [+, -, *, /]:__")


        if choice == "+":
            print(f"your result is :{num1 + num2}")

        elif choice == "-":
            print(f"your result is :{num1 - num2}")

        elif choice == "*":
            print(f"your result is :{num1 * num2}")

        elif choice == "/":
            if num2 == 0:
                print("it can not divided by zero")

            else:
                print(f"your result is :{num1 / num2}")

        else:
            print("invalid operation")

    except ValueError:
        print("could you please enter valid number only")

    except Exception as err:
        print("exception occured as", err)


    visite_again = input("do you want visite again [yes]:__")
    if visite_again != "yes":
        print("thank you for using the calculator...")
        break