# модель Автори
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Signal, QDateTime

from DataWorker import DataWorker


class ModelAuthors(QAbstractListModel):

    #ролі
    R_ID = Qt.UserRole + 1
    R_FAM = Qt.UserRole + 2
    R_NAME = Qt.UserRole + 3
    R_UPD = Qt.UserRole + 4
    R_USER = Qt.UserRole + 5
    R_FULLNAME = Qt.UserRole + 6

    #данні
    MD = []
    USER = 0

    #сигнал помилки
    error = Signal(str, arguments=['error'])

    def __init__(self, conn:str, parent=None):
        super().__init__(parent)
        self.BASE = DataWorker(conn)
        self.loadModel()

    # перегружені базові функції
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
            self.R_UPD:b"_upd",
            self.R_USER:b"_user",
            self.R_FULLNAME:b"_fullName"
        }
    
    #загрузка моделі
    def loadModel(self):
        self.beginResetModel()
        self.MD.clear()

        db_data = self.BASE.data_get(self.BASE.T_AUTHORS)

        if db_data['r']:
            self.MD = db_data['data']
        else:
            self.error.emit(db_data['message'])

        self.endResetModel()

    # віддаємо карту
    @Slot(int, result=dict)
    def getCard(self, index:int):
        return self.MD[index]
    
    # позначаємо юзера
    @Slot(int)
    def setUser(self, user:int):
        self.USER = user

    # збереження
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

            res = self.BASE.data_save(self.BASE.T_AUTHORS, card)
            if res['r']:
                self.loadModel()
                return True
            else:
                self.error.emit(res['message'])
                return False

    # видалення      
    @Slot(int, result=bool)
    def deleteCard(self, id:int):
        res = self.BASE.data_del(self.BASE.T_AUTHORS, id)
        if res['r']:
            self.loadModel()
            return True
        else:
            self.error.emit(res['message'])
            return False

    