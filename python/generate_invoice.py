VAT_RATE = 0.13

def generate_invoice(invoice_data, invoice_file):
    try:
        with open(invoice_file, "a") as file:
            file.write("===========================================\n")
            file.write("                BRJ FURNITURE STORES\n")
            file.write("           Type: " + invoice_data['transaction_type'] + "\n")
            file.write(f"Date & Time: {invoice_data['datetime']}\n")
            file.write(f"Purchaser: {invoice_data['purchaser']}\n")
            file.write("-------------------------------------------\n")
            for item in invoice_data['items']:
                file.write(f"Item ID: {item['id']}\n")
                file.write(f"Manufacturer: {item['manufacturer']}\n")
                file.write(f"Product: {item['product']}\n")
                file.write(f"Quantity: {item['quantity']}\n")
                file.write(f"Price: ${item['price']:.2f}\n")
                file.write("-------------------------------------------\n")
            file.write(f"Total Amount (excluding shipping): ${invoice_data['total_amount']:.2f}\n")
            if 'shipping_cost' in invoice_data:
                file.write(f"Shipping Cost: ${invoice_data['shipping_cost']:.2f}\n")
                file.write(f"Final Amount After Shipping Cost & VAT: ${invoice_data['final_amount']:.2f}\n")
            file.write("===========================================\n\n")

        # Print the invoice to the console
        print("===========================================")
        print("                BRJ FURNITURE STORES")
        print("           Type:", invoice_data['transaction_type'])
        print("Date & Time:", invoice_data['datetime'])
        print("Purchaser:", invoice_data['purchaser'])
        print("-------------------------------------------")
        for item in invoice_data['items']:
            print(f"Item ID: {item['id']}")
            print(f"Manufacturer: {item['manufacturer']}")
            print(f"Product: {item['product']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: ${item['price']:.2f}")
            print("-------------------------------------------")
        print(f"Total Amount (excluding shipping): ${invoice_data['total_amount']:.2f}")
        if 'shipping_cost' in invoice_data:
            print(f"Shipping Cost: ${invoice_data['shipping_cost']:.2f}")
            print(f"Final Amount After Shipping Cost & VAT: ${invoice_data['final_amount']:.2f}")
        print("===========================================\n\n")

        print("Invoice generated successfully.")
    except Exception as e:
        print(f"Error generating invoice: {e}")


    
#function to caluclate total amount and final amount for cases of purchases and sales
def calculate_total(items, apply_vat=True, apply_shipping=False, shipping_cost=0.0):
    total_amount = sum(item['price'] * item['quantity'] for item in items)
    if apply_vat:
        total_amount += total_amount * VAT_RATE
    final_amount = total_amount
    if apply_shipping:
        final_amount += shipping_cost
    return total_amount, final_amount

