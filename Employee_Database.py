print()
print('WELCOME TO THE DATABASE')
print()
print('Following operations you can perform: \n1) add_emp, 2)edit_emp, 3)get_emp')
z=input('Please Enter from the above 3 choices: ')
print()
if z=='add_emp':
    while True:
        i=int(input('Enter the Employee number whose details you want to enter: '))
        emp={}
        def empinfo(a):
            name=input('Enter the name: ')
            email=input('Enter the Email_Id: ')
            number=input('Enter the number: ')
            location=input('Enter the location: ')
            emp['name '+str(i)]=name
            emp['Email_Id '+str(i)]=email
            emp['number '+str(i)]=number
            emp['location '+str(i)]=location
        empinfo(i)
        print()
        print('Do you want to add New Employee Details to the Database')
        n=input('If yes then enter YES and if no enter NO: ')
        while True:
            if n=='YES':
                i=int(input('Enter the Employee number whose details you want to enter: '))
                empinfo(i)
                print('Do you want to add New Employee Details to the Database')
                n=input('If yes then enter YES and if no enter NO: ')
            else:
                break
        break

import pickle

my_file=open('Database add_emp','wb')
pickle.dump(emp,my_file)
my_file.close()

my_file=open('Database add_emp','rb')
emp=pickle.load(my_file)

print()
print('Following operations you can perform: \n1) add_emp, 2)edit_emp, 3)get_emp')
z=input('Please Enter from the above 3 choices: ')
print()
if z=='edit_emp':
    while True:
        i=int(input('Enter the Employee Number Whose Details you want to edit: '))
        print('Enter the Detail you want to edit')
        editvar=int(input('Enter 1 if you want to edit name\nEnter 2 if you want to edit Email_Id\nEnter 3 if you want to edit number\nEnter 4 if you want to edit location\nEnter 5 if you want to edit all details: '))

        
        def editinfo1(a):
                name=input('Enter the name: ')
                emp['name '+str(i)]=name
                
        def editinfo2(a):
                email=input('Enter the Email_Id: ')
                emp['Email_Id '+str(i)]=email
                
        def editinfo3(a):
                number=input('Enter the number: ')
                emp['number '+str(i)]=number
                
        def editinfo4(a):
                location=input('Enter the location: ')
                emp['location '+str(i)]=location
                
        def editinfo5(a):
                name=input('Enter the name: ')
                email=input('Enter the Email Id: ')
                number=input('Enter the number: ')
                location=input('Enter the location: ')
                emp['name '+str(i)]=name
                emp['Email_Id '+str(i)]=email
                emp['number '+str(i)]=number
                emp['location '+str(i)]=location
             
        if editvar==1:        
            editinfo1(i)

        elif editvar==2:
            editinfo2(i)
                
        elif editvar==3:
            editinfo3(i)

        elif editvar==4:
            editinfo4(i)

        elif editvar==5: 
            editinfo5(i)
        
        print()
        print('Do you want to edit another Employee Details in the Database')
        n=input('If yes then enter YES and if no enter NO: ')
        while True:
            if n=='YES':
                i=int(input('Enter the Employee number whose details you want to edit: '))
                print('Enter the Detail you want to edit')
                editvar=int(input('Enter 1 if you want to edit name\nEnter 2 if you want to edit Email_Id\nEnter 3 if you want to edit number\nEnter 4 if you want to edit location\nEnter 5 if you want to edit all details: '))
                if editvar==1:
                    editinfo1(i)
                elif editvar==2:
                    editinfo2(i)
                elif editvar==3:
                    editinfo3(i)
                elif editvar==4:
                    editinfo4(i)
                elif editvar==5:
                    editinfo5(i)
                print('Do you want to edit another Employee Details in the Database')
                n=input('If yes then enter YES and if no enter NO: ')
            else:
                break
        break

    
my_file=open('Database edit_emp','wb')
pickle.dump(emp,my_file)
my_file.close()

my_file=open('Database edit_emp','rb')
emp=pickle.load(my_file)

print()
print('Following operations you can perform: \n1) add_emp, 2)edit_emp, 3)get_emp')
z=input('Please Enter from the above 3 choices: ')
print()
if z=='get_emp':
      while True:
        i=int(input('Enter the Employee Number Whose Details you want to get: '))
        print('Enter the Detail you want to get about the Employee')
        getvar=int(input('Enter 1 if you want to get name\nEnter 2 if you want to get Email_Id\nEnter 3 if you want to get number\nEnter 4 if you want to get location\nEnter 5 if you want to get all details: '))

        
        def getinfo1(a):
            print('Name: ',emp['name '+str(i)])

        def getinfo2(a):
            print('Email_Id: ',emp['Email_Id '+str(i)])

        def getinfo3(a):
            print('Number: ',emp['number '+str(i)])

        def getinfo4(a):
            print('Location: ',emp['location '+str(i)])

        def getinfo5(a):
            print('Name:',emp['name '+str(i)],'Email_Id:',emp['Email_Id '+str(i)],'Number:',emp['number '+str(i)],'Location:',emp['location '+str(i)])

        if getvar==1:
            getinfo1(i)
        elif getvar==2:
            getinfo2(i)
        elif getvar==3:
            getinfo3(i)
        elif getvar==4:
            getinfo4(i)
        elif getvar==5:
            getinfo5(i)

        print()
        print('Do you want to get another Employee Details')
        n=input('If yes then enter YES and if no enter NO: ')
        while True:
            if n=='YES':
                i=int(input('Enter the Employee number whose details you want to get: '))
                print('Enter the Detail you want to get')
                getvar=int(input('Enter 1 if you want to get name\nEnter 2 if you want to get Email_Id\nEnter 3 if you want to get number\nEnter 4 if you want to get location\nEnter 5 if you want to get all details: '))
                if getvar==1:
                    getinfo1(i)
                elif getvar==2:
                    getinfo2(i)
                elif getvar==3:
                    getinfo3(i)
                elif getvar==4:
                    getinfo4(i)
                elif getvar==5:
                    getinfo5(i)
                print()
                print('Do you want to get another Employee Details')
                n=input('If yes then enter YES and if no enter NO: ')
            else:
                break
        break

print()
print('Following operations you can perform: \n1) add_emp, 2)edit_emp, 3)get_emp')
z=input('Please Enter from the above 3 choices: ')
            


































        

    





