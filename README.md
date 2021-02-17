# Project Name
ONLINE LIVE INTERACTION PROTOTYPE with NVIDIA Jetson

# Overview
Live and entertainment industry has faced difficult time because of COVID-19. So, artists have sterted online live more. Because they can't host live at real site. On real site live, artists and audiences enjoy the live by interaction, for example, call and response. However, online live, artists and audiences can't have any interaction, it makes live feeling some kind of lacks. That's the issue definition of this project. To solve the issue, I aim to develop artists and audiences interaction system. In this project, I propose a system of interaction system that edge device recognizes arm gesture from audience by USB camera and notifys it to cloud server and artists. In this time, we develop prototype of one. In this prototype, edge device recognizes arm gesture from person and plays YouTube video. Edge device is NVIDIA Jetson Nano with DNN model of AI recognizing arm gesture. By this prototype artists and audience interaction system described above can be.

# Prototyping
In this prototype, I'm describing the billboard charted artist [Babymetal](https://en.wikipedia.org/wiki/Babymetal) as online live example. For this project, I pick up the song [Ijime Dame Zettai](https://en.wikipedia.org/wiki/Ijime,_Dame,_Zettai) that has interaction between artists and audiences. The interaction is "During the chorus, the three members jump and cross their arms into an "X", while shouting "Dame!" (No!) with their hands as kitsune signs" that is quoted from [the wikipedia page](https://en.wikipedia.org/wiki/Ijime,_Dame,_Zettai), audiences do as well. It is called "Dame Jump". It makes live heating up! In this prorotype, I make DNN model of AI calassifying "X" arm gesture or not by learning, and deploy it to NVIDIA Jetson Nano to Intefence arm gesture and play the YouTube video [Ijime,Dame,Zettai - Live at Sonisphere 2014,UK (OFFICIAL)](https://www.youtube.com/watch?t=117&v=Ro-_cbfdrYE&feature=youtu.be).

# AI model and Training of Deep Learning
- Base DNN model : Simple MNIST convnet
- Number of training data : Over 200 photos each arm gesture  (X or not)
- Training epoch : 30

I tarined my model by condition above. Examle training data are below.

<img src="Images/ExampleTraining-X.jpg" width="320">
<img src="Images/ExampleTraining-NOT-X.jpg" width="320">

First one is training data for X. Second one is training data for Not-X. I tarained my model on [Google Colab](https://colab.research.google.com/notebooks/) with Keras and TensorFlow running on GPU.