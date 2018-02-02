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

    def getInteractiveElement(self, id):
        if len(self.interactiveElements) > id:
            return self.interactiveElements[id]
        return None

    def getVisuelElement(self, id):
        if len(self.visuelElements) > id:
            return self.visuelElements[id]
        return None


    def drawScreen(self, surface):
        for elem in self.visuelElements:
            elem.draw(surface)
        for elem in self.interactiveElements:
            elem.draw(surface)