# coding=utf-8
# author:colby

from hdfs import *




def main():
    client = Client("http://BIGDATA:50070", timeout=1000)
    # upload(client)
    cat_hdfs_file(client)


if __name__ == "__main__":
    main()
