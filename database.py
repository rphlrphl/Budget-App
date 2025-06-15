import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('budget_app.db')
        self.cursor = self.con.cursor()
        # self.create_budget_table()
        # self.create_expense_table()  # Ensure expense table is created as well

    def create_budget_table(self):
        """Create the budget table only if it doesn't exist"""
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                amount REAL NOT NULL, 
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """)
            self.con.commit()
            print("Budget table checked/created successfully")
        except sqlite3.Error as e:
            print(f"Error creating budget table: {e}")
            raise

    def insert_budget(self, amount, category, date):
        try:
            self.cursor.execute(
                "INSERT INTO budget (amount, category, date) VALUES (?, ?, ?)",
                (amount, category, date)
            )
            self.con.commit()
            # Explicitly get the last inserted rowid
            return self.cursor.lastrowid if self.cursor.lastrowid else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_budget_by_id(self, list_id):
        """Get a specific budget by its ID with validation"""
        if id is None:
            print("Error: Cannot search for None ID")
            return None
            
        try:
            self.cursor.execute("SELECT * FROM budget WHERE id = ?", (id,))
            result = self.cursor.fetchone()
            return result if result else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def delete_budget_by_id(self, list_id):
        self.cursor.execute("DELETE FROM budget WHERE id = ?", (list_id,))
        self.con.commit()
        # return f"test {list_id}"

    def get_all_budgets(self):
        """Returns all budget entries as a list of rows"""
        self.cursor.execute("SELECT * FROM budget")
        return self.cursor.fetchall()  # Fetches all rows as a list of tuples
    
    def get_all_amounts(self): # test
        self.cursor.execute("SELECT amount FROM budget")
        return sum([row[0] for row in self.cursor.fetchall()])

    def close_connection(self):
        """Close the database connection"""
        self.con.close()

    """ IMPLEMENT AN OOP CONCEPT LATER FOR OPTIMIZATION """

    def create_expense_table(self):
        """Create the expense table only if it doesn't exist"""
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                amount REAL NOT NULL, 
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """)
            self.con.commit()
            print("Expense table checked/created successfully")
        except sqlite3.Error as e:
            print(f"Error creating expense table: {e}")
            raise

    def insert_expense(self, amount, category, date):
        try:
            self.cursor.execute(
                "INSERT INTO expense (amount, category, date) VALUES (?, ?, ?)",
                (amount, category, date)
            )
            self.con.commit()
            # Explicitly get the last inserted rowid
            return self.cursor.lastrowid if self.cursor.lastrowid else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_expense_by_id(self, list_id):
        """Get a specific expense by its ID with validation"""
        if id is None:
            print("Error: Cannot search for None ID")
            return None
            
        try:
            self.cursor.execute("SELECT * FROM expense WHERE id = ?", (id,))
            result = self.cursor.fetchone()
            return result if result else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def delete_expense_by_id(self, list_id):
        self.cursor.execute("DELETE FROM expense WHERE id = ?", (list_id,))
        self.con.commit()
        # return f"test {list_id}"

    def get_all_expense(self):
        """Returns all expense entries as a list of rows"""
        self.cursor.execute("SELECT * FROM expense")
        return self.cursor.fetchall()  # Fetches all rows as a list of tuples
    
    def get_all_amounts_expense(self): # test
        self.cursor.execute("SELECT amount FROM expense")
        return sum([row[0] for row in self.cursor.fetchall()])

    """  test  """
    def get_budget_from_each(self):
        self.cursor.execute("SELECT amount FROM budget")
        return self.cursor.fetchall()
    
    def get_expense_from_each(self):
        self.cursor.execute("SELECT amount FROM expense")
        return self.cursor.fetchall()
    
    def get_essentials_from_expense(self): #initial logic
        self.cursor.execute("SELECT SUM(amount) FROM expense WHERE CATEGORY = ?", ('Essentials',))
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0
    



db = Database()
print(db.get_essentials_from_expense())
# db.create_expense_table()

# print(db.get_all_budgets())
# # amounts = sum(db.get_all_amounts())
# # print(amounts)

# print(db.get_all_amounts())


# db.delete_budget_by_id(1)
# print(db.get_all_budgets())

# budget = db.get_budget_ids()
# # # print(budget[-1])
# print(budget)

# for budgets in budget:
#     print(budgets[1], budgets[2], budgets[3])

# db.create_budget_table()

# db.close_connection()



