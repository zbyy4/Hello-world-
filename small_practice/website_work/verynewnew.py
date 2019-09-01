import pymssql
sqlConn = None
def connectSQLServer():

    attr = dict(
        server = '10.20.213.10',
        database = 'csc1002',
        user = 'csc1002',
        password = 'csc1002',
        port = 1433
        as_dict = True
    )

    try:
        return pymssql.connect(**attr)
    except Exception as e:
        print(e)
        quit()

tsql = "SELECT * FROM lgu.course order by dept_name"
with sqlConn.cursor(as_dict=Ture) as cursor:
    cursor.execute(tsql)
    for row in cursor:
        print(row['dept_name'], row['title'])

def select2():
    tsql = "SELECT * FROM lgu.course order by dept_name"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        return rows

rows = select2()
for row in rows:
    print(row['dept_name'], row['title'])

def select3(title):
    tsql = "SELECT * FROM lgu.course where title like %s"
    print(tsql, title)
    with sqlConn.cursor(as_dict=Ture) as cursor:
        cursor.execute(tsql, title)
        rows = cursor.fetchall()
        for row in rows:
            print(row['dept_name'], row['title'])

select3(title="bio%")

button = wd.Button(label="Refresh")
textbox = wd.TextInput(title="Name",
    value="", placeholder="enter name ....")