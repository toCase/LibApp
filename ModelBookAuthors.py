from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal, QDateTime

from DataWorker import DataWorker


class ModelBookAuthors(QAbstractListModel):

    #role
    R_ID = Qt.UserRole + 1
    R_BOOK = Qt.UserRole + 2
    R_AUTHOR = Qt.UserRole + 3
    R_AUTHORNAME = Qt.UserRole + 4

    #model data
    MD = []

    BOOK = 0

    #model error
    error = Signal(str, arguments=['error'])

    def __init__(self, conn:str, parent=None):
        super().__init__(parent)
        self.BASE = DataWorker(conn)

    @Slot(result=int)
    def rowCount(self, parent = None):
        return len(self.MD)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        r = None
        row = index.row()
        card = self.MD[row]

        if role == self.R_ID:
            r = card['id']
        if role == self.R_BOOK:
            r = card['book_id']
        if role == self.R_AUTHOR:
            r = card['author_id']
        if role == self.R_AUTHORNAME:
            r = card['authorFam'] + " " + card['authorName']
        return r

    def roleNames(self):
        return {
            self.R_ID:b"_id",
            self.R_BOOK:b"_book",
            self.R_AUTHOR:b"_author",
            self.R_AUTHORNAME:b"_authorName",
        }

    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()
        if self.BOOK > 0:
            filter = {'book_id': self.BOOK}
            db_data = self.BASE.data_get(self.BASE.T_BOOKAUTHORS, filter)

            if db_data['r']:
                self.MD = db_data['data']
            else:
                self.error.emit(db_data['message'])
        print(self.MD)
        self.endResetModel()
    
    
    @Slot(int)
    def setBook(self, book:int):
        self.BOOK = book
        self.loadModel()
        
    @Slot(int)
    def addAuthor(self, author:int):
        self.beginResetModel()
        filters = {'id':author}
        res = self.BASE.data_get(self.BASE.T_AUTHORS, filters)

        if res['r']:
            data = res['data']
            if len(data) > 0:
                cardA = data[0]                
                card = {'id':0, 'book_id':self.BOOK, 'author_id': author, 'authorName': cardA['name'], 'authorFam':cardA['fam']}
                self.MD.append(card)
        self.endResetModel()
    
    @Slot(int)
    def delAuthor(self, index:int):
        self.beginResetModel()
        self.MD.pop(index)
        self.endResetModel()
    
    @Slot(int, result=bool)
    def save(self, book:int):
        del_res = self.BASE.data_del(self.BASE.T_BOOKAUTHORS, book)
        if (del_res['r']):
            if len(self.MD) > 0:
                for card in self.MD:
                    card['id'] = 0
                    card['book_id'] = book
                    res = self.BASE.data_save(self.BASE.T_BOOKAUTHORS, card)

                    if res['r'] == False:
                        self.error.emit(res['message'])
                        return False
            else:
                self.error.emit("Оберіть хоча б одного автора")
                return False
        else:
            self.error.emit(del_res['message'])
            return False
        return True
    
    



    