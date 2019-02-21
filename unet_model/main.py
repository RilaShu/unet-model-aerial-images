from model import *
from data import *

# import tensorflow as tf
# import keras.backend.tensorflow_backend as KTF
#
# KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'cpu': 0})))


data_gen_args = dict()
myGene = trainGenerator(2,'../data/train','image','label',data_gen_args,save_to_dir = None)

model = unet()
model_checkpoint = ModelCheckpoint('unet_Aerial.hdf5', monitor='loss', verbose=1, save_best_only=True)
model.fit_generator(myGene, steps_per_epoch=300, epochs=20, callbacks=[model_checkpoint])

testGene = testGenerator("../data/test")
results = model.predict_generator(testGene,12,verbose=1)
saveResult("../data/test", results)