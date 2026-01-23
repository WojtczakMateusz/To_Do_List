
# Create todo list app that supports 4 commands:
# - ADD <task_description>
# - REMOVE <task_id>
# - DONE <task_id>
# - LIST
# You can use the app via cli
# > ADD "Do laundry"
# Added "Do laundry" to the task list with id=1
# > LIST
# 1 [ ] "Do laundry"
# > DONE 1
# > LIST
# 1 [X] "Do laundry"
# > REMOVE 1
# > LIST
# No tasks on the list



list_of_to_dos = {}
i=0
def dodaj(message):
    global i
    task = {"description": message, "done": False, "index": i}
    list_of_to_dos[i] = task
    i=i+1

def list_of_things():
    i=0
    for message in list_of_to_dos.values():
        # 1: [X?] <description>
        if(message["done"] == False):
            print(str(message["index"])+":"+ "[ ]" +message["description"])
        else:
            print(str(message["index"])+":"+ "[X]" +message["description"])

        i+=1

def remove_from_list(index):
    indexing = int(index)
    del list_of_to_dos[indexing]

def done(index):
    indexing = int(index)
    list_of_to_dos[indexing]['done'] = True

print("Use only words:"+""+"ADD, LIST, REMOVE, EXIT")
first_information = ""
while (first_information != "EXIT"):
    print('>', end='')
    first_information = input()
    two_information = first_information.split(" ")
    information = two_information[0]

    if(information == "ADD"):
        message = two_information[1]
        dodaj(message)
    if(information == "LIST"):
        list_of_things()
    if(information == "REMOVE"):
        message = two_information[1]
        remove_from_list(message)
    if(information == "DONE"):
        message = two_information[1]
        done(message)
