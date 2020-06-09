from os import path
import nonebot
import config

path=path.join(path.dirname(__file__), 'awesome', 'plugins')

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(path,"awesome.plugins")
    nonebot.run()
