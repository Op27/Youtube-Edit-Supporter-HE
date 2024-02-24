# Youtube-Edit-Supporter-HE

## Overview
The Youtube-Edit-Supporter application is designed to enhance the endorsing process of YouTube videos by automating key post-production tasks. This Python-based tool focuses on improving the audio quality of interviews by removing background noise, transcribing spoken text in Hebrew, and translating the transcribed text into English.

<small>Sample: Screenshot from the application showing translated outputs</small>

<img width="473" alt="sample output" src="https://github.com/Op27/Youtube-Edit-Supporter-HE/assets/39921621/debb32b8-883c-42b0-a4f3-13738eb9da66">

<small>Original video source by [the Ask Project](https://www.youtube.com/watch?v=D8jf_PTSY_Y)</small>


## Features
- **Audio Extraction**: Extract audio from MP4 video files.
- **Noise Reduction**: Apply noise reduction techniques to enhance audio clarity.
- **Speech-to-Text**: Transcribe audio content from spoken Hebrew to text.
- **Translation**: Translate the transcribed text into English.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Pip for installing dependencies

### Installation
Clone this repository to your local machine and install the required dependencies:
```bash
git clone https://github.com/Op27/Youtube-Edit-Supporter-HE
```
```bash
cd Youtube-Edit-Supporter
```
```bash
pip install -r requirements.txt
```

### Setup
For detailed setup instructions, refer to [Setup Guide](docs/SetupGuide.md) in the docs directory.

### Usage
To run the application, navigate to the project directory and execute:
```bash
python app.py
```

Place your MP4 video files in the audio_input directory before running the application. For more detailed usage instructions, see [Usage Instructions](docs/UsageInstructions.md).

### License
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.

