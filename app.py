import os

def create_file(filename):
    try:
        with open(filename, 'x') as f :
            print(f"file Name {filename}: created sucessfully ")
    except FileExistsError:
        print(f"file Name{filename} already exist")

    except Exception as E:
        print("an error occurred")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found !")
    else:
        print("Files in directory")
        for file in files:
            print(file) 

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename } has been deleted sucessfully")
    except FileNotFoundError:
        print("File not found")

    except Exception as e :
        print("An error occured!") 

def read_file(filename):
    try:
        with open('sample.txt', 'r')as f :
            content = f.read() 
            print(f"content of'{filename}' :\n{content} ")

    except FileNotFoundError:
        print(f"{filename} does not exist!")

    except Exception as e :
        print("An error occurred!")

def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f :
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print("content added to {filename} sucessfully")

    except FileNotFoundError:
        print(f"{filename} does not exist!")
    
    except Exception as e :
        print("an error occured!")

def main():
    while True:
        print("File Management App")
        print("1:create file ")
        print("2:view files")
        print("3:delete file") 
        print("4:read file")
        print("5:edit file ")
        print("6:exit")
        
        choice = input("enter your choice(1-6) = ")

        if choice =='1':
            filename=input("enter the file name to create ")
            create_file(filename)
        elif choice== '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter the file you want to delete = ")
            delete_file(filename)

        elif choice =='4':
            filename = input("Enter the file name you want  to read =")
            read_file(filename)

        elif choice =='5':
            filename = input("Enter the file you want to edit = ")
            edit_file(filename)

        elif choice =='6':
            print("closing the app......")
            break

        else:
            print("invalid syntax!")
if __name__ =="__main__":
    main()
