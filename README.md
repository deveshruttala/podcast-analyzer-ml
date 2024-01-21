# Podcast analyzer ML
This repo gives a detailed information about ml implementations in podcast for podcast summarizer, transcription, analysis , translation , removing ads , voice analyzer, short cutting  etc 
<br>
<br> <p  align = "center" >  <img src="analysis readme asset.png" width="600" height = "250" align = "center" /> </p>
<br>

## Documentation 
In this project, i have worked on a podcast summarizer, translator and  transcriptor and voice genre classification. <br>
i have used openai-whisper package to run the summary and the transcription and for the genre classifcation i have implemented the module librosa using the model Naive Bayes in the <a href="https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification?resource=download"> dataset  </a> and other models used for implementation are the Long short-term memory networks (LSTMs) and Convolutional neural networks (CNNs) .  <br>
The notebooks are self explainatory and have implemented the function.
<br> Project made in python 3.10 and completly impleneted in google colab notebooks
<br> <p  align = "center" >  <img src="audio processing asset.jpg" width="600" height = "250" align = "center" /> </p>
<br> <p  align = "center" >  <img src="spectrogram analysis.png" width="600" height = "250" align = "center" /> </p>

<br><br>

#### working:

<br>
Before diving deeper into the processing of audio files, we need to introduce specific terms, that you will encounter at almost every step of our journey from sound data collection to getting ML predictions. It’s worth noting that audio analysis involves working with images rather than listening.

A waveform is a basic visual representation of an audio signal that reflects how an amplitude changes over time. The graph displays the time on the horizontal (X) axis and the amplitude on the vertical (Y) axis but it doesn’t tell us what’s happening to frequencies.

A spectrum or spectral plot is a graph where the X-axis shows the frequency of the sound wave while the Y-axis represents its amplitude. This type of sound data visualization helps you analyze frequency content but misses the time component. A spectrogram is a detailed view of a signal that covers all three characteristics of sound. You can learn about time from the x-axis, frequencies from the y-axis, and amplitude from color. The louder the event the brighter the color, while silence is represented by black. Having three dimensions on one graph is very convenient: it allows you to track how frequencies change over time, examine the sound in all its fullness, and spot various problem areas (like noises) and patterns by sight. A mel spectrogram where mel stands for melody is a type of spectrogram based on the mel scale that describes how people perceive sound characteristics. Our ear can distinguish low frequencies better than high frequencies. You can check it yourself: Try to play tones from 500 to 1000 Hz and then from 10,000 to 10,500 Hz. The former frequency range would seem much broader than the latter, though, in fact, they are the same. The mel spectrogram incorporates this unique feature of human hearing, converting the values in Hertz into the mel scale. This approach is widely used for genre classification, instrument detection in songs, and speech emotion recognition.<br> Feature extraction
Audio features or descriptors are properties of signals, computed from visualizations of preprocessed audio data. They can belong to one of three domains
time domain represented by waveforms,
frequency domain represented by spectrum plots, and
time and frequency domain represented by spectrograms. 
Short-time energy (STE) shows the energy variation within a short speech frame.
<br>
It’s a powerful tool to separate voiced and unvoiced segments.
<br>
Root mean square energy (RMSE) gives you an understanding of the average energy of the signal. It can be computed from a waveform or a spectrogram. In the first case, you’ll get results faster. Yet, a spectrogram provides a more accurate representation of energy over time. RMSE is particularly useful for audio segmentation and music genre classification.
<br>
Zero-crossing Rate (ZCR) counts how many times the signal wave crosses the horizontal axis within a frame. It’s one of the most important acoustic features, widely used to detect the presence or absence of speech, and differentiate noise from silence and music from speech.
Frequency domain features.
One of the most popular groups of time-frequency domain features is mel-frequency cepstral coefficients (MFCCs). They work within the human hearing range and as such are based on the mel scale and mel spectrograms we discussed earlier.

No surprise that the initial application of MFCCs is speech and voice recognition. But they also proved to be effective for music processing and acoustic diagnostics for medical purposes, including snoring detection. For example, one of the recent deep learning models developed by the School of Engineering (Eastern Michigan University) was trained on 1000 MFCC images (spectrograms) of snoring sounds.<br>
<br> Audio analysiss software for ml use: <br>
Tensorflow-io package for preparation and augmentation of audio data lets you perform a wide range of operations — noise removal, converting waveforms to spectrograms, frequency, and time masking to make the sound clearly audible, and more. The tool belongs to the open-source TensorFlow ecosystem, covering end-to-end machine learning workflow. So, after preprocessing you can train an ML model on the same platform.<br>
Librosa is an open-source Python library that has almost everything you need for audio and music analysis. It enables displaying characteristics of audio files, creating all types of audio data visualizations, and extracting features from them, to name just a few capabilities.

<br>

#### Conclusion and credits

In the ever world of ai, audio analysis will become crucial part. this podcast analysis may be a smaller implemetaion of the audio function we can make alot of uses from it later on. <br>
i would like to share my thanks to dataset provider and notebook for me to seek some inspiration form their implementation  

<br>
 

