# Mp3-to-txt
Pick an mp3 file that contains spoken English, transcribes it to a txt file, with no formatting.

Uses the speech_recognition module to listen to the audio and ffmpeg-python module to convert the mp3 file to a wav file.
Will output the wav file and txt file in the same directory as the mp3 file.
It is mostly accurate and does of course rely on the clarity of the audio as well as annunciation of the speaker/s.

It is necessary to run the following commands for the script to work: 
pip install ffmpeg-downloader
ffdl install --add-path

This is necessary for ffmpeg-python library to actually use the ffmpeg binary.

There is a maximum file size limit of the wav file of 10 mb, this quota is imposed by Google.
