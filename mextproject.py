import csv
def create():
    c=0
    rec=[]
    with open('adhar_detail.csv','a', newline='') as f:
        add_data = csv.writer(f)
        while c==0:
            print('enter the adhar details to add record')
            while True:
                adhar_no=input('enter the adhar no.:')
                if len(str(adhar_no))==12 and adhar_no.isnumeric():
                    break
                else:
                    print('adhar no. must be 12 digits please try again')
            first_name=input('enter the first name:')
            last_name=input('enter thr last_name:')
            while True:
                age=input('enter the age:')
                if age.isnumeric() and int(age)>=18:
                    age=int(age)
                    break
                else:
                    print('age must be at least 18 years for adhar card')
            father_name=input('enter the father name:')
            mother_name=input('enter the mother name:')
            current_addr=input('enter the current address:')
            state=input('enter the state name:')
            dist=input('enter the district name:')
            while True:
                pin_code=input('enter the pin code:')
                if pin_code.isnumeric() and len(pin_code)==6:
                    pin_code=int(pin_code)
                    break
                else:  
                    print('pin code must be 6 digits please try again')
            records=[adhar_no,first_name,last_name,age,father_name,mother_name,current_addr,state,dist,pin_code]
            rec.append(records)
            ans=input('do you want to add more records y/n:')
            if ans.upper()!='Y':
                c+=1
        add_data.writerows(rec)
        print('record added successfully')
        

 
def display():
    with open('adhar_detail.csv','r') as f:
        adhar_no=int(input('enter the adhar no. to display the details:'))
        read_data=csv.reader(f)
        c=0
        for data in read_data:
            if len(data)>0 and str(adhar_no)==data[0]:
                c+=1
                print('record found successfully')
                ans=input('do you want to see the details y/n:')
                if ans.upper()=='Y':
                    print('here is the details:')
                    print(data)    
        if c==0:
            print('record not found')
                
def update():
    with open('adhar_detail.csv','r') as f:
        while True:
            adhar_no=input('enter the adhar no. to update the details:')
            if len(str(adhar_no))==12 and adhar_no.isnumeric():
                break
            else:   
                print('adhar no. must be 12 digits please try again')
        read_data=csv.reader(f)
        rec=[]
        for data in read_data:
            rec.append(data)
    with open('adhar_detail.csv','w',newline='') as f:
        update_data=csv.writer(f)
        for data in rec:
            if str(adhar_no)==data[0]:
                print('record found successfully')
                first_name=input('enter the first name:')
                last_name=input('enter thr last_name:')
                while True:
                    age=input('enter the age:')
                    if age.isnumeric() and int(age)>=18:
                        age=int(age)
                        break
                    else:
                        print('age must be at least 18 years for update adhar card')
                father_name=input('enter the father name:')
                mother_name=input('enter the mother name:')
                current_addr=input('enter the current address:')
                state=input('enter the state name:')
                dist=input('enter the district name:')
                while True:
                    pin_code=input('enter the pin code:')
                    if pin_code.isnumeric() and len(pin_code)==6:
                        pin_code=int(pin_code)
                        break
                    else:  
                        print('pin code must be 6 digits please try again')
                records=[adhar_no,first_name,last_name,age,father_name,mother_name,current_addr,state,dist,pin_code]
                update_data.writerow(records)
                print('record updated successfully')
            else:
                update_data.writerow(data)  


def delete():
    with open('adhar_detail.csv','r') as f:
        while True:
            adhar_no=input('enter the adhar no. to delete the details:')
            if len(str(adhar_no))==12 and adhar_no.isnumeric():
                break
            else:   
                print('adhar no. must be 12 digits please try again')
        read_data=csv.reader(f)
        rec=[]
        for data in read_data:
            rec.append(data)
    with open('adhar_detail.csv','w',newline='') as f:
        delete_data=csv.writer(f)
        for data in rec:
            if str(adhar_no)==data[0]:
                print('record found successfully')
                print('record deleted successfully')
            else:
                delete_data.writerow(data)
                
def admin_login():
    admin_token=0
    c=3
    for i in range(3):
        username=input('enter the username:')
        password=input('enter the password:')
        if username=='admin' and password=='admin123':
            print('login successful')
            admin_token=1
            break
        elif c>1:
            print('invalid username or password')
            c-=1
            print(f'you have {c} attempts left')
        else:
            print('you have exhausted all attempts')
            break
    if admin_token==1:
        while True:
            print('1.create\n2.display\n3.update\n4.delete\n5.exit')
            choice=input('enter your choice:')
            while True:
                if choice.isnumeric():
                    break
                else:
                    print('invalid input please enter a number')
                    choice=input('enter your choice:')
            if choice==1:
                create()
            elif choice==2:
                display()
            elif choice==3:
                update()
            elif choice==4:
                delete()
            elif choice==5:
                print('thank you for using adhar management system')
                break
            else:
                print('invalid choice please try again')
            
