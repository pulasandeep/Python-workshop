contact_application={}
def store(name,number):
    if (name not in contact_application):
        contact_application.setdefault(name,number)
        print("contact saved!")
    else:
        print('Name already exists in contacts')
        
        
def display():
    if(len(contact_application)!=0):
        for i,j in contact_application.items():
            print(i,j)
    else:
        print("empty contacts")

        
def delete(name):
    if(name not in contact_application.keys()):
        print("name not found!")
    else:
        contact_application.pop(name)
        print('contact deleted.')
        
        
def search(name):
    if(name not in contact_application.keys()):
        print(name,"contact exists")
    else:
        print(name,'contact doesnt exists')

    