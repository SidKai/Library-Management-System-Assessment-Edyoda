#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from datetime import datetime, timedelta
class library:
    Purpose= "Admin access"

# list of book present in the library initially with unique book id    
    list_of_books={1000:{"Book Title": "Nights","Author Name":"Ellie Viesel","Total Pages":114, "Quantity Available":10,"ISBN":1234567891235,'Published Year':1998,"Description":"Biography"},1001:{"Book Title": "The Alchemist","Author Name":"Paulo Coelho", "Total Pages":180, "Quantity Available":10,"ISBN":1234567891236,'Published Year':2010,"Description":"Adventure"}}
# borrow history of each book with key as book id    
    borrow_history={}   
    list_of_admins={}
# list of borrower with full details and list of borrow history of each borrower
    list_of_borrowers={}
    login_borrowers=[]
    count=1001
    temp_list =[]
    
    def __init__(self):
        print("Library Management System")
        
# initial display to access program as an admin or borrower      
    def admin_home(self):
        self.start_action = input("Press 1 >> Admin \nPress 2 >> User\n")
        if self.start_action == '1':
            self.ad_action = input('Press 1 to Sign Up \nPress 2 to Log in\n')
            if self.ad_action == '1':
                self.new_admin()
            elif self.ad_action == '2':
                self.login_admin()
            else:
                print('Invalid Input')
                self.admin_home()
        elif self.start_action == '2':
            self.us_action = input('Press 1 to Sign Up \nPress 2 to Log in\n')
            if self.us_action == '1':
                self.borrower_signup()
            elif self.us_action == '2':
                self.borrower_login()
            else:
                print('Invalid Input')
                self.admin_home()
        
# new admin registration with unique username    
    def new_admin(self):
        print('Admin Sign Up>>')
        self.username = input("Enter Username:")
        self.password = input("Enter Password:")
        
        if self.username in library.list_of_admins: 
            print("The username is already taken.")
            self.new_admin()
        else:
            library.list_of_admins[self.username]=[self.password]
            print("New admin successfully added")
            time.sleep(1)
            self.login_admin()
        
# login for admin if already signed up    
    def login_admin(self):
        print("Admin Log in>>")
        self.username = input("Enter Username:")
        self.password = input("Enter Password:")
        
        if self.username in library.list_of_admins :
            if self.password in library.list_of_admins[self.username]:
                
                print("Logged in successfully")
                self.admin_log_in= True
                self.admin_mainmenu()
                
            else:
                print("Incorrect credentials")
                
                self.admin_log_in= False
                self.login_admin()
        else:
            print('Admin not signed in')
            self.new_admin()
            
# display list of operations admin can perform            
    def admin_mainmenu(self):
        self.main_menu_action = input('Press 1 >> Add New Book \nPress 2 >> View All Books \nPress 3 >> Issue Book \nPress 4 >> Return Book \nPress 5 >> Edit Book \nPress 6 >> Delete Book \nPress 7 >> Book Details \nPress 8 >> Add New Borrower \nPress 9 >> List of All Borrowers \nPress 0 >> Admin Logout\n ')
        if self.main_menu_action == '1':
            self.add_newbook()
        elif self.main_menu_action == '2':
            self.books_catalogue()
        elif self.main_menu_action == '3':
            self.issue_book()
        elif self.main_menu_action == '4':
            self.return_book()
        elif self.main_menu_action == '5':
            self.edit_book()
        elif self.main_menu_action == '6':
            self.del_book()
        elif self.main_menu_action == '7':
            self.book_detail()
        elif self.main_menu_action == '8':
            self.new_borrower()
        elif self.main_menu_action == '9':
            self.borrower_list()
        elif self.main_menu_action == '0':
            self.admin_logout()
        
# new borrower registration         
    def new_borrower(self):
        self.name= input("Enter Full Name:")
        self.dob= input("Enter Date of Birth (dd/mm/yyyy):")
        self.phn_no= input("Enter Contact No:")
        self.email= input("Enter Email ID:")
        self.password= input("Enter Password:")
        self.borrow_history= {"BookID": "admin use","Return Date":"admin use"}
        
        try:
            if self.admin_log_in==True:
            
                library.list_of_borrowers[self.email]={"Name":self.name,"Password":self.password,"Contact":self.phn_no,"Date of Birth":self.dob,"Borrow History":[self.borrow_history]}
                print("New borrower account created ")
                self.temp_action = input("Press 1 >> Enter New Borrower \nPress 0 >> Main Menu\n")
                if self.temp_action == '1':
                    self.new_borrower()
                elif self.temp_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid Input \nRedirecting...')
                    self.admin_mainmenu()
            
        except AttributeError:
            print('Admin not logged in')
        
        
