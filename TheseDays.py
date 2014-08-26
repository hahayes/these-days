import rumps

rumps.debug_mode(True)

class TheseDaysApp(rumps.App):
    def __init__(self):
        super(TheseDaysApp, self).__init__("These Days")
        self.menu = ['Preferences', 'Option', 'Say hi']
        self.icon = 'icon.png'
        self.title = None

    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Option")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Title", "Subtitle", "helloooooooo")

if __name__ == "__main__":
    TheseDaysApp().run()
