def myname(number1, number2):
    number1 = float(input("Enter Your First Number: "))
    number2 = float(input("Enter Your Second Number: "))
    
    return number1 + number2

def main():
    sum = myname()
    print(sum)

if __name__ == "__main__" :
    main()