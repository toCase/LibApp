import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: publishers

    QtObject {
        id: internal

        property int idx: 0

        function add() {
            idx = 0
            form_name.clear()
            form.visible = true
        }

        function edit(index) {
            let card = modelPublishers.getCard(index)
            idx = card['id']
            form_name.text = card['name']
            form.visible = true

            
        }

        function save() {
            let card = {}
            card['id'] = idx
            card['name'] = form_name.text

            let r = modelPublishers.save(card)
            if (r) {
                close()
            } else {
                console.log("ERR")
            }            
        }

        function del() {
            let r = modelPublishers.deleteCard(idx)
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
            Layout.minimumHeight: 120
            Layout.maximumHeight: 120

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

                    spacing: 10

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Назва видавця"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_name
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

            model: modelPublishers
            clip: true

            delegate: Rectangle {

                required property int index
                required property string _name

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
            ScrollBar.vertical: ScrollBar{}           
        }
    }
}