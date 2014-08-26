import rumps
from phrase import load, phrase
words = load()

rumps.debug_mode(True)
class TheseDaysApp(rumps.App):
    def __init__(self):
        super(TheseDaysApp, self).__init__("These Days", title=None, icon='icon.png')
        self.menu = ["These days...", rumps.separator, "Auto-ask?", "Preferences"]

    # @rumps.clicked("Preferences")
    # def prefs(self, _):
    #     rumps.alert("None yet!")

    # @rumps.clicked("Auto-ask?")
    # def onoff(self, sender):
    #     sender.state = not sender.state

    @rumps.clicked("These days...")
    def sayhi(self, _):
        self.window = rumps.Window(dimensions=(300, 100))
        self.window.message = "Whatcha been doing lately?"
        self.window.default_text = phrase(words)
        self.window.icon = self.icon
        self.response = self.window.run()
        # rumps.alert("These days you've been...", self.response.text)

if __name__ == "__main__":
    TheseDaysApp().run()
