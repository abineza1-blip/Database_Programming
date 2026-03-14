from configuration import get_db
conn=get_db()
cursor=conn.cursor()

# inner join to get users with their profiles and posts
def get_users_with_profiles_posts():
    query="""
    SELECT u.id, u.name, p.age, p.city,po.text,po.likes
    FROM users u
    JOIN profiles p ON u.id = p.user_id
    JOIN posts po ON u.id = po.user_id
    """
    try:
        cursor.execute(query)
        #get column names from cursor.description
        columns=[desc[0] for desc in cursor.description]
        #print headers joined by tab
        print("\t".join(columns))
        result=cursor.fetchall()
        for row in result:
            print("\t".join(str(value) for value in row))
    except Exception as e:
        print("Error reading users with profiles and posts")
        print(e)

get_users_with_profiles_posts()
    