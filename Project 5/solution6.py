def EvenTotal(number):
    eventotal=0
    while number > 0:
        digit=number%10
        number//=10
        ckeven=digit
        if ckeven % 2 ==0:
            eventotal+=digit
    return eventotal

def main():
    number=int(input("Enter a 10 digit number or more: \t "))
    if number<999999999:
        print("Enter atleast 10 digits")
    else:
        eventotal=EvenTotal(number)
        print("Total of a all even number =",eventotal)

if __name__ == '__main__':
    main()