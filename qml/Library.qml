import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: readers

    QtObject {
        id: internal

        property int idx: 0

        function add() {
            idx = 0
            form_reader.currentIndex = -1
            form_book.currentIndex = -1
            form_start.clear()
            form_fin.clear()
            form.visible = true
        }

        function edit(index) {
            let card = modelLibrary.getCard(index)
            idx = card['id']
            form_reader.currentIndex = form_reader.find(card['readerFam'] + " " + card['readerName'])
            form_book.currentIndex = form_book.find(card['bookName'])
            form_start.text = card['start']
            form_fin.text = card['fin']
            form.visible = true            
        }

        function save() {
            let card = {}
            card['id'] = idx
            card['reader_id'] = form_reader.currentValue
            card['book_id'] = form_book.currentValue
            card['start'] = form_start.text
            card['fin'] = form_fin.text
            
            let r = modelLibrary.save(card)
            if (r) {
                close()
            } else {
                console.log("ERR")
            }            
        }

        function del() {
            let r = modelLibrary.deleteCard(idx)
            if (r) {
                close()
            } else {
                console.log("ERR")
            }
        }

        function close() {
            form.visible = false
        }

    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 15

        RowLayout {
            Layout.fillWidth: true
            Layout.minimumHeight: 40
            Layout.maximumHeight: 40
            spacing: 15

            Button {
                Layout.fillHeight: true
                Layout.minimumWidth: 120
                Layout.maximumWidth: 120

                text: "Додати"

                onClicked: internal.add()
            }

            Item {
                Layout.fillWidth: true
            }
        }

        Pane {
            id: form
            visible: false
            Layout.fillWidth: true
            Layout.minimumHeight: 170
            Layout.maximumHeight: 170

            background: Rectangle {
                radius: 10
                color: "#F6F6F6"
            }

            ColumnLayout {
                anchors.fill: parent
                spacing: 5

                RowLayout {
                    Layout.fillWidth: true
                    Layout.minimumHeight: 40
                    Layout.maximumHeight: 40

                    spacing: 5

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Читач: "
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    ComboBox {
                        id: form_reader
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        model: modelReaders
                        textRole: "_fullName"
                        valueRole: "_id"
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Книга"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    ComboBox {
                        id: form_book
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        model: modelBooks
                        textRole: "_name"
                        valueRole: "_id"
                    }
                }

                RowLayout {
                    Layout.fillWidth: true
                    Layout.minimumHeight: 40
                    Layout.maximumHeight: 40

                    spacing: 5

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Дата отримання:"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_start
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        font.pointSize: 13
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Дата повернення:"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_fin
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        font.pointSize: 13
                    }
                }

                RowLayout {
                    Layout.fillWidth: true
                    Layout.minimumHeight: 40
                    Layout.maximumHeight: 40

                    spacing: 5

                    Button {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 120
                        Layout.maximumWidth: 120
                        text: "Видалити"
                        onClicked: internal.del()
                    }
                    Item {
                        Layout.fillWidth: true
                    }
                    Button {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 120
                        Layout.maximumWidth: 120
                        text: "Зберегти"
                        onClicked: internal.save()
                    }
                    Button {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 40
                        Layout.maximumWidth: 40
                        text: "X"
                        onClicked: internal.close()
                    }
                }
            }
        }

        ListView {
            id: table
            Layout.fillWidth: true
            Layout.fillHeight: true

            model: modelLibrary
            clip: true

            delegate: Rectangle {

                required property int index
                required property string _readerName
                required property string _bookName
                // required property string _start
                // required property string _fin


                width: table.width
                height: 35
                radius: 5

                color: "transparent"

                RowLayout {
                    anchors.fill: parent
                    anchors.leftMargin: 15
                    anchors.rightMargin: 15
                    spacing: 5

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 40
                        Layout.maximumWidth: 40

                        text: index + 1
                        font.pointSize: 11
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    }

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 350
                        Layout.maximumWidth: 350

                        text: _readerName
                        font.pointSize: 13
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    } 
                    Label {
                        Layout.fillHeight: true
                        Layout.fillWidth: true

                        text: _bookName
                        font.pointSize: 11
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    }
                    // Label {
                    //     Layout.fillHeight: true
                    //     Layout.minimumWidth: 150
                    //     Layout.maximumWidth: 150

                    //     text: _start
                    //     font.pointSize: 11
                    //     horizontalAlignment: Qt.AlignLeft
                    //     verticalAlignment: Qt.AlignVCenter
                    // }
                    // Label {
                    //     Layout.fillHeight: true
                    //     Layout.minimumWidth: 150
                    //     Layout.maximumWidth: 150

                    //     text: _fin
                    //     font.pointSize: 11
                    //     horizontalAlignment: Qt.AlignLeft
                    //     verticalAlignment: Qt.AlignVCenter
                    // }
                }
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onHoveredChanged: parent.color = containsMouse ? "#F2F2F2" : "transparent"
                    onDoubleClicked: internal.edit(index) 
                    
                }

            }   
            ScrollBar.vertical: ScrollBar{}         
        }
    }
}