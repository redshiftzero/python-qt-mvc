import sys
import time

from PyQt5.QtWidgets import QApplication, QListView
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QModelIndex, QAbstractListModel, Qt


def start_app():
    app = QApplication(sys.argv)

    msgs = ["msg1",
            "msg2",
            "msg3"]

    conversation_model = ConversationModel(msgs)
    view = ConversationView()
    view.setModel(conversation_model)

    # Example of adding a message directly 
    # important: this will update the UI automatically
    conversation_model.addData('msg4')

    view.show()

    sys.exit(app.exec_())


class ConversationView(QListView):
    def __init__(self):
        super(QListView, self).__init__()
        self.setWindowTitle = 'My source conversation'


class ConversationModel(QAbstractListModel):
    def __init__(self, msgs=[]):
        super(QAbstractListModel, self).__init__()
        self.msg_list = msgs

    def data(self, index, role=None):
        row = index.row()
        value = self.msg_list[row]

        if role == Qt.DisplayRole:
            return value

    def rowCount(self, parent=None):
        return len(self.msg_list)

    def flags(self, QModelIndex):
        # These items are editable so that we can edit each row
        return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    @pyqtSlot()
    def setData(self, QModelIndex, value, role=None):
        """
        To be used to modify an existing element in the list (e.g. the reply window)
        We can also leave this unimplemented.
        """
        if role == Qt.EditRole:
            row = QModelIndex.row()
            print('I am changing the value of row {} to be {} in my data store'.format(row, value))
            self.msg_list[row] = value
            # Emit dataChanged and now just that row should be repainted
            # This is what we should do to resolve
            # https://github.com/freedomofpress/securedrop-client/issues/185
            self.dataChanged.emit(QModelIndex, QModelIndex, [])
            return True
        return False

    @pyqtSlot()
    def addData(self, value):
        """
        To be used when there's a new message in the conversation
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.msg_list.append(value)
        self.endInsertRows()
        print('I am adding the value: {} to my data store'.format(value))
        return True


if __name__ == '__main__':
    start_app()
