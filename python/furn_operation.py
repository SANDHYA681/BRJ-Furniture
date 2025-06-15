import datetime
from generate_invoice import generate_invoice, calculate_total


def read_furniture_data(file_path="furn_data.txt"):
    with open(file_path, "r") as file:
        return file.readlines()

def write_furniture_data(data, file_path="furn_data.txt"):
    with open(file_path, "w") as file:
        file.writelines(data)

def buy_furniture(item_purchases, purchaser, is_customer, invoice_file):
    try:
        furn_data = read_furniture_data()

        updated_items = []  

        for item_number, quantity_to_buy in item_purchases:
            item_index = -1  

            for i, item in enumerate(furn_data):
                if item.startswith(f"{item_number},"):
                    item_index = i
                    break

            if item_index != -1: 
                item_data = furn_data[item_index].strip().split(",")
                current_quantity = int(item_data[3]) 

                if is_customer:
                    new_quantity = current_quantity - quantity_to_buy
                else:
                    new_quantity = current_quantity + quantity_to_buy

                item_data[3] = str(new_quantity)
                furn_data[item_index] = ",".join(item_data) + "\n"

                updated_items.append({
                    'id': item_data[0],
                    'manufacturer': item_data[1],
                    'product': item_data[2],
                    'quantity': quantity_to_buy,
                    'price': float(item_data[4].replace(' ', '').replace('$', ''))
                })

                transaction_type = 'CUSTOMER PURCHASE' if is_customer else 'MANUFACTURER PURCHASE'

        if updated_items:
            write_furniture_data(furn_data)

            invoice_data = {
                'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'purchaser': purchaser,
                'transaction_type': transaction_type,
                'items': updated_items
            }

            while True:
                try:
                    shipping_cost = float(input("Enter the shipping cost: $"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the shipping cost.")

            total_amount, final_amount = calculate_total(invoice_data['items'], apply_vat=True, apply_shipping=True, shipping_cost=shipping_cost)
            
            invoice_data['shipping_cost'] = shipping_cost
            invoice_data['total_amount'] = total_amount
            invoice_data['final_amount'] = final_amount

            generate_invoice(invoice_data, invoice_file)  

            print("Items have been processed successfully.")
        else:
            print("No valid items were processed.")
    except Exception as e:
        print(f"Error processing transaction: {e}")





# Function to display furniture data in a table format in the terminal
def display_table():
    lines = read_furniture_data()
    data = [['ID', 'Manufacturer Name', 'Furniture Name', 'Quantity', 'Price']]  # Adding headers
    data.extend([line.strip().split(',') for line in lines])

    # Calculating the width of each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    
    def print_separator():
        print('+', end='')
        for width in column_widths:
            print('-' * (width + 2), end='+')
        print()
    
    def print_row(row):
        print('|', end='')
        for i, item in enumerate(row):
            print(f' {item:{column_widths[i]}} ', end='|')
        print()
    
    # Print the table
    print_separator()
    print_row(data[0])  # Print header
    print_separator()
    for row in data[1:]:
        print_row(row)
    print_separator()

def get_furniture_info(furn_no):
    furn_data = read_furniture_data()
    for item in furn_data:
        if item.startswith(f"{furn_no},"):
            item_data = item.strip().split(",")
            return int(item_data[3])  # Return the stock quantity for the given furniture ID
    return None
