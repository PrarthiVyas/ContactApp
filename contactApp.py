names=[]
numbers=[]
def addcontact():
    print("Add contact")
    name=input("Name: ")
    no=input("Number: ")
    names.append(name)
    numbers.append(no)
    #return lst
    
def findcontact():
    print("Find Number")
    name=input("Enter a name which you want to find: ")
    if name not in names:
        print("Sorry,This contact is not in the list")
    else:
        x=names.index(name)
        print(names[x],"----->",numbers[x])
    
def listcontacts():
    if len(names)==0:
        print("List is empty")
    else:
        for i in range(len(names)):
            print("Name:",names[i])
            print("Number:",numbers[i])
        
def editcontacts():
    print("Edit contact")
    name=input("Enter a name which you want to edit: ")
    if name not in names:
        print("Sorry,This contact is not in the list")
 
    
    else:
        x=names.index(name)
        numbers[x]=input("Enter new number: ")
        print(names[x],"----->",numbers[x])
        
def deletecontacts():
    print("Delete Contact")
    name=input("Enter a name which you want to delete: ")
    if name not in names:
        print("Sorry,This contact is not in the list")
 
    else:
        x=names.index(name)
        print(names[x],"is removed")
        names.remove(names[x])
        numbers.remove(numbers[x])
        
    
while True:
    print("\n\t Contacts")
    print("1. Add number")
    print("2. Find number")
    print("3. List Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. QUIT")


    choice=int(input("Enter a choice no: "))

    if choice==1:
        addcontact()

    if choice==2:
        findcontact()
    if choice==3:
        listcontacts()
    if choice==4:
        editcontacts()
    if choice==5:
        deletecontacts()
    if choice==6:
        break
