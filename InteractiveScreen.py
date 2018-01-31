class InteractiveScreen:
    def __init__(self):
        self.elements = []
        self.interactiveElements = [[]]
        self.selectedButton = 0
        self.useRacks = True

    def drawScreen(self, window, font_renderer=None):
        for i in range(len(self.elements)):
            self.elements[i].drawToScreen(window.screen, font_renderer)
        for i in range(len(self.interactiveElements)):
            if self.useRacks:
                for j in range(len(self.interactiveElements[i])):
                    self.interactiveElements[i][j].drawToScreen(window.screen, font_renderer)
            else:
                self.interactiveElements[i].drawToScreen(window.screen, font_renderer)
