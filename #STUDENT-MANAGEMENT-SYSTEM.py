#STUDENT-MANAGEMENT-SYSTEM
students={}
while(True):
    print("---------------STUDENT-MANAGEMENT-SYSTEM-------------")
    print("1. Add student")
    print("2. view student")
    print("3. search student")
    print("4.update student")
    print("5.Delete student")
    print("6.add marks and subjects")
    print("7. EXIT")

    choice = int(input(" ENTER YOUR CHOISE: "))
    
    if choice == 1:
        name= input("STUDENT NAME: ")
        Rollno=int(input(" ENTER ROLL NO: "))
        branch= input("ENTER BRANCH: ")
           

        students[Rollno]={"name":name,"branch":branch}
        print(students)
    
        print("-----student data added successfully-----")

    elif choice == 2:
        if not students:
            print("NO STUDENT FOUND!!!")
        else:
            for k,v in students.items():
                print("roll no:",k,v)
                print("----------------------------------")
    elif choice == 3:
        print("===========SEARCHING STUDENTS DATA==========")
        Rollno=int(input("rollNo of the student: "))
        if Rollno in students:
            print("DATA OF THE STUDENT;ROLL NO: ",Rollno)
            print(students.get(Rollno))
        else:
            print("!!!Roll no not found!!!!")


    elif choice == 4:
        print("========= update students branch=========")
        Rollno=int(input("ENTER ROLL NO: "))
        if Rollno in students:

            new_branch=input("enter NEW branch: ")
            students[Rollno]["branch"]=new_branch
            print("===============UPDATED DETAILS===============")
            for k,v in students.items():
                
                print("roll no:",k,v)
                print("---------------------------------------------")
        else:
            print("roll no not FOUND!!")

    elif choice == 5:
        print("==========DELETING STUDENTS DATA==========")
        Rollno=int(input("ENTER ROLL NO: "))
        if Rollno in students:
            print("deleted students data;",students.pop(Rollno))
            print("AFTER DELETING:: ")
            print(students)
        else:
            print("!!!!!!!!!  ROLL NO NOT FOUND  !!!!!!!!!")

    elif choice == 6:
        print("==========ADD MARKS===========")   
        Rollno=int(input("ENTER ROLL NO: "))
        if Rollno in students:    
            subjects= input("ENTER THE subjects: ")
            marks=int(input("Enter the marks ; "))
            students[Rollno].setdefault("subject", {})[subjects] = marks
            

            print("MARKS AND SUBJECT SUCCESSFULLY ADDED")
            print(students)
        else :
            print("roll no not found!")
    elif choice==7:
        print("!!!YOU ARE EXITING STUDENT-MANAGEMENT-SYSTEM!!")
        print("-------THANK YOU-------")
        break
    else:
        print("SORRY! YOU HAVE ENTERED AN INVALID CHOICE !!!!!")
        print("!! PLEASE try AGAIN !!")


    




        
           