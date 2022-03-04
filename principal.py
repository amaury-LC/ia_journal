
# importing
from database.database import database

# je créé ma base de données
ma_base_de_donnee = database()
ma_base_de_donnee.create_database("journal")
ma_base_de_donnee.create_table()


# insert mes articles
tuple_article = [("ceci est un teste", 1)]
ma_base_de_donnee.insert_article(tuple_article)

