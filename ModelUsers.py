from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal

from DataWorker import DataWorker


class ModelUsers(QAbstractListModel):

    #role
    R_ID = Qt.UserRole + 1
    R_LOGIN = Qt.UserRole + 2
    R_PASS = Qt.UserRole + 3

    #model data
    MD = []
    USER = {}

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
            r = card.get('id')
        elif role == self.R_LOGIN:
            r = card.get('login')
        elif role == self.R_PASS:
            r = card.get('pass')

        return r

    def roleNames(self):
        return {
            self.R_ID:b"_id",
            self.R_LOGIN:b"_login",
            self.R_PASS:b"_pass",
        }

    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()

        db_data = self.BASE.data_get(self.BASE.T_USERS)

        if db_data['r']:
            self.MD = db_data['data']

        self.endResetModel()

    @Slot(int, str, result = str)
    def get(self, index:int, item:str):
        card = self.MD[index]
        return str(card[item])
    
    

    @Slot(result=str)
    def getError(self):
        return self.ERR

    @Slot(dict, result=bool)
    def save(self, card:dict):

        if len(card['login']) == 0:
            self.error.emit("Login is empty")
            return False
        elif len(card['pass']) == 0:
            self.error.emit("Pass is empty")
            return False
        else:
            res = self.BASE.data_save(self.BASE.T_USERS, card)
            if res['r']:
                self.loadModel()
                return True
            else:
                self.error.emit(res['message'])
                return False
            
    @Slot(int, result=bool)
    def deleteCard(self, id:int):
        res = self.BASE.data_del(self.BASE.T_USERS, id)
        if res['r']:
            self.loadModel()
            return True
        else:
            self.error.emit(res['message'])
            return False

    @Slot(str, str, result=bool)
    def logIn(self, login:str, pas:str):
        filters = {'login':login, 'pass':pas}

        res = self.BASE.data_get(self.BASE.T_USERS, filters)
        if res['r']:
            data = res['data']
            if data:
                self.USER = data[0]
                return True
            else:
                self.USER = 0
                self.error.emit("Fail login or pass")
                return False    
        else:
            self.USER = 0
            self.error.emit(res['message'])
            return False
    
    @Slot(result=dict)
    def getUser(self):
        print("u: ", self.USER)
        return self.USER