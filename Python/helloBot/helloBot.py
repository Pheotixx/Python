name = (input("What is your name? "))
age = (input("What is your age? "))

task = str(input("What would you like to know? Your age or name? "))

if task == "Name":
    print("Hello. Your name is "+name)
elif task == "Age":
    print("Hello. Your age is "+age)
elif task == "Name and Age" or task == "Age and Name":
    print("Hello. Your name is "+name+". Your age is "+age+".")
