import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, phone_number):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`phone_number`) VALUES (?)", (phone_number,))

    def get_user(self):
        with self.connection:
            return self.cursor.execute('SELECT `phone_number` FROM `users`').fetchall()

    def save_slovar(self, sp_articul, sp_days, sp_punkt):
        with self.connection:
            return self.cursor.execute("""
            INSERT INTO `slovar` (`articul`, `days`, `punkt`)
            VALUES
            (?,?,?)
            """,(sp_articul, sp_days, sp_punkt,))

    def delete_from_slovar(self, articul):
        with self.connection:
            return self.cursor.execute("DELETE FROM `slovar` WHERE `articul` = ?", (articul,))

#GET REQUESTED COLUMNS
    def get_articul(self):
        with self.connection:
            articul = str(self.cursor.execute('SELECT `articul` FROM `slovar`').fetchone())
            return articul[1:len(articul)-2]

    def get_days(self):
        days = str(self.cursor.execute("SELECT `days` FROM `slovar`").fetchone())
        return days[1:len(days)-2]

    def get_punkt(self):
        punkt = str(self.cursor.execute("SELECT `punkt` FROM `slovar`").fetchone())
        return punkt[2:len(punkt) - 3]

#DELETE CURENT DATA

    def delete_curent_data(self):
        with self.connection:
            return self.cursor.execute('DELETE FROM `slovar`')




