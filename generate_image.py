from datetime import datetime as dt
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


class GenerateImage:
    """日時を描画した画像を生成する."""

    FONT_TYPE: list[str] = ["./font/HannariMincho-Regular.otf"]
    DISPLAY_TEXT: list[str] = [
        "これはテストです",
        "【開催日時】",
        "テストの文章を生成してみよう。\n何も考えられないので結構適当な文章です。"
    ]
    # NOTE: color = [黒, 白, 赤]
    color = [ (0, 0, 0), (256, 256, 256), (255, 0, 0) ]


    def __init__(
        self,
        start: str = "19:00",
        end: str = "21:00",
        file_path: str = "./output/example.jpg"
    ) -> None:
        """インスタンス変数を設定する.

        Args:
            start (str): 開始時刻. HH:MM 形式で渡す. Defaults to "19:00".
            end (str): 終了時刻. HH:MM 形式で渡す. Defaults to "21:00".
            file_path (str): 画像を保存するパス名. Defaults to "./output/example.jpg".            
        """

        self.start = start
        self.end = end
        self.file_path = file_path

        # 画像を生成する
        self.img = Image.new("RGB", (1024, 384), (256, 256, 256))


    def __call__(self) -> None:
        """画像に日時を描画し保存する."""

        draw = ImageDraw.Draw(self.img)

        # 画像を生成する
        draw.text(
            (512, 64),
            GenerateImage.DISPLAY_TEXT[0], 
            fill = GenerateImage.color[0],
            anchor = "mm",
            font = ImageFont.truetype(GenerateImage.FONT_TYPE[0], 60)
        )
        draw.rectangle(
            [(30, 140),(994, 220)],
            fill = GenerateImage.color[2]
        )
        draw.text(
            (512, 180),
            GenerateImage.DISPLAY_TEXT[1] + self.__format__(),
            fill = GenerateImage.color[1],
            anchor = "mm",
            font = ImageFont.truetype(GenerateImage.FONT_TYPE[0], 32)
        )
        draw.text(
            (512, 300),
            GenerateImage.DISPLAY_TEXT[2],
            fill = GenerateImage.color[0],
            anchor = "mm",
            font = ImageFont.truetype(GenerateImage.FONT_TYPE[0], 32)
        )

        # 画像を保存する
        self._save_image()


    def __format__(self) -> str:
        """YYYY年mm月dd日 HH:MM ～ HH:MMという文字列を返す.

        Returns:
            convert date (str): YYYY年mm月dd日 HH:MM ～ HH:MM
        """

        return "{0} {1} ～ {2}".format(dt.today().strftime("%Y年%m月%d日"), self.start, self.end)


    def _save_image(self) -> None:
        """画像を保存する."""

        Path(Path(self.file_path).parent).mkdir(exist_ok=True)
        self.img.save(self.file_path)
        print("Completed Generate Image")
