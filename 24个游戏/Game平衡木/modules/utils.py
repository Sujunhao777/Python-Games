


'''导入关卡文件'''
def loadLevel(levelpath):
    brick_positions = []
    fp = open(levelpath, 'r', encoding='utf-8')
    y = -1
    for line in fp.readlines():
        if (not line.strip()) or (line.startswith('#')):
            continue
        else:
            y += 1
            x = -1
            for c in line:
                x += 1
                if c == 'B':
                    brick_positions.append([x, y])
    return brick_positions