"""
Copyright (c) 2023, DragonSGC
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""
import tkinter as tk
from tkinter import filedialog
import os
import speech_recognition as sr
import ffmpeg

def main():
    root = tk.Tk()
    root.withdraw()

    # get mp3 file to transcribe
    mp3_path = filedialog.askopenfilename()

    if mp3_path:
        # convert mp3 file to wav

        wav_ext = ".wav"
        txt_ext = ".txt"
        directory, filename = os.path.split(mp3_path)

        # Split the filename into base name and extension
        base_name, old_extension = os.path.splitext(filename)

        # Create the new file name with the desired extension
        wav_filename = base_name + wav_ext
        txt_filename = base_name + txt_ext

        # Construct the new filepath by combining the directory path and the new file name
        wav_filepath = os.path.join(directory, wav_filename)

        txt_filepath = os.path.join(directory, txt_filename)

        ffmpeg.input(mp3_path).output(wav_filepath).run()

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(wav_filepath) as source:
            audio = r.record(source)  # read the entire audio file

            text_from_audio = r.recognize_google(audio)

            print("Transcription: " + text_from_audio)

        with open(txt_filepath, "w") as file:
            file.write(text_from_audio)

    else:
        print("No file selected")


if __name__ == '__main__':
    main()


