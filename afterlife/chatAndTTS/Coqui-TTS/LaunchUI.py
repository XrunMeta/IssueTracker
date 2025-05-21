import gradio as gr
import numpy as np
import os
import librosa
import whisper
from TTS.api import TTS

# === Load Models ===
whisper_model = whisper.load_model("base")
tts_model = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

# === Whisper STT Function ===
def transcribe_audio(audio_path):
    if audio_path is None or not os.path.exists(audio_path):
        return "No valid audio file received."
    try:
        audio, sr = librosa.load(audio_path, sr=16000)
    except Exception as e:
        return f"Error loading audio: {e}"
    result = whisper_model.transcribe(audio)
    return result["text"]

# === TTS Function ===
def synthesize_text(text, speaker_idx, noise_scale, length_scale):
    try:
        wav = tts_model.tts(
            text,
            speaker_idx=int(speaker_idx),
            speaker_wav=None,
            style_wav=None,
            language=None,
            speed=length_scale,
            temperature=noise_scale
        )
        return (tts_model.synthesizer.output_sample_rate, np.array(wav, dtype=np.float32))
    except Exception as e:
        return f"TTS generation failed: {e}"

# === Gradio UI ===
with gr.Blocks() as demo:
    gr.Markdown("# 🗣️ Coqui TTS + Whisper STT\nUpload audio to transcribe, or enter text to synthesize using Coqui TTS.")

    with gr.Row():
        input_audio = gr.Audio(source="upload", type="filepath", label="🎧 Audio for Transcription")
        transcribe_btn = gr.Button("🔁 Transcribe Audio → Text")

    transcription_text = gr.Textbox(label="📄 Transcribed or Input Text", lines=6)

    with gr.Row():
        speaker_idx = gr.Number(value=0, label="🧑 Speaker ID (if supported)", precision=0)
        noise_scale = gr.Slider(minimum=0.1, maximum=1.0, value=0.33, label="🎛️ Noise Scale (creativity)")
        length_scale = gr.Slider(minimum=0.5, maximum=2.0, value=1.0, label="⏱️ Length Scale (speed)")

    synth_btn = gr.Button("🧬 Synthesize Speech")
    output_audio = gr.Audio(label="🔊 Synthesized Output")

    transcribe_btn.click(fn=transcribe_audio, inputs=input_audio, outputs=transcription_text)
    synth_btn.click(
        fn=synthesize_text,
        inputs=[transcription_text, speaker_idx, noise_scale, length_scale],
        outputs=output_audio
    )

# === Launch the app ===
demo.launch()
