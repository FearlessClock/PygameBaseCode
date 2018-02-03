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