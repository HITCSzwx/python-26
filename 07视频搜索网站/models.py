import sqlite3
import os


class DB:
    def __init__(self):
        db_file = 'db.sqlite3'
        print(f"Connecting to database: {os.path.abspath(db_file)}")
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def search_by_name(self, name):
        sql = "SELECT * FROM video_info WHERE video_name LIKE ?"
        print(f"Executing SQL: {sql} with parameters: ('%{name}%',)")
        self.cursor.execute(sql, ('%' + name + '%',))
        data = self.cursor.fetchall()
        new_data = []
        for d in data:
            new_data.append({
                "video_id": d[0],
                "video_name": d[1],
                "actor": d[2],
                "came_from": d[3],
                "video_kbps": d[4],
                "video_size": d[5],
                "video_language": d[6],
                "released_data": d[7],
                "bdyun_url": d[8],
                "bdyun_password": d[9],
            })
        print(new_data)
        return new_data



if __name__ == '__main__':
    db = DB()
    db.search_by_name('')

