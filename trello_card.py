import requests

# API Key and Token: Log into the data collection Trello account, then follow the links for the key and token
# Key: https://trello.com/app-key
# Token: https://trello.com/app-key and follow the hyperlink with the text Token on it

# api key and token (might need to be updated periodically)
key = ""
token = ""

# To find a card id (without creating a new card), you can click on a card in Trello manually and type .json after
# the link, and the id will be one of the first things that shows up in the json dump. Otherwise, the card id that
# you are creating will be stored in the variable as the script runs

# current card id
card_id = 0

# Label ids should stay the same and to set for Summer 2019 Coops. To find new label ids if needed, use the get_labels()
# function and copy paste them into the variables

# label ids
no_distance = "5b903bf79c16fb124acc1b89"
no_main_cam = "5b903bf79c16fb124acc1b88"
tripod = "5b903bf79c16fb124acc1b8b"
high_pri = "5d0badd24fee1002fad8787b"
skip = "5b913b0b5d7a3d6a876e9ea0"
skip_distance = "5b903bf79c16fb124acc1b94"
low_pri = "5d24e4e17a6c9e72f7473451"
no_video = "5d4adccd5a23971797bbda9b"
no_data = "5c93dbc036fc1271d677f75a"
race = "5c3def39a7387124e79a44ca"
no_ubias = "5d443f6879b87e8a94dc0801"

# Checklist ids should also stay the same, but might need to be updated based on changes. To find these changes, use
# get_checklists() to find the first three checklists on a template card, and you can index the string to find more if
# needed

# checklist ids
collection_cl = "5d5eab953cb6445bc6421471"
video_cl = "5d5eabfa93d65e7af05642ac"
timing_cl = "5d5eac305053ac7b09de3488"

# Member ids can be found using get_member and copying pasting from the json file. We have included the dc id for you,
# and set the others to blank. Must be changed in add_card!!

# member ids
dc = "5d49bb25d73d338715c72bde"
mz = "5cd04943491e0321bffd959c"

# List ids should not change unless something drastic happens, but you can get it with get_lists()
# and the board id (VHiraN7x) or (5b903bf7b40c8612509f6615). Later on, if you want to add a card to a different list,
# then you can ask the user to input a list in the add_card() function

# list ids
ccr_list = "5b903c534d0f073d0cc79d32"
wvp_list = "5b9141bc2e284d5b3367034b"
bl_list = "5c374f05cc43c8865e49069c"
bltv_list = "5d4adc9e7a916d1a9737414a"
vica_list = "5d24d32b6e2b95121890348a"
dta_list = "5b903c609899883976aa7f6d"
dda_list = "5b90434c18a87a21570db648"
rc_list = "5b904365d0bb7f26c7f8238e"
cbs_list = "5b9aafa4a7fd0a81cb7d314f"
sc_list = "5be4713421ce5d7721d74c5c"
up_list = "5b90435103e8ca03c51e0e3b"
ou_list = "5c374bf2d32ee887b5f0880a"
q_list = "5cd04f443d2dfe1cf7d290ae"


