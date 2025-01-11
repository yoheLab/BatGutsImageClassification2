from contextlib import redirect_stdout
import uvicorn
import os
import sys
sys.path.append("../")
sys.path.append("../../")
from fastapi import FastAPI, File, UploadFile,Form,Query
from src.services.model_service import read_save_image,predict_img,save_feedback_images,load_model,verify_model
from fastapi.responses import FileResponse
from conf.config import get_settings,set_settings
from src.utils.log import Logger
from PIL import Image
from jupyternb.settings import show_python_version
import tensorflow as tf
from tensorflow import keras


import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000
import io
Logger=Logger()

description = """
## Author
**Jaswanth Galle**.

## Instructor

**Dr.Laurel Yohe**.

## Users

You will be able to :
* **Bat guts can be classified by their intestine images**.
* **Displaying the uploaded image**.
"""

set_settings()
show_python_version()
zModelPath = get_settings().MODEL_PATH
zAppTitle = get_settings().APP
zVersion = get_settings().VERSION + "-" + get_settings().ENV
zOwner = get_settings().CODE_OWNER
zInstructor = get_settings().INSTRUCTOR
zModelPath = get_settings().MODEL_PATH
application = FastAPI(title=zAppTitle, description=description,
                      version=zVersion, )


@application.get("/")
async def index():
    return {"CODE Owner":zOwner,'Instructor':zInstructor,
            'Status':'Service' + zAppTitle + ' is Up and running'}


from fastapi.responses import PlainTextResponse
@application.get("/showinfo", response_class=PlainTextResponse)
async def showmodelpath():
    output = "Welcome to the " + zAppTitle + "\n"
    output += "Version: " + zVersion + "\n"
    output += "Instructor: " + zInstructor + "\n"
    output += "Model path: " + zModelPath + "\n"
    output +=  "Python version: " + str(sys.version_info.major)+"."+str(sys.version_info.minor)+"."+str(sys.version_info.micro) + "\n"
    output +=  "TensorFlow version: " + tf.__version__ + "\n"
    import mlflow
    output += "mlflow version: "+str(mlflow.__version__) + "\n"
    import keras
    output += "keras version: "+str(keras.__version__) + "\n"
    import flask
    output += "flask version: "+str(flask.__version__) + "\n"
    return( output )

@application.get("/loadmodel")
async def loadmodel():
    model = load_model()
    # Capture the summary output
    summary_string = io.StringIO()
    with redirect_stdout(summary_string):
        model.summary()
    summary_output = summary_string.getvalue()
    
    # Return the summary as plain text
    return {"model_summary": summary_output}


@application.get("/verifymodel")
async def verifymodel():
    verify_model()

@application.post("/displayimage")
async def display(source: str = Form(...),file: UploadFile = File(...)):
    Logger.info('Image is uploaded for displaying by the user .{}'.format(source))
    read_save_image(file)
    return FileResponse(os.path.join(get_settings().UPLOAD_FOLDER, file.filename))


@application.post("/feedback")
async def feedback(feedback: str = Query("Select Below", enum=["Select Below","blood","plants","insects"]),source: str = Form(...),file: UploadFile = File(...)):
    try:
        if source is None:
            return 'Please provide source'
        Logger.info('Image is uploaded by the user .{} and the feedback is .{}'.format(source,feedback))
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png",'tif')
        if not extension:
            return "Image must be jpg or png or tif format!"

        save_feedback_images(file,feedback)
    except Exception as e:
        Logger.error('Error in feedback api .{} '.format(e))
    return 'Thank you for your feedback'


@application.post("/predict")
async def predict_api(save: int = Form(...),source: str = Form(...),file: UploadFile = File(...)):
    try :
        if source is None:
            return 'Please provide source'
        Logger.info('Image is uploaded by the user .{}'.format(source))
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png",'tif')
        if not extension:
            return "Image must be jpg or png or tif format!"
        if save:
            Logger.info('Image is saving by the user the file name is .{}'.format(file.filename))
            read_save_image(file)
            output = predict_img(file.filename, save=save)
        else:
            Logger.info('Image is not saving by the user')
            request_image = await file.read()
            file = Image.open(io.BytesIO(request_image))
            output=predict_img(file,save=False)
            Logger.info('Image is uploaded by the user .{}  and the output is .{}'.format(source,output))
        return output
    except Exception as e:
        Logger.error('Error in prediction.{} '.format(e))


if __name__ == "__main__":
    print("CWD="+os.getcwd())  
    print('Service is up')
    Logger.info('Service is up ')
    uvicorn.run(application, port=8080, host='0.0.0.0' )

