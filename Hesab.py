from PyQt6.Qtwidgets import QApplication , Qwidget, Qpushbutton

app = QApplication([])

window = Qwidget
window.setgeomtry(0,0,100,100)

for i in range(10):

      btn = Qpushbutton("click",parent = window)
      btn.move(i*10,100)

window.show()

app.exe()