PROJECT FILES

Below is an explanation of each file in the bat-guts-image-classification folder

 Many of the folders contain a sub-folder called "__pycache__".
    The "__pycache__" folder is automatically created by Python when you run a program. 
    It stores bytecode-compiled and optimized bytecode-compiled versions of your program’s files 
    These files have the same name as the .py files in your project’s folder, but with either 
    ".py"c or ".pyo" extensions 
    The purpose of the "__pycache__" folder is to make your program start a little faster by caching the
    compiled code 
    When your python scripts change, they will be recompiled, and if you delete the files or the whole folder 
    and run your program again, they will reappear 

    You can largely ignore the "__pycache__" folder as a programmer When you’re sending your code to other people, 
    the common practice is to delete the "__pycache__" folder, but it doesn’t really matter whether 
    you do or not. If you are using version control (git), the "__pycache__" folder is typically 
    listed in the ignore file (.gitignore) and thus not included

.gitignore defines which files within the directory structure should not be stored in the repository.

.gitattributes defines the very large files (such as model files) which are stored as links
into the github large file system.

"application.py"
    This is the main python application.  This is the file that should have focus when doing 
    "Run and Debug" in vscode.

"Bats-DietType_ImageClassification-UsingDeepLearning.pdf"
    This is Jaswanth Galle's high level description of his project which had a major objective to
    build an image classification model on Bat-guts MRI scanned image data to predict 
    their diet type. 

Tne "conf" folder contains configuration parameters for the program. 

"conf/config.py"
    "config.py" is a text document that is used to store configuration data for a Python applicatio. 
    It contains key-value pairs of settings that are used by the application. 
    The purpose of "config.py" is to separate the configuration data from the application code, 
    making it easier to manage and modify the settings.

    The contents of "config.py" can vary depending on the application’s needs, 
    but it typically includes settings such as database connection strings, API keys, and other environment
    specific variables. "config.py" is typically imported into the application code and the settings can be accessed 
    as attributes of the imported module.

"conf/logging.conf"
    "logging.conf" is a text file that is used to configure the Python logging module. It contains settings 
    for the logging module, such as loggers, handlers, and formatters. The purpose of this file is to separate 
    the logging configuration data from the application code, making it easier to manage and modify the settings.

    The format and semantics of "logging.conf" file are described in detail in the Python documentation. 
    The file can be used to configure the logging module using either a dictionary or a configuration file.

"jupyternb" is a directory of "Jupyter Notebook" files.  These are not part of the web application
which access the model, but are files that are used to prepare and train the model.

"jupyternb/Bats_guts_image_data_preprocessing_.ipynb"

"jupyternb/Bats_image_data_preprocessing_with_dividing_R,G,B_channels.ipynb"

"jupyternb/Siamese_Network_Bats_Image_classification_Training.ipynb"

"jupyternb/Version_2_Bats_Image_classification_Training.ipynb"

"jupyternb/Version_3_Bats_Image_classification_Training.ipynb"

"jupyternb/settings.py"
    Contains common code used by all the jupyter notebooks to read environment settings
    from a ".env" file
    
"logs/bat.log"
    As specified in "conf/logging.conf", this is the where all logging output is apppended during opermatDialogActions
    of the program.

"resources/models/IVP_MODEL.pkl"
    This is a binary file which was specified as the "MODEL_FOLDER" parameter of "conf/config.py".
    It represents the "CNN" used for the image classification.
    "IVP_MODEL.pkl" is a file that contains a machine learning model saved in the 
    pickle format. The pickle module in Python is used to serialize and deserialize 
    Python objects, such as machine learning models, into a byte stream that can be 
    saved to disk or sent over a network2. The .pkl extension is commonly used to indicate 
    that a file contains a pickled object.

    If you have access to the IVP_MODEL.pkl file, you can load the model into your 
    Python environment using the pickle.load() function.

    In the context of machine learning models, IVP can stand for Initial Value Problem. 
    An initial value problem is a mathematical problem that involves finding the solution 
    to a differential equation given an initial condition. 

    There are many other machine learning models that are used for various tasks such as classification, 
    regression, clustering, and more. Here are some of the most popular machine learning models: 

"src/services/model_service.py"

"static/feedback/blood"

"static/feedback/insects"

"static/feedback/plants"

"utils/log.py"
    Contains the default "Logger" constructor function which opens the log file as specified in "conf/logging.conf"

