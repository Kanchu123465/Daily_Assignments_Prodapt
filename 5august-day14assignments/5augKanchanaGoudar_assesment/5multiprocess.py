import multiprocessing,time
def Prime():
    for i in range(10,500):
        for j in range(2,i):
            time.sleep(1)
            if(i%j==0):
                break
        else:
            print(i,"prime number")

        
def palindrome(number):
    temp=number
    rev=0
    while number>0:
        time.sleep(1)
        rem=number%10
        rev=rev*10+rem
        number=number//10
        
    if temp==rev:
        print("palindrome")
        
    else:
        print("not a palindrome")
if(__name__=="__main__"):
    number=int(input("Enter the number to check it is palindrome number or not:"))
    
    p1=multiprocessing.Process(target=Prime)
    p2=multiprocessing.Process(target=palindrome,args=(number,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


