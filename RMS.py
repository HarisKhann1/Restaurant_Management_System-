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
    heading('Generate Bill')
    display_menu()
    # dish_sno = int(input('Enter dish sno: '))
    with open('dbRMS.csv','r') as file:
        x = file.readlines()
        print(x)
        
        for item in x:
            dish_name = item.split(' | ')
            dish = dish_name[0].split(' : ')
            print("dish split",dish[1])
            price = dish_name[1].split(' : ')
            print("price split",price)
            print(dish, price)
            

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

    

    





