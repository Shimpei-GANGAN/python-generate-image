# -*- coding: utf-8 -*-

import argparse
from datetime import datetime as dt
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def draw_text(date:str="2022年07月01日 19:00 ～ 21:00", name:str="test.png") -> None:
    """画像に日時を描画する

    Args:
        date (str): 描画日時. Defaults to "2022年07月01日 19:00 ～ 21:00".
        name (str): 画像名. Defaults to "test.png".
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
    Path("./output").mkdir(exist_ok=True)
    img.save("./output/" + name)


def convert_date(start:str, end:str) -> str:
    """YYYY年mm月dd日 HH:MM ～ HH:MMという文字列を返す

    Args:
        start (str): 開始時刻. HH:MM形式で渡す
        end (str): 終了時刻. HH:MM形式で渡す

    Returns:
        convert date (str): YYYY年mm月dd日 HH:MM ～ HH:MM
    """
    return "{0} {1} ～ {2}".format(dt.today().strftime("%Y年%m月%d日"), start, end)


def main():
    """ main function """

    parser = argparse.ArgumentParser()
    parser.add_argument("--img-name",
                        help="Image Name. Please enter the file extension. (default: 'example.png')",
                        default="example.png", type=str, required=False)
    parser.add_argument("--start", help="Start time. (default: '19:00)",
                        default="19:00", type=str, required=False)
    parser.add_argument("--end", help="Stop time. (default: '21:00')",
                        default="21:00", type=str, required=False)
    args = parser.parse_args()

    print("date {0}".format(convert_date(args.start, args.end)))
    draw_text(convert_date(args.start, args.end), name=args.img_name)


if __name__ == "__main__":
    main()