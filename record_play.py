import pyaudio
import wave
import time
import sys

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
def setTimer(seconds):
    global RECORD_SECONDS
    RECORD_SECONDS = seconds


def recordAudio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    global RECORD_SECONDS, WAVE_OUTPUT_FILENAME
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* recording")
    
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
def playAudio():
    CHUNK = 1024
    global WAVE_OUTPUT_FILENAME
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
    p = pyaudio.PyAudio()
   # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    
    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
    
    # start the stream (4)
    stream.start_stream()
    
    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)
    
    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()
    
    # close PyAudio (7)
    p.terminate()