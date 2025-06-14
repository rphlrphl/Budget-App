import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('budget_app.db')
        self.cursor = self.con.cursor()
        self.create_budget_table()

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

    # def get_budget_id(self):
    #     """Returns a list of all budget IDs (or empty list if none exist)"""
    #     self.cursor.execute("SELECT id FROM budget")
    #     return [row[0] for row in self.cursor.fetchall()]

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


db = Database()

print(db.get_all_budgets())
# amounts = sum(db.get_all_amounts())
# print(amounts)

print(db.get_all_amounts())


# db.delete_budget_by_id(1)
# print(db.get_all_budgets())

# budget = db.get_budget_ids()
# # # print(budget[-1])
# print(budget)

# for budgets in budget:
#     print(budgets[1], budgets[2], budgets[3])

# db.create_budget_table()

# db.insert_budget(1, 1000.00, '2004-10-07','Vivamax')
# db.insert_budget(2, 1000.00, '2004-10-07','Vivamax')
# db.insert_budget(3, 1000.00, '2004-10-07','Vivamax')
# db.insert_budget(4, 1000.00, '2004-10-07','Vivamax')
# db.insert_budget(5, 1000.00, '2004-10-07','Vivamax')

# db.close_connection()



