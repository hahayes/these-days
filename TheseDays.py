import json
import urllib
import os.path
import webbrowser
from datetime import datetime

import rumps
from bin.phrase import load, phrase
from bin.utils import lazypath, data_dump, make_browser

words = load()
rumps.debug_mode(True)

ICONFILE = lazypath('static', 'icon.png')
DATAFILE = lazypath('static', 'data.json')
IN_BROWSERDIR = lazypath('static')
OUT_BROWSERDIR = rumps.application_support('These Days')
BROWSERFILE = os.path.join(OUT_BROWSERDIR, 'index.html')

class TheseDaysApp(rumps.App):
    def __init__(self):
        super(TheseDaysApp, self).__init__("These Days", title=None, icon=ICONFILE)
        self.menu = ["These days...", "View history", rumps.separator, "Auto-ask?", "Preferences"]
        self.browser_url = BROWSERFILE
        self.datafile = DATAFILE
        make_browser(IN_BROWSERDIR, OUT_BROWSERDIR)

    # @rumps.clicked("Preferences")
    # def prefs(self, _):
    #     rumps.alert("None yet!")

    # @rumps.clicked("Auto-ask?")
    # def onoff(self, sender):
    #     sender.state = not sender.state

    @rumps.clicked("View history")
    def check(self, _):
        webbrowser.open('file://' + urllib.quote(self.browser_url))

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
