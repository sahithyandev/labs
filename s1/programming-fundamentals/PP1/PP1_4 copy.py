n=input('Enter the number: ') 
if int(n)>=1 and int(n) <1000: 
    reverse=n[::-1]#reversing the n
    if n == reverse:
        print('The number ',n, 'is a palindrome.')
    else:
        for i in range(0,25):
            n=int(reverse)+int(n)
            n=str(n)
            reverse=n[::-1]
            if n==reverse:
                print('The number ',n, 'is a palindrome.')
                break # to stop the loop when a palindrome number is got
            else:
                continue #to iterate the loop until the palindrome is got
        else:
            print("Palindrome obtained through the above process is too long")
else:
    None 
