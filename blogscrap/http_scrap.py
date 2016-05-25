import http.client
import time
from datetime import datetime
import logging

article_id_list=['9532263','9532289','9532345','9674857','16917667','16932049',
                 '17254871','48877995','49805185','51426590','51496360']
index = 0
size = len(article_id_list)
while True:
    time.sleep(10)
    # print(datetime.now())
    logging.error(datetime.now())
    conn = http.client.HTTPConnection('blog.csdn.net')
    conn.request("GET","/fengyutubu/article/details/%s"%article_id_list[index])
    index = index + 1
    if index > size-1:
        time.sleep(60)
        index = 0
    reps = conn.getresponse()
    print(reps.status,reps.reason)
    data = reps.read()
    conn.close()