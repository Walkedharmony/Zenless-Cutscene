# Zenless-Cutscene
Usm demuxer for ZZZ with [Wannacri](https://github.com/donmai-me/WannaCRI) 

Merger between Wannacri for USM and FFMPEG for Merger video and audio

Before using it you must install from [here](https://github.com/donmai-me/WannaCRI/releases/tag/0.3.0) after that do 
`pip install WannaCRI-0.3.0-py3-none-any.whl` check by opening the terminal type wannacri if it is there then you can proceed to **How To Use**

Please note that the USM that can be opened along with its audio is still very small, so far there are only 3 files and I focus on ZenlessZoneZero_Data\StreamingAssets\Video\HD\Procedure

`c030_ep30.usm |
c030_ep40.usm |
c030_ep50.usm`

You can see the key in `Key.json`

**How To Use**

1. Open terminal `python main.py (input sample file c030_ep30.usm) -k (key that you can see in key.json)`

Actually you can find more and use `wannacri extractusm input file --key (17 digits)`

2. Make sure ffmpeg and audio_files.db are in the directory
3. Finally, just wait until the process is complete.
