import argparse
from datetime import datetime as dt
from PIL import Image, ImageDraw
from typing import Any


def draw_text(text:str="2022年07月01 19:00 ～ 21:00") -> Any:
    """画像に日時を描画する

    Args:
        text (str): 描画日時. Defaults to "2022年07月01 19:00 ～ 21:00".
        
    Returns:
        Any: Pillow.Image.Imageを返すかもしれない
    """


def convertDate(start:str, stop:str) -> str:
    """YYYY年mm月dd日 HH:MM ～ HH:MMという文字列を返す

    Args:
        start (str): 開始時刻. HH:MM形式で渡す
        stop (str): 終了時刻. HH:MM形式で渡す

    Returns:
        str: YYYY年mm月dd日 HH:MM ～ HH:MM
    """
    return "{0} {1} ～ {2}".format(dt.today().strftime("%Y年%m月%d日"), start, stop)


def main():
    """ main function """

    parser = argparse.ArgumentParser()
    parser.add_argument("--img", help="Image for drawing", required=False)
    parser.add_argument("--date", help="Image drawing text.",
                        default="2022/07/01", required=False)
    parser.add_argument("--start", help="Start time.",
                        default="19:00", type=str, required=False)
    parser.add_argument("--stop", help="Stop time.",
                        default="21:00", type=str, required=False)
    args = parser.parse_args()

    print(convertDate(args.start, args.stop))


if __name__ == "__main__":
    main()