import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

#main dashboard accessible after logging in
class GlyphMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # UI Elements for the main window
        self.setWindowTitle('Glyph - Main Window')
        self.setGeometry(100, 100, 800, 800)  # Set window size to 800x800
        self.setStyleSheet('background-color: #012456;')  # Set background color to hex #012456

        # Labels for Contact List and Conversations
        self.contact_list_label = QLabel('Contacts', self) #current contacts list
        font_contact_list = QFont()
        font_contact_list.setPointSize(25)
        self.contact_list_label.setFont(font_contact_list)
        self.contact_list_label.setStyleSheet('color: white;')

        self.conversations_label = QLabel('Conversation', self) #current conversation window
        font_conversations = QFont()
        font_conversations.setPointSize(25)
        self.conversations_label.setFont(font_conversations)
        self.conversations_label.setStyleSheet('color: white;')  # Set text color to white

        # ListWidget for Contacts
        self.contacts_list = QListWidget(self)
        self.contacts_list.setStyleSheet('color: white; font-size: 20px;')

        # Chatbox for Conversations
        self.chatbox = QTextEdit(self)
        self.chatbox.setStyleSheet('color: white; font-size: 20px;')
        self.message_input = QLineEdit(self)
        self.message_input.setStyleSheet('color: white; font-size: 20px;')
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet('color: white; font-size: 20px; background-color: rgb(0, 100, 200);')
        self.send_button.setFixedHeight(40)

        # Layout for the main window
        self.layout = QHBoxLayout(self)

        # Left-side layout for Contacts
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.contact_list_label, alignment=Qt.AlignTop | Qt.AlignLeft)
        left_layout.addWidget(self.contacts_list)
        self.layout.addLayout(left_layout)

        # Add stretch to push the Conversation label to the top right
        self.layout.addStretch(1)
        # Right side layout for Conversations
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.conversations_label, alignment=Qt.AlignTop | Qt.AlignRight)
        right_layout.addWidget(self.chatbox)
        right_layout.addWidget(self.message_input)
        right_layout.addWidget(self.send_button)
        self.layout.addLayout(right_layout)
        self.setLayout(self.layout)

        # Populate contacts data
        self.populate_contacts()

    def populate_contacts(self):
        # Add placeholders to the Contacts list
        for contact in ["Contact 1", "Contact 2", "Contact 3", "Contact 4", "Contact 5", "Contact 6", "Contact 7"]:
            self.contacts_list.addItem(contact)

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.chatbox.append(f"You: {message}")  # Display the message in the chat box
            self.message_input.clear()  # Clear the input field

    def add_received_message(self, message):
        self.chatbox.append(f"Friend: {message}")

# Login screen window, the first thing the user will see
class GlyphLoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        # UI Elements for the login window
        self.setWindowTitle('Glyph')
        self.setGeometry(100, 100, 300, 700)
        self.setStyleSheet('background-color: #012456;')

        # Main header at top of login screen
        self.title_label = QLabel('Glyph\n NHS', self)
        font = QFont('Verlag', 48, QFont.Bold)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet('color: white;')

        # username input field with placeholder text
        self.username_input = QLineEdit(self)
        self.username_input.setFixedHeight(100)
        self.username_input.setPlaceholderText('Username')
        font_username_input = QFont()
        font_username_input.setPointSize(25)
        self.username_input.setFont(font_username_input)
        self.username_input.setStyleSheet('color: white;')

        # password input field with placeholder text
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(100)
        self.password_input.setPlaceholderText('Password')
        font_password_input = QFont()
        font_password_input.setPointSize(25)
        self.password_input.setFont(font_password_input)
        self.password_input.setStyleSheet('color: white;')

        # login button
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)
        font_login_button = QFont()
        font_login_button.setPointSize(50)
        self.login_button.setFont(font_login_button)

        # setting colour of the login button to light blue
        light_blue = QColor(0, 100, 200)
        self.login_button.setStyleSheet(f'color: white; background-color: {light_blue.name()};')

        # Additional label for copyright information
        self.copyright_label = QLabel('(C) David Benes 2024', self)
        font_copyright = QFont()
        font_copyright.setPointSize(10)  # Set a smaller text size
        self.copyright_label.setFont(font_copyright)
        self.copyright_label.setStyleSheet('color: white;')  # Set text color to white

        # Additional label for displaying login failure message
        self.error_label = QLabel('', self)
        self.error_label.setFont(font_copyright)
        self.error_label.setStyleSheet('color: red;')  # Set text color to red

        # Reference to the main window
        self.main_window = GlyphMainWindow()

        # Organised layout for the login window
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.error_label)

        # Adjusted spacing to move fields up
        self.layout.setSpacing(10)

        # Added gap at the bottom for copyright text
        self.layout.addStretch()
        self.layout.addWidget(self.copyright_label, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def login(self):
        # authentication programming will be added here
        username = self.username_input.text()
        password = self.password_input.text()

        # Placeholder authentication check
        if username == 'admin' and password == 'admin':
            print('Login successful')
            self.main_window.show()  # Show the main window
            self.hide()  # Hide the login window

        else:
            print('Login failed')
            self.error_label.setText('Login Failed')  # Set error message
            self.error_label.show()  # Show the error label

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen = GlyphLoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
