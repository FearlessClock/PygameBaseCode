from InteractiveScreen import InteractiveScreen
from UIBar import UIBar
from UIImage import UIImage
from UIText import UIText


class GUI(InteractiveScreen):
    def __init__(self, tileLoader, fontRenderer):
        InteractiveScreen.__init__(self)
        self.addVisuelElement(UIImage(0, 200, 50, 10,5, tileLoader.getImageByName("healthBars", 0, 0)))
        self.score = 0
        self.addVisuelElement(UIText(1, 100, 30, 230, 5, (00,255,0), "Score: 0", fontRenderer))

    def setScore(self, score):
        self.score = score
        self.getVisuelElementById(1).setText("Score: " + self.score)
