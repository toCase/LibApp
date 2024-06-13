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
            form_name.clear()
            form_fam.clear()
            form_fac.clear()
            form_dep.clear()
            form_pos.clear()
            form.visible = true
        }

        function edit(index) {
            let card = modelReaders.getCard(index)
            idx = card['id']
            form_name.text = card['name']
            form_fam.text = card['fam']
            form_fac.text = card['faculty']
            form_dep.text = card['department']
            form_pos.text = card['position']
            form.visible = true            
        }

        function save() {
            let card = {}
            card['id'] = idx
            card['name'] = form_name.text
            card['fam'] = form_fam.text
            card['faculty'] = form_fac.text
            card['department'] = form_dep.text
            card['position'] = form_pos.text

            let r = modelReaders.save(card)
            if (r) {
                close()
            } else {
                console.log("ERR")
            }            
        }

        function del() {
            let r = modelReaders.deleteCard(idx)
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

                        text: "Ім'я"
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

                        text: "Прізвище"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_fam
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

                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Факультет"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_fac
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        font.pointSize: 13
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Кафедра"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_dep
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        font.pointSize: 13
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: implicitWidth
                        Layout.maximumWidth: implicitWidth

                        text: "Посада"
                        font.pointSize: 13
                        verticalAlignment: Qt.AlignVCenter
                    }
                    TextField {
                        id: form_pos
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

            model: modelReaders
            clip: true

            delegate: Rectangle {

                required property int index
                required property string _name
                required property string _fam
                required property string _faculty
                required property string _position


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

                        text: _fam + " " + _name
                        font.pointSize: 13
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    } 
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 250
                        Layout.maximumWidth: 250

                        text: _faculty
                        font.pointSize: 11
                        horizontalAlignment: Qt.AlignLeft
                        verticalAlignment: Qt.AlignVCenter
                    }
                    Label {
                        Layout.fillHeight: true
                        Layout.minimumWidth: 250
                        Layout.maximumWidth: 250

                        text: _position
                        font.pointSize: 11
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