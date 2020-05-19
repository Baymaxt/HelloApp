from qiniu import Auth, put_data, BucketManager


class QiniuManager:

    __access_key = 'P0ZKoI4ZKmFw9i7Ac-AtnZrOruXZitKgk_cxikS7'
    __secret_key = 'Fg_e77wPpy3wfi9-KkXJj9UVAOiiyMPqna0Q2Q2i'
    __bucket_name = 'xiutao1'

    def upload(self, filename, file):
        """
        上传文件
        请将文件名拼装好传过来，一律使用文件类型+uid的方式保存比如uid为1212的用户上传的头像文件名就是portrait1212.png
        声音文件sound+uid
        文章post+uid
        :param filename: 上传后保存的文件名
        :param file: 文件
        :return: 带文件名的完整路径
        """
        key = filename
        q = Auth(self.__access_key, self.__secret_key)
        token = q.upload_token(self.__bucket_name, key, 3600)
        ret, info = put_data(token, key, file)
        print('info: ', info)
        print('ret: ', ret)
        picpath = 'http://qagn0wg13.bkt.clouddn.com/' + key
        return picpath

    def delete(self, filepath):
        """
        删除文件
        :param filename: 文件路径，数据库中取出链接直接传过来就行
        :return: info信息
                _ResponseInfo__response:<Response [200]>, exception:None, status_code:200, text_body:, req_id:VX8AAAAFqYEUYxAW, VX8AAAAFqYEUYxAW, x_log:-

        """
        filename = filepath[33:]
        print(filename)
        q = Auth(self.__access_key, self.__secret_key)
        bucket = BucketManager(q)
        ret, info = bucket.delete(self.__bucket_name, filename)
        return info


# 单例属性
qm = QiniuManager()

if __name__ == '__main__':
    # print(qm.delete('http://qagn0wg13.bkt.clouddn.com/portrait1212'))
    pass