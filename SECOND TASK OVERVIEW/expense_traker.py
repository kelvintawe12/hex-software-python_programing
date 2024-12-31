import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses 
                  (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, category TEXT, 
                   date TEXT, description TEXT, FOREIGN KEY(user_id) REFERENCES users(id))''')
conn.commit()

# User functions
def register_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try again.")

def login_user(username, password):
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    if result:
        print(f"Welcome, {username}!")
        return result[0]
    else:
        print("Invalid login. Try again.")
        return None

# Expense functions
def add_expense(user_id, amount, category, date, description):
    cursor.execute("INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                   (user_id, amount, category, date, description))
    conn.commit()
    print("Expense added successfully!")

def view_summary(user_id):
    cursor.execute("SELECT category, SUM(amount) FROM expenses WHERE user_id = ? GROUP BY category", (user_id,))
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Category', 'Total'])
    print(df)
    # Visualization
    df.plot(kind='bar', x='Category', y='Total', title="Expense Summary", color='teal')
    plt.show()

def export_expenses(user_id):
    cursor.execute("SELECT amount, category, date, description FROM expenses WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Amount', 'Category', 'Date', 'Description'])
    df.to_csv('expense_report.csv', index=False)
    print("Expense report exported to 'expense_report.csv'.")

# Main application
def main():
    print("Welcome to the Expense Tracker!")
    print("1. Register\n2. Login")
    choice = input("Choose an option: ")
    
    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_id = login_user(username, password)
        if user_id:
            while True:
                print("\n1. Add Expense\n2. View Summary\n3. Export Expenses\n4. Logout")
                option = input("Choose an option: ")
                if option == '1':
                    amount = float(input("Enter the amount: "))
                    category = input("Enter the category: ")
                    date = input("Enter the date (YYYY-MM-DD): ")
                    description = input("Enter a description: ")
                    add_expense(user_id, amount, category, date, description)
                elif option == '2':
                    view_summary(user_id)
                elif option == '3':
                    export_expenses(user_id)
                elif option == '4':
                    print("Goodbye!")
                    break
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
