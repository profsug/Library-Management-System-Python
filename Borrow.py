import datetime
import Database

# Main borrow function
def borrow_book(book_list):
    chk_name = False
    borrower_name = input("Enter borrower's name: ").lower()
    with open("name_list.txt","r") as reading_name:
        file_content = reading_name.read().replace("\n","").split(",")
        for name in file_content:
            if borrower_name == name: # Check if borrow's name already exists in name_list.txt
                chk_name = True
        if chk_name == True:
            old_name(borrower_name,book_list)
        else:
            new_name(borrower_name,book_list)

# Borrow for alrerady existing members
def old_name(name,book_list):
    borrow_list = []
    user = "y"
    with open(f"members/{name}.txt", "r") as reading:
        file_content = reading.readlines()
        old_book = []
        for each_list in file_content:
            old_book.append(each_list.replace("\n", "").split(","))
    while user == "y":
        try:
            chk_bookid = False
            book_id = int(input("Enter book id: "))
            for each_list in book_list:
                if book_id == int(each_list[0]): # Check if book id is correct
                    chk_bookid = True
                    for each_element in old_book:
                        if each_element[0] == each_list[1] and each_element[4] == "not returned": # Check if borrower has already borrowed specified book
                            print(f"{name} has already borrowed {each_list[1]}")
                        else:
                            if int(each_list[3]) > 0:  # Check if book is in stock
                                borrow_list.append(each_list)
                            else:
                                print(f"{each_list[1]} is currently out of stock.")
                            break
            if chk_bookid == False:
                print("Please enter correct book id.")
            user = input("Do you want to borrow another book(y/n)? ").lower()
        except:
            print("Please enter correct book id.")
    if len(borrow_list) > 0:
        old_write(name,borrow_list,book_list)
    else:
        print("No books were borrowed.")

# Append in existing file of old member
def old_write(name,borrow_list,book_list):
    total_amount = 0
    for each_list in borrow_list:
        total_amount += float(each_list[4])
    print("Total amount:", total_amount)
    paid = input("Has total amount been paid(y/n)? ").lower()
    if paid == "y": # Check to see if book price have been paid
        with open(f"members/{name}.txt","a") as writing:
            for each_list in borrow_list:
                today_date = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
                deadline = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%d-%m-%y %H:%M")
                line = f"{each_list[1]},{each_list[4]},{today_date},{deadline},not returned\n"
                writing.write(line)
        Database.booklist_update("b",borrow_list,book_list)
    else:
        print("Books were not borrowed.")

# Borrow process for new members
def new_name(name,book_list):
    chk_bookid = False
    borrow_list = []
    user = "y"
    while user == "y":
        try:
            book_id = int(input("Enter book id: "))
            for each_list in book_list:
                if book_id == int(each_list[0]): # Check if book id is correct
                    chk_bookid = True
                    if int(each_list[3]) > 0: # Check if book is in stock
                        borrow_list.append(each_list)
                    else:
                        print(f"{each_list[1]} is currently out of stock.")
            if chk_bookid == False:
                print("Please enter correct book id.")
            user = input("Do you want to borrow another book(y/n)? ").lower()
        except:
            print("Please enter correct book id.")
    if len(borrow_list) > 0:
        new_write(name,borrow_list,book_list)
    else:
        print("No books were borrowed.")

# Create a new txt file for new member
def new_write(name,borrow_list,book_list):
    total_amt = 0
    for each_list in borrow_list:
        total_amt += float(each_list[4])
    print("Total amount:",total_amt)
    paid = input("Has total amount been paid(y/n)? ").lower()
    if paid == "y": # Check to see if book price have been paid
        with open("name_list.txt","a") as appending:
            appending.write(f"{name}\n")
        with open(f"members/{name}.txt","w") as writing:
            for each_list in borrow_list:
                today_date = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
                deadline = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%d-%m-%y %H:%M")
                line = f"{each_list[1]},{each_list[4]},{today_date},{deadline},not returned\n"
                writing.write(line)
        Database.booklist_update("b",borrow_list,book_list)
    else:
        print("Books were not borrowed.")
