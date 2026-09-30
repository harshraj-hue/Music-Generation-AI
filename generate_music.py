import os
import scipy.io.wavfile
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration


MODEL_NAME = "facebook/musicgen-small"
OUTPUT_DIR = "generated_music"

os.makedirs(OUTPUT_DIR, exist_ok=True)


print("Loading MusicGen model...")
processor = AutoProcessor.from_pretrained(MODEL_NAME)
model = MusicgenForConditionalGeneration.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

print(f"Model loaded on: {device}")


def generate_music(prompt, filename="generated_music.wav"):
    """
    Generate music from a text description.
    """

    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt"
    )

    inputs = {key: value.to(device) for key, value in inputs.items()}

    print("Generating music...")

    audio_values = model.generate(
        **inputs,
        do_sample=True,
        guidance_scale=3,
        max_new_tokens=256
    )

    audio = audio_values[0, 0].cpu().numpy()

    sampling_rate = model.config.audio_encoder.sampling_rate

    output_path = os.path.join(OUTPUT_DIR, filename)

    scipy.io.wavfile.write(
        output_path,
        rate=sampling_rate,
        data=audio
    )

    print(f"Music saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    prompt = input("Enter your music description: ")

    generate_music(prompt)