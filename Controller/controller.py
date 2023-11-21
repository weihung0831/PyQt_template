class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def buttonClicked(self):
        text = self.view.getText()
        self.view.setText(text)
