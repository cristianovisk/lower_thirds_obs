import sqlite3

class Manager_Speakers:
    def __init__(self) -> None:
        
        self.conn = sqlite3.connect('data.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS speakers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    subtitle TEXT NOT NULL
            );
            """)
        self.conn.commit()

    def insert_Speaker(self, name, subtitle):
        name = name.upper()
        subtitle = subtitle.title()
        try:
            if self.__check_Speaker(name, subtitle) == False:
                self.cursor.execute(f'INSERT INTO speakers (name, subtitle) VALUES ("{name}", "{subtitle}")')
                self.conn.commit()
                return True
            else:
                return False
        except:
            return False
        
    def delete_Speaker(self, id):
        try:
            self.cursor.execute(f'DELETE FROM speakers WHERE id = {id}')
            self.conn.commit()
            return True
        except:
            return False

    def get_Speakers(self):
        speakers = []
        try:
            query = self.cursor.execute('SELECT * FROM speakers')
            query = self.cursor.fetchall()  
            self.conn.commit()
            for spk in query:
                model = {
                    "id": spk[0],
                    "name": spk[1],
                    "subtitle": spk[2]
                }
                speakers.append(model)
            return speakers
        except:
            return None
    
    def get_Speaker_by_ID(self, id_host):
        speakers = []
        try:
            query = self.cursor.execute(f'SELECT * FROM speakers WHERE id = {id_host}')
            query = self.cursor.fetchall()  
            self.conn.commit()
            for spk in query:
                model = {
                    "id": spk[0],
                    "name": spk[1],
                    "subtitle": spk[2]
                }
                speakers.append(model)
            return speakers
        except:
            return None
    
    def __check_Speaker(self, name, subtitle):
        try:
            query = self.cursor.execute(f'SELECT name, subtitle FROM speakers WHERE name = "{name}" AND subtitle = "{subtitle}"')
            query = self.cursor.fetchall()
            self.conn.commit()
            if len(query) > 0:
                return True
            elif len(query) == 0:
                return False
        except:
            return None
        
if __name__ == "__main__":
    mg = Manager_Speakers()
    print(mg.get_Speakers())