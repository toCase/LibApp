import QtQuick
import QtQuick.Window

Window {
    width: 1200
    height: 750
    visible: true

    title: qsTr("Library App")

    
    Auth {
        anchors.fill: parent
    }
}