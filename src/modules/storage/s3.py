# pylint: disable=too-few-public-methods
import os
from datetime import timedelta
from minio import Minio


class S3:
    """
    This class is used to interact with S3.
    """
    def __init__(self):
        """
        Used to initialize the S3 client.
        """
        self.client = Minio(
            endpoint=f"{os.environ.get('S3_HOST')}:{os.environ.get('S3_PORT')}",
            access_key=os.environ.get('S3_ACCESS_KEY'),
            secret_key=os.environ.get('S3_SECRET_KEY'),
            secure=False,
            region=os.environ.get('S3_REGION')
        )

    def get_object(self, bucket_name: str, object_name: str, seconds_to_expire: int = 3600) -> str:
        """
        This method is used to get an object from a bucket.
        :param bucket_name: str
        :param object_name: str
        :param seconds_to_expire: int
        :return: str
        """
        return self.client.presigned_get_object(bucket_name=bucket_name,
                                                object_name=object_name,
                                                expires=timedelta(seconds=seconds_to_expire)
                                                )
