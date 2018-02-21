import pygame


class InteractiveScreen:
    """Interactive screen parent for the different menu like screens"""
    def __init__(self):
        self.visuelElements = []
        self.interactiveElements = []
        self.selectedButton = 0
        self.useRacks = True

    def addInteractiveElement(self, element):
        """Add an element like a button"""
        self.interactiveElements.append(element)

    def addVisuelElement(self, element):
        """Add an element like an image"""
        self.visuelElements.append(element)

    def getInteractiveElementByIndex(self, index):
        if len(self.interactiveElements) > index:
            return self.interactiveElements[index]
        return None

    def getVisuelElementByIndex(self, index):
        if len(self.visuelElements) > index:
            return self.visuelElements[index]
        return None

    def getVisuelElementById(self, id):
        for element in self.visuelElements:
            if element.id == id:
                return element
        return None

    def getInteractiveElementById(self, id):
        for element in self.interactiveElements:
            if element.id == id:
                return element
        return None

    def updateScreen(self, deltaTime):
        """Update all the elements on the screen."""
        for elem in self.visuelElements:
            elem.update(deltaTime)
        for elem in self.interactiveElements:
            elem.update(deltaTime)

    def drawScreen(self, surface):
        """Draw all the elements on the screen"""
        for elem in self.visuelElements:
            elem.draw(surface)
        for elem in self.interactiveElements:
            elem.draw(surface)

    def handleInput(self, press):
        """Handle the inputs on the screen like up and down"""
        for keypress in press:
            if keypress.type == pygame.KEYDOWN:
                if keypress.key == pygame.K_DOWN:
                    self.getInteractiveElementByIndex(self.selectedButton).setSelected(False)
                    if self.selectedButton + 1 < len(self.interactiveElements):
                        self.selectedButton += 1
                    else:
                        self.selectedButton = 0
                    self.getInteractiveElementByIndex(self.selectedButton).setSelected(True)

                elif keypress.key == pygame.K_UP:
                    self.getInteractiveElementByIndex(self.selectedButton).setSelected(False)
                    if self.selectedButton - 1 >= 0:
                        self.selectedButton -= 1
                    else:
                        self.selectedButton = len(self.interactiveElements) - 1
                    self.getInteractiveElementByIndex(self.selectedButton).setSelected(True)

                elif keypress.key == pygame.K_SPACE or keypress.key == pygame.K_RETURN:
                    if self.getInteractiveElementByIndex(self.selectedButton).callback is not None:
                        self.getInteractiveElementByIndex(self.selectedButton).callback()
                else:
                    print("Key fail")