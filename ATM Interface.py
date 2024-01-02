import pickle
import os
import sys
#************************************************************************
def create_record():
    print("\n")
    f=open("atm.dat", 'ab')
    while True:
        L=[]
        uid = input("\nEnter the User ID: ")
        L.append(uid)
        pin = input("\nEnter the Pin: ")
        L.append(pin)
        balance = float(input("\nEnter the balance: "))
        L.append(balance)
        for i in range(10):
            L.append('Empty');
        pickle.dump(L, f)
        ch=input("Do you want to enter more records?(Y/N) ")
        if ch in 'yY':
            continue
        else:
            break
    f.close()
#************************************************************************
def id_check(user):
    flag=0
    print("\n")
    try:
        f=open("atm.dat", 'rb')
    except FileNotFoundError:
        print("File not found")
        return
    sr=user
    try:
        while True:
            R=pickle.load(f)
            if R[0]==sr:
                flag=1
                break
    except EOFError:
        print("Wrong details...")
    f.close()
    return flag
#************************************************************************
def pin_check(user):
    flag=0
    print("\n")
    try:
        f=open("atm.dat", 'rb')
    except FileNotFoundError:
        print("File not found")
        return
    sr=user
    try:
        while True:
            R=pickle.load(f)
            if R[1]==sr:
                flag=1
                break
    except EOFError:
        print("Wrong details...")
    f.close()
    return flag
#************************************************************************
def withdraw(user):
    print("\n")
    try:
        f=open("atm.dat", 'rb+')
    except FileNotFoundError:
        print("File not found")
        return
    A=float(input("Enter Amount to withdraw:"))
    pos=0
    try:
        while True:
            R=pickle.load(f)
            if R[0]==user:
                f.seek(pos)
                if(R[2]>A):
                    R[2]=R[2]-A
                    print("Money Withdrawn...Record updated")
                    for i in range(3,12):
                        R[i+1]=i
                    s="Withdrawn "+str(A)
                    R[3]=s
                    pickle.dump(R, f)
                    break
                elif(R[2]<A):
                    print("Insufficient Balance");
                    break
                break
            else:
                pos=f.tell()
    except EOFError:
        print("Record not found")
    f.close()    
#************************************************************************
def deposit(user):
    print("\n")
    try:
        f=open("atm.dat", 'rb+')
    except FileNotFoundError:
        print("File not found")
        return
    A=float(input("Enter Amount to deposit:"))
    pos=0
    try:
        while True:
            R=pickle.load(f)
            if R[0]==user:
                f.seek(pos)
                R[2]=R[2]+A
                print("Money Deposited...Record updated")
                for i in range(3,12):
                    R[i+1]=i
                s="Deposited "+str(A)
                R[3]=s
                pickle.dump(R, f)
                break
            else:
                pos=f.tell()
    except EOFError:
        print("Record not found")
    f.close()    
#************************************************************************
def transaction_history(user):
    print("\n")
    f=open("atm.dat", "rb")
    try:
        while True:
            R=pickle.load(f)
            if R[0]==user:
                f.seek(pos)
                print("Last 10 Transactions : \n\n")
                for i in range(3,13):
                    print(R[i],"\n")
    except EOFError:
        f.close()    
#************************************************************************
def transfer(user):
    print("\n")
    try:
        f=open("atm.dat", 'rb+')
    except FileNotFoundError:
        print("File not found")
        return
    A=float(input("Enter Amount to transfer:"))
    K=input("Enter Account Number to transfer:")
    pos=0
    try:
        while True:
            R=pickle.load(f)
            if R[0]==user:
                f.seek(pos)
                if(R[2]>A):
                    R[2]=R[2]-A
                    print("Money Successfully transferred to account number ",K,"...Record updated")
                    for i in range(3,12):
                        R[i+1]=i
                    s="Transferred "+str(A)+" to "+K
                    R[3]=s
                    pickle.dump(R, f)
                    break
                elif(R[2]<A):
                    print("Insufficient Balance");
                    break
                break
            else:
                pos=f.tell()
    except EOFError:
        print("Record not found")
    f.close()    
#************************************************************************
def log_out():
    print("\n")
    sys.exit("\nSession Logged Out Successfully\nThank you")
#************************************************************************
#To create new records remove '#' from the start of next line.
#create_record()
chances=3    
user_id=(input("Enter your User ID: "))
ans=id_check(user_id)
if ans==1:
    while (chances!=0):
        user_pin=(input("Enter your Pin: "))
        ans=pin_check(user_pin)
        if ans==1:
            while True:    
                print("\n\n")
                print("\t\tMAIN MENU")
                print("*********************************************")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Transaction History")
                print("4. Transfer")
                print("5. Log Out")
                print("*********************************************")

                choice=int(input("Enter your choice between 1 to 5---->"))

                if choice==1:
                    withdraw(user_id)
                elif choice==2:
                    deposit(user_id)
                elif choice==3:
                    transaction_history(user_id)
                elif choice==4:
                    transfer(user)
                elif choice==5:
                    log_out()
                else:
                    print("\nWrong Choice!\n\nTry again")
        else:
            chances=chances-1
            print("Wrong Pin, Please Try Again...Attempts Left : ",chances)
    else:
        log_out()



#END OF PROJECT
