import http.client
import time
from datetime import datetime
import logging
# 13724
article_id_list=['9532263','9532289','9532345','9674857','16917667','16932049',
                 '17254871','48877995','49805185','51426590','51496360','42611359'
                  ,'42855589','18165735','42572349']
index = 0
size = len(article_id_list)
while True:
    time.sleep(10)
    conn = http.client.HTTPConnection('blog.csdn.net')
    url = "/fengyutubu/article/details/%s"%article_id_list[index]
    conn.request("GET",url)
    logging.error("time: %s ----url:  %s" % (datetime.now(),url))
    index = index + 1
    if index > size-1:
        time.sleep(60)
        index = 0
    reps = conn.getresponse()
    data = reps.read()
    time.sleep(5)
    conn.close()