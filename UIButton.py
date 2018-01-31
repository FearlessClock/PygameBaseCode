import pygame

from UIElement import UIElement


class UIButton(UIElement):
    def __init__(self, width, height, x, y, notSelectedimage, selectedImage, callback, text):
        UIElement.__init__(self, width, height, x, y, notSelectedimage)
        self.isSelected = False
        self.imageSelected = selectedImage
        self.imageNotSelected = notSelectedimage
        self.callback = callback
        self.text = text

    def update(self):
        print("Update")