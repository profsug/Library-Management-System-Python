import datetime
import Database


# Main return function
def return_book(book_list):
    return_list = []
    check_name = check_book = False
    return_name = input("Enter returner's name: ").lower()
    print()
    with open("name_list.txt","r") as name_file:
        names = name_file.read().replace("\n",",").split(",")
    for each_name in names:
        if return_name == each_name:
            check_name = True
            with open(f"members/{return_name}.txt","r") as reading:
                file_content = reading.readlines()
                for each_list in file_content:
                    return_list.append(each_list.replace("\n", "").split(","))
                print("Book name\t\tPrice($)\tBorrow date\t\tDeadline\t\tStatus")
                for each_list in return_list:
                    if each_list[4] == "not returned":
                        print(f"{each_list[0]}\t\t{each_list[1]}\t\t{each_list[2]}\t\t{each_list[3]}\t\t{each_list[4]}")
            print()
            book_name = input("Enter book's name: ").title()
            for each_list in return_list:
                if each_list[0] == book_name and each_list[4] == "not returned":
                    check_book = True
                    book_return(return_name,book_name,return_list,book_list)
            if check_book == False:
                print()
                print(f"{return_name} has not borrowed {book_name}.")
                print() 
    if check_name == False:
        print()
        print(f"{return_name} has not borrowed any books.")

# Modify .txt of book returning member
def book_return(name,book,return_list,book_list):
    paid = "y"
    for each_list in return_list:
        if each_list[0] == book and each_list[4] == "not returned":
            deadline = datetime.datetime.strptime(each_list[3], "%d-%m-%y %H:%M")
            date_now = datetime.datetime.now()
            if date_now > deadline: # Check to see if return is within deadline
                diff = (date_now - deadline).days
                fine = (float(each_list[1]) * (40/100) * int(diff))
                print("Past deadline")
                print(f"Please pay fine of {fine:.1f}")
                print()
                paid = input("Has fine been paid(y/n)? ").lower()
            else:
                print()
                print("Within deadline")
                
                
    if paid == "y": # Check if fine is paid
        change = []
        with open(f"members/{name}.txt", "w") as writing:
            for each_list in return_list:
                if each_list[0] == book and each_list[4] == "not returned":
                    each_list[4] = "returned"
                    change.append(each_list)
            for each_list in return_list:
                line = f"{each_list[0]},{each_list[1]},{each_list[2]},{each_list[3]},{each_list[4]}\n"
                writing.write(line)
        Database.booklist_update("r",change,book_list)
    else:
        print()
        print("Books were not returned.")
