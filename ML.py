from keras.preprocessing import image
from tensorflow import keras
import numpy as np

def detect_gender(path):
    new_model = keras.models.load_model('gender_model.h5')
    size=150
    test_image = image.load_img(path, target_size=(size, size))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image.reshape(size, size, 3)

    result = new_model.predict(test_image, batch_size=1) 

    if result[0][0]==0:
        print('Male')
        return 'Male'
    else:
        print('Female')
        return 'Female'
    print(result)
    return result
