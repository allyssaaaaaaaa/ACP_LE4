#Apritado, Allyssa Grace A.
#BSIT - 2108

import os 
doc_path = os.path.expanduser("~/Documents")

if not os.path.exists(doc_path):
    os.makedirs(doc_path)
    
while(True):
    print("-------Register Student-------")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == '1':
        print("------ Register Student --------")
        student_num = int(input("Student No.: "))
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        progRam = input("Program: ")
        age = int(input("Age: "))
        sex = input("Gender : ")
        bdate = input("Birthday : ")
        contact_num = int(input("Contact No : "))

        data = [
            f"Student No.: {student_num}",
            f"Last Name: {last_name}",
            f"First Name: {first_name}",
            f"Middle Name: {middle_name}",
            f"Program : {progRam}",
            f"Age : {age}",
            f"Gender : {sex}",
            f"Birthday : {bdate}",
            f"Contct No : {contact_num}",
        ]

        file_path = os.path.join(doc_path, f"{student_num}.txt")
        with open(file_path, "w") as f:
            for line in data:
                f.write(str(line) + "\n")

    elif choice == '2':
        try:
            student_num = input("Student No.: ")
            file_path = os.path.join(doc_path, student_num + ".txt")
            with open(file_path, "r") as f:
                content = f.read()
                print("----- Open Student Record -----")
                print(content)
        except FileNotFoundError:
            print("❌ Student record not found.")
            
            
    elif choice == '3':
        print("goodbye, nice try!")
        break
    else:
        print("Invalid") 
        break           
    
            
        

    
    
        
    

    
