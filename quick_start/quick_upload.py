from os import remove
from useful.board import get_boards_dic
import arduino_cli


def quick_upload(ino_path):
    boards = get_boards_dic()
    if len(boards) == 1:
        FQBN = boards[0]["FQBN"]
        PORT = boards[0]["PORT"]
        compile_message = arduino_cli.compile(
            ino_path=ino_path, FQBN=FQBN, output="a")
        print("[compile]")
        print(compile_message)

        upload_message = arduino_cli.upload(
            FQBN=FQBN, PORT=PORT, source_path="a", verify=True)
        print("[upload]")
        print(upload_message)
        remove("a.hex")
        remove("a.elf")
        print("[:done:]")
