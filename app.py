import streamlit as st
import requests
import cv2
import numpy as np
import time
from landingai.postprocess import crop
from landingai.predict import Predictor, OcrPredictor
from landingai import visualize
import landingai.pipeline as pl


st.title('helasdlo world')

video = st.file_uploader('Video Uploader')
if video:
    st.video(video)

    # Replace 'path_to_video_file' with the actual path to your video file
    # 1. iPhone Video to image
    img_src = pl.image_source.VideoFile(video, samples_per_second=1)
    frames = [] 
    for frame in img_src:
        frames.append(frame.frames[0].image)
