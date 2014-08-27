import urllib
import os.path
import subprocess
import webbrowser
from datetime import datetime

import rumps
from bin.phrase import load, phrase
from bin.utils import lazypath, data_dump, init_browser

words = load()
rumps.debug_mode(True)

ICONFILE = lazypath('static', 'icon.png')
HTMLDIR = lazypath('static')
SETTINGS_DIR = rumps.application_support('These Days')
DATAFILE = os.path.join(SETTINGS_DIR, 'data.json')
BROWSERFILE = os.path.join(SETTINGS_DIR, 'index.html')

class TheseDaysApp(rumps.App):
    def __init__(self):
        super(TheseDaysApp, self).__init__("These Days", title=None, icon=ICONFILE)
        self.menu = ["These days...", "View history", rumps.separator, "Auto-ask?", "Preferences"]
        self.browser_url = BROWSERFILE
        self.settings_dir = SETTINGS_DIR
        self.datafile = DATAFILE
        init_browser(HTMLDIR, SETTINGS_DIR)
        self.PORT = 1988

    # @rumps.clicked("Preferences")
    # def prefs(self, _):
    #     rumps.alert("None yet!")

    # @rumps.clicked("Auto-ask?")
    # def onoff(self, sender):
    #     sender.state = not sender.state

    @rumps.clicked("View history")
    def check(self, _):
        # webbrowser.open('file://' + urllib.quote(self.browser_url))
        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', str(self.PORT)], cwd=self.settings_dir, stdin=None, stdout=None, stderr=None, close_fds=True)
        webbrowser.open_new_tab('http://0.0.0.0:{0}'.format(self.PORT))

    @rumps.clicked("These days...")
    def sayhi(self, _):
        self.window = rumps.Window(dimensions=(300, 100))
        self.window.message = "Whatcha been doing lately?"
        self.window.default_text = phrase(words)
        self.window.icon = self.icon
        self.response = self.window.run()
        data_dump({'dt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'msg': self.response.text}, self.datafile)

if __name__ == "__main__":
    TheseDaysApp().run()
