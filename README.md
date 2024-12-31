# DevPro AI Assistant

## Overview

The **DevPro AI Assistant** is a versatile and beginner-friendly project designed to create a personal voice assistant using Python. This project is ideal for those new to programming and interested in exploring artificial intelligence and speech recognition technologies. Unlike complex systems like Jarvis, this assistant focuses on practical speech recognition functionalities.

The assistant can perform various tasks such as opening applications, searching Google, Wikipedia, and YouTube, and more, all through voice commands. It utilizes the Google Speech Recognition API for voice input and Google Text-to-Speech for voice output.

## Features

- **Voice Commands**: Interact with the assistant using natural language voice commands.
- **Application Control**: Open installed applications on your system.
- **Web Search**: Perform searches on Google, Wikipedia, and YouTube.
- **Customizable**: Easily extend and modify functionalities based on your needs.

## Installation and Setup Guide

Follow these steps to install and run the DevPro AI Assistant on your system:

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/shivamksharma/DevPro-Python-Al-Assistant.git
cd DevPro-Python-Al-Assistant
```

### Step 2: Create a Virtual Environment (Optional)

It is recommended to create a virtual environment to manage dependencies. You can create one using:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Packages

Install the required packages using pip. Make sure you are in the project directory where `requirements.txt` is located:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Microphone Permissions

Ensure that your microphone is set up correctly and that your operating system has granted permission to access it. You may need to adjust settings in your system preferences.

### Step 5: Run the Assistant

You can now run the assistant using the following command:

```bash
python main.py
```

### Step 6: Interact with the Assistant

Once the assistant is running, you can interact with it using voice commands. Here are some example commands you can try:

- "Hey, how are you?"
- "What is your name?"
- "Search for Python programming on Google."
- "What’s the time?"

## Key Libraries Used

- **gTTS**: Google Text-to-Speech for converting text to speech.
- **speech_recognition**: For recognizing voice commands and converting them to text.
- **pyttsx3**: A text-to-speech conversion library that works offline.
- **PyObjC**: A bridge between Python and Objective-C.
- **yfinance**: A Pythonic way to download historical market data from Yahoo! finance.
- **pylint**: A Python static code analysis tool for finding programming errors and enforcing coding standards.
- **playsound**: For playing saved audio files.
- **pyaudio**: For voice engine in Python.

## Troubleshooting

If you encounter any issues, check the following:

- Ensure your microphone is working and properly configured.
- Verify that all required packages are installed without errors.
- Check your internet connection, as some functionalities require online access.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

