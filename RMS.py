import os

# Function to clear screen and display heading
def heading(name):
    os.system('cls')
    print(f'\n--------------------- {name} -----------------------\n')

# Function to display a line of dashes
def closeLine():
    print("------------------------------------------------")

# Function to add dishes to the database    
def add_dish():
    heading('ADD DISHES')

    with open("dbRMS.txt",'a') as file:
        try:
            while True:
                # taking input for dish and its price
                dish_name = input("Enter dish name: ")
                dish_price = int(input("Enter dish price: "))
                add_moredish = input("Add more dishes (yes/no): ")
                # writing into dbRMs.txt 
                file.writelines(f'{dish_name} : {dish_price}\n')
                # if the input is no from user it will not excute further more
                if add_moredish == 'no':
                    print("Added successfully ...")
                    break
        except Exception as e:
            print("Error: Can't store data in file ...", e)

        closeLine()

# Function to load data from database
def load_data_from_file():
    database = ''
    with open('dbRMS.txt', 'r') as file:
        try:
            database = file.readlines()
        except Exception as e:
            print("Error: Can't load data from file ", e)

    return database

# Function to display the menu
def display_menu():
    heading('Menu')
    database = load_data_from_file()

    for count,content in enumerate(database, 1):
        print(f' {count}. {content}')
    closeLine()

# Function to print the bill
def print_bill(customer_dish_num, content, dish_countity):
    heading('Bill')
    customer_order = []  
    prices = []
    price_and_quantity = []

    # Extracting dish and its price from content list
    # with help of customer_dish_num list
    # and appending to customer_order list
    for i in customer_dish_num:
        customer_order.append(content[i])

    # Extracting price from comtomer_order list and appeding to prices list
    # Using split function
    for item in customer_order:
        parts = item.split(':')          
        price = parts[1]   
        prices.append(int(price))

    # Calulating total bill
    total = 0
    for num, value in enumerate(prices):
        price_of_item = value * dish_countity[num]
        total = total + price_of_item
        price_and_quantity.append(price_of_item)

    # Displaying dish and its price with quantity 
    for num, i in enumerate(customer_order):
        print(f'{num+1}. {i}countity : {dish_countity[num]} --> {price_and_quantity[num]}\n')

    # displaying total amount
    closeLine()
    print(f'Total bill: {total}')
    closeLine()

# Function to Generate the bill
def generate_bill():
    customer_dish_num = []  
    dish_countity = []
    content = load_data_from_file()
    
    heading('Generate Bill')
    display_menu()

    while True:
        dish_num = int(input("Enter dish number: "))
        dish_cout = int(input("Enter dish countity: "))
        yes_no = input("Another dish to bill (yes/no): ")

        customer_dish_num.append(dish_num-1)
        dish_countity.append(dish_cout)

        if yes_no == 'no':
            print("Bill generated successfully ...")
            break
    
    print_bill(customer_dish_num, content, dish_countity)

# Function to search for a dish
def search_dish():
    names = []
    content = load_data_from_file()
    heading('Search section')

    for name in content:
        parts = name.split(':')
        names.append(parts[0].strip())
    try:
        search_name = input("Enter Dish Name: ")
        x = names.index(search_name)

        print(f'\nDish Found\n{content[x]}')
        closeLine()

    except ValueError:
            print("\nError: Dish not found ...", )
            closeLine()

# Function to delete dish
def delete_dish():
    heading('Delete section')
    content = load_data_from_file()
    names = []
    new_dish_list = []


    for name in content:
        # splite content list (':') to get name and price as individual index
        parts = name.split(':') 
        # extracting dish name from parts list (above)
        names.append(parts[0].strip())
    try:
        # user input
        search_name = input("Enter Dish Name: ")
        # returns index if the given dish name in the list
        x = names.index(search_name)
        print(f'\nDish Found\n{content[x]}')

        # appending all item in new_dish_list except the given dish name to be deleted
        for num, item in enumerate(content):
            if num == x:
                pass
            else:
                new_dish_list.append(item)

        # overwriting new_dish_list to the database
        with open('dbRMS.txt', 'w') as file:
            for item in new_dish_list:
                file.writelines(item)
        print(f'\nDish Delete Successfully ...')
        closeLine()
    except ValueError:
            print("\nError: Dish not found ...", )
            closeLine()

# Function to define sort key function
def sort_key_fun(item):
    # extracting price
    return int(item.split(':')[1])

# Function to sort dishes by price
def sort_by_price():
    heading('Sort')
    content = load_data_from_file()
    sorted_list = sorted(content, key=sort_key_fun)
    
    for num, item in enumerate(sorted_list,1):
        print(f'{num}. {item}')
    closeLine()

# Main Function
def main():
    lst = ['Add Dish', 'show Dish', 'Generate Bill', 'Search Dish', 'Delete Dish', 'Sort dish', 'Exit']
    # displaying above list
    flag = True
    while flag:
        heading('RMS')
        for num,list in enumerate(lst,1):
            print(num, list)

        closeLine()
        choice = int(input('Enter your choice: '))
        if choice == 7:
            flag = False
            break
        else:
            match choice:
                case 1:
                    add_dish()
                case 2:
                    display_menu()
                case 3:
                    generate_bill()
                case 4:
                    search_dish()
                case 5:
                    delete_dish()
                case 6:
                    sort_by_price()

        wait = input('\nPress Enter ...')
    
if __name__ == '__main__':
    main()

    

    





