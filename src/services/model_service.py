import pickle
import os
import sys
sys.path.append("../")
sys.path.append("../../")
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from keras.applications.xception import preprocess_input
from conf.config import get_settings
import numpy as np
from src.utils.log import Logger
from PIL import Image
import PIL.Image
import io
PIL.Image.MAX_IMAGE_PIXELS = 933120000
import tensorflow as tf
from tensorflow import keras

# Load the model

# If you want to see a summary of the model
Logger=Logger()
model=None

def load_model():
    global model
    try:
        zModelPath = get_settings().MODEL_PATH
        model = keras.models.load_model(zModelPath)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading the model: {e}")
    return model
 

def  verify_model():
    zModelPath = get_settings().MODEL_PATH
    
    with open(zModelPath, "rb") as f:
        pickle_data = f.read()
        import pickletools
        output = pickletools.genops(pickle_data)
        opcodes = []
        for opcode, arg, pos in output:
            zName = opcode.name
            opcodes.append(opcode.name)
        zFirst = opcodes[0]
        zLast = opcodes[-1]
        if zFirst == 'PROTO' and zLast == 'STOP':
            print( zModelPath + " is a Valid pickle file")
        else:
            print(zModelPath + " is an Invalid pickle file")
              
def save_feedback_images(file,feedback):
    try:
        filename = secure_filename(file.filename)
        file_location = os.path.join("",*[get_settings().FEEDBACK_FOLDER,feedback,filename])
        print(file_location)
        with open(file_location, 'wb+') as fileobj:
            fileobj.write(file.file.read())
            Logger.info('Image saved in feedback file name is .{}'.format(filename))

    except Exception as e:
        Logger.error("Error in  .{}".format(e))
    return

def read_save_image(file):
    try:
        filename = secure_filename(file.filename)
        file_location = os.path.join(get_settings().UPLOAD_FOLDER, filename)

        with open(file_location, 'wb+') as fileobj:
            fileobj.write(file.file.read())
            Logger.info('Image saved in uploads file name is .{}'.format(filename))

    except Exception as e:
        Logger.error("Error in read_save_image .{}".format(e))
    return

def load_image(filename):
    img=None
    try:
        img=image.load_img(os.path.join(get_settings().UPLOAD_FOLDER, filename), target_size=get_settings().TARGET_SIZE)

    except Exception as e:
        Logger.error("Error in loading image .{}".format(e))
    return img

def preprocess_image(img):
    img_preprocessed=None
    try:
        img_array = image.img_to_array(img)

        img_batch = np.expand_dims(img_array, axis=0)

        img_preprocessed = preprocess_input(img_batch)
        Logger.info('Image is Preprocessed')

    except Exception as e:
        Logger.error("Error in preprocessing the image  .{}".format(e))
    return img_preprocessed

def predict_img(filename,save=False):


    global model
    Prediction = 'None'
    try:
        if model is None:
            print('loading')
            model=load_model()
        if save:
            img = load_image(filename)
        else:

            img= filename
        img = preprocess_image(img)
        prediction = model.predict(img)

        prediction_max = [int(i > .5) for i in prediction[0]]
        Prediction = 'None'
        if 1 in prediction_max and sum(prediction_max) == 1:
            # if prediction_max.index(1) ==0:
            #   return 'Bat eats Blood'
            if prediction_max.index(1) == 0:
                Prediction = 'This Bat eat Insects'
            if prediction_max.index(1) == 1:
                Prediction = 'This Bat eat Plants'
        return Prediction
    except Exception as e:
        Logger.error("Error in preprocessing the image image .{}".format(e))
    return Prediction





