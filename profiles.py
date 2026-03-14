from configuration import get_db
conn=get_db()
cursor=conn.cursor()

#Read data from database profiles table
def read_profiles():
    query="SELECT * FROM profiles"
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
        print("Error reading profiles")
        print(e)

read_profiles()
