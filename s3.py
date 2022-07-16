import boto3
from boto3.session import Session
from pathlib import Path


class S3:
    """AWS S3 に関する処理を行うクラス.
    
    Attributes:
        TODO: 書き方を確認してコメント書く
    """
    
    def __init__(
        self,
        aws_role_arn: str = "arn:aws:iam::XXXXX:role/role_name",
        aws_role_session_name: str = "test",
        aws_region_name: str = "ap-northeast-1"
    ) -> None:
        """Assume Role を取得する.

        Args:
            aws_role_arn (str):
                Role Arn. Defaults to "arn:aws:iam::XXXXX:role/role_name". 
            aws_role_session_name (str):
                Role Session Name. Defaults to "test".
            aws_region_name (str):
                Region Name. Defaults to "ap-northeast-1".
        """

        # NOTE: 以下と同義.
        # $ aws sts assume-role --role-arn roleArn --role-session-name roleSessionName
        _response = boto3.client("sts").assume_role(
            RoleArn = aws_role_arn,
            RoleSessionName = aws_role_session_name
        )

        # NOTE: 以下と同義.
        # $ export AWS_ACCESS_KEY_ID="XXXXX"; export AWS_SECRET_ACCESS_KEY="XXXXX"; export AWS_SESSION_TOKEN="XXXXX"
        self._session = Session(
            aws_access_key_id = _response["Credentials"]["AccessKeyId"],
            aws_secret_access_key = _response["Credentials"]["SecretAccessKey"],
            aws_session_token = _response["Credentials"]["SessionToken"],
            region_name = aws_region_name
        )
        # print("Account ID: {0}".format(self._session.client("sts").get_caller_identity()["Account"]))
        print("Completed")
    
    def __call__(
        self,
        bucket_name: str = "bucket_name",
        bucket_dir: str = "bucket_dir/",
        file_name: str = "./output/example.jpg"
    ) -> None:
        """S3 にファイルをアップロードする.

        Args:
            bucket_name (str):
                アップロードする S3 のバケット名. Defaults to "bucket_name".
            bucket_dir (str):
                アップロードする S3 のフォルダ名. "dirName/" のように "/" は後ろに配置する. Defaults to "bucket_dir/".
            file_name (str):
                アップロードするファイル名. "/dir/filename" の形式で渡すことが可能である. Defaults to "./output/example.jpg".
        """

        # NOTE: upload_file(対象ファイルのパス, S3のアップロード先) のため, file_name から basename のみを抽出する.
        _file_name = Path(file_name).name
        _bucket = self._session.resource("s3").Bucket(bucket_name)

        _bucket.upload_file(file_name, bucket_dir + _file_name)
        print(
            "Completed upload: {0} to s3://{1}/{2}{3}".format(file_name, bucket_name, bucket_dir, _file_name)
        )
