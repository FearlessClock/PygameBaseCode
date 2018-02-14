class AnimationStrip:
    def __init__(self, animationSpriteSheetStrip, animationStripName, animationSpeed):
        self.animationSprites = animationSpriteSheetStrip
        self.animationStep = 0
        self.animationSpeed = animationSpeed
        self.currentFrameTime = 0
        self.animationStripName = animationStripName
        self.nmbrOfAnimationFrames = len(self.animationSprites)

    def getCurrentAnimationFrame(self):
        return self.animationSprites[self.animationStep]

    def stepForwardAnimation(self, deltaTime):
        self.currentFrameTime += deltaTime
        if self.currentFrameTime > self.animationSpeed:
            self.currentFrameTime = 0
            self.animationStep += 1
            if self.animationStep >= self.nmbrOfAnimationFrames:
                self.animationStep = 0

    def resetAnimation(self):
        self.currentFrameTime = 0
        self.animationStep = 0


class AnimationController:
    def __init__(self):
        self.animationStrips = {}
        self.currentAnimation = None
        self.loadedAnimation = None

    def addAnimationStrip(self, animationStrip):
        self.animationStrips.update({animationStrip.animationStripName: animationStrip})

    def addAnimations(self, *args):
        for arg in args:
            self.addAnimationStrip(arg)

    def getCurrentAnimationFrame(self):
        return self.loadedAnimation.getCurrentAnimationFrame()

    def stepCurrentAnimation(self, deltaTime):
        self.animationStrips.get(self.currentAnimation).stepForwardAnimation(deltaTime)

    def changeCurrentAnimationTo(self, nextAnimation):
        # if self.currentAnimation is not None:
        #     self.animationStrips.get(self.currentAnimation).resetAnimation()
        if nextAnimation is not None:
            self.currentAnimation = nextAnimation
            animation = self.animationStrips.get(self.currentAnimation)
            if animation is not None:
                self.loadedAnimation = animation
