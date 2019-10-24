from subprocess import run


def run_and_get_stdout(cmd):
    return run(cmd, capture_output=True).stdout.decode("utf-8")


def attach(*, PORT=None, FQBN=None, sketchPath, timeout="5s"):
    """
    Attaches a sketch to a board.
    ボードとスケッチを紐づける
    Parameters
    ----------
    PORT|FQBN : str
        PORTもしくはFQBN
    sketchPath : str
        スケッチの存在するパス
    timeout : str
        デバイスが見つからなかった場合にattachを中断する時間
    """
    if PORT or FQBN:
        cmd = "arduino-cli board attach {0} {1} --timeout {2}".format(
            PORT or FQBN, sketchPath, timeout)
        return run_and_get_stdout(cmd)
    else:
        raise TypeError


def details(FQBN=None):
    """
    Show information about a board,
    in particular if the board has options to be specified in the FQBN.
    FQBNで指定したボードの情報を出力する。
    Parameters
    ----------
    FQBN : str
        知りたいボードのFQBN
    """

    cmd = "arduino-cli board details {0}".format(FQBN)
    return run_and_get_stdout(cmd)


def list(*, timeout="0s"):
    """
    Detects and displays a list of connected boards to the current computer.
    コンピュータに接続されているボードの一覧を表示する。
    Parameters
    ----------
    timeout : str
        デバイスが見つからなかった場合にlistを中断する時間
    """

    cmd = "arduino-cli board list --timeout {0}".format(timeout)
    return run_and_get_stdout(cmd)


def listall(boardname=None):
    """
    List all boards that have the support platform installed. You can search
    for a specific board if you specify the board name.
    インストール済みのplatformをすべて表示する。
    Parameters
    ----------
    boardname : boardname
        ボードの名前
    """
    cmd = "arduino-cli board listall {0}".format(
        boardname if boardname else "")
    print(cmd)
    return run_and_get_stdout(cmd)
