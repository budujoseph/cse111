def myname(number1, number2):
    
    return number1 + number2

def main():
    number1 = float(input("Enter Your First Number: "))
    number2 = float(input("Enter Your Second Number: "))
    
    sum = myname(number1, number2)
    print(sum)

if __name__ == "__main__" :
    main()