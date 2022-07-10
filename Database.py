# Update booklist
def booklist_update(return_type,user_list,book_list):
    if return_type == "b": # Update booklist after borrowing books
        for each_list in user_list:
            for each_book in book_list:
                if each_book[1] == each_list[1]:
                    each_book[3] = str(int(each_book[3]) - 1)
        with open("booklist.txt","w") as writing:
            for each_book in book_list:
                writing.write(f"{each_book[0]},{each_book[1]},{each_book[2]},{each_book[3]},{each_book[4]}\n")
        print("Books have been succefully borrowed.")
    elif return_type == "r": # Update booklist after returning books
        for each_list in user_list:
            for each_book in book_list:
                if each_book[1] == each_list[0]:
                    each_book[3] = str(int(each_book[3]) + 1)
        with open("booklist.txt","w") as writing:
            for each_book in book_list:
                writing.write(f"{each_book[0]},{each_book[1]},{each_book[2]},{each_book[3]},{each_book[4]}\n")
        print("Books have been succefully returned.")
        