def create_user():
    with open('user_detail.csv', mode='w', newline='') as f:
        add_data = csv.writer(f)
        rec=[]
        while True:
            print('enter the user details to add record')
            username=input('enter the username:')
            password=input('enter the password:')
            records=[username,password]
            rec.append(records)
            ans=input('do you want to add more records y/n:')
            if ans.upper()!='Y':
                break
        add_data.writerows(rec)
        print('user record added successfully')

def user_login():
    username=input('enter the username:')
    password=input('enter the password:')
    with open('user_detail.csv','r') as f:
        read_data=csv.reader(f)
        c=0
        for data in read_data:
            if username==data[0] and password==data[1]:
                c+=1
                print('login successful')
            elif  username=='' and password=='':
                print('username and password cannot be empty')
                break
        if c==0:
            print('invalid username or password')
    if c==1:
        while True:
            print('1.display\n2.udate request\n3.apply for adhar card\n4.exit')
            choice=input('enter your choice:')
            while True:
                if choice.isnumeric():
                    break
                else:
                    print('invalid input please enter a number')
                    choice=input('enter your choice:')
            if choice==1:
                display()
            elif choice==2:
                update_adhardata_request()
            elif choice==3:
                apply_adharcard()
            elif choice==4:
                break
            else:
                print('invalid choice please try again')
            
import random
otp_generator=[random.randint(1000,9999) for _ in range(100)]
def forget_userpassword():
    username=input('enter the username:')
    with open('user_detail.csv','r') as f:
        read_data=csv.reader(f)
        c=0
        for data in read_data:
            if username==data[0]:
                c+=1
                otp=otp_generator.pop()
                print(f'your otp is:{otp}')
                entered_otp=int(input('enter the otp:'))
                if entered_otp==otp:
                    new_password=input('enter the new password:')
                    rec=[]
                    with open('user_detail.csv','r') as f:
                        read_data=csv.reader(f)
                        for data in read_data:
                            rec.append(data)
                    with open('user_detail.csv','w',newline='') as f:
                        update_data=csv.writer(f)
                        for data in rec:
                            if username==data[0]:
                                records=[username,new_password]
                                update_data.writerow(records)
                                print('password updated successfully')
                            else:
                                update_data.writerow(data)
                else:
                    print('invalid otp')
        if c==0:
            print('username not found')
            
def update_adhardata_request():
    print('your request to update adhar data has been sent to admin')
    print('admin will contact you soon')
    
def apply_adharcard():
    with open('adhar_apply.csv','a', newline='') as f:
        add_data = csv.writer(f)
        while True:
            print('enter the adhar application details to add record')
            first_name=input('enter the first name:')
            last_name=input('enter thr last_name:')
            while True:
                age=input('enter the age:')
                if age.isnumeric() and int(age)>=18:
                    age=int(age)
                    break
                else:
                    print('age must be at least 18 years for adhar card')
            father_name=input('enter the father name:')
            mother_name=input('enter the mother name:')
            current_addr=input('enter the current address:')
            state=input('enter the state name:')
            dist=input('enter the district name:')
            while True:
                pin_code=input('enter the pin code:')
                if pin_code.isnumeric() and len(pin_code)==6:
                    pin_code=int(pin_code)
                    break
                else:  
                    print('pin code must be 6 digits please try again')
            records=[first_name,last_name,age,father_name,mother_name,current_addr,state,dist,pin_code]
            add_data.writerow(records)
            print('application submitted successfully')
            break
def main_menu():
    while True:
        print('1.admin login\n2.user login\n3.create user\n4.forget user password\n5.exit')
        while True:
            choice=input('enter your choice:')
            if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
                if choice==1:
                   admin_login()
                elif choice==2:
                    user_login()
                elif choice==3:
                    create_user()
                elif choice==4:
                    forget_userpassword()
                elif choice==5:
                    print('thank you for using adhar management system')
                    print(70*'-')
                    break
            else:
                print('invalid choice please try again')
                continue  
        
print(70*'-')
print('welcome to adhar management system')
main_menu()
    