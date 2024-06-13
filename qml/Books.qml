import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: authors

    QtObject {
        id: internal

        property int idx: 0

        function add() {
            idx = 0;
            form_name.clear()
            form_isbn.clear()
            form_publisher.currentIndex = -1
            form_writed.clear()
            form_anot.clear()

            form.visible = true;
        }

        function edit(index) {
            let card = modelBooks.getCard(index);
            idx = card['id'];
            form_name.text = card['name']
            form_isbn.text = card['isbn']
            form_publisher.currentIndex = form_publisher.find(card['pubName'])
            form_writed.text = card['writed']
            form_anot.text = card['anotation']

            form.visible = true;
        }

        function save() {
            let card = {};
            card['id'] = idx
            card['name'] = form_name.text
            card['isbn'] = form_isbn.text
            card['publisher_id'] = form_publisher.currentValue
            card['writed'] = form_writed.text
            card['anotation'] = form_anot.text

            let r = modelBooks.save(card);
            if (r) {
                close();
            } else {
                console.log("ERR");
            }
        }

        function del() {
            let r = modelBooks.deleteCard(idx);
            if (r) {
                close();
            } else {
                console.log("ERR");
            }
        }

        function close() {
            form.visible = false;
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
            Layout.minimumHeight: 430
            Layout.maximumHeight: 430

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

                        text: "Назва"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_name
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        font.pointSize: 13
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "ISBN"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_isbn
                        Layout.fillHeight: true
                        Layout.minimumWidth: 200
                        Layout.maximumWidth: 200
                        font.pointSize: 13
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

                        text: "Видавець"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    ComboBox {
                        id: form_publisher
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        model: modelPublishers
                        textRole: "_name"
                        valueRole: "_id"
                        font.pointSize: 13
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Дата:"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_writed
                        Layout.fillHeight: true
                        Layout.minimumWidth: 120
                        Layout.maximumWidth: 120
                        validator: IntValidator {}
                    }
                }

                RowLayout {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    spacing: 10

                    ColumnLayout {
                        
                        Layout.fillHeight: true
                        Layout.minimumWidth: form.width * 0.45
                        Layout.maximumWidth: form.width * 0.45
                        spacing: 5

                        Label {
                            Layout.minimumHeight: 40
                            Layout.maximumHeight: 40
                            Layout.fillWidth: true
                            text: "Анотація:"
                            font.pointSize: 13
                            verticalAlignment: Qt.AlignVCenter
                        }
                        TextArea {
                            id: form_anot
                            Layout.fillWidth: true
                            Layout.fillHeight: true

                            background: Rectangle {
                                radius: 5
                                color: "#FFFFFF"
                            }

                            wrapMode: TextEdit.WordWrap

                        }

                    }
                    ColumnLayout {
                        Layout.minimumWidth: form.width * 0.45
                        Layout.maximumWidth: form.width * 0.45
                        Layout.fillHeight: true
                        spacing: 5

                        RowLayout {
                            Layout.minimumHeight: 40
                            Layout.maximumHeight: 40
                            Layout.fillWidth: true
                            spacing: 5

                            Button {
                                Layout.fillHeight: true
                                Layout.minimumWidth: 40
                                Layout.maximumWidth: 40

                                text: "+"
                                onClicked: console.log("ADD AUTH")
                            }
                            Button {
                                Layout.fillHeight: true
                                Layout.minimumWidth: 40
                                Layout.maximumWidth: 40

                                text: "-"
                                onClicked: console.log("DEL AUTH")
                            }
                        }

                        Pane {
                            id: form_ba
                            visible: false
                            Layout.minimumHeight: 40
                            Layout.maximumHeight: 40
                            Layout.fillWidth: true

                            RowLayout {
                                anchors.fill: parent
                                spacing: 5

                                ComboBox {
                                    id: form_author
                                    Layout.fillHeight: true
                                    Layout.fillWidth: true
                                    model: modelAuthors
                                    textRole: "_fam" + " " + "_name" 
                                    valueRole: "_id"
                                }
                                Button {
                                    Layout.fillHeight: true
                                    Layout.minimumWidth: 120
                                    Layout.maximumWidth: 120
                                    text: "Зберегти"

                                }
                            }
                        }

                        ListView {
                            id: table_ba
                            Layout.fillHeight: true
                            Layout.fillWidth: true

                            clip: true
                            model: []
                            delegate: Rectangle {

                                width: table_ba.width
                                height: 35

                                color: "transparent"
                            }
                            ScrollBar.vertical: ScrollBar{}
                        }

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

            model: modelBooks
            clip: true

            delegate: Rectangle {

                required property int index
                required property string _name
                required property string _writed

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
                        Layout.fillWidth: true

                        text: _name
                        font.pointSize: 13
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    }
                }
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onHoveredChanged: parent.color = containsMouse ? "#F2F2F2" : "transparent"
                    onDoubleClicked: internal.edit(index)
                }
            }
            ScrollBar.vertical: ScrollBar {}
        }
    }
}
