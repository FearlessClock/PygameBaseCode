from InteractiveScreen import InteractiveScreen
from UIBar import UIBar
from UIImage import UIImage
from UIText import UIText


class GUI(InteractiveScreen):
    def __init__(self, tileLoader):
        InteractiveScreen.__init__(self)
        self.elements = [UIImage(0, 0, 0, 560, tileLoader.getStatBar(0)),
                         UIText(0, 0, 0, 100, 591, (218, 216, 216), "100"),
                         UIText(1, 0, 0, 300, 591, (218, 216, 216), "100"),
                         UIBar(1, 80, 80, 536, 560, tileLoader.hourglass, tileLoader.logoFiller)]

    def update(self, tileLoader, sect):
        self.elements = [UIImage(0, 0, 0, 560, tileLoader.getStatBar(1 if sect.reputation < 100 else 2 if sect.reputation > 1000 else 0)),
                         UIText(0, 0, 0, 100, 591, (218, 216, 216), str(sect.money)),
                         UIText(1, 0, 0, 300, 591, (218, 216, 216), str(sect.cultists)),
                         UIBar(1, 80, 80, 536, 560, tileLoader.hourglass, tileLoader.logoFiller)]
