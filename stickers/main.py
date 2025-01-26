#
#
#       Written by : Jourdan Rampoldi
#       description: Automation of creating personalized labels 
#       to be printed.
#
#

import pandas as pd
import os
import template_to_label, create_template




def main():
        menu()

def menu():
    #attempt to read sheet
    try:
        sheet = pd.read_csv("dropspreadsheet/current.csv")    
    except:
        print("File not found. Check file name in \'dropspreadsheet\' Directory. ")
    

    user_selection = 0
    #print menu
    while(user_selection != 4):
        grab_show_data(sheet)
        print("\n--------    Select options   --------")
        print(" 1. Get Order Data. ")
        print(" 2. Create Templates for Labels.")
        print(" 3. Create Labels. ")
        print(" 4. Quit. ")
        user_selection = int(input("\nSelection: "))

        if user_selection == 1:
            data_menu(sheet)
        elif user_selection == 2:
            prepare_templates(sheet)
        elif user_selection == 3:
            prepare_the_labels(sheet)
        elif user_selection == 4:
            quit()
        else:
            print("Not a valid entry.")

def grab_show_data(sheet):
    print("\n######################################\n")
    print("Date Range: ", sheet["Sale Date"][len(sheet.index) - 1], "-", sheet["Sale Date"][1])
    print("Number of Orders:", len(sheet.index) - 1)
    print("\n######################################")

def data_menu(sheet):
    user_selection = 0
    while(user_selection != 4):
        print("\n-----   Select options (Data)   -----\n")
        print(" 1. Search order info. ")
        print(" 2. View amount by color. ")
        print(" 3. View amount by date. ")
        print(" 4. Return home. ")

        user_selection = int(input("\nSelection: "))

        if user_selection == 1:
            index = []
            search_name = input("Enter name: ")
            for i in (sheet.index):
                if search_name.lower() in sheet["Variations"][i].lower():
                    index.append(i)
            print("\n---- Search Results for ", search_name, ": ----") 
            for i in index:
                color_ind_start = sheet["Variations"][i].find("Color:")
                picture_ind_start = sheet["Variations"][i].find("Picture on Trailer of Truck:")
                name_ind_start = sheet["Variations"][i].find("Personalization:")
                CHAR_RANGE_COLOR = 6
                CHAR_RANGE_PIC = 28
                CHAR_RANGE_NAME = 16
                color_pick = sheet["Variations"][i][color_ind_start+CHAR_RANGE_COLOR:picture_ind_start - 1]
                picture_pick = sheet["Variations"][i][picture_ind_start+CHAR_RANGE_PIC:name_ind_start - 1]
                name_pick = sheet["Variations"][i][name_ind_start+CHAR_RANGE_NAME:]
                amount_ordered = sheet["Quantity"][i]
                print(f"\nName: \033[1m{name_pick}\033[0m\tColor: \033[1m{color_pick}\033[0m\tPicture: \033[1m{picture_pick}\033[0m\tQuantity: {amount_ordered}")

        elif user_selection == 2:
            red = 0
            orange = 0
            purple = 0
            blue = 0
            CHAR_RANGE_COLOR = 6
            for i in sheet.index:
                color_ind_start = sheet["Variations"][i].find("Color:")
                picture_ind_start = sheet["Variations"][i].find("Picture on Trailer of Truck:")
                color_pick = sheet["Variations"][i][color_ind_start+CHAR_RANGE_COLOR:picture_ind_start - 1]

                if color_pick == "Red":
                    red += 1
                elif color_pick == "Orange":
                    orange += 1
                elif color_pick == "White-Purple letters":
                    purple += 1
                elif color_pick == "Blue":
                    blue += 1
                else:
                    continue

            print(f"Order amount by colors: ")
            print(f"\t\033[1mRed:\033[0m{red}\n")
            print(f"\t\033[1mOrange:\033[0m{orange}\n")
            print(f"\t\033[1mBlue:\033[0m{blue}\n")
            print(f"\t\033[1mPurple:\033[0m{purple}\n")            
        elif user_selection == 3:
            pass

        elif user_selection == 4:
            return
        else:
            print("Not a valid entry. ")

