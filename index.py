import Return
import Borrow
  

print()
print("--------------------------------------------------------------------------------------------")
print("--------------------------WELCOME TO THE LIBRARY MANAGEMENT SYSTEM--------------------------")
print("------------------------------------By Sugam Dangal-----------------------------------------")
print()
print("                      Please enter your desired input to run the program                    ")
# Read from booklist.txt and display booklist
def read_booklist():
    with open("booklist.txt","r") as reading:
        file_content = reading.readlines()
        for each_list in file_content:
            book_list.append(each_list.replace("\n",",").split(","))
        print("---------------------------------------------------------------------------------------")
        
        print("Book id\t\tBook name\t\tAuthor\t\t\tQuantity\tPrice($)")
        print("---------------------------------------------------------------------------------------")
        for each_list in book_list:
            
            print(f"{each_list[0]}\t\t{each_list[1]}\t\t{each_list[2]}\t\t{each_list[3]}\t\t{each_list[4]}")
            
  

# Main loop for user input
user = "a"
while user != "4":
    book_list = []
    
         
    user = input("\nEnter 1 to display book information\nEnter 2 to borrow book\nEnter 3 to return book\nEnter 4 to exit program\n>> ").lower()
    if user=="1":
       read_booklist()
    elif user == "2":
       read_booklist()
       print()
       Borrow.borrow_book(book_list)
    elif user == "3":   
        print()
        Return.return_book(book_list)
    elif user == "4":
        print("Thank You For Visiting")
        break
    else:
        print()
        print("Please enter a valid keyword")
    print()



