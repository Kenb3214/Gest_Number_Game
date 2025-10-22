import random
import json

openingmode = False
tipesmode = False
leve = 1
xp = 0
updatexp = 10
hp = 10

print("Gest Number Game")
print("Welcome to My Game!")
print("Make by Kenb3214 Link:https://github.com/Kenb3214/Gest_Number_Game/tree/main")
while True:
    print("1.Start")
    print("2.seting")
    print("3.exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("1.Start")
        print("2.read save")
        print("3.exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                if hp <= 0:
                    print("You are dead!")
                    next = input("next mode? (y/n): ")
                    if next == "y":
                        leve = 1
                        xp = 0
                        updatexp = 10
                        hp = 10
                        continue
                    elif next == "n":
                        break
                    else:
                        print("Invalid input")
                elif hp <= 5:
                    next = input("Do you need more hp?It will make you xp less 50% (y/n): ")
                    if next == "y":
                        if xp == 0:
                            print("You no any xp")
                        else:
                            hp = 10
                            xp //= 2
                    elif next == "n":
                        continue
                    else:
                        continue
                if leve == 2:
                    updatexp = 20
                elif leve == 3:
                    updatexp = 50
                elif leve == 4:
                    updatexp = 100
                elif leve == 5:
                    updatexp = float("inf")

                if xp >= updatexp:
                    leve = leve + 1
                    xp = 0
                    print(f"Leve UP!Now is leve {leve}")

                print(f"Now you have {hp} HP and you is LV {leve} ({xp}/{updatexp})")
                print("Let gest number")
                print("0. meun")
                if leve == 1:
                    random1 = random.randint(1, 10)
                    if tipesmode == True:
                        if 5 == random1:
                            tips = "It half"
                        elif 5 < random1:
                            tips = "more than helf"
                        elif 5 > random1:
                            tips = "less than helf"
                    else:
                        tips = "NULL"
                    if openingmode == True:
                        openingnumber = random1
                    else:
                        openingnumber = "False"
                    numbers = int(input(f"Let gest number(1-10)(tips: {tips})(number:{openingnumber}): "))
                    if numbers == 0:
                        print("meun")
                        print("1.save")
                        print("2.exit")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            save_data = {}
                            save_data["leve"] = f"{leve}"
                            save_data["xp"] = f"{xp}"
                            save_data["hp"] = f"{hp}"
                            with open("save.json", "w") as save:
                                json.dump(save_data, save)
                            print("saved")
                        elif choice == "2":
                            break
                        else:
                            print("Invalid input")
                    elif numbers == random1:
                        xp = xp + 1
                        print("Good job!")
                    else:
                        hp = hp - 1
                        print(f"You worng!It is {random1}")
                elif leve == 2:
                    random1 = random.randint(1, 20)
                    if tipesmode == True:
                        if 10 == random1:
                            tips = "It half"
                        elif 10 < random1:
                            tips = "more than helf"
                        elif 10 > random1:
                            tips = "less than helf"
                    else:
                            tips = "NULL"
                    if openingmode == True:
                        openingnumber = random1
                    else:
                        openingnumber = "False"
                    numbers = int(input(f"Let gest number(1-20)(tips:{tips})(number:{openingnumber}): "))
                    if numbers == 0:
                        if numbers == 0:
                            print("meun")
                            print("1.save")
                            print("2.exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                save_data = {}
                                save_data["leve"] = f"{leve}"
                                save_data["xp"] = f"{xp}"
                                save_data["hp"] = f"{hp}"
                                with open("save.json", "w") as save:
                                    json.dump(save_data, save)
                                print("saved")
                            elif choice == "2":
                                break
                    elif numbers == random1:
                        xp = xp + 5
                        print("Good job!")
                    else:
                        hp = hp - 1
                        print(f"You worng!It is {random1}")
                elif leve == 3:
                    random1 = random.randint(1, 50)
                    lessthen = random1 - 5
                    morethen = random1 + 5
                    if tipesmode == True:
                        if 25 == random1:
                            tips = "It half"
                        elif 25 < random1:
                            tips = "more than helf"
                        elif 25 > random1:
                            tips = "less than helf"
                    else:
                            tips = "NULL"
                    if openingmode == True:
                        openingnumber = random1
                    else:
                        openingnumber = "False"
                    numbers = int(input(f"Let gest number(1-50)(tips :{tips})(number:{openingnumber}): "))
                    if numbers == 0:
                        if numbers == 0:
                            print("meun")
                            print("1.save")
                            print("2.exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                save_data = {}
                                save_data["leve"] = f"{leve}"
                                save_data["xp"] = f"{xp}"
                                save_data["hp"] = f"{hp}"
                                with open("save.json", "w") as save:
                                    json.dump(save_data, save)
                                print("saved")
                            elif choice == "2":
                                break
                    elif numbers == random1:
                        xp = xp + 10
                        print("Good job!")
                    elif numbers >= lessthen and numbers < random1:
                        xp = xp + 5
                        print(f"You less then it is {random1} but you also get xp")
                    elif numbers <= morethen and numbers > random1:
                        xp = xp + 5
                        print(f"You more then it is {random1} but you also get xp")
                    else:
                        random2 = random.randint(1, 5)
                        hp = hp - random2
                        print(f"You worng!It is {random1}")
                elif leve == 4:
                    random1 = random.randint(1, 100)
                    lessthen = random1 - 5
                    morethen = random1 + 5
                    if tipesmode == True:
                        if 50 == random1:
                            tips = "It half"
                        elif 50 < random1:
                            tips = "more than helf"
                        elif 50 > random1:
                            tips = "less than helf"
                    else:
                            tips = "NULL"
                    if openingmode == True:
                        openingnumber = random1
                    else:
                        openingnumber = "False"
                    numbers = int(input(f"Let gest number(1-100)(tips :{tips})(number:{openingnumber}): "))
                    if numbers == 0:
                        if numbers == 0:
                            print("meun")
                            print("1.save")
                            print("2.exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                save_data = {}
                                save_data["leve"] = f"{leve}"
                                save_data["xp"] = f"{xp}"
                                save_data["hp"] = f"{hp}"
                                with open("save.json", "w") as save:
                                    json.dump(save_data, save)
                            elif choice == "2":
                                break
                            print("saved")
                    elif numbers == random1:
                        xp = xp + 20
                        print("Good job!")
                    elif numbers >= lessthen and numbers < random1:
                        xp = xp + 5
                        print(f"You less then {random1} but you also get xp")
                    elif numbers <= morethen and numbers > random1:
                        xp = xp + 5
                        print(f"You more then {random1} but you also get xp")
                    else:
                        random2 = random.randint(2, 5)
                        hp = hp - random2
                        print(f"You worng!It is {random1}")
                elif leve == 5:
                    print("Good job!You did it!This is a boss let done GOOD!")
                    random1 = random.randint(1, 200)
                    if tipesmode == True:
                        if 100 == random1:
                            tips = "It half"
                        elif 100 < random1:
                            tips = "more than helf"
                        elif 100 > random1:
                            tips = "less than helf"
                    else:
                            tips = "NULL"
                    if openingmode == True:
                        openingnumber = random1
                    else:
                        openingnumber = "False"
                    numbers = int(input(f"Let gest number(1-200)(tips :{tips})(number:{openingnumber}): "))
                    if numbers == 0:
                        if numbers == 0:
                            print("meun")
                            print("1.save")
                            print("2.exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                save_data = {}
                                save_data["leve"] = f"{leve}"
                                save_data["xp"] = f"{xp}"
                                save_data["hp"] = f"{hp}"
                                with open("save.json", "w") as save:
                                    json.dump(save_data, save)
                                print("saved")
                            elif choice == "2":
                                break
                    elif numbers == random1:
                        print("Good job!You did it!!!!!!!!")
                        next = input("next mode? (y/n): ")
                        if next == "y":
                            leve = 1
                            xp = 0
                            updatexp = 10
                            hp = 10
                            continue
                        elif next == "n":
                            break
                    else:
                        hp = 0
                        print(f"You worng!It is {random1} and also you die")
        elif choice == "2":
            print("read save")
            try:
                with open("save.json", "r") as save:
                    save_data = json.load(save)
                    leve = int(save_data["leve"])
                    xp = int(save_data["xp"])
                    hp = int(save_data["hp"])
                    print("Save loaded!")
            except:
                print("save file not found")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
    elif choice == "2":
        while True:
            print("seting mode")
            print(f"1.opening mode is {openingmode}")
            print(f"2.tips mode is {tipesmode}")
            print("3.exit")
            setingchoice = input("Enter your choice: ")
            if setingchoice == "1":
                if openingmode == False:
                    openingmode = True
                else:
                    openingmode = False
            if setingchoice == "2":
                if tipesmode == False:
                    tipesmode = True
                else:
                    tipesmode = False
            elif setingchoice == "3":
                print("exit")
                break
            else:
                print("Invalid choice")
    elif choice == "3":
        print("exit")
        break
    else:
        print("Invalid Choice")
#all people can use this code