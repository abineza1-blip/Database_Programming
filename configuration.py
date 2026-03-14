import mysql.connector

# print("Program started ")

# try:
#     db = mysql.connector.connect(
#         host="localhost",   # IMPORTANT
#         user="root",        # use your real username
#         password="root123",
#         port=3306,
#         use_pure=True   #  IMPORTANT
#     )

#     print("Connected successfully ")

# except Exception as e:
#     print("Connection failed ")
#     print(e)

# print("Program finished ")
def get_db():
    conn=mysql.connector.connect(
        host="localhost",   # IMPORTANT
        user="root",        # use your real username
        password="root123",
        database="social_media",
        port=3306,
        use_pure=True   #  IMPORTANT

    )
    print("Connected successfully ")
    return conn


