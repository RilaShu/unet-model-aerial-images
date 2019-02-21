from model import *
from data import *
from keras.models import load_model

# import tensorflow as tf
# import keras.backend.tensorflow_backend as KTF
#
# KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'cpu': 0})))


data_gen_args = dict()

model = load_model('unet_Aerial.hdf5')

testGene = testGenerator("../data/test")
results = model.predict_generator(testGene,12,verbose=1)
saveResult("../data/test", results)