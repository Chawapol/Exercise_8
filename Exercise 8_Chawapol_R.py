userInput = input("Username :")
passInput = input("Password :")

print("**********Chawapol's Shop**********")
if userInput == "Chawapol" and passInput == "123456":
    print("Pass !!")
    print("*********************************")
    print("Price Lists :")
    print("Apple      50 THB/Kg")
    print("Orange     100 THB/Kg")
    print("*********************************")
    print("Please Select Number of item below :")
    print("(1) Apple ")
    print("(2) Orange ")
    numberSelected = int(input("Number : "))
    if numberSelected == 1 :
        print("Apple  50  THB/Kg")
        print("How many kilograms do you want ?")
        kiloOfApple = int(input())
        print("You Selected Apple :", kiloOfApple,"kg")
        priceOfApple = kiloOfApple * 50
        print("Price of Apple :", priceOfApple, "THB")
        print("*********************************")
        print("Do you want anything else ?")
        print("(2) Orange ")
        print("(3) No, I don't.")
        numberSelectedApple = int(input("Number :"))
        if numberSelectedApple == 2:
            print("Orange  100  THB/Kg")
            print("How many kilograms do you want ?")
            kiloOfOrange = int(input())
            print("You Selected Orange :", kiloOfOrange, "kg")
            priceOfOrange = kiloOfOrange * 100
            print("Price of Orange :", priceOfOrange, "THB")
            print("*********************************")
            ResultPriceApple = priceOfApple
            ResultPriceOrange = priceOfOrange
            ResultKiloApple = kiloOfApple
            ResultKiloOrange = kiloOfOrange
            totalPrice = priceOfApple + priceOfOrange
            print("==============invoice============")
            print("Apple", kiloOfApple, "kg" , priceOfApple, "THB")
            print("Orange", kiloOfOrange, "kg", priceOfOrange, "THB" )
            print("=================================")
            print("Total       ", totalPrice,"THB")
            print("=================================")
        elif numberSelectedApple == 3:
            ResultPriceApple = priceOfApple
            ResultKiloApple = kiloOfApple
            totalPrice = priceOfApple
            print("==============invoice============")
            print("Apple", kiloOfApple, "kg", priceOfApple, "THB")
            print("=================================")
            print("Total       ", totalPrice, "THB")
            print("=================================")
    elif numberSelected == 2 :
        print("Orange  50  THB/Kg")
        print("How many kilograms do you want ?")
        kiloOfOrange = int(input())
        print("You Selected Orange :", kiloOfOrange,"kg")
        priceOfOrange = kiloOfOrange * 50
        print("Price of Apple :", priceOfOrange, "THB")
        print("*********************************")
        print("Do you want anything else ?")
        print("(1) Apple ")
        print("(3) No, I don't.")
        numberSelectedOrange = int(input("Number : "))
        if numberSelectedOrange == 1:
            print("Apple  50  THB/Kg")
            print("How many kilograms do you want ?")
            kiloOfApple = int(input())
            print("You Selected Apple :", kiloOfApple, "kg")
            priceOfApple = kiloOfApple * 100
            print("Price of Apple :", priceOfApple, "THB")
            print("*********************************")
            ResultPriceApple = priceOfApple
            ResultPriceOrange = priceOfOrange
            ResultKiloApple = kiloOfApple
            ResultKiloOrange = kiloOfOrange
            totalPrice = priceOfApple + priceOfOrange
            print("==============invoice============")
            print("Apple", kiloOfApple, "kg", priceOfApple, "THB")
            print("Orange", kiloOfOrange, "kg", priceOfOrange, "THB")
            print("=================================")
            print("Total       ", totalPrice, "THB")
            print("=================================")
        elif numberSelectedOrange == 3:
            ResultPriceOrange = priceOfOrange
            ResultKiloOrange = kiloOfOrange
            totalPrice = priceOfOrange
            print("==============invoice============")
            print("Apple", kiloOfOrange, "kg", priceOfOrange, "THB")
            print("=================================")
            print("Total       ", totalPrice, "THB")
            print("=================================")
else:
    print("Username or Password is incorrect. Please try Again !!")