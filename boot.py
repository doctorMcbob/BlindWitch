from src import game

if __name__ == "__main__":
        G = game.set_up()
        game.run(G)

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
    os.chdir(os.path.dirname(sys.executable))
