#Apritado, Allyssa Grace A.
#BSIT - 2108

import os

docpath = os.path.expanduser("~/Documents")

if not os.path.exists(docpath):
    os.makedirs(docpath)

while(True):
    print("===== Student Records Menu =====")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit ")
    
    choice =  int(input("Enter your choice: "))
    
    print()
    
    if choice == 1:
        print("===== Register Student =====")
        student_no = int(input("Student No.: "))
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        program = input("Program: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        birthday= input("Birthday: ")
        contact_no = int(input("Contact No.: "))
        
        data = [
            {"Student No." : student_no},
            {"Last Name" : last_name},
            {"First Name" : first_name},
            {"Middle Name" : middle_name},
            {"Program" : program},
            {"Age" : age},
            {"Gender" : gender},
            {"Birthday" : birthday},
            {"Contact No." : contact_no}
        ]

        file_path = os.path.join(docpath, f"{student_no}.txt")
        with open(file_path, "w") as f:
            for line in data:
                f.write(str(line) + "\n")

        print(f"✅ Student record saved to: {file_path}")

    elif choice == 2:
        try: 
            print("===== Open Student Record =====")
            
            student_no = int(input("Enter Student No.: "))
           
            
            file_path = os.path.join(docpath, f"{student_no}.txt")
            if os.path.exists(file_path):
                print(f"✅ Student record found: {file_path}")
                with open(file_path, "r") as f:
                    for line in f:
                        print(line.strip())
            else:
                print("✖️ Student record not found.")

        except FileNotFoundError:
            print("✖️ Student record not found.")
    
    elif choice == 3:
        print("Exiting the program... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
