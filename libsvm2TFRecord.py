import tensorflow as tf
import os

def generate_tfrecords(input_filename, output_filename):

	print("Start to convert {} to {}".format(input_filename, output_filename))
	writer = tf.python_io.TFRecordWriter(output_filename)

	for line in open(input_filename, "r"):
		data = line.split(" ")
		label = int(data[0])
		indices = []
		values = []
		for fea in data[1:] :
			if fea < "0" :
				break
			id, value = fea.split(":")
			indices.append(int(id))
			values.append(float(value))

	# Write each example one by one
		example = tf.train.Example(features=tf.train.Features(feature={
		"label":	tf.train.Feature(int64_list = tf.train.Int64List(value = [label])),
		"indices":	tf.train.Feature(int64_list = tf.train.Int64List(value = indices)),
		"values":	tf.train.Feature(float_list = tf.train.FloatList(value = values))
	}))

	writer.write(example.SerializeToString())

	writer.close()
	print("Successfully convert {} to {}".format(input_filename,output_filename))


if __name__ == "__main__":
	generate_tfrecords("GPUdata/Problem1/train.txt", "MLPdata/train.tfrecords")
	generate_tfrecords("GPUdata/Test/test.txt", "MLPdata/test.tfrecords")
