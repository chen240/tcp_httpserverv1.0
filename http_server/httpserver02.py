from socket import *

#处理客户端请求－－－＞http协议(处理请求及响应)
def handleClient(connfd):
    request=connfd.recv(4096) #接受客户端请求字串
    request_lines=request.splitlines() #将bytes格式按行分割
    for line in request_lines: #将http请求循环打印
        print(line.decode())
    #-------------->这一部分为http响应部分
    try:
        f=open('06_img.html') #打开html文件
    except IOError: #如果没有文件，则返回该响应
        response="HTTP/1.1 not found\r\n" #响应行
        response="\r\n" #空行
        response+='=======sorry not found====' #响应体
    else:
        response="HTTP/1.1 200 OK\r\n" #响应头
        response+="\r\n" #空行
        response+=f.read() #响应体
    finally:
        connfd.send(response.encode())

#主函数用来创建套节字
def main():
    sockfd=socket() #创建套节字对象
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #设置端口重用
    sockfd.bind(('192.168.101.13',8880)) #绑定地址及端口
    sockfd.listen(5) #设置监听队列
    print('Listen to the port 8880')
    while True: #循环等待连接及关闭客户端(浏览器)套节字
        connfd,addr=sockfd.accept()
        print("Connecting to",addr)
        handleClient(connfd) #处理客户端(浏览器)请求
        connfd.close() #关闭客户端套节字

if __name__ == '__main__':
    main()