def prepare_templates(sheet):
    os.popen("rm labels/*")
    order_vars = sheet["Variations"].tolist()
    order_amt = sheet["Quantity"].tolist()
    order_type = sheet["Listing ID"].tolist()

    CHAR_RANGE_COLOR = 6
    CHAR_RANGE_COLOR_CAB = 13
    CHAR_RANGE_PIC = 28
    CHAR_RANGE_NAME = 16

    label_order = [0, 0, 0, 0]
    for i in range(len(order_vars)):
        listing_id = order_type[i]

        if (listing_id == 956902557):
            color_ind_start = order_vars[i].find("Color:")
            picture_ind_start = order_vars[i].find("Picture on Trailer of Truck:")
            name_ind_start = order_vars[i].find("Personalization:")

            color_pick = order_vars[i][color_ind_start+CHAR_RANGE_COLOR:picture_ind_start - 1]
            picture_pick = order_vars[i][picture_ind_start+CHAR_RANGE_PIC:name_ind_start - 1]
            name_pick = order_vars[i][name_ind_start+CHAR_RANGE_NAME:]

            if color_pick == "White-Purple letters":
                color_pick = "Purple"

            if picture_pick == "Picture of truck":
                picture_pick = "Trucker"
            elif picture_pick == "Dog and Cat":
                picture_pick = "DogCat"
            elif picture_pick == "Pony":
                picture_pick = "Horse"
            elif picture_pick == "Soccer":
                picture_pick = "Soccerball"

#           UNCOMMENT FOR NAMES AND ORDER NUMBERS
            for amt in range(order_amt[i]):
                print(name_pick, "-", picture_pick, "-", color_pick) 
                create_template.make_template(name_pick, color_pick, picture_pick, i)
        elif (listing_id == 1447486594):
            name_ind_start = order_vars[i].find("Personalization:")
            name_pick = order_vars[i][name_ind_start+CHAR_RANGE_NAME:]
            create_template.make_flame_template(name_pick, i)


        elif (listing_id == 1703069661):
            name_ind_start = order_vars[i].find("Personalization:")
            color_ind_start = order_vars[i].find("Color of cab:")
            name_pick = order_vars[i][name_ind_start+CHAR_RANGE_NAME:]
            color_pick = order_vars[i][color_ind_start+CHAR_RANGE_COLOR_CAB:name_ind_start - 1]
        
            if color_pick == "White-Purple letters":
                color_pick = "Purple"

            create_template.make_template(name_pick, color_pick, "Racecar", i)


        elif (listing_id == 1657496184):
            name_ind_start = order_vars[i].find("Personalization:")
            color_ind_start = order_vars[i].find("Color of cab:")
            name_pick = order_vars[i][name_ind_start+CHAR_RANGE_NAME:]
            color_pick = order_vars[i][color_ind_start+CHAR_RANGE_COLOR_CAB:name_ind_start - 1]
            if color_pick == "White-Purple letters":
                color_pick = "Purple"


            create_template.make_template(name_pick, color_pick, "NewTruck", i)
            
        else:
            print(f"##### {i} skipped #####")
def prepare_labels(sheet):
    labels = "labels/"
    names_of_files = [f for f in os.listdir(labels) if os.path.isfile(os.path.join(labels, f))]
    names_of_files.sort(reverse=True)
    order_number = 0
    number_of_labels = 1
    list_to_label = [0, 0, 0, 0]
    for name in names_of_files:
        if (order_number % 4 == 0) and (order_number > 0):
            template_to_label.create_label(list_to_label[0], list_to_label[1], list_to_label[2], list_to_label[3], number_of_labels)
            number_of_labels += 1
            order_number += 1
            list_to_label[(order_number - 1)%4] = name
        else:
            order_number += 1
            list_to_label[(order_number-1)%4] = name
    
def prepare_the_labels(sheet):
    os.popen("rm go_for_pdf/*")

    names_of_files = [f for f in os.listdir("labels/") if os.path.isfile(os.path.join("labels/", f))]
    names_of_files.sort(reverse=True)
    order_number = 0
    number_of_labels = 1
    list_to_labels = [0, 0, 0, 0, 0, 0, 0, 0]

    for name in names_of_files:
        if ((name[3] == 'f') or (name[4] == 'f')):
            list_to_labels[order_number % 8] = name
        else:
            list_to_labels[order_number % 8] = name
            order_number += 1
            list_to_labels[order_number % 8] = name
        order_number += 1
        if (order_number % 8 == 0) and (order_number > 0):
            template_to_label.make_label(list_to_labels[0], list_to_labels[1], list_to_labels[2], list_to_labels[3], list_to_labels[4], list_to_labels[5], list_to_labels[6], list_to_labels[7], number_of_labels)
            print(f"Label {number_of_labels} created.")
            number_of_labels += 1
if __name__ == "__main__":
    main()
