import sqlite3

class database :

    conn = None

    def create_database(self,name_database):

        """
        create ma database
        
        """

        self.conn = sqlite3.connect(name_database + '.db')

    def create_table(self):

        """
        create table
        
        """

        cursor = self.conn.cursor()

        # create table article
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS article(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            article TEXT,
            titre TEXT,
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

     

    def insert_article(self,articles):

        """
        insert dans la table article
        entrée:
        article :  
            tuple (article,id)
        """

        cursor = self.conn.cursor()

        cursor.executemany("""
            INSERT INTO article(article, id_journal) VALUES(?, ?)""", articles)

        self.conn.commit()

        

    def articles(self):

        cursor = self.conn.cursor()

        cursor.execute("""SELECT article , id_journal FROM article""")
        rows = cursor.fetchall()
        for row in rows:
            print('{0} , {1}'.format(row[0], row[1]))
        




       