# addition of new books into the stock with details       
    def add_newbook(self):
        library.count+=1
        self.book_id=library.count
        self.book_title= input("Book Title:")
        self.author_name= input("Author Name:")
        self.total_pages= int(input("Total Pages:"))
        self.quantity= int(input("Quantity Available:"))
        self.isbn= int(input("ISBN:"))
        self.pub_year = int (input('Published Year:'))
        self.description= input("Description:")
        
        try:
            if self.admin_log_in==True:
        
                library.list_of_books[self.book_id]={"Book Title":self.book_title,"Author Name":self.author_name,"Total Pages":self.total_pages,"Quantity Available":self.quantity,"ISBN":self.isbn,'Published Year':self.pub_year,"Description":self.description}
                library.borrow_history[self.book_id]= None
                time.sleep(1)

                print("Book",self.book_title,"added to the list of books")
                self.t_action = input("Press 1 >> Enter New Book \nPress 0 >> Main Menu\n")
                if self.t_action == '1':
                    self.add_newbook()
                elif self.t_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid Input \nRedirecting...')
                    self.admin_mainmenu()
                
        except AttributeError:
            print('Admin not logged in')
        
# list of all the books present in library with borrow history        
    def books_catalogue(self):
        try:
            if self.admin_log_in==True:
                print("Books Catalogue: \n")
                for key in library.list_of_books:
                    print('-------------------------------------------------------------------------------------------------------------------------')
                    print(key,':',library.list_of_books[key])
                self.te_action = input("Press 0 >> Main Menu\n")
                if self.te_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid Input \nRedirecting...')
                    self.admin_mainmenu()
                    
        except AttributeError:
            print('Admin not logged in')
            
            
# book detail of a particular book with unique book id and borrow history of that book    
    def book_detail(self):
        self.book_id= int(input("Enter Book ID:"))
        
        try:
            if self.admin_log_in==True:
                if self.book_id in library.list_of_books:

                    try:
                        print('---------------------------------------------------------------------------------------------------------------------')
                        print("Book Detail: \nBook ID:",self.book_id,"\n",library.list_of_books[self.book_id],'\n',"Book Borrow History:",library.borrow_history[self.book_id])
                        print('---------------------------------------------------------------------------------------------------------------------')
                    except AttributeError as a:
                        print("There are no books added in list. Please update list.")
                    self.tmp_action = input("Press 1 >> Book Detail of Other Book \nPress 0 >> Main Menu\n")
                    if self.tmp_action == '1':
                        self.book_detail()
                    elif self.tmp_action == '0':
                        self.admin_mainmenu()
                    else:
                        print('Invalid Input \nRedirecting...')
                        self.admin_mainmenu()
                else:
                    print("Book ID does not match")
                    self.admin_mainmenu()
                    
        except AttributeError:
            print('Admin not logged in')
            
            
# edit and update details of existing books    
    def edit_book(self):
        self.book_id = int(input('Enter Book ID of Book you want to Update: \n'))        
        try:
            if self.admin_log_in== True:
                if self.book_id in library.list_of_books:
                    edit_action = input("Select from the options to edit:\nPress 1 >> Book Title\nPress 2 >> Author Name\nPress 3 >> Total Pages \nPress 4 >> Quantity Available\nPress 5 >> ISBN \nPress 6 >> Published Year \nPress 7 >> Description \n ")
                    if edit_action == '1':
                        input_name = input('Enter New Book Title:')
                        library.list_of_books[self.book_id]["Book Title"] = input_name
                    elif edit_action == '2':
                        input_author = input('Enter New Author Name:')
                        library.list_of_books[self.book_id]['Author Name'] = input_author
                    elif edit_action == '3':
                        input_page = int(input('Enter No of Pages:'))
                        library.list_of_books[self.book_id] = input_page
                    elif edit_action == '4':
                        input_quan = int(input('Enter Quantity Available:'))
                        library.list_of_books[self.book_id]['Quantity Available'] = input_quan
                    elif edit_action == '5':
                        input_isbn = int(input('Enter New ISBN'))
                        library.list_of_books[self.book_id]['ISBN'] = input_isbn
                    elif edit_action == '6':
                        input_pub = int(input('Enter Published Year'))
                        library.list_of_books[self.book_id]['Published Year'] = input_pub
                    elif edit_action == '7':
                        input_desc = input('Enter New Description:')
                        library.list_of_books[self.book_id]['Description'] = input_desc
                else:
                    print('Book ID does not match. Please enter correct Book ID')
                    self.admin_mainmenu()
                    
                print("Detail of Book ID",self.book_id,"updated successfully")
                print(library.list_of_books[self.book_id]) 
                self.edit_action = input("Press 0 >> Main Menu\n")
                if self.edit_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid input \nRedirecting...')
                    time.sleep(1)
                    self.admin_home()
               
        except AttributeError:
            print('Admin not logged in')
            

