def usrguess():
    print("1.Stone")
    print("\n2.Paper")
    print("\n3.Scissor")

    user=input("Enter no. according to objects:")

    if user.isdigit():
        user=int(user)
        

        if user==1:
            return "Stone"
        elif user==2:
            return "Paper"
        elif user==3:
            return "Scissor"
        else:
            print("Invalid Input....")
            return None
