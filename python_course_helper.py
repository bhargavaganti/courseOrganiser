import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print('Unable to create a DB !')


    # TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private)VALUES (?,?,?,?)", data
                )
        except Exception:
            return False

    # TODO: fetch data
    def fetch_data(self):
        pass
    
    # TODO: delete data
    def delete_data(self, id):
        pass



# TODO: provide interface to user