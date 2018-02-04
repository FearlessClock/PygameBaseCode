from InteractiveScreen import InteractiveScreen
from UIBar import UIBar
from UIImage import UIImage
from UIText import UIText


class GUI(InteractiveScreen):
    def __init__(self, tileLoader):
        InteractiveScreen.__init__(self)
        self.addVisuelElement(UIImage(0, 200, 50, 10,10, tileLoader.getImageByName("healthBars", 0, 0)))