# delete a particular book completely from the stock            
    def del_book(self):
        self.book_id= int(input('Enter ID of Book you want to delete: \n'))
           
        try:    
            if self.admin_log_in== True:
                if self.book_id in library.list_of_books:
                    del library.list_of_books[self.book_id]
                    time.sleep(1)
                    print('Removed Book ID',self.book_id)
                else:
                    print('Book ID does not match. Please enter correct Book ID')
                    self.admin_mainmenu()
                self.del_action = input("Press 1 >> Delete Another Book \nPress 0 >> Main Menu\n")
                if self.del_action == '1':
                    self.del_book()
                elif self.del_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid Input \nRedirecting...')
                    self.admin_mainmenu()
        except AttributeError:
            print('Admin not logged in')
        except:
            print('Book cannot be deleted. Error!')
            

# list of all the borrowers who have registered and borrow history of every borrower            
    def borrower_list(self):
        try:   
            if self.admin_log_in== True:
                for key in library.list_of_borrowers:
                    print('List of Registered Users:')
                    print('_________________________________________________________________________________________________________________________')
                    print(key,':',library.list_of_borrowers[key])
                    
                self.bor_action = input('Press 0 >> Main Menu\n')
                if self.bor_action == '0':
                    self.admin_mainmenu()
                else:
                    print('Invalid Input \nRedirecting...')
                    self.admin_mainmenu()
                    
        except AttributeError:
            print('Admin not logged in')
            

# issues new book to the existing borrower            
    def issue_book(self):
        self.book_id = int(input("Enter Book ID:"))
        self.email = input("Enter User Email ID:")
        
        try:
            if self.admin_log_in== True:
                if self.email in library.list_of_borrowers: 
                    if self.book_id in library.list_of_books:
                        if library.list_of_books[self.book_id]["Quantity Available"]!=0:

                            #updating issue date
                            self.issue_date=datetime.now()
                            self.return_date=None

                            #updating issue date in borrow history of list of borrower and borrow history of books
                            library.list_of_borrowers[self.email]["Borrow History"].append({"BookID":self.book_id,"Issue Date":self.issue_date,"Return Date":self.return_date})

                            library.temp_list.append({"email":self.email,"Issue Date":self.issue_date,"Return Date":self.return_date})
                            library.borrow_history[self.book_id] = library.temp_list

                            time.sleep(1)
                            print("Book ID",self.book_id,library.list_of_books[self.book_id]["Book Title"],"issued to",self.email, "at",self.issue_date)
                            library.list_of_books[self.book_id]["Quantity Available"]-=1

                            self.issue_action = input('Press 1 >> Issue Book Again \nPress 0 >> Main Menu\n')
                            if self.issue_action == '1':
                                self.issue_book()
                            elif self.issue_action == '0':
                                self.admin_mainmenu()
                            else:
                                print('Invalid Input \nRedirecting...')
                                self.admin_mainmenu()
                                
                        else:
                            print('Book ID does not match. Try Again')
                            self.issue_book()
                        
                    else:
                        print("Book Unavailable")
                        self.admin_mainmenu()
                else:
                    print("Customer not registered. Sign up first")
                    self.new_borrower()
        except AttributeError:
            print('Admin not logged in [Admin Access Only]')
            

