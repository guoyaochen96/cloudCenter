import sys
import time
import os
from PyQt6.QtCore import QThread, QSize, Qt, pyqtSignal
from PyQt6.QtWidgets import QApplication, QListWidget, QAbstractItemView, QListWidgetItem, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QCursor


# --------Thread class---------------#
class WorkerThread(QThread):
    status = pyqtSignal(str)

    def run(self):
        time.sleep(2)
        self.status.emit('...')
        print('...')


class todo(QWidget):
    def __init__(self):
        super().__init__()

        # adding logo of the window
        self.setWindowIcon(QIcon('icons/icon.png'))

        # setting the title of the window
        self.setWindowTitle('ToDo List')

        # fixed size window
        self.setFixedSize(350, 480)

        # defining layouts
        horizontalLayout = QHBoxLayout()
        horizontalLayoutforbutton = QHBoxLayout()
        verticalLayout = QVBoxLayout()

        # label widget
        label = QLabel('To Do''\'s')
        label.setObjectName('header')
        status = QLabel('Status:')
        status.setObjectName('status')
        self.toast = QLabel('...')
        # self.toast.setAlignment(Qt.Alignment.AlignCenter)
        self.toast.setObjectName('toast')

        # listwidget
        self.list = QListWidget()
        # self.list.setAlternatingRowColors(True)
        self.list.setAutoScroll(True)
        self.list.setWordWrap(True)
        # setting selection mode property
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.itemClicked.connect(self.item)

        # Textbox widget
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText('Take a note!')
        self.textbox.setFocus()
        self.textbox.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        # Add button widget
        btn_addTask = QPushButton('Add Task')
        btn_addTask.clicked.connect(self.addTask)
        # self.btn_addTask.setIcon(QIcon('icons/plus.png'))
        btn_addTask.setObjectName('addButton')
        btn_addTask.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Delete button widget
        btn_deleteTask = QPushButton()
        btn_deleteTask.clicked.connect(self.deleteT)
        btn_deleteTask.setIcon(QIcon('icons/trash-regular.png'))
        btn_deleteTask.setIconSize(QSize(20, 20))
        btn_deleteTask.setToolTip('Delete selected task')
        btn_deleteTask.setObjectName('deleteButton')
        btn_deleteTask.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Save button widget
        btn_saveTask = QPushButton()
        btn_saveTask.clicked.connect(self.saveT)
        btn_saveTask.setIcon(QIcon('icons/save-regular.png'))
        btn_saveTask.setIconSize(QSize(20, 20))
        btn_saveTask.setToolTip('Save Your List')
        btn_saveTask.setObjectName('saveButton')
        btn_saveTask.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Load button widget
        btn_loadTask = QPushButton()
        btn_loadTask.clicked.connect(self.loadTask)
        btn_loadTask.setIcon(QIcon('icons/spreadsheet-regular.png'))
        btn_loadTask.setIconSize(QSize(20, 20))
        btn_loadTask.setToolTip('Load previously saved List')
        btn_loadTask.setObjectName('loadButton')
        btn_loadTask.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # ClearAll button widget
        btn_clearAll = QPushButton('Clear All')
        btn_clearAll.clicked.connect(self.clearAllTask)
        btn_clearAll.setObjectName('clearAllButton')
        btn_clearAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # setting Layouts
        verticalLayout.addWidget(label)
        horizontalLayout.addWidget(status)
        horizontalLayout.addWidget(self.toast, 1)
        horizontalLayout.addWidget(btn_loadTask)
        horizontalLayout.addWidget(btn_saveTask)
        horizontalLayout.addWidget(btn_deleteTask)
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addWidget(self.list)
        verticalLayout.addWidget(self.textbox)
        horizontalLayoutforbutton.addWidget(btn_clearAll)
        horizontalLayoutforbutton.addWidget(btn_addTask)
        verticalLayout.addLayout(horizontalLayoutforbutton)
        self.setLayout(verticalLayout)

    # Set Toast when item is selected from the list
    def item(self):
        if self.list.selectedItems():
            self.toast.setText('Item Selected')
        else:
            self.toast.setText('...')

    # Event handling method when any key is pressed
    def keyPressEvent(self, event):
        # print(event.key())
        self.textbox.setFocus()

        # when user press enter, it automatically add func() to add task in the list
        if event.key() == 16777220 or event.key() == 16777221:
            self.addTask()

    # clear listwidget and linedit
    def clearAllTask(self):
        self.list.clear()
        self.textbox.clear()
        self.toast.setText('Reset')
        self.ThreadClass()

    # Adding listItem into the listwidget
    def addTask(self):
        task = self.textbox.text()
        # print(len(task))
        if task != "":
            self.list.addItem(task)
            self.textbox.clear()
            self.toast.setText('Item Added')
            self.ThreadClass()
        else:
            self.toast.setText('Add Item first')
            self.toast.setStyleSheet('''color:   #d9534f; ''')
            self.ThreadClass()

    # Delete the selected listItem
    def deleteT(self):
        if (self.list.selectedItems()):
            for i in self.list.selectedItems():
                task_index = self.list.row(i)
                print(self.list.item(task_index).text())
                self.list.takeItem(task_index)
                self.toast.setText('Item deleted.')
            self.ThreadClass()
        else:
            self.toast.setText('Select! item')
            self.toast.setStyleSheet('''color:  #d9534f;''')
            self.ThreadClass()

    # Save the selected listItem
    def saveT(self):
        if (self.list.selectedItems()):
            with open('load.txt', 'a+') as file:

                # getting the current time
                current_time = time.asctime(time.localtime(time.time()))
                print(self.list.count())
                for i in reversed(self.list.selectedItems()):
                    timestamp = '\n------------ {}'.format(current_time)
                    task_index = self.list.row(i)
                    strr = self.list.item(task_index).text()

                    # concatinate time after the list item
                    strr = strr[0:] + timestamp

                    # replacing '\n' (new line) with symbol '$$' in the list item
                    strr = strr.replace('\n', '$$')
                    file.write(strr + '\n')

            self.toast.setText('Task saved')
            self.ThreadClass()

        else:
            self.toast.setText('Select! item')
            self.toast.setStyleSheet('''color:  #d9534f;''')
            self.ThreadClass()

    # Load the Saved task from the file named: load.txt
    def loadTask(self):
        try:
            # check the file size or file not exist throws an exception
            if os.stat('load.txt').st_size != 0:
                self.list.clear()

                # reading the item one by one
                with open('load.txt', 'r') as file:
                    for i in file.readlines():
                        # replacing '$$' with '\n' in the list item
                        i = i.replace('$$', '\n')

                        self.list.addItem(i)

                self.toast.setText('Task Loaded')
                self.ThreadClass()
            else:
                self.toast.setText('Task List empty!')
                self.toast.setStyleSheet('''color: #d9534f;''')
                self.ThreadClass()

        except:
            file = open('load.txt', 'a+')
            print('file created !')
            self.loadTask()

    # Default Toast Message
    def toast_msg(self, msg):
        self.toast.setText(msg)
        self.toast.setStyleSheet('''color: #1a73e8;''')

    # Thread function calling
    def ThreadClass(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.status.connect(self.toast_msg)


# ------------------Main---------------------#
app = QApplication(sys.argv)
app.setStyleSheet('''
    *{
        background-color:        #ffffff;
        font-family:            Century Gothic;
    }

    #header{
       font-size:               30px; 
       /*font-family:             Mistral;*/
       color:                   #787c80;
       margin:                  0px  5px;
    }
    #toast, #status{
        font-size:              12px;
        color:                  #1a73e8;
        font-weight:            bold;
        margin-left:            5px;
    }
    QToolTip { 
        color:                  #ffffff;
        background-color:       #1a73e8;
        padding:                10px; 
        outline:                0;
        border:                 0;
        /*opacity:              200;*/ 
    }

    QListWidget{
        background-color:       rgba(241, 243, 244, 1);
        border:                 1px solid rgba(241, 243, 244,1);
        border-radius:          8px;
        padding:                0.8em 0.5em 0.8em 0.5em ;
        outline:                0;
        font-size:              15px;
        margin:                 2px 5px 8px 5px;
    }
    QListWidget::item {
        background-color:       #ffffff;
        /*background:           qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #cccccc, stop:1 #fcfcfc);*/
        border-radius:          8px;
        margin-top:             0.4em;
        padding:                0.5em;       
    }
    QListWidget::item:selected {
        background-color:       #d2e3fc;
        border :                none;
        color:                  #0275d8;
    }

    #deleteButton{
        border-radius:          5px;
        max-width:              2em;
        padding:                0.2em;
        margin-left:            0;
        margin-right:           5px;
    }
    #deleteButton::hover, #loadButton::hover, #saveButton::hover{
        background-color:       #f0f0f0;
    }
    #deleteButton::pressed, #loadButton::pressed,  #saveButton::pressed{
        background-color:       #e0f0fd;
    }
    #loadButton{
        border-radius:          5px;
        max-width:              2em;
        padding:                0.2em;
    }
    #saveButton{
        border-radius:          5px;
        /*background-color:     #0275d8;*/
        max-width:              2em;
        margin-left:            0;
        padding:                0.2em;
    }
    #addButton, #clearAllButton{
        padding:                1em;
        background-color:       #1a73e8;
        margin-bottom:          5px;
        margin-top:             3px;  
    }
    #clearAllButton{
        margin-left:            5px;
    }
    #addButton{
        margin-right:           5px;
    }
    QPushButton{
        font-size:              15px;
        border-radius:          8px;
        color:                  #ffffff;
        font-weight:            bold;
    }  
    QPushButton::hover, #addButton::hover, #clearAllButton::hover{
        background-color:       #1967d2;
    }
    QPushButton::pressed, #addButton::pressed, #clearAllButton::pressed{
        background-color:       #185abc;
    }
    QLineEdit{
        background-color:       rgba(241, 243, 244, 1);
        border:                 1px solid rgba(241, 243, 244,1);
        border-radius:          8px;
        min-height:             2em;
        padding:                0.5em;
        font-size:              16px;
        margin:                 5px 5px 0px 5px;
    }

    QScrollBar{
        border:                 none;
        background-color:       rgba(241, 243, 244, 1);  
    }
    QScrollBar:vertical {              
        width:                  18px;
    }
    QScrollBar:horizontal {              
        height:                 10px;     
    }
    QScrollBar::handle:vertical{
        background :            #CFD1D0;
        border-radius:          5px;   
        margin-left:            0.5em; 
    }
    QScrollBar::handle:horizontal{
        background :            #CFD1D0;
        border-radius:          5px;    
    }
    QScrollBar::add-line:horizontal {
        border:                 none;
        background:             none;
        width:                  20px;
        subcontrol-position:    right;
        subcontrol-origin:      margin;
    }
    QScrollBar::add-line:vertical {
        border:                 none;
        background:             none;
        height:                 20px;
        margin-left:            5px;
        subcontrol-position:    top;
        subcontrol-origin:      margin;
    }
    QScrollBar::sub-line:horizontal {
        border:                 none;
        background:             none;
        width:                  20px;
        subcontrol-position:    left;
        subcontrol-origin:      margin;
    }
    QScrollBar::sub-line:vertical {
        border:                 none;
        background:             none;
        height:                 20px;
        subcontrol-position:    bottom;
        subcontrol-origin:      margin;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background:             none;
    } 
    ''')
window = todo()
window.show()
sys.exit(app.exec())