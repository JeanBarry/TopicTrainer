from src.modules.storage.s3 import S3
from src.modules.storage.bucket import Bucket
from src.modules.storage.constants import LOGOS_BUCKET_NAME

s3 = S3()
logos_bucket = Bucket(s3_class=s3, bucket_name=LOGOS_BUCKET_NAME)
