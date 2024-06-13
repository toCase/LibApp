from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataWorker(QObject):

    CON: str

    T_USERS: int = 30
    T_BOOKS: int = 31
    T_AUTHORS: int = 32
    T_READERS: int = 33
    T_LIBRARY: int = 34
    T_PUBLISHERS: int = 35
    T_BOOKAUTHORS: int = 36

    def __init__(self, con:str, parent = None):
        super().__init__(parent)
        self.CON = con
        self.connectDatabase()

    def connectDatabase(self):
        db = QSqlDatabase.addDatabase('QSQLITE', self.CON)
        db.setDatabaseName("lib.db3")
        db.open()
        if db.isOpen():
            qstr = [
                "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, pass TEXT) ",
                "CREATE TABLE IF NOT EXISTS Authors (id INTEGER PRIMARY KEY AUTOINCREMENT, fam TEXT, name TEXT, updated INTEGER, user_id INTEGER) ",
                "CREATE TABLE IF NOT EXISTS Publishers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, updated INTEGER, user_id INTEGER) ",
                '''CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, isbn TEXT, 
                anotation TEXT, writed INTEGER, publisher_id INTEGER, updated INTEGER, user_id INTEGER) ''',
                "CREATE TABLE IF NOT EXISTS BookAuthors (id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGR, author_id INTEGER) ",
                '''CREATE TABLE IF NOT EXISTS Readers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, fam TEXT, 
                faculty TEXT, department TEXT, position TEXT, updated INTEGER, user_id INTEGER) ''',
                '''CREATE TABLE IF NOT EXISTS Lib (id INTEGER PRIMARY KEY AUTOINCREMENT, reader_id INTEGER, book_id INTEGER, 
                start TEXT, fin TEXT, updated INTEGER, user_id INTEGER) ''',
            ]
            for q in qstr:
                query = QSqlQuery(q, db)
                query.exec()  

    

    def data_save(self, table:int, card:dict):
        db = QSqlDatabase.database(self.CON)
        if db.isOpen():
            id = card['id']
            if id == 0:

                if table == self.T_USERS:
                    qstr = "INSERT INTO Users (login, pass) VALUES (?, ?)"
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['login'])
                    query.bindValue(1, card['pass'])                

                if table == self.T_AUTHORS:
                    qstr = "INSERT INTO Authors (`fam`, `name`, `updated`, `user_id`) VALUES (?, ?, ?, ?) "
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['fam'])                    
                    query.bindValue(1, card['name'])
                    query.bindValue(2, card['updated'])
                    query.bindValue(3, card['user_id'])

                if table == self.T_PUBLISHERS:
                    qstr = "INSERT INTO Publishers (`name`, `updated`, `user_id`) VALUES (?, ?, ?) "
                    query = QSqlQuery(qstr, db)                 
                    query.bindValue(0, card['name'])
                    query.bindValue(1, card['updated'])
                    query.bindValue(2, card['user_id'])

                if table == self.T_BOOKS:
                    qstr = "INSERT INTO Books (`name`, `isbn`, `anotation`, `writed`, `publisher_id`, `updated`, `user_id`) VALUES (?, ?, ?, ?, ?, ?, ?) "
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['name'])                    
                    query.bindValue(1, card['isbn'])
                    query.bindValue(2, card['anotation'])
                    query.bindValue(3, card['writed'])
                    query.bindValue(4, card['publisher_id'])
                    query.bindValue(5, card['updated'])
                    query.bindValue(6, card['user_id'])
                
                if table == self.T_BOOKAUTHORS:
                    qstr = "INSERT INTO BookAuthors (`book_id`, `author_id`) VALUES (?, ?) "
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['book_id'])                    
                    query.bindValue(1, card['author_id'])
                
                if table == self.T_READERS:
                    qstr = "INSERT INTO Readers (`name`, `fam`, `faculty`, `department`, `position`, `updated`, `user_id`) VALUES (?, ?, ?, ?, ?, ?, ?) "
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['name'])                    
                    query.bindValue(1, card['fam'])
                    query.bindValue(2, card['faculty'])
                    query.bindValue(3, card['department'])
                    query.bindValue(4, card['position'])
                    query.bindValue(5, card['updated'])
                    query.bindValue(6, card['user_id'])
                
                if table == self.T_LIBRARY:
                    qstr = "INSERT INTO Lib (`reader_id`, `book_id`, `start`, `fin`, `updated`, `user_id`) VALUES (?, ?, ?, ?, ?, ?) "
                    query = QSqlQuery(qstr, db)
                    query.bindValue(0, card['reader_id'])                    
                    query.bindValue(1, card['book_id'])
                    query.bindValue(2, card['start'])
                    query.bindValue(3, card['fin'])
                    query.bindValue(4, card['updated'])
                    query.bindValue(5, card['user_id'])

                if query.exec():
                    r = {'r': True, 'message': '', 'id':query.lastInsertId()}
                else:
                    r = {'r': False, 'message': query.lastError().text(), 'id':0}
            else:

                if table == self.T_USERS:
                    qstr = f''' UPDATE Users SET login = \'{card['login']}\', pass=\'{card['pass']}\'
                        WHERE (Company.id = \'{card[id]}\') '''

                if table == self.T_AUTHORS:
                    qstr = f''' UPDATE Authors SET `fam`=\'{card['fam']}\', `name`=\'{card['name']}\', `updated`=\'{card['updated']}\', 
                    `user_id`=\'{card['user_id']}\' 
                    WHERE (Authors.id = \'{card['id']}\') '''

                if table == self.T_PUBLISHERS:
                    qstr = f''' UPDATE Publishers SET  `name`=\'{card['name']}\', `updated`=\'{card['updated']}\', 
                    `user_id`=\'{card['user_id']}\' 
                    WHERE (Publishers.id = \'{card['id']}\') '''
                
                if table == self.T_BOOKS:
                    qstr = f''' UPDATE Books SET  `name`=\'{card['name']}\', `isbn`=\'{card['isbn']}\', `anotation`=\'{card['anotation']}\', 
                    `writed`=\'{card['writed']}\', `publisher_id`=\'{card['publisher_id']}\', `updated`=\'{card['updated']}\', 
                    `user_id`=\'{card['user_id']}\' 
                    WHERE (Books.id = \'{card['id']}\') '''
                
                if table == self.T_READERS:
                    qstr = f''' UPDATE Readers SET  `name`=\'{card['name']}\', `fam`=\'{card['fam']}\', `faculty`=\'{card['faculty']}\', 
                    `department`=\'{card['department']}\', `position`=\'{card['position']}\', `updated`=\'{card['updated']}\', 
                    `user_id`=\'{card['user_id']}\' 
                    WHERE (Readers.id = \'{card['id']}\') '''

                if table == self.T_LIBRARY:
                    qstr = f''' UPDATE Lib SET `reader_id`=\'{card['reader_id']}\', `book_id`=\'{card['book_id']}\', `start`=\'{card['start']}\', 
                    `fin`=\'{card['fin']}\', `updated`=\'{card['updated']}\', 
                    `user_id`=\'{card['user_id']}\' 
                    WHERE (Lib.id = \'{card['id']}\') '''

                query = QSqlQuery(qstr, db)
                if query.exec():
                    r = {'r': True, 'message': '', 'id':card['id']}
                else:
                    r = {'r': False, 'message': query.lastError().text(), 'id':0}

        else:
            r = {'r': False, 'message': self.ERR_CON, 'id':0}
        return r


    def data_del(self, table:int, id:int):
        db = QSqlDatabase.database(self.CON)
        if db.isOpen():
            if table == self.T_USERS:
                qstr = f"DELETE FROM Users WHERE Users.id = {id}"
                query = QSqlQuery(qstr, db)

            if table == self.T_AUTHORS:
                qstr = f"DELETE FROM Authors WHERE Authors.id = {id}"
                query = QSqlQuery(qstr, db)
            
            if table == self.T_PUBLISHERS:
                qstr = f"DELETE FROM Publishers WHERE Publishers.id = {id}"
                query = QSqlQuery(qstr, db)
            
            if table == self.T_BOOKS:
                qstrX = f"DELETE FROM BookAuthors WHERE BookAuthors.book_id = {id}"
                queryX = QSqlQuery(qstrX, db)
                if queryX.exec():
                    qstr = f"DELETE FROM Books WHERE Books.id = {id}"
                    query = QSqlQuery(qstr, db)

            if table == self.T_BOOKAUTHORS:
                qstr = f"DELETE FROM BookAuthors WHERE BookAuthors.book_id = {id}"
                query = QSqlQuery(qstr, db)

            if table == self.T_READERS:
                qstr = f"DELETE FROM Readers WHERE Readers.id = {id}"
                query = QSqlQuery(qstr, db)
            
            if table == self.T_LIBRARY:
                qstr = f"DELETE FROM Lib WHERE Lib.id = {id}"
                query = QSqlQuery(qstr, db)

            if query.exec():
                r = {'r': True, 'message': ''}
            else:
                r = {'r': False, 'message': query.lastError().text()}  
        else:
            r = {'r': False, 'message': self.ERR_CON}
        return r

    def data_get(self, table:int, filters:dict = None):
        db = QSqlDatabase.database(self.CON)
        if db.isOpen():
            if table == self.T_USERS:
                qstr = "SELECT * FROM Users WHERE (Users.id > \'0\') "
                if filters:
                    if 'login' in filters:
                        qstr = qstr + f"AND (Users.`login` = \'{filters['login']}\') "
                    if 'pass' in filters:
                        qstr = qstr + f"AND (Users.`pass` = \'{filters['pass']}\') "

                qstr = qstr + "ORDER BY Users.id "

            if table == self.T_AUTHORS:
                qstr = "SELECT * FROM Authors WHERE (Authors.id > \'0\') "
                if filters:
                    if 'name' in filters:
                        qstr = qstr + f"AND (Authors.`name` LIKE \'%{filters['name']}%\') "
                    if 'id' in filters:
                        qstr = qstr + f"AND (Authors.`id` = \'{filters['id']}\') "
                qstr = qstr + "ORDER BY Authors.fam, Authors.name "

            if table == self.T_PUBLISHERS:
                qstr = "SELECT * FROM Publishers WHERE (Publishers.id > \'0\') "
                if filters:
                    if 'name' in filters:
                        qstr = qstr + f"AND (Publishers.`name` LIKE \'%{filters['name']}%\') "
                qstr = qstr + "ORDER BY Publishers.name "

            if table == self.T_BOOKS:
                qstr = '''SELECT b.*, p.name AS pubName, GROUP_CONCAT(Authors.fam || ' ' || Authors.name) AS authors
                FROM Books AS b 
                INNER JOIN Publishers AS p ON p.id = b.publisher_id 
                JOIN BookAuthors ON b.id = BookAuthors.book_id
                JOIN Authors ON BookAuthors.author_id = Authors.id
                WHERE (b.id > \'0\') '''
                if filters:
                    if 'name' in filters:
                        qstr = qstr + f"AND (b.`name` LIKE \'%{filters['name']}%\') "
                    if 'isbn' in filters:
                        qstr = qstr + f"AND (b.`isbn` LIKE \'%{filters['isbn']}%\') "
                    if 'writed' in filters:
                        qstr = qstr + f"AND (b.`writed` LIKE \'%{filters['writed']}%\') "
                    
                qstr = qstr + "GROUP BY b.id ORDER BY b.name "
            
            if table == self.T_READERS:
                qstr = "SELECT * FROM Readers WHERE (Readers.id > \'0\') "
                if filters:
                    if 'fam' in filters:
                        qstr = qstr + f"AND (Readers.`fam` LIKE \'%{filters['fam']}%\') "
                    if 'name' in filters:
                        qstr = qstr + f"AND (Readers.`name` LIKE \'%{filters['name']}%\') "
                    if 'faculty' in filters:
                        qstr = qstr + f"AND (Readers.`faculty` LIKE \'%{filters['faculty']}%\') "
                    if 'department' in filters:
                        qstr = qstr + f"AND (Readers.`department` LIKE \'%{filters['department']}%\') "
                    if 'position' in filters:
                        qstr = qstr + f"AND (Readers.`position` LIKE \'%{filters['position']}%\') "

                qstr = qstr + "ORDER BY Readers.fam, Readers.name "

            if table == self.T_LIBRARY:
                qstr = '''SELECT l.*, r.name AS readerName, r.fam AS readerFam, b.name AS bookName FROM Lib AS l 
                INNER JOIN Readers AS r ON r.id = l.reader_id 
                INNER JOIN Books AS b ON b.id = l.book_id 
                WHERE (l.id > \'0\') '''
                if filters:
                    if 'reader_id' in filters:
                        qstr = qstr + f"AND (l.`reader_id` = \'{filters['reader_id']}\') "
                    if 'book_id' in filters:
                        qstr = qstr + f"AND (l.`book_id` = \'{filters['book_id']}\') "
                    if 'start' in filters:
                        qstr = qstr + f"AND (l.`start` > \'{filters['start']}\') "
                    if 'fin' in filters:
                        qstr = qstr + f"AND (l.`fin` = \'{filters['fin']}\') "

                qstr = qstr + "ORDER BY l.id "
            
            if table == self.T_BOOKAUTHORS:
                qstr = ''' SELECT ba.*, a.fam AS authorFam, a.name AS authorName  
                FROM BookAuthors AS ba 
                INNER JOIN Authors AS a ON a.id = ba.author_id 
                WHERE (ba.id > \'0\') '''
                if filters:
                    if 'book_id' in filters:
                        qstr = qstr + f"AND (ba.book_id = \'{filters['book_id']}\') "
                

            data = []
            query = QSqlQuery(qstr, db)

            while query.next():
                card = {}
                for i in range(0, query.record().count()):
                    field = query.record().field(i)

                    if table == self.T_BOOKAUTHORS and field.name() == 'id':
                        card['id'] = 0
                    else:
                        card[field.name()] = query.value(i)
                data.append(card)
                    

            if query.exec():
                r = {'r': True, 'message': "", 'data':data}
            else:                
                r = {'r': False, 'message': query.lastError().text(), 'data':[]}
                print(query.lastQuery())
        else:
            r = {'r': False, 'message': self.ERR_CON, 'data':[]}
        return r

    