# create_card() takes in a string (name of a card) and creates a card on a specific list and returns the id
def create_card(name):
    global card_id 
    url = "https://api.trello.com/1/cards"
    querystring = {"name": f"{name}", "pos": "top",
                   "idList": "5b903c534d0f073d0cc79d32", "keepFromSource": "all",
                   "key": f"{key}",
                   "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    description = response.text
    card_id = description[7:31]
    print(card_id)


# copy_card() takes in a already existing card id copies an already existing card
def copy_card(id):
    global card_id
    url = "https://api.trello.com/1/cards"
    querystring = {"pos": "top",
                   "idList": "5b903c534d0f073d0cc79d32",
                   "idCardSource": f"{id}",
                   "keepFromSource": "all",
                   "key": f"{key}",
                   "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    description = response.text
    card_id = description[7:31]
    print(card_id)


# label_ids() takes in a board id and finds the labels on a board
def get_labels(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/labels"
    querystring = {"fields": "name, id", "limit": "50", "key": f"{key}", "token": f"{token}"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


# add_label() takes in a card id and a label id and adds that label to the card
def add_label(id, label_id):
    url = f"https://api.trello.com/1/cards/{id}/idLabels"
    querystring = {"value": f"{label_id}", "key": f"{key}", "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    print(response.text)


# get_lists() takes in a board id and gets the list ids of the board
def get_lists(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    querystring = {"cards": "none", "card_fields": "all", "filter": "open", "fields": "all", "key": f"{key}",
                   "token": f"{token}"}

    response = requests.request("GET", url, params=querystring)

    print(response.text)


# get_checklists() takes in a card id and gets checklist ids for a specific card
def get_checklists(id):
    global checklist1
    global checklist2
    global checklist3
    url = f"https://api.trello.com/1/cards/{id}/checklists"
    querystring = {"checkItems": "none", "filter": "all", "fields": "none", "key": f"{key}", "token": f"{token}"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
    description = response.text
    checklist1 = description[8:32]
    checklist2 = description[42:66]
    checklist3 = description[76:100]


# get_completed_items() takes in a card id and prints only checked off items on that card
def get_completed_items(id):
    url = f"https://api.trello.com/1/cards/{id}/checkItemStates"
    querystring = {"fields": "idCheckItem", "key": f"{key}", "token": f"{token}"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


# check_item_states() takes a checklist id and prints all items and their states
def check_item_states(checklist_id):
    url = f"https://api.trello.com/1/checklists/{checklist_id}/checkItems"
    querystring = {"fields":"state","key":f"{key}","token":f"{token}"}
    response = requests.request("GET", url, params=querystring)
    description = response.text
    print(description)


# add_checklist() takes in a card id and a checklist id and adds a checklist to the top of the card
def add_checklist(id, checklist_id):
    url = "https://api.trello.com/1/checklists"
    querystring = {"idCard": f"{id}", "pos": "top", "idChecklistSource": f"{checklist_id}",
                   "key": f"{key}", "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    print(response.text)


# add_comments() takes in a card id and a string and adds a comment to a card
def add_comments(id, text):
    url = f"https://api.trello.com/1/cards/{id}/actions/comments"
    querystring = {"text": f"{text}", "key": f"{key}", "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    print(response.text)


# add_description() takes in a card id and a string and adds a description to a card
def add_description(id, text):
    url = f"https://api.trello.com/1/cards/{id}"
    querystring = {"desc": f"{text}", "key": f"{key}", "token": f"{token}"}
    response = requests.request("PUT", url, params=querystring)
    print(response.text)


# get_members() takes in a card id and gets member IDs on a card
def get_member(id): 
    url = f"https://api.trello.com/1/cards/{id}/members"
    querystring = {"fields": "none", "key": f"{key}", "token":f"{token}"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)


# add_member() adds a member to a card
def add_member(id, member_id):
    url = f"https://api.trello.com/1/cards/{id}/idMembers"
    querystring = {"value": f"{member_id}", "key": f"{key}", "token": f"{token}"}
    response = requests.request("POST", url, params=querystring)
    print(response.text)


# delete_card() deletes a card by its id
def delete_card(id):
    url = f"https://api.trello.com/1/cards/{id}"
    querystring = {"key": f"{key}", "token": f"{token}"}
    response = requests.request("DELETE", url, params=querystring)
    print(response.text)


# month_converter() takes in a number (01-12) and  converts numbers to short form months
def month_converter(number):
    if number == "01":
        return "Jan"
    elif number == "02":
        return "Feb"
    elif number == "03":
        return "Mar"
    elif number == "04":
        return "Apr"
    elif number == "05":
        return "May"
    elif number == "06":
        return "Jun"
    elif number == "07":
        return "Jul"
    elif number == "08":
        return "Aug"
    elif number == "09":
        return "Sep"
    elif number == "10":
        return "Oct"
    elif number == "11":
        return "Nov"
    elif number == "12":
        return "Dec"


# add_card() adds all of the necessary things to a card
def add_card():
    prompt = input("Welcome! Do you know your collection record tag or would you like us to generate one for you?\n"
                   "1. Collection Record Tag Known\n2. Generate a Tag\n")
    if prompt == "2":
        date = input("What date was the collection on? (YYYY/MM/DD)?\n")
        year = date[0:4]
        print(year)
        month_letters = month_converter(date[5:7])
        print(month_letters)
        day = date[8:10]
        print(day)
        time = input("Was it an AM or PM session?\n1. AM\n2. PM\n")
        club = input("What club was the swimmer from?\n")
        name = input("What was their name? (ex. John Bird -> JohnB)\n")
        device = input("What was the device number? (UTxxx)\n")
        length = input("was the pool 25 or 50 metres?\n1. 25m\n2. 50m\n")
        if time == "1":
            if length == "1":
                tag = year + month_letters + day + "_AM_" + club + "_" + name + "_UT" + device + "_25m"
            elif length == "2":
                tag = year + month_letters + day + "_AM_" + club + "_" + name + "_UT" + device + "_50m"
        elif time == "2":
            if length == "1":
                tag = year + month_letters + day + "_PM_" + club + "_" + name + "_UT" + device + "_25m"
            elif length == "2":
                tag = year + month_letters + day + "_PM_" + club + "_" + name + "_UT" + device + "_50m"
        else:
            print("Invalid input! This script will restart.")
            add_card()
        create_card(tag)
    elif prompt == "1":
        tag_name = input("Enter the collection tag: ")
        print(tag_name)
        create_card(tag_name)
    else:
        print("You didn't pick a valid option. This script will restart.")
        add_card()

    member = input("Enter your member initials.\n") 
    if member.lower() == 'dc':
        add_member(card_id, dc)
    elif member.lower() == 'mz': 
        add_member(card_id, mz) 
    else: 
        other = input("Member not found.\n 1. Continue\n 2. Start over?\n")
        if other == '2': 
            add_card()
    
    checklist = input("Is this collection a main cam or tripod video?\n1. Main cam\n2. Tripod\n")
    if checklist == "1":
        add_checklist(card_id, timing_cl)
        add_checklist(card_id, video_cl)
        add_checklist(card_id, collection_cl)
    elif checklist == "2":
        add_label(card_id, tripod)
        add_label(card_id, no_main_cam)
        add_checklist(card_id, timing_cl)
        add_checklist(card_id, video_cl)
        add_checklist(card_id, collection_cl)
    labels = input("What additional labels would you like on the card?\n0. None\n1. No Distance\n2. Skip\n"
                   "\3. High Priority\n4. Low Priority\n5. Skip Distance\n6. No Data\n7. No Video\n8. Cannot Ubias\n"
                   "9. Race\n")
    print(labels)
    print(card_id)
    for x in labels:
        if x == "0":
            break
        elif x == "1":
            add_label(card_id, no_distance)
        elif x == "2":
            add_label(card_id, skip)
        elif x == "3":
            add_label(card_id, high_pri)
        elif x == "4":
            add_label(card_id, low_pri)
        elif x == "5":
            add_label(card_id, skip_distance)
        elif x == "6":
            add_label(card_id, no_data)
        elif x == "7":
            add_label(card_id, no_video)
        elif x == "8":
            add_label(card_id, no_ubias)
        elif x == "9":
            add_label(card_id, race)
        else:
            delete_continue = input("Invalid option chosen.\n1. Continue creating the card\n2. Delete the card\n")
            if delete_continue == "2":
                delete_card(card_id)
                return

    description = input("Would you like you add a description of your swimmer?\n1: Yes\n2: No\n")
    if description == "1":
        description_text = input("Please enter your description below.\n")
        add_description(card_id, description_text)

    comment = input("Are there any comments you would like to add on the card?\n1: Yes\n2: No\n")
    if comment == "1":
        comment_text = input("Please enter your comment below.\n")
        add_comments(card_id, comment_text)

    print("Card successfully created!")


add_card()
