# Speech to GenAI

## Demo
There is an example for an answer to the audio "NLP research fields.mp3"

![Response example](/docs/response-example.png)

## Components diagram
I've decided to use components diagram to show main modules of the project and some best practices that I've used.

![Components diagram](/docs/speech-to-genai.drawio.png)

## Installation
### Natively
```sh
git clone git@github.com:MksmOrlov/speech-to-genai.git
cd speech-to-genai
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Using Docker
```sh
git clone git@github.com:MksmOrlov/speech-to-genai.git
cd speech-to-genai
docker build -t speech-to-genai .
```

## Configuration
To run this app you need .env configuration file. You can find an example in .env.example.

You need to create gemini api key. Use VPN if your country is not supported by google gemini.

## Run
### Natively
```sh
cd speech-to-genai
uvicorn src.main:app # or python -m src.main
```
### Using Docker
```sh
cd speech-to-genai
docker run --env-file .env -p 8000:8000 speech-to-genai
```
Then open http://localhost:8000/docs and send any audio file with speech. You can find examples in speech-files directory.

## Resources
1. Fast audio recorder https://online-voice-recorder.com/ru/
2. Gemini audio API docs https://ai.google.dev/gemini-api/docs/audio?hl=ru#python_1
3. About diagrams https://www.visual-paradigm.com/guide/uml-unified-modeling-language
4. Markdown cheetsheet https://www.markdownguide.org/basic-syntax/

## Perspectives
1. Dockerize and deploy app
2. Tests
3. Configure what LLM to use
   1. Make an ability to run it local
   2. Use speech-to-text step if needed
4. Make it multi-user and save history
5. Develop user interface
