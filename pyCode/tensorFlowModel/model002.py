#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import tensorflow as tf
# Network Parameters
index_prediction = tf.argmax(prediction, 1)
index_correct = tf.argmax(output_tensor, 1)
correct_prediction = tf.equal(index_prediction, index_correct)
# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
total_test_data = len(newsgroups_test.target)
batch_x_test, batch_y_test = get_batch(newsgroups_test, 0, total_test_data)
print("Accuracy:", accuracy.eval({input_tensor: batch_x_test, output_tensor: batch_y_test}))