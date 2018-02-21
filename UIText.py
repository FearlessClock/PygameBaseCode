from UIElement import UIElement


class UIText(UIElement):
    """UIElement, Show text on the screen, no background"""

    def __init__(self, ID, width, height, x, y, color, text, fontRenderer):
        UIElement.__init__(self, ID, width, height, x, y)
        self.color = color
        self.id = ID
        self.fontRenderer = fontRenderer
        self.text = text

    def setText(self, value):
        """Change the text on the screen."""
        self.text = value

    def draw(self, window):
        """Draw the text to the screen. """
        if self.image is not None:
            window.screen.blit(self.image, (self.x, self.y))
        window.screen.blit(self.fontRenderer.render(self.text, False, self.color),
                           (self.x, self.y))
