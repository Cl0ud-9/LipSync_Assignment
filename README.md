# Lip Sync Video Generator 🤖

Seamlessly sync facial animations with audio using ElevenLabs TTS + Wav2Lip

## 🚀 Quick Start Guide
📋 Prerequisites
- Python 3.8+
- FFmpeg
- ElevenLabs API Key
- Wav2Lip dependencies

## 🛠️ Usage Guide
### Step 1: Generate Audio
Place your script in input/script.txt
Run: `python Elevenlab.py`

Output: audio.wav generated in project root

### Step 2: Prepare Input Files

` Move required files
mv audio.wav Wav2Lip/
mv your_image.jpg Wav2Lip/image.jpg` to Wav2Lip folder

### Step 3: Generate Lip-Synced Video

Paste : `python inference.py --checkpoint_path checkpoints/wav2lip.pth --face image.jpg --audio audio.wav --outfile output_video.mp4` in terminal to generate the output
