import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import ModelUsers
import ModelPublisher
import ModelAuthors
import ModelBooks
import ModelReaders
import ModelLib
import ModelBookAuthors

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "qml/main.qml"

    modelUsers = ModelUsers.ModelUsers("USERS")
    engine.rootContext().setContextProperty("modelUsers", modelUsers)

    modelPublishers = ModelPublisher.ModelPublishers("PUB")
    engine.rootContext().setContextProperty("modelPublishers", modelPublishers)

    modelAuthors = ModelAuthors.ModelAuthors("AUT")
    engine.rootContext().setContextProperty("modelAuthors", modelAuthors)

    modelBooks = ModelBooks.ModelBooks("BOOKS")
    engine.rootContext().setContextProperty("modelBooks", modelBooks)

    modelReaders = ModelReaders.ModelReaders("READ")
    engine.rootContext().setContextProperty("modelReaders", modelReaders)

    modelLibrary = ModelLib.ModelLib("LIB")
    engine.rootContext().setContextProperty("modelLibrary", modelLibrary)

    modelBA = ModelBookAuthors.ModelBookAuthors("BA")
    engine.rootContext().setContextProperty("modelBA", modelBA)

    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