# return book if issued to an existing borrower            
    def return_book(self):
        self.book_id= int(input('Enter Book ID:'))
        self.email= input('Enter Email ID of User:')
        
        try:
            if self.admin_log_in == True:
                for item in library.borrow_history[self.book_id]:
                        if item['email']==self.email and item['Return Date']== None:
                            for key in library.list_of_borrowers[self.email]['Borrow History']:
                                        if key['BookID'] == self.book_id and key['Return Date']== None:


                                            #initializing date of book return and calculating no fine duration
                                            self.return_date = datetime.now()
                                            no_fine_duration= self.issue_date + timedelta(days=14) 
                                            time_difference= no_fine_duration - self.issue_date
                                            fine_check= self.return_date - self.issue_date

                                            #iterating over borrow history of list of borrowers to update the return date 
                                            for item in library.list_of_borrowers[self.email]['Borrow History']:
                                                if item['BookID'] == self.book_id and item['Return Date']== None:
                                                    item["Return Date"]=self.return_date
                                            #iterating over borrow history of books to update the return date        
                                            for item in library.borrow_history[self.book_id]:
                                                if item['email']==self.email and item['Return Date']== None:
                                                    item["Return Date"]=self.return_date



                                            #checking if fine is applicable for a book
                                            if fine_check > time_difference:
                                                time.sleep(1)
                                                print("Applicable Fine - Rs. 100 ")
                                                print(self.book_id , library.list_of_books[self.book_id]["Book Title"],"returned by",self.email, "on",self.return_date)
                                                library.list_of_books[self.book_id]["Quantity Available"]+=1
                                                self.return_action = input("Press 0 >> Main Menu\n")
                                                if self.return_action == '0':
                                                    self.admin_mainmenu()
                                                else:
                                                    print('Invalid input \nRedirecting...')
                                                    time.sleep(1)
                                                    self.admin_home()
                                            else:
                                                time.sleep(1)
                                                print("Fine. No Fine ")
                                                print(self.book_id,library.list_of_books[self.book_id]["Book Title"],"returned by",self.email, "on",self.return_date)
                                                library.list_of_books[self.book_id]["Quantity Available"]+=1
                                                self.return_action = input("Press 0 >> Main Menu\n")
                                                if self.return_action == '0':
                                                    self.admin_mainmenu()
                                                else:
                                                    print('Invalid input \nRedirecting...')
                                                    time.sleep(1)
                                                    self.admin_home()
                                       
        except AttributeError:
            print('Admin not logged in [Admin Access Only]')
        except: 
            print('Something went wrong while trying to return the book')
            
            
# calculating time left to return the book in time for borrower display            
    def time_calc(self,email):
        
        
        for item in library.list_of_borrowers[self.email]["Borrow History"]:
            if item['Return Date']== None:
                self.issue_date= item['Issue Date']
                no_fine_duration= self.issue_date + timedelta(days=14)
                self.time_difference= no_fine_duration - datetime.now()
                return self.time_difference
            
            elif item['Return Date']== 'admin_use':
                pass
            
                
            
# to logout the current logged in admin        
    def admin_logout(self):
            self.admin_log_in= False
            print("Admin logged out.")
            print('Redirecting...')
            time.sleep(1)
            self.admin_home()
            
            
################################################################################################################################
# borrower class for borrrower side access            
class borrower(library):
    Purpose="Borrow Book"
    
    def __init__ (self):
        self.admin_home()
        
        
# new borrower signup with details with not already signup up by admin       
    def borrower_signup(self):
        print('Lets get signed up!')
        self.name= input("Full Name:")
        self.dob= input("Date of Birth (dd/mm/yyyy):")
        self.phn_no= input("Contact No:")
        self.email= input("Email ID:")
        self.password= input("Password:")
        self.borrow_history= {"BookID": "admin","Return Date":"admin_use"}

        if self.email in library.list_of_borrowers:
            print('Already Signed up by admin. Login with credentials')
            self.borrower_login()
        else:
            library.list_of_borrowers[self.email]={"Name":self.name,"Password":self.password,"Contact":self.phn_no,"Date of Birth":self.dob,"Borrow History":[self.borrow_history]}
            print("New User Account Created")
            self.borrower_login()
            
# login for signed up borrower        
    def borrower_login(self):
        print('User LOG IN!')
        self.email= input("Enter Email ID:")
        self.password= input("Enter Password:")

        if self.email in library.list_of_borrowers:
            if self.password in library.list_of_borrowers[self.email]["Password"]:
                print("User Logged in successfully")
                library.login_borrowers.append(self.email)
                self.borrower_log_in= True
                self.main_menu()
            else:
                print("Incorrect credentials")
                self.borrower_log_in= False
                self.borrower_login()
        else:
            print('User not signed up')
            self.borrower_signup()

