#!pip install requests pydub
#!apt-get install ffmpeg

import requests
from pydub import AudioSegment

def generate_audio_with_elevenlabs(script_path, output_audio_path, voice_id, api_key,model_id="eleven_turbo_v2_5", stability=0.6, similarity_boost=0.5):
    """
    Reads text from the given script file and sends a request to the ElevenLabs API to generate speech.
    The generated audio (MP3) is saved to output_audio_path.

    Parameters:
      - script_path: Path to the text file containing your script.
      - output_audio_path: Path where the generated MP3 audio will be saved.
      - voice_id: ElevenLabs voice ID (choose one with an Indian accent).
      - api_key: Your ElevenLabs API key.
      - stability: (Optional) Controls voice stability (default: 0.5).
      - similarity_boost: (Optional) Controls similarity boost (default: 0.5).
    """
    # Read the input text
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    # Set up headers and payload for the API request
    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": model_id,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(output_audio_path, "wb") as out_file:
            out_file.write(response.content)
        print(f"[INFO] Audio saved at: {output_audio_path}")
    else:
        print("Error:", response.status_code, response.text)

def convert_mp3_to_wav(mp3_path, wav_path):
    """
    Converts an MP3 file to WAV format.
    """
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    print(f"[INFO] Converted MP3 to WAV at: {wav_path}")

# Usage Example
if __name__ == "__main__":
    # Adjust the file paths as needed (these assume your files are in /content/ in Colab)
    script_file = "/content/script.txt"         # Your text script
    output_mp3 = "/content/audio.mp3"            # Output audio (MP3) from ElevenLabs
    output_wav = "/content/audio.wav"            # (Optional) Converted WAV file if required by your pipeline

    # Replace with your ElevenLabs credentials and chosen voice ID for an Indian accent.
    voice_id = "Sm1seazb4gs7RSlUVw7c"            # e.g., a voice that sounds Indian (check your ElevenLabs dashboard)
    api_key = "sk_4ac41c7a950b3f40e804334accf8603747457c08f390261d"

    # Generate audio using ElevenLabs
    generate_audio_with_elevenlabs(script_file, output_mp3, voice_id, api_key, model_id="eleven_turbo_v2_5" , stability=0.6, similarity_boost=0.5)

    # Convert the generated MP3 to WAV
    convert_mp3_to_wav(output_mp3, output_wav)
