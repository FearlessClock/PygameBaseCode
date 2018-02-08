import GameLoop
from Vector import Vector


def main():
    gameloop = GameLoop.Gameloop("GameName", Vector(500, 500), Vector(60, 60))
    gameloop.startLoop()


if __name__ == '__main__': main()
