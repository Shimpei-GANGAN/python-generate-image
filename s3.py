# -*- coding: utf-8 -*-

import boto3
from boto3.session import Session
from typing import Any

def upload_s3(
    session: boto3.Session,
    bucketName: str = "testBucket",
    bucketDir: str = "/tttttt",
    fileName: str = "test.txt"
) -> None:
    """S3にファイルをアップロードする

    Args:
        session (boto3.Session): AssumeROle取得済みSession情報.
        bucketName (str): アップロードするS3のバケット名. Defaults to "testBucket".
        bucketDir (str): アップロードするS3のフォルダ名. Defaults to "/tttttt".
        fileName (str): アップロードするファイル名. Defaults to "test.txt".
    """
    s3 = session.resource("s3")
    bucket = s3.Bucket(bucketName)
    bucket.upload_file(fileName, bucketDir + "/" + fileName)


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
        region_namee="ap-northeast-1"
    )
    
    # テスト
    client = session.client("sts")
    account_id = client.get_caller_identity()["Account"]
    print("Account ID: {0}".format(account_id))

    return session