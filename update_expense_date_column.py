import sqlite3

def update_date_column_type():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Step 1: Create a new table with the correct schema
    cursor.execute('''
        CREATE TABLE expense_new (
            id INTEGER PRIMARY KEY,
            date DATE NOT NULL,  -- Define date as DATE
            description VARCHAR(200) NOT NULL,
            amount FLOAT NOT NULL,
            category VARCHAR(50) NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
    ''')

    # Step 2: Copy data from old table to new table with date conversion
    cursor.execute('''
        INSERT INTO expense_new (id, date, description, amount, category, user_id)
        SELECT id, 
               CASE 
                   WHEN LENGTH(date) = 10 THEN date 
                   ELSE NULL 
               END AS date,  -- Check date format
               description, amount, category, user_id
        FROM expense
    ''')

    # Step 3: Drop the old table
    cursor.execute('DROP TABLE expense')

    # Step 4: Rename the new table to the old table’s name
    cursor.execute('ALTER TABLE expense_new RENAME TO expense')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    update_date_column_type()

