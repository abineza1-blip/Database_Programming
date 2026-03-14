from configuration import get_db
conn=get_db()
cursor=conn.cursor()

#Read data from database users table
def read_users():
    query="SELECT * FROM users"
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print("Error reading users")
        print(e)



#insert data into users table 
def insert_user(name):
    query="INSERT INTO users (name) VALUES (%s)"
    try:
        cursor.execute(query,(name,))
        conn.commit()
        print("User inserted successfully")
    except Exception as e:
        print("Error inserting user")
        print(e)

def update_user(user_id,new_name):
    query="UPDATE users SET name=%s WHERE id=%s"
    try:
        cursor.execute(query,(new_name,user_id))
        conn.commit()
        print("User updated successfully")
    except Exception as e:
        print("Error updating user")
        print(e)

#delete a user from users table
def delete_user(user_id):
    query="DELETE FROM users WHERE id=%s"
    try:
        cursor.execute(query,(user_id,))
        conn.commit()
        print("User deleted successfully")
    except Exception as e:
        print("Error deleting user")
        print(e)

# Example usage
# insert_user("Aline kEZA")
# read_users()
# update_user(1, "Aline Smith")
# read_users()
delete_user(1)
read_users()

