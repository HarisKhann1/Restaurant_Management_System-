import os

def heading(name):
    os.system('cls')
    print(f'\n--------------------- {name} -----------------------\n')

def add_dish():
    # here all data will be stored in dbRMD.txt
    print('---------------------- Little Lemon --------------------')

    with open("dbRMS.txt",'a') as file:
        try:
            while True:
                # taking input for dish and its price
                dish_name = input("Enter dish name: ")
                dish_price = int(input("Enter dish price: "))
                add_moredish = input("Add more dishes (yes/no): ")
                # writing into dbRMs.txt 
                file.writelines(f'\nDish name : {dish_name} | Price : {dish_price}')
                # if the input is no from user it will not excute further more
                if add_moredish == 'no':
                    print("Added successfully ...")
                    break

        except Exception as e:
            print("Error in write to database ...", e)

def display_menu():
     # displaying all dishes with price from database (dbRMS)
    heading('menu')
    with open('dbRMS.txt', 'r') as file:
        try:
            for count,content in enumerate(file, 1):
                print(f' {count}) {content}')
        except Exception as e:
            print("Error in print_menu ", e)

def generate_bill():
    #  lst_prices stores prices from file of each dish
    lst_prices = []
    customer_dish_list = []
    heading('Generate Bill')
    display_menu()
    with open('dbRMS.txt','r') as file:
        content = file.readlines()
        for item in content:
            parts = item.split('|')          # splites string With respect to '|'
            price = parts[1].split(':')[1]   # splites first index of parts list with respect to ':' after spliting taking 1st index vales
            lst_prices.append(int(price)) # appednding each extracted vales to price list
            print(lst_prices)
            print(lst_prices)

        while True:
                # taking input for dish and its price
                dish_num = input("Enter dish number: ")
                yes_no = input("Another dish to bill (yes/no): ")
                customer_dish_list.append(dish_num)
                # file.writelines(f'Dish name : {dish_name} | Price : {dish_price}\n')
                if yes_no == 'no':
                    print("Bill generated successfully ...")
                    break
        print(customer_dish_list)


def main():
    lst = ['Add Dish', 'show Dish', 'Generate Bill', 'Search Dish', 'Delete Dish', 'Sort dish', 'Exit']
    # displaying above list
    flag = True
    while flag:
        heading('RMS')
        for num,list in enumerate(lst,1):
            print(num, list)

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

        wait = input('Press Enter ...')
    
if __name__ == '__main__':
    main()

    

    





