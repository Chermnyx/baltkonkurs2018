import tensorflow as tf
from keras.models import load_model

from moleimages import MoleImages

mimg = MoleImages()
path_to_file = '/media/superuser/C5E7-536E/фото/зло/DSC_1181.JPG'
X = mimg.load_image(path_to_file)

graph = tf.get_default_graph()
model = load_model('/home/superuser/Рабочий стол/Родинки/bests_weight.h5')

with graph.as_default():
    y_pred = model.predict(X)[0, 0]
    #print(y_pred, type(y_pred))
if y_pred > 0.9:
    result = 'High Risk'
elif 0.5 < y_pred <= 0.9:
    result = 'Medium Risk'
else:
    result = 'Low Risk'

print(result)
print(y_pred)
