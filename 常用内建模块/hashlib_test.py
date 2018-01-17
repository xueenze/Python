import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5_2 = hashlib.md5()
md5_2.update('how to use md5 in '.encode('utf-8'))
md5_2.update('python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())