start = '''
*rumble rumble* Hmmm? Where is that coming from? OOHHHHH it's my tummy. This is not good. You need food...
'''


print(start)


user_input = input("Do you wnat to make pie or cookies?\n")
while True:
    if user_input == "pie":
        user_input = input("You will be fat. Would you like to be fat on blueberry or pumpkin?\n")
        if user_input == "blueberry":
            user_input = input("No blueberry. Would you rather make pumpkin pie or cookies?\n")
            if user_input == "pumpkin pie":
                user_input = input("Do you want CHEESE pumpkins or FIELD pumpkins?\n")
                if user_input == "cheese pumpkins":
                    print("You've made a cheese pumpkin pie!")
                elif user_input == "field pumpkins":
                    print("You've made a field pumpkin pie!")
            elif user_input == "cookies":
                user_input = input("Do you want to be fat on chocolate chips or oatmeal?\n")
                if user_input =="chocolate chips":
                    user_input = input("White or Milk chocolate\n")
                    if user_input == "white":
                        print("Congrats! Your white chocolate chip cookies are made. Your stomach is satisfied!")
                    elif user_input =="milk":
                        print("So apparently you are allergic to cocoa beans, and no one was there to give you your epi pen. Sadly RIP X_X")
                elif user_input == "oatmeal":
                    user_input = input("You really don't like oatmeal, so do you want to continue making oatmeal or switch to chocolate?\n")
                    if user_input == "oatmeal":
                        print("Making oatmeal makes you mad, so you get frustrated and give up. byebye!")
                    elif user_input == "chocolate":
                        user_input = input("White or Milk chocolate\n")
                        if user_input == "white":
                            print("Congrats! Your white chocolate chip cookies are made. Your stomach is satisfied!")
                        elif user_input =="milk":
                            print("So apparently you are allergic to cocoa beans, and no one was there to give you your epi pen. Sadly RIP X_X")
        elif user_input == "pumpkin":
            user_input = input("Do you want CHEESE pumpkins or FIELD pumpkins?\n")
            if user_input == "cheese pumpkins":
                print("You've made a cheese pumpkin pie!")
            elif user_input == "field pumpkins":
                print("You've made a field pumpkin pie!")
    elif user_input == "cookies":
        print("Do you want to be fat on chocolate chips or oatmeal?")
        user_input = input()
        if user_input =="chocolate chips":
            user_input = input("White or Milk chocolate?\n")
            if user_input == "white":
                print("Congrats! Your white chocolate chip cookies are made. Your stomach is satisfied!")
            elif user_input =="milk":
                print("So apparently you are allergic to cocoa beans, and no one was there to give you your epi pen. Sadly RIP X_X")
        elif user_input == "oatmeal":
            print("You really don't like oatmeal, so do you want to continue making oatmeal or switch to chocolate?")
            user_input = input()
            if user_input == "oatmeal":
                print("Making oatmeal makes you mad, so you get frustrated and give up. byebye!")
            elif user_input == "chocolate":
                print("White or Milk chocolate")
                user_input = input()
                if user_input == "white":
                    print("Congrats! Your white chocolate chip cookies are made. Your stomach is satisfied!")
                elif user_input =="milk":
                    print("So apparently you are allergic to cocoa beans, and no one was there to give you your epi pen. Sadly RIP X_X")
        break
    else:
        user_input = input("didn't understand")
