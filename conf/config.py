from functools import lru_cache # read .env only once
from jupyternb.settings import load_BatGutsSettings







class EnvSettings():
  ENV: str = "dev"
  APP: str = "Bat Guts Image Classification"
  VERSION: str = "0.0.0"
  DESCRITION : str = "Code Owner : Jaswanth Galle, Instructor : Dr.Laurel Yohe , Description : Bat Guts Can be Classified by their intestine images"
  UPLOAD_FOLDER: str = "src/static/uploads/"
  LOGCONF_PATH:str ='conf/logging.conf'
  LOGFILE_PATH:str = 'logs/bat.log'
  FEEDBACK_FOLDER:str = 'src/static/feedback/'
  MODEL_PATH: str = "resources/models/IVP_MODEL.pkl"
  CODE_OWNER: str ='Jaswanth G'
  INSTRUCTOR:str = 'Dr.Laurel Yohe'
  TARGET_SIZE: tuple =(256,256)

my_env_settings = EnvSettings()



@lru_cache()
def get_settings():
  global my_env_settings
  return my_env_settings 

def set_settings():
    global my_env_settings
    S = load_BatGutsSettings("jupyternb/.env")
    my_env_settings.MODEL_PATH = S.zContentPath + "/" + S.zModelFilename
    
  