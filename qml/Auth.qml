import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Basic

Item {
    id: auth

    QtObject{
        id: internal

        function test() {
            let r = modelUsers.logIn(fLogin.text, fPass.text)
            if (r) {
                let card = modelUsers.getUser()
                modelPublishers.setUser(card['id'])
                modelAuthors.setUser(card['id'])
                modelBooks.setUser(card['id'])
                modelReaders.setUser(card['id'])
                modelLibrary.setUser(card['id'])

                authStack.push(app)        
            } else {
                console.log("NOT LOGIN")
            }            
        }       
    }

    StackView {
        id: authStack
        anchors.fill: parent
        initialItem: pAuth

    }

    Pane {
        id: pAuth


        Item {
            anchors.centerIn: parent

            width: pAuth.width * .7
            height: pAuth.height * .7

            // color: "#00FF00"

            ColumnLayout {
                anchors.fill: parent
                spacing: 25

                Text {
                    Layout.fillWidth: true
                    Layout.minimumHeight: implicitHeight
                    Layout.maximumHeight: implicitHeight

                    text: "Authorizathion"
                    font.pointSize: 15
                    horizontalAlignment: Qt.AlignHCenter
                    verticalAlignment: Qt.AlignVCenter

                }

                RowLayout {
                    Layout.fillWidth: true
                    Layout.minimumHeight: 40
                    Layout.maximumHeight: 40

                    spacing: 15

                    TextField {
                        id: fLogin
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        placeholderText: "LOGIN"
                        font.pointSize: 13                        
                    }
                    TextField {
                        id: fPass
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        placeholderText: "PASSWORD"
                        font.pointSize: 13                        
                    }
                }

                RowLayout {
                    Layout.fillWidth: true
                    Layout.minimumHeight: 40
                    Layout.maximumHeight: 40
                    spacing: 40

                    Button {
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        text: "Cancel"
                        
                    }
                    Button {
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        text: "OK"
                        onClicked: internal.test()

                    }
                }
                Item {
                    Layout.fillHeight: true
                }                
            }
        }        
    }


    App {
        id: app
        visible: false
    }
    
}