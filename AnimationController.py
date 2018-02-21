class AnimationStrip:
    """Store the information for seperate animation strips"""
    def __init__(self, animationSpriteSheetStrip, animationStripName, animationSpeed):
        """initialise the sheet, name and speed of the animation"""
        self.animationSprites = animationSpriteSheetStrip
        self.animationStep = 0
        self.animationSpeed = animationSpeed
        self.currentFrameTime = 0
        self.animationStripName = animationStripName
        self.nmbrOfAnimationFrames = len(self.animationSprites)

    def getCurrentAnimationFrame(self):
        """Return the current frame in the animation"""
        return self.animationSprites[self.animationStep]

    def stepForwardAnimation(self, deltaTime):
        """Move to the next frame in the animation"""
        self.currentFrameTime += deltaTime
        if self.currentFrameTime > self.animationSpeed:
            self.currentFrameTime = 0
            self.animationStep += 1
            if self.animationStep >= self.nmbrOfAnimationFrames:
                self.animationStep = 0

    def resetAnimation(self):
        """Reset the animation to the beginning of the strip"""
        self.currentFrameTime = 0
        self.animationStep = 0


class AnimationController:
    """Container for all the animation strips of a certain entity"""
    def __init__(self):
        """Define all the self values"""
        self.animationStrips = {}
        self.currentAnimation = None
        self.loadedAnimation = None

    def addAnimationStrip(self, animationStrip):
        """Add the animation strip to the list of animations"""
        self.animationStrips.update({animationStrip.animationStripName: animationStrip})

    def addAnimations(self, *args):
        """Add more then 1 animation strip"""
        for arg in args:
            self.addAnimationStrip(arg)

    def getCurrentAnimationFrame(self):
        """Get the current animation frame from the selected animation strip"""
        return self.loadedAnimation.getCurrentAnimationFrame()

    def stepCurrentAnimation(self, deltaTime):
        """Move the current animation forward 1 frame"""
        self.loadedAnimation.stepForwardAnimation(deltaTime)

    def changeCurrentAnimationTo(self, nextAnimation):
        """Change the current animation strip to the next animation"""
        if nextAnimation is not None:
            self.currentAnimation = nextAnimation
            animation = self.animationStrips.get(self.currentAnimation)
            if animation is not None:
                self.loadedAnimation = animation

    def resetCurrentAnimation(self):
        """Reset the current animation to the start of the strip"""
        self.loadedAnimation.resetAnimation()