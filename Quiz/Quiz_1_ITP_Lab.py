top = {'object': ' ', 'amount': '15'}
mid = {'object': ' ', 'amount': '15'}
bot = {'object': ' ', 'amount': '15'}

print("Welcome to the refrigerator!")

while True:
    x = input("Do you want to use the refrigerator? Y/N ")
    if x == "Y" or x == "y":
        x = input("What do you want to do? Take/Put ")
        if x == "put" or x == "Put":
            x = input ("Which side do you want to use? Top/Mid/Bot ")
            if x == "Top" or x == "top":
                itemt = input("What do you want to put? ")
                amt = int(input("Amount? "))
                top[itemt] = amt
                top.update({'amount': int(top['amount']) - amt})
                print (itemt.upper() , "is in the top section of the fridge!")
                print ("The top section has" , top.get('amount'), "space(s) left.")
                x = input ("Do you still want to use the refrigerator? Y/N ")
                if x == "Y" or x == "y":
                    continue
                elif x == "N" or x == "n":
                    print("\n" , "OK BYE!")
                    break
                else:
                    print ("ERROR!!!")
                    continue
            elif x == "Mid" or x == "mid":
                itemm = input("What do you want to put? ")
                amt = int(input("Amount? "))
                mid[itemm] = amt
                mid.update({'amount': int(mid['amount']) - amt})
                print(itemm.upper(), "is in the middle section of the fridge!")
                print("The middle section has", mid.get('amount'), "space(s) left.")
                x = input("Do you still want to use the refrigerator? Y/N ")
                if x == "Y" or x == "y":
                    continue
                elif x == "N" or x == "n":
                    print("\n", "OK BYE!")
                    break
                else:
                    print("ERROR!!!")
                    continue
            elif x == "Bot" or x == "bot":
                itemb = input("What do you want to put? ")
                amt = int(input("Amount? "))
                bot[itemb] = amt
                bot.update({'amount': int(bot['amount']) - amt})
                print(itemb.upper(), "is in the bottom section of the fridge!")
                print("The bottom section has", bot.get('amount'), "space(s) left.")
                x = input("Do you still want to use the refrigerator? Y/N ")
                if x == "Y" or x == "y":
                    continue
                elif x == "N" or x == "n":
                    print("\n", "OK BYE!")
                    break
                else:
                    print("ERROR!!!")
                    continue

        elif x == "take" or x == "Take":
            x = input ("Which side do you want to use? Top/Mid/Bot ")
            if x == "top" or x == "Top":
                itemt = input ("What do you want to take? ")
                if not (itemt in top.keys()):
                    print (itemt.upper(), "is not in the fridge!")
                    x = input ("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
                else:
                    amt = int(input("Amount? "))
                    top.update({'amount': int(top['amount']) + amt})
                    print (amt , itemt, " has been taken from the top section of the refrigerator.")
                    print("The top section of the fridge has", top.get('amount'), "space(s) left")
                    x = input("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
            if x == "mid" or x == "Mid":
                itemm = input ("What do you want to take? ")
                if not (itemm in mid.keys()):
                    print (itemm.upper(), "is not in the fridge!")
                    x = input ("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
                else:
                    amt = int(input("Amount? "))
                    mid.update({'amount': int(mid['amount']) + amt})
                    print (amt , itemm, " has been taken from the middle section of the refrigerator.")
                    print("The middle section of the fridge has", mid.get('amount'), "space(s) left")
                    x = input("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
            if x == "bot" or x == "Bot":
                itemb = input ("What do you want to take? ")
                if not (itemb in bot.keys()):
                    print (itemb.upper(), "is not in the fridge!")
                    x = input ("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
                else:
                    amt = int(input("Amount? "))
                    bot.update({'amount': int(bot['amount']) + amt})
                    print (amt , itemb, " has been taken from the bottom section of the refrigerator.")
                    print("The bottom section of the fridge has", bot.get('amount'), "space(s) left")
                    x = input("Do you still want to use the fridge? Y/N ")
                    if x == "Y" or x == "y":
                        continue
                    elif x == "N" or x == "n":
                        print("\n", "OK BYE!")
                        break
                    else:
                        print("ERROR!!!")
                        continue
        else:
            print ("ERROR!!!")
            continue

    elif x == "N" or "n":
        print ("\n" , "OK BYE!")
        break
    else:
        print ("ERROR!!!")
        continue



