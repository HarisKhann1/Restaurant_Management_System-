import os

def heading(name):
    os.system('cls')
    print(f'\n--------------------- {name} -----------------------\n')

def closeLine():
    print("------------------------------------------------")
    
def add_dish():
    # here all data will be stored in dbRMD.txt
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

def load_data_from_file():

    database = ''
    with open('dbRMS.txt', 'r') as file:
        try:
            database = file.readlines()
        except Exception as e:
            print("Error: Can't load data from file ", e)

    return database

# displaying all dishes with price from database (dbRMS)
def display_menu():

    heading('Menu')
    database = load_data_from_file()

    for count,content in enumerate(database, 1):
        print(f' {count}. {content}')

    closeLine()

def print_bill(customer_dish_num, content, dish_countity):
    customer_order = []
    prices = []
    for i in customer_dish_num:
        customer_order.append(content[i])
        
    os.system('cls')
    heading('Bill')
    for num, i in enumerate(customer_order):
        print(f'{num+1}. {i}countity : {dish_countity[num]}\n')

    for item in customer_order:
        parts = item.split(':')          
        price = parts[1]   
        prices.append(int(price))

    total = 0
    for num, value in enumerate(prices):
        total = total + (value * dish_countity[num])
        
    closeLine()
    print(f'Total bill: {total}')
    closeLine()

def generate_bill():

    customer_dish_num = []  
    dish_countity = []
    content = load_data_from_file()
    
    heading('Generate Bill')
    display_menu()

    while True:
        # taking input for dish and its price
        dish_num = int(input("Enter dish number: "))
        dish_cout = int(input("Enter dish countity: "))
        yes_no = input("Another dish to bill (yes/no): ")

        customer_dish_num.append(dish_num-1)
        dish_countity.append(dish_cout)

        if yes_no == 'no':
            print("Bill generated successfully ...")
            break

    print_bill(customer_dish_num, content, dish_countity)

def search_dish():

    heading('Search section')
    content = load_data_from_file()
    names = []

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

def delete_dish():

    heading('Delete section')
    content = load_data_from_file()
    names = []
    new_dish_list = []

    for name in content:
        parts = name.split(':')
        names.append(parts[0].strip())
    try:
        search_name = input("Enter Dish Name: ")
        x = names.index(search_name)
        print(f'\nError: Dish Found\n{content[x]}')

        for num, item in enumerate(content):
            if num == x:
                pass
            else:
                new_dish_list.append(item)

        with open('dbRMS.txt', 'w') as file:
            for item in new_dish_list:
                file.writelines(item)

        print(f'\nDish Delete Successfully ...')
        closeLine()

    except ValueError:
            print("\nError: Dish not found ...", )
            closeLine()

def sort_key_fun(item):
    return int(item.split(':')[1])

def sort_by_alpha():
    heading('Sort')
    content = load_data_from_file()
    sorted_list = sorted(content, key=sort_key_fun)
    
    for num, item in enumerate(sorted_list,1):
        print(f'{num}. {item}')
    closeLine()

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
                    sort_by_alpha()

        wait = input('\nPress Enter ...')
    
if __name__ == '__main__':
    main()

    

    





