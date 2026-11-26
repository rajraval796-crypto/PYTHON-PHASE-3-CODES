class Atm:
    def __init__(self,name,acc):
        self.name=name
        self.acc=acc
        self.pin=None
        self.bal=0
    def create_pin(self):
        self.pin=int(input(" ENTER YOUR PIN:"))
        self.bal=int(input("ENTER YOUR BALANCE:"))
        print("PIN CREATED SUCCESSFULLY!")
        print(f"THE PIN IS {self.pin} AND THE BALANCE IS {self.bal}")
        self.menu()
    def change_pin(self):
        old=int(input("ENTER YOUR CURRENT PIN:"))
        if self.pin==old:
            self.pin=int(input("ENTER NEW PIN:"))
            print("PIN CHANGED SUCCCESSFULLY!")
            self.menu()
        else:
                print("WORNG PIN ENTERED")
                self.menu()
    def check_balance(self):
            val=int(input("ENETR PIN:"))
            if self.pin==val:
                print(f"THE TOTAL BALANCE IS :{self.bal}")
                self.menu()
            else:
                 print("WORNG PIN")
                 self.menu()

    def withdrawl(self):
        v=int(input("ENTER PIN:"))
        if self.pin==v:
            withdraw=int(input("ENTER AMOUNT TO WITHDRAW:"))
            self.bal-=withdraw
            print(f" BALANCE AFTER WITHDRAWL IS:{self.bal}")
        else:
             print("WRONG PIN ENETRED")
        self.menu()
    def deposit(self):
        v=int(input("ENTER PIN:"))
        if self.pin==v:
            dep=int(input("ENTER AMOUNT TO WITHDRAW:"))
            self.bal+=dep
            print(f" BALANCE AFTER DEPOSIT IS:{self.bal}")
        else:
             print("WRONG PIN ENETRED")
        self.menu()

    def menu(self):
        print("1. CREATE PIN:")
        print("2. CHANGE PIN:")
        print("3. CHECK BALANCE:")
        print("4. WITHDRAW:")
        print("5. DEPOSIT:")
        print("6. EXIT")
        ch=int(input("ENTER YOUR CHOICE:"))

        if ch==1:
            self.create_pin()
        if ch==2:
            self.change_pin()
        if ch==3:
            self.check_balance()
        if ch==4:
            self.withdrawl()
        if ch==5:
            self.deposit()
        if ch==6:
             print("EXIT")

a=Atm("RAJ",734)
a.menu()
        