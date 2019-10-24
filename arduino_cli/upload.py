from subprocess import run


def run_and_get_stdout(cmd):
    return run(cmd, capture_output=True).stdout.decode("utf-8")


def upload(*, FQBN, PORT, source_path, verbose=False, verify=False):
    """
    Upload Arduino sketches.
    Arduinoにコンパイルしたスケッチを書き込む
    Parameters
    ----------
    PORT : str
        ポート(COM5など)
    FQBN : str
        ボードの種類
    source_path : int
        書き込みたいスケッチのパス
    verbose : bool
        書き込みの詳細確認モード
    verify : bool
        書き込み後にバイナリを確認
    """
    upload_options = [
        "--verbose" if verbose else False,
        "--verify" if verify else False
    ]
    upload_options = [option for option in upload_options if option]
    cmd = "arduino-cli upload -b {0} -p {1} -i {2} {3}".format(
        FQBN, PORT, source_path, " ".join(upload_options)
        )
    return run_and_get_stdout(cmd)