"readme.txt"
    This file.

"requirements.txt"
    This is a text file that specifies the python packages that must be installed in order to run this program.
    In some cases a specific version of a package is required.  In most cases a minimum version of a packages
    is specified.

    Here is the definition of some important terms that pertain to the packages:
        ASG - stands for Asynchronous Server Gateway Interface. It is a specification 
        that describes the interface between a web server and a Python web 
        application or framework.  ASG allows multiple, asynchronous events 
        per application and supports both synchronous and asynchronous apps. 
        It is the spiritual successor of WSGI, which stands for Web Server Gateway Interface.
        ASG processes requests asynchronously, which means that different requests can do 
        their processing and finish in no particular order 1. This is different from WSGI, 
        which handles requests synchronously and processes them sequentially or one after the other.

        CNN - Convolutional Neural Network (CNN) is a type of neural network that is commonly
        used for image classification and recognition tasks. It is a deep learning algorithm 
        that is designed to automatically learn the features of an image by itself through 
        filters optimization. CNNs are composed of multiple layers of convolutional, pooling, 
        and fully connected layers. Some of the popular CNN models include LeNet, AlexNet, ResNet, 
        GoogleNet, and MobileNet.

        Neural Network: A series of algorithms that endeavors to recognize underlying 
        relationships in a set of data through a process that mimics the way the human brain 
        operates. Neural networks are a subset of machine learning and are at the heart of 
        deep learning algorithms. They consist of a node layers, each with an input, output, 
        weight, and threshold. They use training data to learn and improve their accuracy over time.

        WSWG - Web server gateway interface

    The following python packages are required:
        keras==2.8.0
            Keras is a high-level, user-friendly API used for building and training neural networks. 
            It is an open-source library built in Python that runs on top of TensorFlow, JAX, or PyTorch. 
            Keras was developed to enable fast experimentation and iteration, and it lowers the barrier to 
            entry for working with deep learning.

            To use Keras, you should install the backend of your choice: TensorFlow, JAX, or PyTorch. 
            Note that TensorFlow is required for using certain Keras features, such as certain preprocessing 
            layers and tf.data pipelines. Keras is available on PyPI as keras. 
            To install it, run pip install keras --upgrade.

            This program uses Keras ImageDataGenerator is used to perform  data augmentations to the 
            original data and further, it makes the transformation of this data on a random basis 
            and gives the output resultant containing only the data that is newly transformed. 
            It does not add the data.

        
        markupsafe>=2.1.1
            MarkupSafe is a Python package that provides a text object that escapes characters so 
            that it is safe to use in HTML and XML 12. This package is used to mitigate injection attacks, 
            meaning untrusted user input can safely be displayed on a page. 
            The package is open-source and available on PyPI.

            The MarkupSafe package is used to create a text object that can be used in place of a regular string. 
            The text object automatically escapes characters that have special meanings in HTML and XML, 
            such as <, >, and &.  This ensures that the text is safe to use in HTML and XML, even if it contains untrusted 
            user input.

            To install MarkupSafe, you can use pip by running pip install markupsafe. 
            Once installed, you can import the package in your Python code and use the Markup class to create text 
            objects that are safe to use in HTML and XML.

        fastapi==0.79.0
            FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+. 
            It is designed to be fast, easy to use, and easy to learn. FastAPI is built on top of 
            the Starlette framework and uses Pydantic for data validation and serialization. It is 
            one of the fastest Python frameworks available, with performance on par with NodeJS and Go. 
            Some of the key features of FastAPI include:
                    - Fast: Very high performance, on par with NodeJS and Go.
                    - Fast to code: Increase the speed to develop features by about 200% to 300%.
                    - Fewer bugs: Reduce about 40% of human (developer) induced errors.
                    - Intuitive: Great editor support. Completion everywhere. Less time debugging.
                    - Easy: Designed to be easy to use and learn. Less time reading docs.
                    - Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
                    - Robust: Get production-ready code. With automatic interactive documentation.
                    - Standards-based: Based on (and fully compatible with) the open standards for APIs: 
                        OpenAPI and JSON Schema

            To install FastAPI, you should first install the backend of your choice: TensorFlow, JAX, or Py. 
            Then, you can install FastAPI using pip by running pip install fastapi 
        
        Pillow==9.2.0
            Pillow is a Python Imaging Library (PIL) fork that adds image processing capabilities to 
            your Python interpreter. It provides extensive file format support, an efficient internal 
            representation, and fairly powerful image processing capabilities. The core image library is 
            designed for fast access to data stored in a few basic pixel formats 1. It should provide a 
            solid foundation for a general image processing tool.

            To install Pillow, you can use pip by running pip install pillow 
            Once installed, you can import the package in your Python code and use it to open, manipulate, and 
            save images. The package provides a wide range of functions for image processing, such as 
            cropping, resizing, rotating, and filtering.
        
        starlette==0.19.1
            Starlette is a lightweight, production-ready ASGI framework and toolkit for building async 
            web services in Python. It is designed to be fast, easy to use, and easy to learn. 
            Starlette is built on top of the ASGI specification and uses asyncio for concurrency. 

            To install Starlette, you can use pip by running pip install starlette 
            Once installed, you can import the package in your Python code and use it to build async 
            web services.

        gunicorn==20.1.0
            Gunicorn is a Python WSGI HTTP Server for UNIX that is used to serve Python web 
            applications. It is a pre-fork worker model ported from Ruby’s Unicorn project. 
            The Gunicorn server is broadly compatible with various web frameworks, simply 
            implemented, light on server resource usage, and fairly speedy. 

            To install Gunicorn, you can use pip by running pip install gunicorn 
            Once installed, you can use the gunicorn command to start the server and serve your Python 
            web application. The basic usage of Gunicorn is as follows:

                    $ gunicorn [OPTIONS] APP_MODULE

            Where APP_MODULE is of the pattern (MODULE_NAME):(VARIABLE_NAME). The module name can be a full 
            dotted path, and the variable name refers to a WSGI callable that should 
            be found in the specified module.
        
        uvicorn==0.18.2
            Uvicorn is an ASGI web server implementation for Python. 

        python-dotenv
            Used to process local environment variables from a ".env" file.

        python-multipart==0.0.5
            python-multipart is a Python package that provides a streaming multipart parser for Python. 
            The package is open-source and available on PyPI

            The python-multipart package is used to parse multipart/form-data requests in Python web applications. 
            It can read from a file, a socket, or a WSGI environment 1. The package provides a number of functions 
            for parsing and processing multipart data, such as parse_options_header, parse_content_disposition, 
            and parse_multipart.

            To install python-multipart, you can use pip by running pip install python-multipart 
            Once installed, you can import the package in your Python code and use it to parse 
            multipart data in your web application.


        
        pydantic>=1.6.2
            Pydantic is a Python package that provides data validation using Python type hints. 
            It is fast, extensible, and plays nicely with your linters/IDE/brain. Pydantic is 
            designed to define how data should be in pure, canonical Python 3.7+ and validate it 
            with Pydantic. Pydantic is also capable of generating JSON Schema and OpenAPI (formerly Swagger) 
            schemas with ease.

            To install Pydantic, you can use pip by running pip install pydantic 
            Once installed, you can import the package in your Python code and use it to define and 
            validate data. Pydantic provides a number of classes and functions for defining data 
            models, such as BaseModel, Field, and validator. These classes and functions can be used to 
            define data models that are easy to read, write, and validate.

        python-dotenv==0.17.1
            python-dotenv is a Python package that provides a way to load environment variables 
            from a .env file into your Python application. It reads key-value pairs from a .env 
            file and can set them as environment variables. This package is useful when you are 
            developing an application that requires environment variables to be set, but you don’t 
            want to set them manually every time you run the application.

            To install python-dotenv, you can use pip by running pip install python-dotenv 
            Once installed, you can import the package in your Python code and use it to load environment 
            variablesi rom a .env file. The package provides a number of functions for loading environment 
            variables, such as load_dotenv, dotenv_values, and find_dotenv.

        werkzeug==2.2.1
            Werkzeug is a comprehensive WSGI web application library for Python. 
            It provides a collection of utilities for WSGI applications and has become 
            one of the most advanced WSGI utility libraries 1. The name “Werkzeug” is 
            German for “tool1. Some of the key features of Werkzeug include:

            - An interactive debugger that allows inspecting stack traces and 
            source code in the browser with an interactive interpreter for 
            any frame in the stack.
            - A full-featured request object with objects to interact with headers, 
            query args, form data, files, and cookies.
            - A response object that can wrap other WSGI applications and handle streaming data.
            - A routing system for matching URLs to endpoints and generating URLs for endpoints, 
            with an extensible system for capturing variables from URLs.
            - HTTP utilities to handle entity tags, cache control, dates, user agents, cookies, files, and more.
            - A threaded WSGI server for use while developing applications locally.
            - A test client for simulating HTTP requests during testing without requiring running a server.

            Werkzeug is designed to be fast, easy to use, and easy to learn 1. It doesn’t enforce 
            any dependencies, so it’s up to the developer to choose a template engine, database 
            adapter, and even how to handle requests. It can be used to build all sorts of 
            end-user applications such as blogs, wikis, or bulletin boards
        
        protobuf==3.20.*
            Python protobuf package is a package used to encode and decode data in 
            the protobuf format. To use it in your Python code, you need to first 
            define the data structure you want to encode or decode using a .proto file. 
            This file contains the definition of the data structure, including the field 
            names, types, and default values.

            You can install the protobuf package using pip install protobuf

         matplotlib
            is a widely-used data visualization library in Python, designed to create 
            static, interactive, and animated visualizations.   

        tifffile
             library designed for reading and writing TIFF (Tagged Image File Format) files, 
             particularly those used in bioimaging.

        imagecodecs
            library that provides block-oriented, in-memory buffer transformation, compression, 
            and decompression functions. 

        opencv-python
            a popular computer vision and image processing library
        

