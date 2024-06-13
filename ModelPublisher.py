from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal, QDateTime

from DataWorker import DataWorker


class ModelPublishers(QAbstractListModel):

    #role
    R_ID = Qt.UserRole + 1
    R_NAME = Qt.UserRole + 2
    R_UPD = Qt.UserRole + 3
    R_USER = Qt.UserRole + 4

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
        if role == self.R_NAME:
            r = card['name']
        if role == self.R_UPD:
            r = card['updated']
        if role == self.R_USER:
            r = card['user']
        return r

    def roleNames(self):
        return {
            self.R_ID:b"_id",
            self.R_NAME:b"_name",
            self.R_UPD:b"_upd",
            self.R_USER:b"_user"
        }

    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()

        db_data = self.BASE.data_get(self.BASE.T_PUBLISHERS)

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
        print("USER: ", self.USER)
        if len(card['name']) == 0:
            self.error.emit("Назва не має бути пустою")
            return False        
        else:
            card['updated'] = QDateTime.currentDateTime().toSecsSinceEpoch()
            card['user_id'] = self.USER

            res = self.BASE.data_save(self.BASE.T_PUBLISHERS, card)
            if res['r']:
                self.loadModel()
                return True
            else:
                self.error.emit(res['message'])
                return False
            
    @Slot(int, result=bool)
    def deleteCard(self, id:int):
        res = self.BASE.data_del(self.BASE.T_PUBLISHERS, id)
        if res['r']:
            self.loadModel()
            return True
        else:
            self.error.emit(res['message'])
            return False

    