# display list of currently issued books with remaining time for deadline            
    def view_current_books(self):

        try:
            if self.borrower_log_in == True:
                    if self.email in library.list_of_borrowers:

                        print('Current Issued Books:')
                        for item in library.list_of_borrowers[self.email]["Borrow History"]:
                                if item["Return Date"] == None:
                                    print('--------------------------------------------------------------------------------------------------------------------')
                                    print(item)

                                    #calling remaining time method
                                    self.time_calc(self.email)
                                    print("Remaining Time:",self.time_difference)
                                    


                                elif item["Return Date"] == "admin_use":
                                    pass


                        self.curr_action = input('Press 0 >> Main Menu\n')
                        if self.curr_action == '0':
                            self.main_menu()
                        else:
                            print('Invalid Input!')
                            print('Redirecting...')
                            time.sleep(1)
                            self.main_menu()

                    else: 
                        print('Email not found. Enter correct email')
                        self.main_menu()
        except AttributeError:
            print("User not logged in")
        except:
            print('Something went wrong in displaying books')
            
# display book details of currently issued books                            
    def issued_book_details(self):
        self.book_id= int(input("Enter Book ID:"))

        try:
            if self.borrower_log_in == True:

                if self.book_id in library.list_of_books:
                    for item in library.borrow_history[self.book_id]:
                        if item["Return Date"] == None:
                            print('------------------------------------------------------------------------------------------------------------------------')
                            print("Issued Book Detail:\n",library.list_of_books[self.book_id])
                            break
                        else:
                            print('No Book Issued Currently')
                            time.sleep(1)
                            print('Returning to Main Menu')
                            time.sleep(1)
                            self.main_menu()
                    self.bd_action = input('Press 0 >> Main Menu\n')
                    if self.bd_action == '0':
                        self.main_menu()
                    else:
                        print('Invalid Input!')
                        print('Redirecting...')
                        time.sleep(1)
                        self.main_menu()
                    
                else:
                    print('Book ID not in list')
                    self.main_menu()
        except AttributeError:
            print("User not logged in")
            
# display list of books borrowed in past
    def issue_history(self):
        self.logged_in_email=self.email

        try:
            if self.borrower_log_in == True:
                if self.logged_in_email in library.list_of_borrowers:
                    for item in library.list_of_borrowers[self.logged_in_email]["Borrow History"]:
                        if item["Return Date"] != None:
                            print('****************************************************************************************************************************')
                            print('Book Issue History:')
                            for key in library.list_of_borrowers[self.email]["Borrow History"]:   
                                 print(key)
                                
                            self.his_action = input('Press 0 >> Main Menu\n')
                            if self.his_action == '0':
                                self.main_menu()
                            else:
                                print('Invalid Input!')
                                print('Redirecting...')
                                time.sleep(1)
                                self.main_menu()

                            break
                        else:
                            print('No past record')
                            self.main_menu()
                else:
                    print('User not found')
                    self.admin_home()
        except AttributeError:
            print("User not logged in")
            
# display of list of operations user can perform
    def main_menu(self):
        print('-------------------------------MAIN MENU------------------------------------')
        self.main_action = input("Press 1 >> View Current Issued Books \nPress 2 >> Issued Book Details \nPress 3 >> Issue History \nPress 0 >> Log Out\n")
        if self.main_action == "1":
            self.view_current_books()
        elif self.main_action == "2":
            self.issued_book_details()
        elif self.main_action == "3":
            self.issue_history()
        elif self.main_action == '0':
            self.borrower_logout()
        else: 
            print(" Input does not match. Try again.")
            self.main_menu()
                
# to log out logged in borrower        
    def borrower_logout(self):
        try:
            if self.borrower_log_in == True:
                if self.email in library.login_borrowers:
                    library.login_borrowers.remove(self.email)
                    print('User logged out successfully')
                    self.borrower_log_in = False
                    self.admin_home()
                else: 
                    print('Already logged out or not logged in')
                    self.admin_home()
        except AttributeError:
                print("User not logged in")
      
                
        

admin=borrower()    


# In[ ]:


1

