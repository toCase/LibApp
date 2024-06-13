import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: app

    QtObject {
        id: internal

        function makeMessa(messa, i){
            messageText.text = messa
            if (i == 1){
                messageBox.color = "#ffc6d5"
            } else {
                messageBox.color = "#bde0af"
            }
            messageBox.visible = true
            messaTimer.start()
        }

    }

    MenuBar {
        anchors.top: app.top
        width: app.width
        height: 40

        
        MenuBarItem {
            text: "Книги"
            onTriggered: {
                appStack.pop()
                appStack.push(books)
            }
        }
        MenuBarItem {
            text: "Автори"
            onTriggered: {
                appStack.pop()
                appStack.push(authors)
            }
        }
        MenuBarItem {
            text: "Видавці"
            onTriggered: {
                appStack.pop()
                appStack.push(publishers)
            }
        }
        MenuBarItem {
            text: "Читачі"
            onTriggered: {
                appStack.pop()
                appStack.push(readers)
            }
        }
        MenuBarItem {
            text: "Бібліотека"
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

    Rectangle {
        id: messageBox
        width: app.width * 0.8
        height: 60
        y: app.height - 100
        x: app.width - width

        color: "#bde0af"
        visible: false

        Text {
            id: messageText
            anchors.fill: parent
            anchors.margins: 10

            text: "Some problen"
            font.pointSize: 13
            horizontalAlignment: Qt.AlignLeft
            verticalAlignment: Qt.AlignVCenter
        }
    }

    Timer {
        id: messaTimer
        interval: 3000;
        running: false
        repeat: false
        onTriggered: messageBox.visible = false
    }

    Connections{
        target: modelPublishers
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }
    Connections{
        target: modelAuthors
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }
    Connections{
        target: modelBooks
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }
    Connections{
        target: modelBA
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }
    Connections{
        target: modelReaders
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }
    Connections{
        target: modelLibrary
        function onError(error){
            internal.makeMessa(error, 1)
        }
    }

    Connections{
        target: books
        function onError(message){
            internal.makeMessa(message, 1)
        }
    }

    
}