BACKEND PROCESS

AWS RESOURCES

DATABASE

    This project uses the MONGO database to store image data.   

    MongoDB is a popular choice for neural network applications due to its scalability 
    and flexibility. MongoDB is built on a scale-out architecture that has become popular 
    with developers of all kinds for developing scalable applications with evolving data 
    schemas. As a document database, MongoDB makes it easy for developers to store structured 
    or unstructured data. It uses a JSON-like format to store documents. This makes it easier 
    to store and retrieve data in a format that is compatible with the requirements of neural networks.

    In addition, MongoDB’s query API allows developers to query deep into documents and perform complex 
    analytics pipelines with just a few lines of declarative code. This is particularly useful for neural 
    network applications, which often require complex querying and analysis of large datasets.

    Finally, MongoDB’s real-time analytics and high-speed logging capabilities make it an ideal choice 
    for neural network applications that require fast and efficient data processing. Overall, MongoDB’s 
    scalability, flexibility, and powerful query API make it a popular choice for on neural network applications.

    MONGO DB Schema

JUPYTER NOTEBOOK

    You can run the ".ipynb" files from the jupyternb directory.  You can create a ".env" file
    which allows the notebook files in different environments such as locally on the Mac or in 
    a google colab.  The ".env" settings as defined in a sample file are as follows:

        USE_GOOGLE_COLAB=False
        USE_NVIDIA=False
        CONTENT_PATH="{$HOME}/isr/bguts"

        USE_GOOGLE_COLAB is a true/false that indicates that you are running in google colab
        environment; default False.   USE_NVIDIA indeates that you have Nvidia GPU support; default
        False.  CONTENT_PATH is the base folder where all the .tiff and jpeg files are stored, 
        this path can contain environment variables enclosed in curly braces; Default {$HOME}/bguts.

