import tensorflow as tf
hello=tf.constant('hello everyone, welcome to tensorflow!')
sess=tf.Session()
print(sess.run(hello))
a=tf.constant(10)
b=tf.constant(42)
print(sess.run(a+b))
