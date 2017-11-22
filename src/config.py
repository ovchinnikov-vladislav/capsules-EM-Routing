import tensorflow as tf

flags = tf.app.flags

############################
#    hyper parameters      #
############################
flags.DEFINE_float('clip_min', 1e-8, 'epsilon')
flags.DEFINE_float('clip_max', 1000, 'clip_max')

flags.DEFINE_integer('epoch', 300, 'epoch')
flags.DEFINE_integer('batch_size', 20, 'batch size')
flags.DEFINE_integer('iter_routing', 3, 'number of iterations')

################################
#    structure parameters      #
################################
flags.DEFINE_integer('A', 32, 'number of channels in output from ReLU Conv1')
flags.DEFINE_integer('B', 8, 'number of capsules in output from PrimaryCaps')
flags.DEFINE_integer('C', 8, 'number of channels in output from ConvCaps1')
flags.DEFINE_integer('D', 8, 'number of channels in output from ConvCaps2')
flags.DEFINE_integer('E', 10, 'number of channels in output from ConvCaps2')

############################
#   environment setting    #
############################
flags.DEFINE_string('dataset', './data', 'the path for dataset')

cfg = tf.app.flags.FLAGS