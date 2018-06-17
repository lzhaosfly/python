import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.setWindowTitle('PyQt5')
window.resize(500, 500)

window.show()
sys.exit(app.exec_())
