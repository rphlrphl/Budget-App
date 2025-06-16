import sqlite3

class Database:
    def __init__(self):
        self._con = sqlite3.connect('budget_app.db')   # Protected
        self._cursor = self._con.cursor()                # Protected

    def _commit(self):  # Protected helper method
        self._con.commit()

    def create_budget_table(self):
        """Create the budget table only if it doesn't exist"""
        try:
            self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                amount REAL NOT NULL, 
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """)
            self._commit()
            print("Budget table checked/created successfully")
        except sqlite3.Error as e:
            print(f"Error creating budget table: {e}")
            raise

    def create_expense_table(self):
        """Create the expense table only if it doesn't exist"""
        try:
            self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                amount REAL NOT NULL, 
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """)
            self._con.commit()
            print("Expense table checked/created successfully")
        except sqlite3.Error as e:
            print(f"Error creating expense table: {e}")
            raise

    def close_connection(self):
        """Close the database connection"""
        self._con.close()

class BudgetDatabase(Database):
    def __init__(self):
        super().__init__()
        self.__insert = "INSERT INTO budget (amount, category, date) VALUES (?, ?, ?)"  # Private
        self.__get_budgetbyid = "SELECT * FROM budget WHERE id = ?"
        self.__get_allbudget = "SELECT * FROM budget "
        self.__get_allamounts = " SELECT amount FROM budget "
        self.__get_totalessentials = "SELECT SUM(amount) FROM budget WHERE CATEGORY = ?"
        self.__get_totalobligations = "SELECT SUM(amount) FROM budget WHERE CATEGORY = ?"
        self.__get_totalothers = "SELECT SUM(amount) FROM budget WHERE CATEGORY = ?"
        self.__get_budgetfromeach = "SELECT amount FROM budget"
        self.__delete_budgetbyid = "DELETE FROM budget WHERE id = ?"


    def insert_budget(self, amount, category, date):
        """Public method to insert a new budget entry"""
        try:
            self._cursor.execute(self.__insert, (amount, category, date,))
            self._commit()
            return self._cursor.lastrowid if self._cursor.lastrowid else None
        except sqlite3.Error as e:
            print(f"Error inserting budget: {e}")
            raise

    def get_budget_by_id(self, list_id):
        if list_id is None: # changed from id -> list_id
            print("Error: Cannot search for None ID")
            return None  
        try:
            self._cursor.execute(self.__get_budgetbyid, (list_id,))
            result = self._cursor.fetchone()
            return result if result else None
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return None
        
    def get_all_budgets(self):
        self._cursor.execute(self.__get_allbudget)
        return self._cursor.fetchall()

# This class is an example of encapsulation (with inheritance). SQL queries are made private by
# storing it in private attributes, encapsulating raw SQL strings and enforcing separation
# between query definitions and execution logic 

    def get_all_amounts(self):
        self._cursor.execute(self.__get_allamounts)
        return sum([row[0] for row in self._cursor.fetchall()])

    def get_all_essentials_budget(self):
        self._cursor.execute(self.__get_totalessentials, ('Essentials',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_all_obligations_budget(self):
        self._cursor.execute(self.__get_totalobligations, ('Financial Obligations',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_all_others_budget(self):
        self._cursor.execute(self.__get_totalothers, ('Others',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_budget_from_each(self):
        self._cursor.execute(self.__get_budgetfromeach)
        return self._cursor.fetchall()
    
    def delete_budget_by_id(self, list_id):
        if list_id is None:
            print("Error: Cannot search for None ID")
            return None
        else:
            self._cursor.execute(self.__delete_budgetbyid, (list_id,))
            self._con.commit()




class ExpenseDatabase(Database):
    def __init__(self):
        super().__init__()
        self.__insert = "INSERT INTO expense (amount, category, date) VALUES (?, ?, ?)"
        self.__get_expensebyid = "SELECT * FROM expense WHERE id = ?"
        self.__get_allexpense = "SELECT * FROM expense"
        self.__get_allamount = "SELECT amount FROM expense"
        self.__get_totalessentials = "SELECT SUM(amount) FROM expense WHERE CATEGORY = ?"
        self.__get_totalobligations = "SELECT SUM(amount) FROM expense WHERE CATEGORY = ?"
        self.__get_totalothers = "SELECT SUM(amount) FROM expense WHERE CATEGORY = ?"
        self.__get_expensefromeach = "SELECT amount FROM expense"
        self.__delete_expensebyid = "DELETE FROM expense WHERE id = ?"

    def insert_expense(self, amount, category, date):
        try:
            self._cursor.execute(self.__insert,(amount, category, date))
            self._con.commit()
            # Explicitly get the last inserted rowid
            return self._cursor.lastrowid if self._cursor.lastrowid else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        
    def get_expense_by_id(self, list_id):
        """Get a specific expense by its ID with validation"""
        if id is None:
            print("Error: Cannot search for None ID")
            return None
            
        try:
            self._cursor.execute(self.__get_expensebyid, (id,))
            result = self._cursor.fetchone()
            return result if result else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def get_all_expense(self):
        """Returns all expense entries as a list of rows"""
        self._cursor.execute(self.__get_allexpense)
        return self._cursor.fetchall()  # Fetches all rows as a list of tuples
    
    def get_all_amounts_expense(self): # test
        self._cursor.execute(self.__get_allamount)
        return sum([row[0] for row in self._cursor.fetchall()])
    
    def get_all_essentials_expense(self):
        self._cursor.execute(self.__get_totalessentials, ('Essentials',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_all_obligations_expense(self):
        self._cursor.execute(self.__get_totalobligations, ('Financial Obligations',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0
    
    def get_all_others_expense(self):
        self._cursor.execute(self.__get_totalothers, ('Others',))
        result = self._cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def get_expense_from_each(self):
        self._cursor.execute(self.__get_expensefromeach)
        return self._cursor.fetchall()

    def delete_expense_by_id(self, list_id):
        self._cursor.execute(self.__delete_expensebyid, (list_id,))
        self._con.commit()

class ClearDatabase(Database):
    def __init__(self):
        super().__init__()
        self.__clear_budget = "DELETE FROM budget"
        self.__clear_expense = "DELETE FROM expense"

    def clear_data(self):
        self._cursor.execute(self.__clear_budget)
        self._con.commit()
        self._cursor.execute(self.__clear_expense)
        self._con.commit()

db = Database()
budget_db = BudgetDatabase()
expense_db = ExpenseDatabase()
clear_db = ClearDatabase()
