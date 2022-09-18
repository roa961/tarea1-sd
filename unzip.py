import shutil
import gzip

def unziptxt():
    with gzip.open("user-ct-test-collection-09.txt.gz", 'rb') as in_f:
        with open('user-ct-test-collection-09.txt','wb')  as out_f:
            shutil.copyfileobj(in_f, out_f)
            return True

