import pymongo
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["Teachers"]
collection = db["Teachers_Data"]
##collection.insert_many([{"Name":"John","Email":"john@gmail.com","Designation":"HOD","Address":"Pune","Age":30,"Contact":1111111111},{"Name":"Jack","Email":"jack@gmail.com","Designation":"Professor","Address":"Pune","Age":50,"Contact":2222222222},{"Name":"Andrew","Email":"Andrew@gmail.com","Designation":"Professor","Address":"Mumbai","Age":40,"Contact":3333333333}])

#print("Enter Member's detail :")
 #staffMember =input("Name:").split() print("Email:").split() input("Designation:") 
''' name = input("Name: "),
        email = input("Email: "),
        designation = input("Designation: "),
        address = input("Address: "),
        age = int(input("Age: ")),
        contact = int(input("Contact: ")), '''

#Creating Function to get multiple staff details
def add_staff_members():
#Creating List to save all details of members
    staff_list = []
#Creating loop to get as many details as we want of members
    while True:
        print("Enter Staff Members detail:")
        name = input()
        email = input()
        designation = input()
        address = input()
        age = int(input())
        contact = int(input())
         #creating dictionary for it 
        staff_member = {
         "Name" : name,
         "Email" : email,
         "Designation": designation,
         "Address": address,
         "Age": age,
         "Contact": contact
        }
        #To get all dictionary values into list
        staff_list.append(staff_member)

     #if user want to add more details 
        add_another = input("Add another staff member?(yes/no):").strip().lower()
        if add_another != "yes":
             break
    if staff_list:
      collection.insert_many(staff_list)
      print("Staff members added successfully!")
      
    
    
add_staff_members()



