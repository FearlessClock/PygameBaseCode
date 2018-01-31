from UIElement import UIElement


class UIText(UIElement):
    def __init__(self, ID, width, height, x, y, color, text):
        UIElement.__init__(self, width, height, x, y, None)
        self.color = color
        self.id = ID
        self.text = text

    def drawToScreen(self, screen, font_renderer=None):
        UIElement.drawToScreen(self, screen)
        # 2nd argument = Antialiasing
        screen.blit(font_renderer.render(self.text, 0, self.color), (self.x, self.y))