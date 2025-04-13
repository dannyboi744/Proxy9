from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEnginePage
import sys


class ProxyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proxy Browser")
        self.setGeometry(100, 100, 1024, 768)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.google.com")  # Default URL
        self.browser.page().setLinkDelegationPolicy(QWebEnginePage.DelegateAllLinks)
        self.browser.linkClicked.connect(self.handle_link_click)

        # Add the browser to the layout
        self.layout.addWidget(self.browser)

    def handle_link_click(self, url):
        # Ensure links open within the same browser
        self.browser.setUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    proxy_browser = ProxyBrowser()
    proxy_browser.show()
    sys.exit(app.exec_())