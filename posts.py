from configuration import get_db
conn=get_db()
cursor=conn.cursor()

#Read data from database posts table
def read_posts():
    query="SELECT * FROM posts"
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
        print("Error reading posts")
        print(e)

read_posts()
