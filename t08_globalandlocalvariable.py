# Global and local varibales


discount = 30  # Global variable

def calculate_total(amout):

    # Default value
    discount = 10  # Local variable
    tax_rate = 0.1  # Local variable

    # Calculation
    tax = amout * tax_rate
    total = amout + tax - discount

    # Print the final price
    print(f"Total : Rs. {total}")
    pass

discount               # it is a global variable so, it can be accessed.

# tax_rate              # it is a local variable so, it can't be accessed globally
calculate_total(100)
