from subprocess import run
import os
from json import loads


def run_and_get_stdout(cmd):
    return run(cmd, capture_output=True).stdout.decode("utf-8")


def compile(*, ino_path, FQBN=None, build_cache_path="", build_path="",
            build_properties="", output="", preprocess=False, quiet=False,
            show_properties=False, verbose=False, vid_pid="", warnings="none"):
    """
    Compiles Arduino sketches.
    スケッチをコンパイルする。
    Parameters
    ----------
    ino_path : str
        コンパイルしたいスケッチのパス。ファイル名またはフォルダ名(フォルダ名の場合同名.inoのファイル)
    FQBN : str
        ボードの種類。指定しない場合はsketch.jsonを読む。
    build_cache_path : str
        ビルドのキャッシュを保存するパス
    build_path : str
        コンパイルしたファイルを格納するフォルダ
    build_properties : str
        カスタムビルドプロパティのリスト
    output : str
        コンパイルしたファイルの名前。`hoge`にすると`hoge.拡張子`が生成される。
    preprocess : bool
        コンパイルせずに、前処理がされたソースコードを出力
    quiet : bool
        ほぼすべての出力を抑制します。
    show_properties : bool
        コンパイルせずにビルドのプロパティを出力
    verbose : bool
        コンパイルメッセージ冗長モード
    vid_pid : str
        指定したVID/PIDに固有のビルドプロパティを使用
    warnings : str
        gccに警告レベルを伝える。`none`,`default`,`more`,`all`
    """
    if not (FQBN or os.path.exists("sketch.json")):
        raise TypeError("please set `FQBN` or use `board.attach()`!")

    fqbn_cmd = "--fqbn {0} ".format(FQBN if FQBN
                                    else loads(open("sketch.json").read())
                                    ["cpu"]["fqbn"])

###############################################################################

    compile_options = [
        "--build-cache-path {0}".format(build_cache_path) if build_cache_path
        else "",
        "--build-path {0}".format(build_path) if build_path else "",
        "--build-properties {0}".format(build_properties) if build_properties
        else "",
        "--output {0}".format(output) if output else "",
        "--preprocess" if preprocess else "",
        "--quiet".format(quiet) if quiet else "",
        "--show-properties" if show_properties
        else "",
        "--verbose" if verbose else "",
        "--vid-pid" if vid_pid else "",
        "--warnings '{0}'".format(warnings)
    ]
    compile_options = " ".join(
        [option for option in compile_options if option != ""])

    cmd = "arduino-cli compile {0}{1} {2}".format(
        fqbn_cmd, ino_path, compile_options
    )
    return run_and_get_stdout(cmd)
