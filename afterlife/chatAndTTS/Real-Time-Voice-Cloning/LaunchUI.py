#Editor: Diaz Reza
# This script is a Gradio web interface for the Real-Time Voice Cloning project.

import gradio as gr
import numpy as np
import torch
import sys
import os
from pathlib import Path
import librosa

# Add repo modules to path
sys.path.append(".")

from encoder import inference as encoder
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder
from encoder import audio


'''
#  Default Path Load models
encoder.load_model(Path("encoder/saved_models/pretrained.pt"))
synthesizer = Synthesizer(Path("synthesizer/saved_models/logs-pretrained/"))
vocoder.load_model(Path("vocoder/saved_models/pretrained/pretrained.pt"))
'''

# Adjusted paths to your saved models
encoder.load_model(Path("saved_models/default/encoder.pt"))
synthesizer = Synthesizer(Path("saved_models/default/synthesizer.pt"))  # Synthesizer accepts path to file
vocoder.load_model(Path("saved_models/default/vocoder.pt"))

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

# Gradio Interface
gr.Interface(
    fn=clone_voice,
    inputs=[
        gr.Audio(source="upload", type="filepath", label="Upload Speaker Audio"),
        gr.Textbox(lines=2, label="Text to Synthesize")
    ],
    outputs=gr.Audio(label="Cloned Voice Output"),
    title="Real-Time-Voice-Cloning Test",
    description="Upload a short audio of a speaker and type text to hear their cloned voice.\n#XRun_Diaz Reza",
    allow_flagging="never"
).launch()
