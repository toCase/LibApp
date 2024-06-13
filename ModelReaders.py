from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal, QDateTime

from DataWorker import DataWorker


class ModelReaders(QAbstractListModel):

    #role
    R_ID = Qt.UserRole + 1
    R_FAM = Qt.UserRole + 2
    R_NAME = Qt.UserRole + 3
    R_FAC = Qt.UserRole + 4
    R_DEP = Qt.UserRole + 5
    R_POS = Qt.UserRole + 6
    R_UPD = Qt.UserRole + 7
    R_USER = Qt.UserRole + 8
    R_FULLNAME = Qt.UserRole + 9

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
        if role == self.R_FAM:
            r = card['fam']
        if role == self.R_NAME:
            r = card['name']
        if role == self.R_FAC:
            r = card['faculty']
        if role == self.R_DEP:
            r = card['department']
        if role == self.R_POS:
            r = card['position']
        if role == self.R_UPD:
            r = card['updated']
        if role == self.R_USER:
            r = card['user']
        if role == self.R_FULLNAME:
            r = card['fam'] + " " + card['name']
        return r

    def roleNames(self):
        return {
            self.R_ID:b"_id",
            self.R_FAM:b"_fam",
            self.R_NAME:b"_name",
            self.R_FAC:b"_faculty",
            self.R_DEP:b"_department",
            self.R_POS:b"_position",
            self.R_UPD:b"_upd",
            self.R_USER:b"_user",
            self.R_FULLNAME:b"_fullName"
        }

    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()

        db_data = self.BASE.data_get(self.BASE.T_READERS)

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
        if len(card['name']) == 0:
            self.error.emit("Не вказано ім'я ")
            return False  
        elif len(card['fam']) == 0:
            self.error.emit("Не вказано прізвище")
            return False  
        else:
            card['updated'] = QDateTime.currentDateTime().toSecsSinceEpoch()
            card['user_id'] = self.USER

            res = self.BASE.data_save(self.BASE.T_READERS, card)
            if res['r']:
                self.loadModel()
                return True
            else:
                self.error.emit(res['message'])
                return False
            
    @Slot(int, result=bool)
    def deleteCard(self, id:int):
        res = self.BASE.data_del(self.BASE.T_READERS, id)
        if res['r']:
            self.loadModel()
            return True
        else:
            self.error.emit(res['message'])
            return False

    