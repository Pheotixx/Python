import os
import shutil
import random
class Atm(object):
    def __init__(self,cardNumber, pin,userName):
        self.cardNumber = cardNumber
        self.pin = pin
        self.userName = userName

    def cashWithdrawal(self):
        cardNumber1 = input("Enter your 9 digit card number: ")
        pin = input("Enter your 4 digit pin: ")
        if pin == self.pin and cardNumber1 == self.cardNumber:
            withdrawalMoney = input("How much money do you want to withdraw? ")
            print("Withdrawing "+withdrawalMoney+" rupees...")
            print("Successfully withdrawed "+withdrawalMoney+" rupees")
        elif pin != self.pin : 
            print("You entered a wrong pin.")
        else:
            print("You entered a wrong card number.")

    def balanceEnquiry(self):
        cardNumber1 = input("Enter your 9 digit card number: ")
        pin = input("Enter your 4 digit pin: ")
        if pin == self.pin and cardNumber1 == self.cardNumber:
            currentBalance = str(random.randint(100000,550000))
            print("Your current account balance is "+currentBalance+" rupees")
        elif pin != self.pin:
            print("You entered a wrong pin.")
        else:
            print("You entered a wrong card number.")

cardNumber = input("Set your 9 card number: ")
pin = input("Set you card's 4 digit pin: ")
userName = input("Enter the name you want to register your account with: ")

bankAccount = Atm(cardNumber, pin, userName)
atmOperations = input("Do you want to withdraw money or check your account balance? ")
 
if(atmOperations == "Withdraw" or atmOperations == "withdraw" or atmOperations == "Withdrawal" or atmOperations == "withdrawal"):
    bankAccount.cashWithdrawal()

elif(atmOperations == "Account Balance" or atmOperations == "Account balance" or atmOperations == "account balance" or atmOperations == "account Balance"
    or atmOperations == "accountbalance" or atmOperations == "AccountBalance" or atmOperations == "ACCOUNT BALANCE" or atmOperations == "ACCOUNTBALANCE"
    or atmOperations == "balance" or atmOperations == "Balance" or atmOperations == "Check Balance" or atmOperations == "check balance"):
    bankAccount.balanceEnquiry()

