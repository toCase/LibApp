from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal, QDateTime

from DataWorker import DataWorker


class ModelLib(QAbstractListModel):

    #role
    R_ID = Qt.UserRole + 1
    R_BOOK = Qt.UserRole + 2
    R_BOOKNAME = Qt.UserRole + 3
    R_READER = Qt.UserRole + 4
    R_READERNAME = Qt.UserRole + 5
    R_START = Qt.UserRole + 6
    R_FIN = Qt.UserRole + 7
    R_UPD = Qt.UserRole + 8
    R_USER = Qt.UserRole + 9

    #model data
    MD = []
    USER = 0

    #model error
    error = Signal(str, arguments=['error'])

    def __init__(self, conn:str, parent=None):
        super().__init__(parent)
        self.BASE = DataWorker(conn)
        self.loadModel()


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
        if role == self.R_BOOKNAME:
            r = card['bookName']
        if role == self.R_READER:
            r = card['reader_id']
        if role == self.R_READERNAME:
            r = card['readerFam'] + " " + card['readerName']
        if role == self.R_START:
            r = card['start']
        if role == self.R_FIN:
            r = card['fin']
        if role == self.R_UPD:
            r = card['updated']
        if role == self.R_USER:
            r = card['user']
        return r

    def roleNames(self):
        return {
            self.R_ID:b"_id",
            self.R_BOOK:b"_book_id",
            self.R_BOOKNAME:b"_bookName",
            self.R_READER:b"_reader_id",
            self.R_READERNAME:b"_readerName",
            self.R_START:b"_startDate",
            self.R_FIN:b"_finDate",
            self.R_UPD:b"_upd",
            self.R_USER:b"_user"
        }

    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()

        db_data = self.BASE.data_get(self.BASE.T_LIBRARY)

        if db_data['r']:
            self.MD = db_data['data']
        else:
            self.error.emit(db_data['message'])
        
        self.endResetModel()

    @Slot(int, result=dict)
    def getCard(self, index:int):
        return self.MD[index]
    
    @Slot(result=str)
    def getError(self):
        return self.ERR
    
    @Slot(int)
    def setUser(self, user:int):
        self.USER = user

    @Slot(dict, result=bool)
    def save(self, card:dict):
        

        if card['reader_id'] == 0:
            self.error.emit("Вкажіть читача")
            return False  
        elif card['book_id'] == 0:
            self.error.emit("Вкажіть книгу")
            return False  
        else:
            card['updated'] = QDateTime.currentDateTime().toSecsSinceEpoch()
            card['user_id'] = self.USER

            # print("SAVE LIB: ", card)
            # return True

            res = self.BASE.data_save(self.BASE.T_LIBRARY, card)
            if res['r']:
                self.loadModel()
                return True
            else:
                self.error.emit(res['message'])
                return False
            
    @Slot(int, result=bool)
    def deleteCard(self, id:int):
        res = self.BASE.data_del(self.BASE.T_LIBRARY, id)
        if res['r']:
            self.loadModel()
            return True
        else:
            self.error.emit(res['message'])
            return False

    