import csv
import os
f,lc,m=0,0,0
fieldnames=['name','roll','gender','physics','maths','chemistry']
while True:
    user_input=input("Enter 1 to add 2 to search")
    if user_input=='1':
        try:
            if os.stat('student_details.csv').st_size >0:
                pass
            else:
                with open('student_details','a+',newline='\n') as f1:
                    writer=csv.DictWriter(f1,fieldnames=fieldnames)
                    writer.writeheader()
        except OSError:
            with open('student_details','a+',newline='\n') as f1:
                writer=csv.DictWriter(f1,fieldnames=fieldnames)
                writer.writeheader()
        try:
            with open('student_details','a+',newline='\n') as file1:
                writer=csv.DictWriter(file1,fieldnames=fieldnames)
                user_data=input('Enter the data').split( )
                writer.writerow({fieldnames[0]:user_data[0],fieldnames[1]:user_data[1],fieldnames[2]:user_data[2],fieldnames[3]:user_data[3],fieldnames[4]:user_data[4],fieldnames[5]:user_data[5]})
        except Exception:
            print('Enter the fields correctly')
    elif user_input=='2':
        try:
            with open('student_details','r+',newline='\n') as file2:
                reader=csv.DictReader(file2)
                user_search=input('Enter the field').lower()
                if user_search in fieldnames:
                    val=input('Enter the value')
                    for i in reader:
                        if i[user_search].lower()==val.lower() or i[user_search].upper()==val.upper() or i[user_search].title()==val.title():
                            print(i)
                            m=1
                else:
                    print('Field Not Found')
                    m=1
                if m==0:
                    print('Value Not Found')
                f=0
                m=0
        except Exception:
                print('Create the file first')
    else:
        print('Enter the input correctly')
                
            
                        
        
