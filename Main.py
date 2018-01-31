import GameLoop
from Vector import Vector


def main():
    gameloop = GameLoop.Gameloop("GameName", Vector(500, 500), Vector(80, 80))
    gameloop.startLoop()


if __name__ == '__main__': main()
