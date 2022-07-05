#This is a simple Health Management System using python.
#In this program we can log or retrive data about a client
#Here we are using pyton dictionary for storing the client name
#Using file system for storing details about client



print("\t\t\t\t\t...WELCOME TO HEALTH MANAGEMENT SYSTEM...\t\t\t\t\t")           

client_list = {1: "Rohit", 2: "Subha", 3: "Rahul"}
log_list = {1: "Exercise", 2: "Diet"}

#For adding new client to our program
print("Want to add new client ? y/n:",end="")
x=input()

while(x != "n"):
    print("Enter client name : ", "\n", end="")
    c_name = input()
    i = client_list.__len__()+1
    client_list[i] = c_name

    x = input("ADD MORE ? y/n:")
    continue


#For log or retrive the data about clients
def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value,"\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op == 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value,"\n", end="")
        log_name =  int(input())
        print("Selected Job : ", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k != "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        log_name =  int(input())
        print(client_list[client_name], "-", log_list[log_name], "Report :","\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Data not found")
