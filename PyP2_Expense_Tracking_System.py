"""
Expense Tracking System

A simple user registration module that demonstrates:
- Validation functions
- Exception handling
- Duplicate checking
- Basic in-memory storage
"""
# ---------------------------------------------------------
# Part 1: Simulated Database
# ---------------------------------------------------------
"""
Each expense should be stored as a dictionary containing: amount, category, description.
"""
expenses = [] # A global list that stores all expense entries.
errors = [] # A global list that stores all input errors.

# ---------------------------------------------------------
# Part 2: Add Expense Function
# ---------------------------------------------------------

def add_expense(amount: float, category: str, description: str) -> dict:
    """
    Add a new expense to the system.

    Args:
        amount (float): The expense amount (must be positive).
        category (str): The expense category.
        description (str): Short description of the expense.
    Returns:
        dict: The created expense dictionary.
        False: if any validation condition is fulfilled.
    Appends:
        dictionary for the expense to the expenses list
        dictionary for the erros to the errors list
    """
    dict_expense = {
                "amount": amount,
                "category": category,
                "description": description
                   } 
    if amount is None or category is None or description is None:
        errors.append(f"Fields cannot be None {dict_expense}")        
        return False    
    
    if not isinstance(amount, (int, float)):      
        errors.append(f"Invalid amount, must be a Number {dict_expense}")
        return False
    
    if amount <= 0:      
        errors.append(f"Invalid amount, must be greater than 0 {dict_expense}")
        return False
   
    if category.strip() == "" or description.strip() == "":        
        errors.append(f"Fields cannot be Empty {dict_expense}")
        return False      
     
    expenses.append(dict_expense)
    
    return dict_expense
    
# ---------------------------------------------------------
# Part 3: Total Expenses
# ---------------------------------------------------------
    
def calculate_total_expenses() -> float:
    """
    Loop through all expenses.
    Calculate the total of all expenses.

    Returns:
        float: Total amount of all expenses.
    """
    total_expenses = 0

    for expense in expenses:       
        total_expenses = total_expenses + expense.get("amount", 0)

    return total_expenses

# ---------------------------------------------------------
# Part 4: Total by Category
# ---------------------------------------------------------

def calculate_total_by_category(category: str) -> float:
    """
    Loop through expenses.
    Calculate total expenses for a specific category.

    Args:
        category (str): The category to filter by.
    Returns:
        float: Total amount for that category.
    """
    total_by_category = 0

    for expense in expenses:
        if expense["category"].strip().lower() == category.strip().lower():
            total_by_category = total_by_category + expense["amount"]

    return total_by_category
    """
    total_by_category = {}

    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        
        # We filter: only process if it matches the requested category
        if cat == category:
            total_by_category[cat] = total_by_category.get(cat, 0) + amt
            
    return total_by_category
    """
# ---------------------------------------------------------
# Part 5: Show All Expenses
# ---------------------------------------------------------

def show_expenses() -> None:
    """
    Display all stored expenses.

    Returns:
        None
    """
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']} : ${expense['amount']}"
             )

# ---------------------------------------------------------
# Part 6: Testing Section
# ---------------------------------------------------------

def run_tests() -> None:
    """
    Execute example expense scenarios.
    """
    add_expense(amount=50, category="Food", description="Groceries")
    add_expense(None, None, "Energy") # Invalid example          
    add_expense(20, "Transport", "Taxi")
    add_expense(100, "Food", "Restaurant")
    add_expense(40, "Transport", "Bus")
    add_expense(65, "Basic_Services", "Water")
    add_expense(0, "Entertainment", "Cinema") # Invalid example 
    add_expense("$", "" , "") # Invalid example
    add_expense(25, "  " , "kkk") # Invalid example  
    add_expense(None, None, None) # Invalid example
    add_expense(90, "Entertainment", "Videogames")
    add_expense(30, "Cleaning", "Detergent")
    add_expense(-70, "Car", "Insurance") # Invalid example    
    
    # Dynamic Category Extraction
    # ---------------------------------------------------------
    # The category of each expense is extracted from the 'expenses' list.
    # 'set()' removes duplicates to avoid repeating the calculate_total_by_category calculation.

    all_categories = set([expense["category"] for expense in expenses])
    
    # Prints total expenses.
    print("\nDynamic Totals by Category:")
    print("Total Expenses: $", calculate_total_expenses(), sep = "")

    # The loop automatically processes any new categories added previously.
    # Prints total for a specific category.
    for cat in all_categories:        
        total = calculate_total_by_category(cat)
        print(f"Total {cat} Expenses: ${total}")
    
    # Displays all stored expenses
    show_expenses()    

    print("\nErrors:")
    for index, error in enumerate(errors, start=1):
        print(index, error)
    
if __name__ == "__main__":
    run_tests()