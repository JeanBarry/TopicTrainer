# pylint: disable=too-few-public-methods
from src.modules.storage.s3 import S3


class Bucket:
    """
    This class is used to interact with a bucket in S3.
    """
    def __init__(self, s3_class: S3, bucket_name: str):
        """
        Used to initialize the bucket properties.
        :param s3_class: S3
        :param bucket_name:
        """
        self.client = s3_class
        self.bucket_name = bucket_name

    def get_object(self, object_name: str) -> str:
        """
        This method is used to get an object from a bucket.
        :param object_name: str
        :return: Object url
        """
        return self.client.get_object(bucket_name=self.bucket_name, object_name=object_name)
