import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: app

    QtObject {
        id: internal

    }

    MenuBar {
        anchors.top: app.top
        width: app.width
        height: 40

        
        MenuBarItem {
            text: "Books"
            onTriggered: {
                appStack.pop()
                appStack.push(books)
            }
        }
        MenuBarItem {
            text: "Authors"
            onTriggered: {
                appStack.pop()
                appStack.push(authors)
            }
        }
        MenuBarItem {
            text: "Publishers"
            onTriggered: {
                appStack.pop()
                appStack.push(publishers)
            }
        }
        MenuBarItem {
            text: "Readers"
            onTriggered: {
                appStack.pop()
                appStack.push(readers)
            }
        }
        MenuBarItem {
            text: "Library"
            onTriggered: {
                appStack.pop()
            }
        }
    }

    StackView {
        id: appStack
        anchors.fill: parent
        anchors.topMargin: 40
        initialItem: lib
    }

    

    Publishers {
        id: publishers
        visible: false
    }

    Authors {
        id: authors
        visible: false
    }

    Books {
        id: books
        visible: false
    }

    Readers {
        id: readers
        visible: false
    }

    Library {
        id: lib
        visible: false
    }

    
}