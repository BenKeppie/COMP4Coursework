import smtplib

from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *

from email.mime.text import MIMEText

class DisplaySupportWidget(QWidget):
    """A class to display the model and represent a view on the support tab"""

    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.VBoxLayout=QVBoxLayout()
        self.form_layout=QGridLayout()
        self.form_widget=QWidget()

        self.display_support_layout()

        self.setLayout(self.VBoxLayout)

        self.submit_button.pressed.connect(self.send_email)

    def send_email(self):
        msg=MIMEText(self.form_email_line_edit.text()+ self.form_message_line_edit.toPlainText())
        print(msg)
        msg["Subject"]="Skateboard Progress Tracker Support"
        msg["From"]="SkateboardProgressTracker@gmail.com"
        msg["To"]= "BenKeppie@hotmail.co.uk"

        Send=smtplib.SMTP("smtp.gmail.com")
        Send.sendmail(msg["From"],msg["To"],msg)
        Send.quit

    def display_support_layout(self):
        if not hasattr(self, "developer"):
            self.developer=QLabel("Application Developed By: Ben Keppie")
            self.VBoxLayout.addWidget(self.developer)

        if not hasattr(self, "form_name"):
            self.form_name=QLabel("Name: ")
            self.form_layout.addWidget(self.form_name,0,0)
        if not hasattr(self,"form_name_line_edit"):
            self.form_name_line_edit=QLineEdit()
            self.form_layout.addWidget(self.form_name_line_edit,0,1)

        if not hasattr(self,"form_email"):
            self.form_email=QLabel("Email Address: ")
            self.form_layout.addWidget(self.form_email,1,0)
        if not hasattr(self,"form_email_line_edit"):
            self.form_email_line_edit=QLineEdit()
            self.form_layout.addWidget(self.form_email_line_edit,1,1)

        if not hasattr(self,"form_message"):
            self.form_message=QLabel("Message: ")
            self.form_layout.addWidget(self.form_message,2,0)
        if not hasattr(self,"form_message_line_edit"):
            self.form_message_line_edit=QTextEdit()
            #print(self.form_message_line_edit.toPlainText())
            self.form_layout.addWidget(self.form_message_line_edit,2,1)

        self.form_widget.setLayout(self.form_layout)
        self.VBoxLayout.addWidget(self.form_widget)

        if not hasattr(self,"submit_button"):
            self.submit_button=QPushButton("Submit")
            self.VBoxLayout.addWidget(self.submit_button)

            
        
            
            
            


        
