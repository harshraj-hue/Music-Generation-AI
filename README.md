# AI Music Generation

An AI-based music generation web application that creates music from natural-language text descriptions.

## Objective

The objective of this project is to demonstrate how Artificial Intelligence can be used to generate original audio based on a user's text prompt.

For example, a user can enter:

"Calm relaxing music with soft drums and a peaceful melody"

The application uses Meta's MusicGen model to generate the requested audio.

## Features

- Text-to-music generation
- Simple web interface
- AI-generated audio
- Audio playback in the browser
- Download generated music
- Prompt-based music creation
- Automatic WAV audio generation
- Responsive web interface

## Technologies Used

- Python
- Flask
- PyTorch
- Hugging Face Transformers
- Meta MusicGen
- SciPy
- SoundFile
- HTML
- CSS
- JavaScript

## AI Model

This project uses:

**MusicGen Small**

Model:

`facebook/musicgen-small`

MusicGen is a text-conditioned music generation model developed by Meta.

## Project Structure

```text
Music-Generation-AI/
│
├── generated_music/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── venv/
│
├── app.py
├── generate_music.py
├── requirements.txt
├── README.md
└── .gitignore
## Limitations

- The application requires a large pretrained AI model, so the initial model download can take significant time.
- Music generation can be slow when the application is running on a CPU because generative AI models require considerable computational resources.
- The quality of the generated music depends on the clarity and detail of the user's text prompt.
- The generated music may not always exactly match the user's requested style, instruments, mood, or tempo.
- The current system generates a single audio output for each request.
- The application does not currently provide advanced controls for tempo, duration, key, instruments, or musical structure.
- The current MusicGen model is primarily designed for music generation and does not reliably generate exact user-provided lyrics or complete singing vocals.
- The generated audio is currently saved as a WAV file, which may require more storage space than compressed audio formats.
- The application currently runs locally and has not been deployed as a production service.
- The project does not currently maintain a history or database of previously generated music.
- The system may require a GPU for faster generation when handling larger workloads.
- Generated content can vary between requests because generative AI models can produce different outputs from similar prompts.

## Future Improvements

- Add controls for music duration and generation length.
- Add genre selection such as pop, classical, electronic, jazz, rock, and cinematic.
- Add instrument selection so users can specify instruments such as guitar, piano, drums, violin, or synthesizer.
- Add tempo and mood controls.
- Allow users to generate multiple music variations from the same prompt.
- Add audio waveform visualization for generated music.
- Add a music history feature to store and access previously generated tracks.
- Add user authentication and personalized music libraries.
- Add database support for storing generation details and user preferences.
- Add support for MP3 and other compressed audio formats.
- Add a dedicated lyrics-generation component.
- Integrate a specialized singing or vocal-generation model for generating music with vocals.
- Add multilingual lyric-generation support.
- Add advanced prompt controls for better control over musical structure.
- Add background music and instrumental mode selection.
- Optimize model loading and inference for faster generation.
- Add GPU acceleration support for improved generation speed.
- Deploy the application online so users can access it from different devices.
- Add cloud-based model inference for users who do not have powerful local hardware.
- Add user feedback and rating features to evaluate generated music.
- Add content-safety and copyright-awareness checks for generated outputs.