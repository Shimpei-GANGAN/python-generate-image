# -*- coding: utf-8 -*-

import argparse
from datetime import datetime as dt
from PIL import Image, ImageDraw, ImageFont


def draw_text(date:str="2022年07月01 19:00 ～ 21:00") -> None:
    """画像に日時を描画する

    Args:
        date (str): 描画日時. Defaults to "2022年07月01 19:00 ～ 21:00".
    """
    img = Image.new("RGB", (1024, 384), (256, 256, 256))
    draw = ImageDraw.Draw(img)
    font_type = ["./font/HannariMincho-Regular.otf"]
    color = [(0, 0, 0), (256, 256, 256)]
    text = [
        "これはテストです",
        "【開催日時】",
        "テストの文章を生成してみよう。\n何も考えられないので結構適当な文章です。"
    ]

    # 描画する
    draw.text((512, 64), text[0], fill=color[0], anchor="mm",
            font=ImageFont.truetype(font_type[0], 60))
    draw.rectangle([(30, 140),(994, 220)], fill=(255, 0, 0))
    draw.text((512, 180), text[1] + date, fill=color[1], anchor="mm",
            font=ImageFont.truetype(font_type[0], 32))
    draw.text((512, 300), text[2], fill=color[0], anchor="mm",
            font=ImageFont.truetype(font_type[0], 32))

    # 画像を保存する
    img.save("./output/test.png")


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