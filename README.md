# Zenless-Cutscene
Usm demuxer for ZZZ with [Wannacri](https://github.com/donmai-me/WannaCRI) And thanks for Dimbreath for Keys

Merger between Wannacri for USM and FFMPEG for Merger video and audio

Before using it you must install from [here](https://github.com/donmai-me/WannaCRI/releases/tag/0.3.0) after that do 
`pip install WannaCRI-0.3.0-py3-none-any.whl` check by opening the terminal type wannacri if it is there then you can proceed to **How To Use**

Please note that this is just another alternative for audio because in the original cutscene when demuxing there is no audio extracted and if you find the original way then ignore this Repository, I focus on ZenlessZoneZero_Data\StreamingAssets\Video\HD\Procedure

You can see the key in `Key.json`

**How To Use**

1. Open terminal `python main.py (input sample file c030_ep040.usm) -k (key that you can see in key.json)`

Actually you can find more and use `wannacri extractusm input file --key (17 digits)`

2. Make sure ffmpeg and audio_files.db are in the directory
3. Finally, just wait until the process is complete.

![Screenshot 2024-09-29 215803](https://github.com/user-attachments/assets/7f16644b-859e-4065-8104-b0c78d8c10fb)

