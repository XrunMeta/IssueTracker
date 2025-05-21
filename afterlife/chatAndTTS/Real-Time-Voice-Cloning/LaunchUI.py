#Editor: Diaz Reza
# This script is a Gradio web interface for the Real-Time Voice Cloning project.

import gradio as gr
import numpy as np
import torch
import sys
import os
from pathlib import Path
import librosa
import whisper
import tempfile
import soundfile as sf

# Add repo modules to path
sys.path.append(".")

from encoder import inference as encoder
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder
from encoder import audio

# Adjusted paths to your saved models
encoder.load_model(Path("saved_models/default/encoder.pt"))
synthesizer = Synthesizer(Path("saved_models/default/synthesizer.pt"))  # Synthesizer accepts path to file
vocoder.load_model(Path("saved_models/default/vocoder.pt"))

# === Load Whisper model (base model) ===
whisper_model = whisper.load_model("base")  # or use "medium"/"large" if needed

# Inference function
def clone_voice(speaker_audio, text_input):
    # Load speaker audio and embed
    original_wav, sampling_rate = librosa.load(speaker_audio, sr=None)
    preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
    embed = encoder.embed_utterance(preprocessed_wav)

    # Generate spectrogram
    specs = synthesizer.synthesize_spectrograms([text_input], [embed])
    spec = specs[0]

    # Generate waveform
    generated_wav = vocoder.infer_waveform(spec)

    # Convert to suitable format for Gradio (np.float32, 16kHz)
    generated_wav = np.pad(generated_wav, (0, 4000), mode="constant")
    return (16000, generated_wav)

# === Whisper STT Function ===
def transcribe_audio(audio_path):
    print(f"[DEBUG] Received audio_path: {audio_path}")  # <--- Add this

    if audio_path is None or not os.path.exists(audio_path):
        return "No valid audio file received."

    try:
        audio, sr = librosa.load(audio_path, sr=16000)
    except Exception as e:
        return f"Error loading audio: {e}"

    result = whisper_model.transcribe(audio)
    return result["text"]



# === Gradio UI ===
with gr.Blocks() as demo:
    gr.Markdown("# 🎙️ Real-Time Voice Cloning + Whisper STT\nUpload a target speaker voice, transcribe the speech to text, and synthesize a cloned voice.")

    with gr.Row():
        stt_audio = gr.Audio(source="upload", type="filepath", label="🗣️ Audio to Transcribe")
        speaker_audio = gr.Audio(source="upload", type="filepath", label="🎤 Target Speaker Audio to Clone")

    with gr.Row():
        text_input = gr.Textbox(label="💬 Text to Synthesize", lines=8)

    with gr.Row():
        transcribe_btn = gr.Button("🔁 Transcribe Audio → Text")
        clone_btn = gr.Button("🧬 Clone Voice")

    cloned_output = gr.Audio(label="🧠 Cloned Output")

    # Actions
    transcribe_btn.click(fn=transcribe_audio, inputs=stt_audio, outputs=text_input)
    clone_btn.click(fn=clone_voice, inputs=[speaker_audio, text_input], outputs=cloned_output)

# === Launch the app ===
demo.launch()
