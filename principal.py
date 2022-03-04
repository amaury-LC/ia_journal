
# importing
from database.database import database

# je crée ma base de données

ma_base_de_donnee = database()
ma_base_de_donnee.create_database("journal")
ma_base_de_donnee.create_table()

