import boto3


class Uploader:
    """アップロード用クラス"""

    def __init__(self, bucket_name):
        """イニシャライザ"""
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload(self, key, local_path):
        self.s3.upload_file(self.bucket_name, key, local_path)