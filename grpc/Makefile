# 指令  : https://zhuanlan.zhihu.com/p/34960247
# proto : https://github.com/wectf/2020/tree/master/light_sequel/proto

init:
	sudo pip3 install protobuf
	sudo pip3 install grpcio
	sudo pip3 install grpcio-tools

gen_pb2:
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. main.proto

clean:
	rm main_pb2*	
