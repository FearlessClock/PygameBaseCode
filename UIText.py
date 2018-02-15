from UIElement import UIElement


class UIText(UIElement):
    def __init__(self, ID, width, height, x, y, color, text, fontRenderer):
        UIElement.__init__(self, ID, width, height, x, y, None)
        self.color = color
        self.id = ID
        self.fontRenderer = fontRenderer
        self.text = text

    def drawToScreen(self, screen, font_renderer=None):
        UIElement.drawToScreen(self, screen)
        # 2nd argument = Antialiasing
        screen.blit(font_renderer.render(self.text, 0, self.color), (self.x, self.y))

    def setText(self, value):
        self.text = value

    def draw(self, window):
        if self.image is not None:
            window.screen.blit(self.image, (self.x, self.y))
        window.screen.blit(self.fontRenderer.render(self.text, False, self.color),
                           (self.x, self.y))