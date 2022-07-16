import argparse

from generate_image import generate_image, save_image
from s3 import S3

def main():
    """ main function """

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img-name",
                        help="Image Name. Please enter the file extension. (default: 'example.jpg')",
                        default="example.png", type=str, required=False)
    parser.add_argument("--start", help="Start time. (default: '19:00')",
                        default="19:00", type=str, required=False)
    parser.add_argument("--end", help="Stop time. (default: '21:00')",
                        default="21:00", type=str, required=False)
    parser.add_argument("-n", "--role-session-name", help="AWS Role Session Name.",
                        type=str, required=True)
    args = parser.parse_args()

    _file_path = "./output/"

    # テスト画像を生成し保存する
    img = generate_image(start = args.start, end = args.end)
    save_image(img, file_path=_file_path, file_name=args.img_name)

    # インスタンス生成
    s3 = S3(
        aws_role_arn="arn:aws:iam::XXXXX:role/role_name",
        aws_role_session_name=args.role_session_name
    )
    # S3に画像をアップロードする
    s3(
        bucket_name="testBucket",
        bucket_dir="bucketDir/",
        file_name = _file_path + args.img_name
    )


if __name__ == "__main__":
    main()
