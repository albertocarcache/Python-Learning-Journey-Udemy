""""
Mini Banking System

A simple banking system that allows:
- Account creation
- Deposits
- Withdrawals
- Transaction tracking
- Account summary display
- Exception handling
"""
# ---------------------------------------------------------
# Part 1: Simulated Database
# ---------------------------------------------------------
"""
Create a global list called:
- accounts: This list will store all bank accounts.
- Each account should be stored as a dictionary containing: name, balance, transactions.
- The transactions field must be a list. Each transaction should be stored as a dictionary containing: type and amount.
"""

accounts = []

# Helper Function: Find Account

def find_account(name: str):
    """
    Find an account by name.
    Args:
        name (str): Account holder name.
    Returns:
        dict: Account dictionary if found.
        None: If account does not exist.
    """
    for account in accounts:
        if account["name"].strip().lower() == name.strip().lower():
            return account
    return None

# ---------------------------------------------------------
# Part 2: Add Expense Function
# ---------------------------------------------------------

def create_account(name: str, initial_balance: float):   
   """
   Create a new bank account.
    Args:
        name (str): Account holder name.
        initial_balance (float): Starting balance.
    Returns:
        dict: Created account dictionary.
    Raises:
        ValueError: If balance is negative or account exists.
   Appends:
        Created account dictionary to the accounts list.  
   """

   if initial_balance < 0:
      raise ValueError(f"Initial balance cannot be negative.\n       Error creating account: {name}")
   
   if find_account(name):
      raise ValueError(f"Account with this name already exists: {name}")  

   dict_account = {
              "name": name, 
              "initial_balance": initial_balance,              
              "balance": initial_balance, 
              "transactions": []
                  }
   accounts.append(dict_account)
   
   return dict_account

# ---------------------------------------------------------
# Part 3: Deposit Function
# ---------------------------------------------------------

def deposit(name: str, amount: float):
   """
   Deposit money into an account.
   Increase the balance.   
    Args:
        name (str): Account holder name.
        amount (float): Amount to deposit.
    Returns:
        float: Updated balance.
    Raises:
        ValueError: If amount is invalid or account not found.
    Appends:
        Add a transaction record of type "Deposit" to the account holder's name in the accounts list.    
   """

   if amount <= 0:
      raise ValueError(f"Deposit must be greater than 0.\n       Account: {name} / Invalid Amount: ${amount}")

   account = find_account(name)  
   
   if find_account(name):                  
      account["balance"] = account["balance"] + amount                           
        
      account["transactions"].append({"type": "Deposit", "amount": amount})                        
              
      return account["balance"]
   
   raise ValueError(f"Failed deposit / Account not found: {name}")

# ---------------------------------------------------------
# Part 4: Withdraw Function
# ---------------------------------------------------------

def withdraw(name: str, amount: float):
   """
   Withdraw money from an account.
   Decrease the balance
    Args:
        name (str): Account holder name.
        amount (float): Amount to withdraw.
    Returns:
        float: Updated balance.
    Raises:
        ValueError: If insufficient funds or invalid amount or account not found.
    Appends:
       Add a transaction record of type "Withdrawal" to the account holder's name in the accounts list.  
   """

   if amount <= 0:
      raise ValueError(f"Withdrawal must be greater than 0.\n       Account: {name} / Invalid Amount: ${amount}")
   
   account = find_account(name)  
   
   if find_account(name):               
      if account["balance"] < amount:
         raise ValueError(f"Funds are insufficient.\n       Account: {name} / Withdrawal Attempt: ${amount } / Current Balance: ${account["balance"]}")
      
      account["balance"] = account["balance"] - amount

      account["transactions"].append({"type": "Withdrawal", "amount": amount})
         
      return account["balance"]
   
   raise ValueError(f"Failed withdrawal / Account not found: {name}")

# ---------------------------------------------------------
# Part 5: Show Account Summary
# ---------------------------------------------------------

def show_account(name: str):
   """
    Display account summary (account name, current balance, transactions)
    Dispay if an account is not found:
    Args:
        name (str): Account holder name.   
   """
  
   print("\n===================================================")
   print("              BANK ACCOUNTS SUMMARY            ")
   print("===================================================")

   account = find_account(name)

   if account:
       index = accounts.index(account) + 1 

   #account_found = False # Flag to track if we found the account 

       # 1. We print the main account details (Account number, opening balance and current balance)
       print(f"{index}. Account: {account['name']}\n   Initial Balance: ${account['initial_balance']} // Current Balance: ${account['balance']}")
         
       # 2. We check if the account has any registered transactions
       lista_trans = account["transactions"] # We extract the list of dictionaries in the transactions field
      
       if not lista_trans:
          print("\n   ** No transactions recorded yet.")

       else:
          print("\n   Transactions:")
          print("-" * 51)
       # 3. This second loop enumerates each transaction in this account starting from 1
          for t_index, trans in enumerate(lista_trans, start=1):
             print(f"   {t_index}. {trans['type']}: ${trans['amount']}")        

   else:
      print(f"Account not found: {name}")

   print("-" * 51) # Dividing line between each customer
          
# ---------------------------------------------------------
# Part 6: Testing Section
# ---------------------------------------------------------
def run_tests() -> None:
   """
   Execute example expense scenarios.
   """
   
   try: # Creates account / Performs multiple deposits / Performs multiple withdrawals test   
      create_account(name= "Albert", initial_balance= 4000) 
      deposit(name= "Albert", amount= 2500) 
      withdraw(name= "Albert", amount= 500) 
      deposit("Albert", 3500) 
      withdraw("Albert", 1500)       
      deposit("Albert", 1000) 
      withdraw("Albert", 1500)           

   except ValueError as error:
        print("Error:", error)

   try: # Initial balance cannot be negative test     
      create_account(name= "Cristiano Ronaldo", initial_balance= -100)

   except ValueError as error:
        print("Error:", error)   

   try: # Duplicate account test     
      create_account(name= "Yara", initial_balance= 1000) 
      deposit("Yara", 2500) 
      withdraw("Yara", 500) 
      deposit("Yara", 2500) 
      withdraw("Yara", 1000)             
      create_account(name= "Albert",initial_balance= 100)                  

   except ValueError as error:
        print("Error:", error)    

   try: # Failed deposit / Account not found test     
      deposit(name= "Luis", amount= 900)               

   except ValueError as error:
        print("Error:", error)

   try: # Failed withdrawal / Account not found test   
      withdraw(name= "Jorge", amount= 500)               

   except ValueError as error:
        print("Error:", error)    

   try: # Overdraft test       
        create_account(name= "Baraa", initial_balance= 1000)
        deposit("Baraa", 200)
        withdraw("Baraa", 150)
        withdraw("Baraa", 2000) 

   except ValueError as error:
        print("Error:", error) 

   # Displays the account summary
   for account in accounts:   
      show_account(account["name"])

   # Account not found test
   show_account("Cristiano Ronaldo") 

##if __name__ == "__main__":
run_tests()