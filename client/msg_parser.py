import re


def parse_cmd(cmd):
    type, params = cmd.split(' ', 1)

    if type == 'board':
        figure_positions = re.findall(r'\([a-zA-Z]*\d* \d* \d*\)', params)

        new_positions = dict()

        for figure_position in figure_positions:
            info = figure_position.strip('(),').split()
            name = info[0]
            x = int(info[1])
            y = int(info[2])

            new_positions[name] = (x, y)

        return type, new_positions

    elif type == 'board_size':
        info = params.strip('()').replace(',', '').split()
        width = int(info[0])
        height = int(info[1])
        return type, (width, height)

    else:
        return type, params