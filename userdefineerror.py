def main():
    try:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplcation")
        print("4. Division")
        choice = int(input("Enter your choice(1/2/3/4) :"))
        x = int(input("Enter number 1 :"))
        y = int(input("Enter number 2 :"))
        if choice == 1:
            result1 = x+y
            print(result1)
        elif choice == 2:
            result2 = x-y
            print(result2)
        elif choice == 3:
            result3 = x*y
            print(result3)
        elif choice == 4:
            if y != 0:
                result = x/y
                print(result)
            else:
                print("con't divide")
    except ZeroDivisionError:
        print("Con't divied by 0")
    except ValueError:
        print("Enter valid number")
    else:
        print("number are :",x,y)
    finally:
        print("calculator created")
if __name__=="__main__":
    main()        

        


           
