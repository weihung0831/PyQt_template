class Model:
    def __init__(self):
        self.text = ""

    def getText(self):
        self.text = "Hello World!"
        return self.text

    def setText(self, text):
        self.text = text
