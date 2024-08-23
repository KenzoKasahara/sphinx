import boto3


class Downloader:
    """ダウンロード用クラス"""

    def __init__(self, bucket_name):
        """イニシャライザ"""
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def download(self, key, local_path):
        self.s3.download_file(self.bucket_name, key, local_path)