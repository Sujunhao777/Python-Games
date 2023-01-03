
import cfg
from modules import breakoutClone


'''主函数'''
def main():
    game = breakoutClone(cfg)
    game.run()


'''run'''
if __name__ == '__main__':
    main()