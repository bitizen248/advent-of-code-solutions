def parse_game_line(line):
    game_id, game_data = line.split(":")
    game_id = int(game_id[4:])
    blocks_strings = game_data.split(";")
    blocks = []
    for block in blocks_strings:
        content_map = parse_blocks_line(block)
        blocks.append(content_map)

    return {
        "game_id": game_id,
        "blocks": blocks,
    }


def parse_blocks_line(line):
    content_map = {}
    content = line.split(",")
    for item in content:
        number, color = item.split()
        content_map[color] = int(number)
    return content_map
