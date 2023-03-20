import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QShortcut, QPushButton, QHBoxLayout

from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebBrowser(QWidget):
    def __init__(self, url):
        super().__init__()

        self.setWindowTitle("chatGPT App")
        self.setMinimumSize(1000, 600)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        # Add refresh button
        refresh_button = QPushButton("R")
        refresh_button.setIcon(QIcon.fromTheme("view-refresh"))
        refresh_button.text()
        refresh_button.setFixedSize(25, 25)
        refresh_button.clicked.connect(self.refresh_page)

        # Create top right layout
        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch()
        top_right_layout.addWidget(refresh_button)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_right_layout)
        main_layout.addWidget(self.browser)

        self.setLayout(main_layout)

        # Add shortcuts
        enter_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        enter_shortcut.activated.connect(self.submit_form)
        shift_enter_shortcut = QShortcut(QKeySequence(Qt.SHIFT + Qt.Key_Return), self)
        shift_enter_shortcut.activated.connect(self.new_line)

    def submit_form(self):
        # Submit the form
        self.browser.page().runJavaScript("document.activeElement.form.submit();")

    def new_line(self):
        # Insert a new line character
        self.browser.page().runJavaScript("document.activeElement.value += '\n';")

    def refresh_page(self):
        # Reload the current page
        self.browser.reload()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser("https://chat.openai.com/chat/")
    browser.show()
    sys.exit(app.exec_())
