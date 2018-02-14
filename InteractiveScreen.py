import pygame


class InteractiveScreen:
    def __init__(self):
        self.visuelElements = []
        self.interactiveElements = []
        self.selectedButton = 0
        self.useRacks = True

    def addInteractiveElement(self, element):
        self.interactiveElements.append(element)

    def addVisuelElement(self, element):
        self.visuelElements.append(element)

    def getInteractiveElementByIndex(self, id):
        if len(self.interactiveElements) > id:
            return self.interactiveElements[id]
        return None

    def getVisuelElementByIndex(self, id):
        if len(self.visuelElements) > id:
            return self.visuelElements[id]
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
        for elem in self.visuelElements:
            elem.update(deltaTime)
        for elem in self.interactiveElements:
            elem.update(deltaTime)

    def drawScreen(self, surface):
        for elem in self.visuelElements:
            elem.draw(surface)
        for elem in self.interactiveElements:
            elem.draw(surface)

    def handleInput(self, press):
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