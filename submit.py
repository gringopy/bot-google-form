import time
from fbxz import getFbxz



url= 'https://docs.google.com/forms/d/e/1FAIpQLSd6FZvuqy5l7kAlUzctjRYMgVpYW5DfE-S1gt0iAPZ2msQglg/viewform'

getFbxz(url)

timestamp_seconds = int(time.time())