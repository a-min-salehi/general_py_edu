while True:
    try:
        input_ = eval(input("enter a number: "))
        print(type(input_))
        if isinstance(input_ , bool):
            raise ValueError("the input is not a number")
        else:
            if input_  > 5:
                print("upper than 5")
            elif input_  < 5:
                print("lower than 5")
            else:
                print("5")

    except Exception as exp:
        print(exp)
