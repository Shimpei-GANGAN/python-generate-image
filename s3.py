# -*- coding: utf-8 -*-

import boto3
from boto3.session import Session
from pathlib import Path


def upload_s3(
    session: boto3.Session,
    bucketName: str = "testBucket",
    bucketDir: str = "/tttttt",
    fileName: str = "test.txt"
) -> None:
    """S3にファイルをアップロードする

    Args:
        session (boto3.Session):
            Assume Role で取得した Session 情報.
        bucketName (str):
            アップロードする S3 のバケット名. Defaults to "testBucket".
        bucketDir (str):
            アップロードする S3 のフォルダ名. dirName/ のように / は後ろに配置する. Defaults to "/tttttt".
        fileName (str):
            アップロードするファイル名. /dir/filename の形式で渡すことが可能である. Defaults to "test.txt".
    """
    s3 = session.resource("s3")
    bucket = s3.Bucket(bucketName)

    # NOTE: upload_file(対象ファイルのパス, S3のアップロード先) のため, fileNameからbasenameのみを抽出する
    bucket.upload_file(fileName, bucketDir + Path(fileName).name)


def get_assume_role(
    roleArn: str = "arn:aws:iam:: XXXXX:role/role_name",
    roleSessionName: str = "test"
) -> boto3.Session:
    """AssumeRoleを取得する

    Args:
        roleArn (str): Role Arn. Defaults to "arn:aws:iam:: XXXXX:role/role_name".
        roleSessionName (str): Role Session Name. Defaults to "test".
    Returns:
        AssumeRole Session.
    """
    client = boto3.client("sts")

    # NOTE: aws sts assume-role --role-arn roleArn --role-session-name roleSessionName
    response = client.assume_role(
        RoleArn = roleArn,
        RoleSessionName = roleSessionName
    )

    # NOTE: 以下の設定と同義.
    # export AWS_ACCESS_KEY_ID="XXXXX"
    # export AWS_SECRET_ACCESS_KEY="XXXXX"
    # export AWS_SESSION_TOKEN="XXXXX"
    session = Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
        region_name="ap-northeast-1"
    )
    
    # テスト
    client = session.client("sts")
    account_id = client.get_caller_identity()["Account"]
    print("Account ID: {0}".format(account_id))

    return session


if __name__ == "__main__":
    session = get_assume_role(
        roleArn="ttttt",
        roleSessionName="ttttt"
    )

    upload_s3(
        session=session,
        fileName="./output/example.png"
    )