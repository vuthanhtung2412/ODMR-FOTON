

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import QtDesignToolTest

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Button {
        id: button
        x: 1048
        y: 547
        text: qsTr("Button")
    }

    Text {
        id: text1
        x: 414
        y: 179
        width: 420
        height: 260
        text: qsTr("Text")
        font.pixelSize: 12
    }

    GridView {
        id: gridView
        x: 473
        y: 460
        width: 593
        height: 447
        cellWidth: 70
        delegate: Item {
            x: 5
            height: 50
            Column {
                spacing: 5
                Rectangle {
                    width: 40
                    height: 40
                    color: colorCode
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Text {
                    x: 5
                    text: name
                    font.bold: true
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }

            ListElement {
                name: "Red"
                colorCode: "red"
            }

            ListElement {
                name: "Blue"
                colorCode: "blue"
            }

            ListElement {
                name: "Green"
                colorCode: "green"
            }
        }
        cellHeight: 70
    }
}
