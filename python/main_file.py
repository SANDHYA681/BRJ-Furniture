#final codee
from furn_operation import buy_furniture, display_table,get_furniture_info

def main():
    while True:
        print("\n===========================================")
        print("       Welcome to Furniture Management System      ")
        print("===========================================") 
        print("1. View all Furnitures")
        print("2. Sell Furniture to Customer")
        print("3. Buy Furniture From Manufacturer")
        print("4. Exit\n")
        print("===========================================\n")
        
        try:
            user_choice = input("Enter your choice: ")
            if user_choice == "":
                raise ValueError
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > 4:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 4.")
            continue

        if user_choice == 1:
            display_table()
        
        elif user_choice == 2:
            process_purchase(is_customer=True)
        
        elif user_choice == 3:
            process_purchase(is_customer=False)
        
        elif user_choice == 4:
            print("Thankyou for using the Furniture Management System. Goodbye!")
            break
        
        print("Do you want to Continue?")
        print("1. Yes")
        print("2. No")
        continue_choice = input("Enter your choice: ")
        if continue_choice == "2":
            print("Thank you for using the Furniture Management System. Goodbye!")
            break

def process_purchase(is_customer):
    try:
        purchases = []
        while True:
            if is_customer:
                furn_no = input("Enter Furniture ID To Sell (or type 'done' to finish): ")
            else:
                furn_no = input("Enter Furniture ID To Buy (or type 'done' to finish): ")

            if furn_no.lower() == 'done':
                break

            stock = get_furniture_info(furn_no)
            if stock is not None:
                if stock > 0 or not is_customer:
                    quantity = int(input("Enter quantity: "))
                    if is_customer:
                        if quantity <= stock:
                            print(f'Sold {quantity} quantity of furniture with ID number {furn_no}')
                            purchases.append((furn_no, quantity))
                        else:
                            print(f'Entered quantity exceeds current stock of {stock} for furniture with ID {furn_no}')
                    else:
                        print(f'Purchased {quantity} quantity of furniture with ID number {furn_no}')
                        purchases.append((furn_no, quantity))
                else:
                    print(f'Furniture with ID {furn_no} is currently out of stock')
            else:
                print('Entered ID does not exist in the inventory')

        purchaser = input("Enter Purchaser's Name: ")

        # Generate invoice filename based on purchaser's name
        invoice_file = f"{purchaser.replace(' ', '_')}_customer_invoices.txt" if is_customer else f"{purchaser.replace(' ', '_')}_manufacturer_invoices.txt"
        
        # Pass the invoice filename to the buy_furniture function
        buy_furniture(purchases, purchaser, is_customer, invoice_file)

    except Exception as e:
        print(f"Error processing purchase: {e}")


if __name__ == '__main__':
    main()
