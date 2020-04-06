import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('drill.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_docs( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    for fileName in fileList:
        if fileName.endswith('txt'):
            cur.execute('INSERT INTO tbl_docs(col_name) VALUES (?)', (fileName,))
            print(fileName)



