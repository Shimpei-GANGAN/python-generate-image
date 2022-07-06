from datetime import datetime as dt
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def generate_image(
    start: str = "19:00",
    end: str = "21:00"
) -> Image:
    """画像に日時を描画する.

    Args:
        start (str): 開始時刻. HH:MM 形式で渡す. Defaults to "19:00".
        end (str): 終了時刻. HH:MM 形式で渡す. Defaults to "21:00".

    Returns:
        generate image (Image): 生成したテスト画像. 画像は RGB 形式.
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
    draw.text(
        (512, 180),
        text[1] + convert_date(start, end),
        fill=color[1],
        anchor="mm",
        font=ImageFont.truetype(font_type[0], 32)
    )
    draw.text((512, 300), text[2], fill=color[0], anchor="mm",
            font=ImageFont.truetype(font_type[0], 32))

    return img


def generate_black_image() -> None:
    pass


def save_image(
    img: Image,
    file_path: str = "./output",
    file_name: str = "example.jpg"
) -> None:
    """画像を保存する.

    Args:
        img (Image): Pillow で生成した画像ファイル.
        file_path (str): 画像を保存するパス. Defaults to "./output".
        file_name (str): 画像名. Defaults to "example.jpg".
    """

    Path(file_path).mkdir(exist_ok=True)
    img.save(file_path + file_name)


def convert_date(start:str, end:str) -> str:
    """YYYY年mm月dd日 HH:MM ～ HH:MMという文字列を返す

    Args:
        start (str): 開始時刻. HH:MM形式で渡す
        end (str): 終了時刻. HH:MM形式で渡す

    Returns:
        convert date (str): YYYY年mm月dd日 HH:MM ～ HH:MM
    """
    return "{0} {1} ～ {2}".format(dt.today().strftime("%Y年%m月%d日"), start, end)
