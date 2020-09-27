# SMART CROWD ANALYZER


Smart Crowd Analyzer is a product which can enhance your Managing experience. Field of area we implied our product is Shopping Mall. Our Product can: 

  - Count the people Entering and leaving a place. (People Counting)
  - Detect Age , Gender , Emotion and Group of peoples. (Stock Management)
  - Heatmap of platform (Occupancy Management)
  - Statistical Report (Daily/Monthly/Yearly Report)
  
Brochure is Uploaded in files 

## Age and Gender detection:
Datasets were taken from:

Age and Gender Detection Dataset: https://www.kaggle.com/jangedoo/utkface-new?

Data was Uploaded , Trained , preprocesed and then Evaluated. The accuracy we got was 60-70% for Age Detection . and 80% for Gender detection by this Model.

The Code is under: Age_and_Gender_Prediction.ipynb

## Emotion detection:
Dataset was taken from:

Emotion Detection Dataset: https://www.kaggle.com/shawon10/ckplus

Data was Uploaded , Trained , preprocesed and then Evaluated. The accuracy we got was 100% training accuracy and 100% validation accuracy.
>Note: Whenever a model gives a 100% accuracy on test data, we need to check the training accuracy, if that is also 100%. It means the model is actually overfitting and the test set is having a very close distribution to the train set. So, it is showing great results. I think in these circumstances, it’s better to use cross-validation to get the correct intuition of how the model actually works

The Code is under: Emotion_Detection.ipynb

##Age , Gender and Emotion detection by Deepface

To improve it accuracy wise , what we adopted is DEEPFACE METHOD.
## For Deep Face:
### Dependencies 
For Colab : Deepface.ipynb is uploaded.

If you're working on a Local Machine, install the dependencies from your terminal with -

pip install -r requirements.txt
    - Run
    -Download the Repository.
    -Install the Dependencies in your system through your terminal/cmd using -
    -pip install -r requirements.
    -Open DeepFace.ipynb using any ipynb based console. (Eg- Colab, Jupyter Lab etc)
### For Live Facial Recognition and Verification,
   
 run the following command in your Terminal/cmd - python deep_face.py

### Requirements:
-absl-py==0.9.0
-astunparse==1.6.3
-cachetools==4.1.0
-certifi==2020.4.5.1
-chardet==3.0.4
-click==7.1.2
-cv==1.0.0
-deepface==0.0.24
-filelock==3.0.12
-Flask==1.1.2
-gast==0.3.3
-gdown==3.11.0
-google-auth==1.16.1
-google-auth-oauthlib==0.4.1
-google-pasta==0.2.0
-grpcio==1.29.0
-h5py==2.10.0
-idna==2.9
-itsdangerous==1.1.0
-Jinja2==2.11.2
-Keras==2.3.1
-Keras-Applications==1.0.8
-Keras-Preprocessing==1.1.2
-Markdown==3.2.2
-MarkupSafe==1.1.1
-numpy==1.18.5
-oauthlib==3.1.0
-opencv-python==4.2.0.34
-opt-einsum==3.2.1
-pandas==1.0.4
-Pillow==7.1.2
-protobuf==3.12.2
-pyasn1==0.4.8
-pyasn1-modules==0.2.8
-PySocks==1.7.1
-python-dateutil==2.8.1
-pytz==2020.1
-PyYAML==5.3.1
-requests==2.23.0
-requests-oauthlib==1.3.0
-rsa==4.0
-scipy==1.4.1
-six==1.15.0
-tensorboard==2.2.2
-tensorboard-plugin-wit==1.6.0.post3
-tensorflow==2.2.0
-tensorflow-estimator==2.2.0
-termcolor==1.1.0
-tqdm==4.46.1
-urllib3==1.25.9
-Werkzeug==1.0.1
-wrapt==1.12.1

##People counting code
#Running the program
"python peoplecounter.py -vid Input/1.mp4 -roi manually"
This will take the video 2.mp4 from Input folder and the distinct peoples' images will be stored in the Output_Images folder automatically. The output video, i.e. the video with the detection and counting taking place is saved in Output_Video. You'll have to create the Region of Interest (RoI) manually (by default). The RoI is a thin green rectangle drawn in the first frame which disappears after it is created, and the video is begun retaining only the RoI. However, to minimize repeated efforts for drawing the RoI, you can create it once and test to see if the results are good (preferred to draw a tall RoI which will encompass the entire length of a person; this ensures that different parts of the person recognized do not output as different people). If you have a well created and tested RoI, the program will ask you whether you want to save the RoI for future testing. To use the pre-tested RoIs, just use the argument "pre-tested" instead of "manually" in the command line. Example:

"python peoplecounter.py -vid Input/2.mp4 -roi pre-tested"
#Input Examples
The Input folder has currently 2 video examples, taken from the internet. These videos are very short and only for testing. These videos - 1.mp4 and 2.mp4 have pre-tested RoI text files already created, so you can run the command line with RoI creation argument as "pre-tested", or "manually" if you prefer.

There have been some parameters used throughout the program, such as HOG Descriptor parameters, NMS parameters, Feature Matching and SIFT parameters, which have their values as a result of repeated testing. However, these are not hard and fast parameters, as in they may not be the best parameters for all possible inputs, so the users can change them from within the program.


### References:
https://medium.com/@myac.abhijit/facial-data-based-deep-learning-emotion-age-and-gender-prediction-47f2cc1edda7

License
----

MIT


