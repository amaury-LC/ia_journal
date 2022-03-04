import sqlite3

class database :

    conn = None

    def create_database(self,name_database):

        self.conn = sqlite3.connect(name_database + '.db')

    def create_table(self):

        cursor = self.conn.cursor()

        # create table article
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS article(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            article TEXT,
            id_journal INTERGER
            )
        """)
        self.conn.commit()

        # create table journal
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS journal(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT
            )
        """)
        self.conn.commit()

        self.conn.close()

    def insert_table()

        
