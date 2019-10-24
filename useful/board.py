from arduino_cli import board


def get_boards_dic():
    board_info_list = []
    boards = board.list().split("\n")[1:-1]
    for line in boards:
        data = line.split()
        board_info = {"PORT": data[0],
                      "Type": " ".join(data[1:4]),
                      "Board Name": " ".join(data[4:6]),
                      "FQBN": data[6]}
        board_info_list.append(board_info)
    return board_info_list
