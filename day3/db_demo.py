import sqlite3

con = sqlite3.connect('tickets.db')
con.row_factory = sqlite3.Row

con.execute('''CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    customer_id TEXT,
    subject TEXT,
    description TEXT,
    status TEXT
)''')

cursor = con.execute('''insert into tickets (customer_id, subject, description, status) values
    ('123', 'Issue with login', 'I cannot log in to my account.', 'open'),
    ('456', 'Payment issue', 'My payment did not go through.', 'open'),
    ('789', 'Bug report', 'I found a bug in the system.', 'closed')''')

con.commit()

row = con.execute('SELECT * FROM tickets where id = ?', (cursor.lastrowid,)
                  ).fetchone()

print(dict(row))

con.close()