GIT REPOSITORY SETUP

    To initalliy setup the git repository on github do the following steps:

        - Create a new repository called "BatGutsImageClassification2" on github.
        
        - On github, define all the team members as collaborators on this repo.  Have each team
        member create a personal access token (PAT).  Make sure this token has expiration of one year,
        and make sure that you check all the boxes for "Select scopes" are checked.

        - do a "git clone" of this repository

     
        - enter the following to add everything extensible
                git add *

        - enter the following command to commit the changes:
                git commit

        - push the changes back to the repo with this command:
                git push origin main

GIT EXAMPLES

    To clone the repository with a personal access token of "yourPAT":

        git clone https://ghp_YourPAT@github.com/TomYo55/BatGutsImageClassification.git

    To add a new file called "FileName" to the repo:

        git add "FileName"

    To commit changes the changes:

        git commit -a -m "Description of change"

    To push changes to the main repository.

        git push origin main

    To forget all changes:

        git reset --hard

VS-Code

    Install all extensions related to python, git, jupyter notebooks, and conda

CONDA 

    After installing Anaconda, create a new environment with the following command:

        conda env create -f environment.yml

    This will create a new conda environment with all the packages needed to run the 
    jupyter notebooks.  The name of this environment is "BatGuts4".  You should activate
    "BatGuts4" when you select interpreter in VS-Code.
    
~                                     