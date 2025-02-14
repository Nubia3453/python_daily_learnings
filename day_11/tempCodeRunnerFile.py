def add_new_item():
        contact=[]
        name=input('Name:')
        mobile=input('Mobile:')
        email=fake.email()
        contact.append(mobile)
        contact.append(email)
        my_dict[name]=contact
        print('added successfuly')

add_new_item()