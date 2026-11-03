<a id="language"></a>
# Language / Язык

**Choose your language / Выберите язык:**

[![English](https://img.shields.io/badge/Language-English-4F46E5?style=for-the-badge)](#english)
[![Русский](https://img.shields.io/badge/Язык-Русский-EC4899?style=for-the-badge)](#russian)

[![Download](https://img.shields.io/badge/MEGA-Model%20%2F%20Модель-D90007?style=for-the-badge&logo=mega&logoColor=white)](https://mega.nz/file/iGASUTBS#X2mZ0bz34OEL8beSMLSoURGRkxU5PMU6FM19j1YSrWk)

---

<a id="english"></a>
# ✦ Nola — AI VTuber

[![Linux](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![CUDA 12.1](https://img.shields.io/badge/CUDA-12.1-76B900?style=flat-square&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)
[![VTube Studio](https://img.shields.io/badge/VTube%20Studio-API-FF69B4?style=flat-square)](https://denchisoft.com/)
[![XTTS v2](https://img.shields.io/badge/Voice-XTTS%20v2-8B5CF6?style=flat-square)](https://github.com/coqui-ai/TTS)

> A sharp-tongued virtual companion who listens, speaks in her own voice, and comes to life in VTube Studio.

Nola is an experimental Linux project that brings together speech recognition, a language model, voice synthesis, and Live2D animation. She receives audio, transcribes speech with Whisper, generates a reply with an LLM, voices it through XTTS v2, and controls a VTube Studio model through its API.

Russian-language conversation, short replies, a sharp personality, and a love of Roblox and VRChat are part of her character. You can change her personality in the prompt.

[↑ Choose language / Выбрать язык](#language)

---

## Contents

- [Video examples and model](#en-examples)
- [How it works](#en-how-it-works)
- [Requirements](#en-requirements)
- [Installation](#en-installation)
- [Configuration](#en-configuration)
- [Running Nola](#en-running)
- [Project structure](#en-structure)
- [Troubleshooting](#en-troubleshooting)
- [Security](#en-security)

<a id="en-examples"></a>
## ✧ See Nola in action

These examples show someone talking to Nola and the model responding:

[![English example](https://img.shields.io/badge/Watch-English%20example-4F46E5?style=for-the-badge)](assets/EU%20%7C%20Example.mp4)
[![Russian example](https://img.shields.io/badge/Watch-Russian%20example-EC4899?style=for-the-badge)](assets/RU%20%7C%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80.mp4)

[English example (MP4)](assets/EU%20%7C%20Example.mp4) · [Russian example (MP4)](assets/RU%20%7C%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80.mp4)

### Model appearance

The image below shows what the intended model looks like, so it can be distinguished from other models. The image filename uses `KIRU23`; the VTube Studio model filenames supplied with the project are `KITU_RE23.model3.json` and `KITU_RE23.vtube.json`.

![Appearance of the character model](<assets/Character%20KIRU23%20%7C%20HOW%20LOOKS%20MODEL.png>)

[![Download model](https://img.shields.io/badge/MEGA-Download%20Model-D90007?style=for-the-badge&logo=mega&logoColor=white)](https://mega.nz/file/iGASUTBS#X2mZ0bz34OEL8beSMLSoURGRkxU5PMU6FM19j1YSrWk)

> The MP4 buttons link to the video files in `assets/`; whether a video plays inline or opens on a separate page depends on the hosting platform.

<a id="en-how-it-works"></a>
## ✧ How it works

```text
Microphone / system audio
          │
          ▼
  VAD + faster-whisper       speech recognition
          │
          ▼
    DeepInfra / LLM          generation of Nola's reply
          │
          ▼
   AllTalk TTS / XTTS v2     speech synthesis
          │
          ▼
    Audio output + VTube Studio
                      │
                      ▼
                Nola's Live2D model
```

Eye movement, blinking, head movement, and facial expressions are implemented as separate animation modules. They control model parameters through the **VTube Studio Public API**. The modules run concurrently through `asyncio.gather`, while requests to the shared WebSocket are protected by an `asyncio.Lock`.

| Component | Purpose |
|---|---|
| **faster-whisper** | Converts speech to text |
| **VAD** | Detects speech in audio |
| **DeepInfra + LLM** | Generates responses in Nola's character |
| **AllTalk TTS + XTTS v2** | Voices responses |
| **VTube Studio + pyvts** | Controls the Live2D model through the API |

> This is an experimental project: configuration depends on your audio setup, hardware, model, and environment. The names and paths below are based on the project structure provided by the author.

<a id="en-requirements"></a>
## ✧ Requirements

- **Linux x86-64** and **Python 3.11** for the main application.
- An NVIDIA GPU with **at least 12 GB VRAM for the standard setup**, plus a working **CUDA 12.1** setup and compatible driver. Check GPU memory and the driver with `nvidia-smi`. If you have less VRAM, try a smaller Whisper model as described below.
- Access to **VTube Studio** with its Public API enabled. It must be running in a way that makes the API accessible from Linux at `localhost:8001`. If using Wine/Proton, check API connectivity separately.
- The **KITU_RE23** model loaded in VTube Studio: `KITU_RE23.model3.json` and `KITU_RE23.vtube.json` must be present in the installed VTube Studio model.
- **AllTalk TTS** with XTTS v2, located at `VTuber/alltalk_tts/` and accessible at `127.0.0.1:7851`.
- An audio system with available input and output devices. The current configuration names a PulseAudio monitor source.
- A **DeepInfra** API key and internet access to the configured LLM.
- A `requirements.txt` file in the project root. The provided dependency set targets Python 3.11, Linux x86-64, and CUDA 12.1.

> The 12 GB figure is a baseline, not a guarantee: actual memory usage depends on the Whisper model, precision, AllTalk/XTTS, and other GPU workloads. A CUDA-enabled PyTorch build, a compatible driver, and GPU access matter beyond installation: verify that the individual models and services work on your machine. AllTalk's model weights and environment may require additional setup according to its own instructions.

<a id="en-installation"></a>
## ✧ Installation

### 1. Prepare the project

Place the project files in a `VTuber` directory and enter its root:

```bash
cd VTuber
```

Unless stated otherwise, the commands below assume you are in this directory. This matters for relative paths to `token.txt`, `.env`, and other files.

### 2. Create a Python 3.11 environment

**With conda:**

```bash
conda create -n nola python=3.11 pip
conda activate nola
python --version
```

**Or with `venv`, if `python3.11` is already installed:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python --version
```

Make sure the command reports `Python 3.11.x`. Do not install this dependency set into a Python 3.14 environment: the specified PyTorch build will not be found for it.

### 3. Install system dependencies and Python packages

On **Arch Linux**:

```bash
sudo pacman -S --needed base-devel portaudio linux-api-headers
```

`portaudio` is needed, among other things, to build PyAudio. On other distributions, install the equivalent compiler, Linux headers, and PortAudio development packages using your package manager.

Then, from the `VTuber` root with your Python 3.11 environment active:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

Installation may take some time and several gigabytes of free space: the list includes PyTorch and NVIDIA libraries. The `requirements.txt` file specifies the additional PyTorch index for the `+cu121` build.

> Dependency resolution was checked with `pip install --dry-run` on Python 3.11. This checks package resolution; it does not guarantee that every component will build or run on every machine.

### 4. Prepare AllTalk TTS

Make sure AllTalk is located at `VTuber/alltalk_tts/`, has been configured according to its own instructions, and has XTTS v2 and the desired voice available. AllTalk's setup and dependencies may be separate from the main application's environment.

<a id="en-configuration"></a>
## ✧ Configuration

### 1. DeepInfra API key

Create a `.env` file in the `VTuber` root and add your key:

```dotenv
KEY_FOR_LLM=your_DeepInfra_key
```

In `llm/llm_config.py`, the key is loaded with `python-dotenv` and used in the `Authorization` header. Do not publish `.env` or share its contents.

Current model endpoint:

```python
llm_url_api = "https://api.deepinfra.com/v1/inference/NousResearch/Hermes-3-Llama-3.1-405B"
```

To use another model, change `llm_url_api` in `llm/llm_config.py`. Model availability, request formats, and usage conditions depend on DeepInfra; changing the model may also require adapting the request code.

### 2. VTube Studio token

[![Download model from MEGA](https://img.shields.io/badge/MEGA-Download%20Model-D90007?style=for-the-badge&logo=mega&logoColor=white)](https://mega.nz/file/iGASUTBS#X2mZ0bz34OEL8beSMLSoURGRkxU5PMU6FM19j1YSrWk)

Enable the **Public API** in VTube Studio and load the `KITU_RE23` model. In the provided configuration, the application connects to:

```text
localhost:8001
```

#### Where to enable the API

In VTube Studio, open the settings and enable the Public API as shown below. Then keep VTube Studio running and approve the plugin's request when prompted.

![VTube Studio settings showing how to enable the API](<assets/VTS%20%7C%20HOW%20TO%20ON%20API.png>)


Create `token.txt` in the `VTuber` root:

```bash
touch token.txt
```

If you already have a suitable token for this plugin, put **only the token itself** in the file—without labels, quotation marks, or extra characters. If the file or token is missing, the shown `pyvts` code requests a token from VTube Studio and saves it to `./token.txt`. On the first connection, approve plugin access by clicking **Allow** in VTube Studio.

The file is also created in advance because the shown `llm/llm_config.py` reads `token.txt` at import time. This is **not your DeepInfra key**: the LLM key is configured separately in `.env`.

Connection and plugin settings are in `vts_model/api_parameters.py`:

```python
PLUGIN_INFO = {
    'plugin_name': 'move',
    'developer': 'Evis',
    'requests_token': True,
    'authentication_token_path': './token.txt'
}

VTS_API_INFO = {
    'host': 'localhost',
    'port': 8001,
    'version': '1.0',
    'name': 'VTubeStudioPublicAPI'
}
```

If VTube Studio uses another address or port, change `host` and `port`. The path `./token.txt` depends on the **current working directory**, so run `main.py` from the project root.

### 3. Audio source and Whisper

The main settings are in `whisper_stt/whisper_config.py`:

```python
samplerate = 16000
chunk_sec = 2
whisper_language = 'ru'
when_silence_sec_limit = 2

get_microphone_id = 'alsa_output.usb-Logitech_G733_Gaming_Headset_0000000000000000-00.analog-stereo.monitor'
```

| Setting | Meaning |
|---|---|
| `samplerate` | Audio sample rate, currently 16,000 Hz |
| `chunk_sec` | Audio chunk size in seconds |
| `whisper_language` | Recognition language, currently Russian (`ru`) |
| `when_silence_sec_limit` | Silence threshold, currently 2 seconds |
| `get_microphone_id` | Audio source name in the current configuration |

The example device name refers to a specific headset. Replace it with a source available on your system. A `.monitor` suffix usually denotes an **output-device monitor**: it captures system playback, not necessarily your microphone.

To list PulseAudio sources, or those exposed by a compatible PipeWire server:

```bash
pactl list short sources
```

Copy the appropriate source name into `get_microphone_id`. If you choose an output monitor, make sure Nola's own voice is not fed back into recognition and creating an audio loop.

#### Less than 12 GB VRAM: choose a smaller Whisper model

If the standard setup runs out of GPU memory, change the faster-whisper model to `tiny`, `small`, `medium`, or `large-v3-turbo` (also available as `turbo`). Start with `tiny` or `small` when memory is tight; `medium` and `large-v3-turbo` need more memory and are not guaranteed to fit. Smaller models generally trade recognition accuracy for lower resource usage.

Look for the existing `WhisperModel(...)` initialization, starting with `whisper_stt/whisper_model.py`, and change its model name while preserving the other settings used by the project:

```bash
grep -R -n 'WhisperModel' whisper_stt/
```

For example, if the current call passes a model name as its first argument, replace that argument with `"small"`. The provided configuration excerpt does not show the actual initialization, so verify the existing code before editing. Restart the application and check memory usage with `nvidia-smi`.

Whisper is not the only GPU consumer: XTTS/AllTalk and other applications can also occupy VRAM. A smaller Whisper model alone does not guarantee the full pipeline will fit; if needed, reduce other GPU workloads or configure a supported component to run on CPU.

### 4. Nola's personality and responses

The prompt and conversation history are in `llm/llm_config.py`:

```python
llm_prompt = '''
Тебя зовут Нола. Ты — дерзкая девочка с острым языком и колким юмором...
'''

llm_history = [
    {"role": "system", "content": llm_prompt}
]
```

Change `llm_prompt` to adjust the character's personality, manner of speaking, and interests. The shown code sends the conversation history over HTTP with a streamed response (`stream=True`); the generation limit is controlled by `max_new_tokens` in `llm_response`.

### 5. Voice and AllTalk TTS

TTS settings are in `tts/config_tts.py`:

```python
alltalktts_url = 'http://127.0.0.1:7851'
cable_name = 'pulse'

tts_language = 'ru'
tts_character_voice = 'VO_Ganyu_About_the_Vision.wav'
```

| Setting | What it controls |
|---|---|
| `alltalktts_url` | Address of the running AllTalk service |
| `cable_name` | Audio device/backend name used in the project configuration |
| `tts_language` | Synthesis language, currently `ru` |
| `tts_character_voice` | Filename of the reference voice WAV |

Make sure the selected WAV file is available to AllTalk where the service expects voice files. The exact location depends on the AllTalk installation and configuration. For voice cloning, use a recording you have permission to use.

### 6. Model animation

Animation settings are in their respective folders inside `vts_model/`, for example `config_blink.py`, `config_eye_x.py`, `config_move_head_x.py`, and `config_mouth.py`.

The provided `vts_model/move.py` sends the following VTube Studio parameters:

| Animation | Parameters |
|---|---|
| Blinking | `EyeOpenLeft`, `EyeOpenRight` |
| Horizontal gaze | `EyeRightX`, `EyeLeftX` |
| Vertical gaze | `EyeRightY`, `EyeLeftY` |
| Head rotation | `FaceAngleX`, `FaceAngleY`, `FaceAngleZ` |
| Smile / mouth position | `MouthSmile` |
| Cheek puff | `CheekPuff` |

The model must support the parameters being used and suitable value ranges. If you replace the model, you may need to configure parameters in VTube Studio and change IDs or ranges in the animation code.

<a id="en-running"></a>
## ✧ Running Nola

### Step 1. Start VTube Studio

1. Open VTube Studio and load the **KITU_RE23** model.
2. Enable the Public API and check the address and port in `vts_model/api_parameters.py`.
3. Leave the application running. The first time Nola connects, allow access for the plugin.

### Step 2. Start AllTalk TTS

In a separate terminal:

```bash
cd VTuber/alltalk_tts
bash start_alltalk.sh
```

Wait until AllTalk is ready. In the current configuration, the main project connects to the service at `http://127.0.0.1:7851`. Leave this terminal running.

### Step 3. Start Nola

In another terminal, go to the project root and activate your Python 3.11 environment:

```bash
cd VTuber
conda activate nola
# or: source .venv/bin/activate

python --version
python main.py
```

If VTube Studio asks for permission, click **Allow**. Once started, check the audio source, speech recognition, LLM response, voice output, and model movement.

To stop the main application, normally press `Ctrl+C` in its terminal. Stop AllTalk separately in the terminal where it is running.

<a id="en-structure"></a>
## ✧ Project structure

```text
VTuber/
├── main.py                     # Main application entry point
├── requirements.txt            # Project Python dependencies
├── token.txt                   # Local VTube Studio token; do not publish
├── assets/                     # Model images and demonstration videos
│   ├── Character KIRU23 | HOW LOOKS MODEL.png
│   ├── EU | Example.mp4
│   ├── RU | Пример.mp4
│   └── VTS | HOW TO ON API.png
├── alltalk_tts/                # AllTalk TTS
├── whisper_stt/                # Audio capture and speech recognition
│   ├── whisper_config.py       # Device, language, and audio settings
│   ├── whisper_model.py
│   ├── vad_model.py
│   ├── transcribition.py
│   ├── microphone_detector.py
│   ├── speakers_detector.py
│   └── main_rt_whisper.py
├── llm/                        # LLM response logic and configuration
├── .env                        # Local DeepInfra key; do not publish
│   ├── llm_config.py           # Key, endpoint, prompt, and history
│   ├── llm_answer.py
│   └── llm_main.py
├── tts/                        # AllTalk TTS integration
│   ├── config_tts.py           # Address, language, voice, audio backend
│   ├── tts_logic.py
│   ├── tts_response.py
│   └── main_tts.py
└── vts_model/                  # VTube Studio connection and animation
    ├── api_parameters.py       # API address and plugin settings
    ├── authentication.py       # Connection and authentication
    ├── shared.py               # WebSocket lock
    ├── send.py                 # Send parameters to VTube Studio
    ├── move.py                 # Model parameter control functions
    ├── vts_main.py             # Concurrent animation startup
    ├── blink_eye_animation/
    ├── move_eyes_x_animation/
    ├── move_eyes_y_animation/
    ├── move_head_x_animation/
    ├── move_head_y_animation/
    ├── move_head_z_animation/
    ├── mouth_smiling_for_tts/
    ├── mouth_puff/
    └── mouth_sadding_logic/
```

This tree shows the main files and directories; tests and some helper modules are omitted for brevity. The presence of an animation directory does not by itself mean the animation is started by `vts_main.py`: the actual list is determined by the calls in `asyncio.gather`.

<a id="en-troubleshooting"></a>
## ✧ Troubleshooting

### `No matching distribution found for torch==2.5.1+cu121`

Check the Python version, environment, and start of the requirements file:

```bash
python --version
python -m pip --version
head -5 requirements.txt
```

The prepared file requires Python 3.11 and access to the additional index `https://download.pytorch.org/whl/cu121`. Use `python -m pip` to avoid accidentally invoking `pip` from a different environment.

### PyAudio build fails or `portaudio.h` is missing

On Arch Linux, install the system dependencies and retry:

```bash
sudo pacman -S --needed base-devel portaudio linux-api-headers
python -m pip install -r requirements.txt
```

### Cannot connect to VTube Studio

- Check that VTube Studio is running, the model is loaded, and the Public API is enabled.
- Compare the address and port with `vts_model/api_parameters.py`.
- Approve plugin access in VTube Studio.
- If VTube Studio runs under Wine/Proton or on another machine, check API network connectivity separately. `localhost` refers to the application's current network context.
- If the token is invalid or revoked, rename the old `token.txt`, create an empty file, and authorize again. Do not delete a token needed by another application.

### Whisper cannot hear anything

- Run `pactl list short sources` and check `get_microphone_id`.
- Make sure you selected the intended microphone or output monitor.
- Check the input level and the application's access to the audio device.
- When capturing system audio, check for a feedback loop involving Nola's voice.

### The LLM does not respond

- Check that `KEY_FOR_LLM` is present in `.env`, without publishing the key itself.
- Make sure you start the application from the project root and can reach DeepInfra.
- Check the model's availability, the key's permissions, and API error messages.
- In the shown `async def llm_response`, `requests` is synchronous: this can block the event loop and affect latency. An optimization would be to move the request to a thread or use an asynchronous HTTP client.

### No voice output

- Check that AllTalk is running and accessible at the address in `alltalktts_url`.
- Check the WAV filename, XTTS v2 settings, and AllTalk messages.
- Check the audio backend and device configured through `cable_name`.

### The model does not move or moves incorrectly

- Make sure the correct model is loaded and the plugin is authorized.
- Compare the model's parameter IDs and ranges with `vts_model/move.py` and the animation configuration.
- Check application and VTube Studio messages: a successful connection does not guarantee that every model parameter is accepted.

<a id="en-security"></a>
## ✧ Security

Do not add secrets or local environments to a public repository. Minimal `.gitignore` rules:

```gitignore
.env
.venv/
token.txt
```

A `token.txt` rule without a leading `/` also excludes identically named files in nested directories. If a secret has already been published, revoke or replace it: adding a file to `.gitignore` does not remove it from Git history.

---

**Nola** · Voice, character, and Live2D in one experimental pipeline.

[↑ Choose language / Выбрать язык](#language)

---

<a id="russian"></a>
# ✦ Нола — AI VTuber

[![Linux](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![CUDA 12.1](https://img.shields.io/badge/CUDA-12.1-76B900?style=flat-square&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)
[![VTube Studio](https://img.shields.io/badge/VTube%20Studio-API-FF69B4?style=flat-square)](https://denchisoft.com/)
[![XTTS v2](https://img.shields.io/badge/Voice-XTTS%20v2-8B5CF6?style=flat-square)](https://github.com/coqui-ai/TTS)

> Дерзкая виртуальная собеседница, которая слушает, отвечает своим голосом и оживает в VTube Studio.

Нола — экспериментальный Linux-проект, объединяющий распознавание речи, языковую модель, синтез голоса и анимацию Live2D-персонажа. Она получает звук, превращает речь в текст с помощью Whisper, формирует ответ через LLM, озвучивает его через XTTS v2 и управляет моделью в VTube Studio через API.

Русский язык, короткие реплики, острый характер и любовь к Roblox и VRChat — часть её образа. Характер можно изменить в промпте.

[↑ Choose language / Выбрать язык](#language)

---

## Содержание

- [Примеры и модель](#ru-examples)
- [Как устроен проект](#ru-how-it-works)
- [Что понадобится](#ru-requirements)
- [Установка](#ru-installation)
- [Настройка](#ru-configuration)
- [Запуск](#ru-running)
- [Структура проекта](#ru-structure)
- [Решение проблем](#ru-troubleshooting)
- [Безопасность](#ru-security)

<a id="ru-examples"></a>
## ✧ Нола в действии

В примерах с Нолой разговаривают, а модель отвечает собеседнику:

[![Пример на русском](https://img.shields.io/badge/Смотреть-Пример%20на%20русском-EC4899?style=for-the-badge)](assets/RU%20%7C%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80.mp4)
[![English example](https://img.shields.io/badge/Watch-English%20example-4F46E5?style=for-the-badge)](assets/EU%20%7C%20Example.mp4)

[Пример на русском (MP4)](assets/RU%20%7C%20%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80.mp4) · [Пример на английском (MP4)](assets/EU%20%7C%20Example.mp4)

### Как выглядит модель

На изображении показана нужная модель, чтобы её не перепутать с другими. В названии изображения указано `KIRU23`, а предоставленные имена файлов модели VTube Studio — `KITU_RE23.model3.json` и `KITU_RE23.vtube.json`.

![Внешний вид модели персонажа](<assets/Character%20KIRU23%20%7C%20HOW%20LOOKS%20MODEL.png>)

[![Скачать модель](https://img.shields.io/badge/MEGA-Скачать%20модель-D90007?style=for-the-badge&logo=mega&logoColor=white)](https://mega.nz/file/iGASUTBS#X2mZ0bz34OEL8beSMLSoURGRkxU5PMU6FM19j1YSrWk)

> Кнопки MP4 ведут к видеофайлам в `assets/`; воспроизведение прямо на странице или открытие на отдельной странице зависит от платформы.

<a id="ru-how-it-works"></a>
## ✧ Как устроен проект

```text
Микрофон / системный звук
          │
          ▼
  VAD + faster-whisper       распознавание речи
          │
          ▼
    DeepInfra / LLM          генерация ответа Нолы
          │
          ▼
   AllTalk TTS / XTTS v2     синтез речи
          │
          ▼
    Аудиовывод + VTube Studio
                      │
                      ▼
             Live2D-модель Нолы
```

Движения глаз, моргание, движения головы и выражения лица реализованы отдельными анимационными модулями. Они управляют параметрами модели через **VTube Studio Public API**. Модули работают параллельно через `asyncio.gather`, а отправка запросов к общему WebSocket защищена блокировкой `asyncio.Lock`.

| Компонент | Назначение |
|---|---|
| **faster-whisper** | Распознавание речи в текст |
| **VAD** | Определение наличия речи в аудио |
| **DeepInfra + LLM** | Генерация ответов с характером Нолы |
| **AllTalk TTS + XTTS v2** | Озвучивание ответов |
| **VTube Studio + pyvts** | Управление Live2D-моделью по API |

> Проект экспериментальный: конфигурация зависит от вашей звуковой системы, устройства, модели и окружения. Названия и пути ниже приведены по предоставленной структуре проекта.

<a id="ru-requirements"></a>
## ✧ Что понадобится

- **Linux x86-64** и **Python 3.11** для основного приложения.
- Видеокарта NVIDIA с **минимум 12 ГБ VRAM для штатной конфигурации**, работающая **CUDA 12.1** и совместимый драйвер. Проверить видеопамять и драйвер можно командой `nvidia-smi`. Если VRAM меньше, попробуйте уменьшить модель Whisper, как описано ниже.
- Доступ к **VTube Studio** с включённым Public API. Приложение должно быть запущено так, чтобы из Linux был доступен его API на `localhost:8001`. При использовании Wine/Proton проверьте доступность API отдельно.
- Загруженная в VTube Studio модель **KITU_RE23**: файлы `KITU_RE23.model3.json` и `KITU_RE23.vtube.json` должны находиться в установленной модели VTube Studio.
- **AllTalk TTS** с XTTS v2, расположенный в `VTuber/alltalk_tts/` и доступный на `127.0.0.1:7851`.
- Аудиосистема с доступным устройством захвата и вывода. В текущей конфигурации указан источник-монитор PulseAudio.
- Ключ **DeepInfra** и доступ к настроенной LLM через интернет.
- Файл `requirements.txt` в корне проекта. Готовый вариант зависимостей в этом репозитории рассчитан на Python 3.11, Linux x86-64 и CUDA 12.1.

> 12 ГБ — ориентир для штатной конфигурации, а не гарантия: фактический расход зависит от модели Whisper, точности, AllTalk/XTTS и других задач на GPU. CUDA-сборка PyTorch, совместимый драйвер и доступность GPU нужны не только при установке: работу конкретных моделей и сервисов также необходимо проверить на своей машине. Установка весов и окружения AllTalk может требовать дополнительных шагов самого AllTalk.

<a id="ru-installation"></a>
## ✧ Установка

### 1. Подготовьте проект

Поместите файлы проекта в каталог `VTuber` и перейдите в его корень:

```bash
cd VTuber
```

Все команды ниже предполагают, что вы находитесь именно в этом каталоге, если не указано иное. Это важно для относительных путей к `token.txt`, `.env` и другим файлам.

### 2. Создайте окружение Python 3.11

**Вариант с conda:**

```bash
conda create -n nola python=3.11 pip
conda activate nola
python --version
```

**Или через `venv`, если `python3.11` уже установлен:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python --version
```

Убедитесь, что команда выводит `Python 3.11.x`. Не устанавливайте этот набор зависимостей в окружение с Python 3.14: для указанной версии PyTorch нужная сборка не находится.

### 3. Установите системные зависимости и Python-пакеты

Для **Arch Linux**:

```bash
sudo pacman -S --needed base-devel portaudio linux-api-headers
```

`portaudio` нужен, в частности, для сборки PyAudio. В других дистрибутивах установите аналогичные пакеты компилятора, заголовков Linux и разработки PortAudio через свой менеджер пакетов.

Затем, находясь в корне `VTuber` с активированным окружением Python 3.11:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

Установка может занять время и потребовать несколько гигабайт свободного места: список включает PyTorch и библиотеки NVIDIA. В `requirements.txt` указан дополнительный индекс PyTorch для версии `+cu121`.

> Подбор зависимостей проверен с помощью `pip install --dry-run` на Python 3.11. Это проверка разрешения пакетов, а не гарантия успешной сборки всех компонентов и работы приложения на любом оборудовании.

### 4. Подготовьте AllTalk TTS

Проверьте, что AllTalk находится в `VTuber/alltalk_tts/`, настроен по собственной инструкции и в нём доступны XTTS v2 и нужный голос. Настройка и зависимости самого AllTalk могут быть отдельными от окружения основного приложения.

<a id="ru-configuration"></a>
## ✧ Настройка

### 1. Ключ DeepInfra

Создайте в корне `VTuber` файл `.env` и добавьте ключ:

```dotenv
KEY_FOR_LLM=ваш_ключ_DeepInfra
```

В `llm/llm_config.py` ключ загружается через `python-dotenv` и используется в заголовке `Authorization`. Не публикуйте `.env` и не отправляйте его содержимое другим людям.

Текущий адрес модели:

```python
llm_url_api = "https://api.deepinfra.com/v1/inference/NousResearch/Hermes-3-Llama-3.1-405B"
```

Для смены модели измените `llm_url_api` в `llm/llm_config.py`. Доступность модели, формат запроса и условия использования зависят от DeepInfra; при смене модели может потребоваться адаптировать код запроса.

### 2. Токен VTube Studio

[![Download model from MEGA](https://img.shields.io/badge/MEGA-Download%20Model-D90007?style=for-the-badge&logo=mega&logoColor=white)](https://mega.nz/file/iGASUTBS#X2mZ0bz34OEL8beSMLSoURGRkxU5PMU6FM19j1YSrWk)

Включите **Public API** в настройках VTube Studio и загрузите модель `KITU_RE23`. В предоставленной конфигурации приложение подключается к:

```text
localhost:8001
```

#### Где включить API

Откройте настройки VTube Studio и включите Public API, как показано на изображении. Затем оставьте VTube Studio запущенным и подтвердите запрос плагина, когда он появится.

![Настройки VTube Studio: как включить API](<assets/VTS%20%7C%20HOW%20TO%20ON%20API.png>)


В корне `VTuber` создайте файл `token.txt`:

```bash
touch token.txt
```

Если у вас уже есть подходящий токен для этого плагина, поместите в файл **только сам токен** — без подписей, кавычек и лишних символов. Если файла или токена нет, показанный код `pyvts` запрашивает токен у VTube Studio и сохраняет его по пути `./token.txt`. При первом подключении подтвердите доступ плагина кнопкой **Allow / Разрешить** в VTube Studio.

Файл создаётся заранее ещё и потому, что в показанном `llm/llm_config.py` есть чтение `token.txt` при импорте. Это **не ключ DeepInfra**: ключ LLM задаётся отдельно в `.env`.

Настройки подключения и плагина находятся в `vts_model/api_parameters.py`:

```python
PLUGIN_INFO = {
    'plugin_name': 'move',
    'developer': 'Evis',
    'requests_token': True,
    'authentication_token_path': './token.txt'
}

VTS_API_INFO = {
    'host': 'localhost',
    'port': 8001,
    'version': '1.0',
    'name': 'VTubeStudioPublicAPI'
}
```

Если VTube Studio использует другой адрес или порт, измените `host` и `port`. Путь `./token.txt` зависит от **текущего рабочего каталога**, поэтому запускайте `main.py` из корня проекта.

### 3. Источник звука и Whisper

Основные настройки находятся в `whisper_stt/whisper_config.py`:

```python
samplerate = 16000
chunk_sec = 2
whisper_language = 'ru'
when_silence_sec_limit = 2

get_microphone_id = 'alsa_output.usb-Logitech_G733_Gaming_Headset_0000000000000000-00.analog-stereo.monitor'
```

| Параметр | Значение |
|---|---|
| `samplerate` | Частота дискретизации аудио, сейчас 16 000 Гц |
| `chunk_sec` | Размер аудиофрагмента в секундах |
| `whisper_language` | Язык распознавания, сейчас русский (`ru`) |
| `when_silence_sec_limit` | Порог тишины, сейчас 2 секунды |
| `get_microphone_id` | Имя источника звука в текущей конфигурации |

Имя устройства в примере привязано к конкретной гарнитуре. Замените его на источник своей системы. Суффикс `.monitor` обычно обозначает монитор **выходного** устройства: он захватывает воспроизводимый системный звук, а не обязательно микрофон.

Для просмотра источников PulseAudio или совместимого сервера PipeWire можно использовать:

```bash
pactl list short sources
```

Скопируйте подходящее имя источника в `get_microphone_id`. Если выбран монитор выхода, следите за тем, чтобы собственный голос Нолы не попадал обратно в распознавание и не создавал звуковую петлю.

#### Если VRAM меньше 12 ГБ: смените модель Whisper

Если штатная конфигурация не помещается в видеопамять, выберите для faster-whisper модель `tiny`, `small`, `medium` или `large-v3-turbo` (также доступна как `turbo`). При сильной нехватке памяти начните с `tiny` или `small`: `medium` и `large-v3-turbo` требуют больше памяти и могут не поместиться. Модели меньшего размера обычно экономят ресурсы ценой качества распознавания.

Найдите существующее создание `WhisperModel(...)`, начав с `whisper_stt/whisper_model.py`, и замените название модели, сохранив остальные настройки проекта:

```bash
grep -R -n 'WhisperModel' whisper_stt/
```

Например, если название модели передаётся первым аргументом, замените его на `"small"`. В предоставленном фрагменте конфигурации само создание модели не показано, поэтому перед изменением проверьте существующий код. Перезапустите приложение и проверьте использование памяти через `nvidia-smi`.

Whisper — не единственный потребитель видеопамяти: XTTS/AllTalk и другие приложения тоже могут занимать VRAM. Уменьшение Whisper само по себе не гарантирует, что весь пайплайн поместится; при необходимости уменьшите другую нагрузку на GPU или настройте поддерживаемый компонент для работы на CPU.

### 4. Характер и ответы Нолы

Промпт и история диалога находятся в `llm/llm_config.py`:

```python
llm_prompt = '''
Тебя зовут Нола. Ты — дерзкая девочка с острым языком и колким юмором...
'''

llm_history = [
    {"role": "system", "content": llm_prompt}
]
```

Меняйте `llm_prompt`, чтобы настроить характер, манеру речи и интересы персонажа. Показанный код отправляет историю через HTTP с потоковым ответом (`stream=True`); лимит генерации задаётся параметром `max_new_tokens` в `llm_response`.

### 5. Голос и AllTalk TTS

Настройки TTS находятся в `tts/config_tts.py`:

```python
alltalktts_url = 'http://127.0.0.1:7851'
cable_name = 'pulse'

tts_language = 'ru'
tts_character_voice = 'VO_Ganyu_About_the_Vision.wav'
```

| Параметр | Что настраивает |
|---|---|
| `alltalktts_url` | Адрес запущенного сервиса AllTalk |
| `cable_name` | Используемое имя аудиоустройства/бэкенда в конфигурации проекта |
| `tts_language` | Язык синтеза, сейчас `ru` |
| `tts_character_voice` | Имя WAV-файла с референсом голоса |

Убедитесь, что выбранный WAV-файл доступен AllTalk в том месте, где сервис ожидает голоса. Точный путь зависит от установки и конфигурации AllTalk. Для клонирования голоса используйте запись, на которую у вас есть разрешение.

### 6. Анимация модели

Настройки анимаций расположены в соответствующих папках внутри `vts_model/`: например, `config_blink.py`, `config_eye_x.py`, `config_move_head_x.py` и `config_mouth.py`.

В предоставленном `vts_model/move.py` отправляются следующие параметры VTube Studio:

| Анимация | Параметры |
|---|---|
| Моргание | `EyeOpenLeft`, `EyeOpenRight` |
| Взгляд по X | `EyeRightX`, `EyeLeftX` |
| Взгляд по Y | `EyeRightY`, `EyeLeftY` |
| Поворот головы | `FaceAngleX`, `FaceAngleY`, `FaceAngleZ` |
| Улыбка / положение рта | `MouthSmile` |
| Надувание щёк | `CheekPuff` |

Модель должна поддерживать используемые параметры и подходящие диапазоны значений. При замене модели может потребоваться настроить параметры в VTube Studio и изменить ID или диапазоны в коде анимаций.

<a id="ru-running"></a>
## ✧ Запуск

### Шаг 1. Запустите VTube Studio

1. Откройте VTube Studio и загрузите модель **KITU_RE23**.
2. Включите Public API и проверьте адрес и порт, заданные в `vts_model/api_parameters.py`.
3. Оставьте приложение запущенным. При первом подключении Нолы разрешите доступ плагина.

### Шаг 2. Запустите AllTalk TTS

В отдельном терминале:

```bash
cd VTuber/alltalk_tts
bash start_alltalk.sh
```

Дождитесь готовности AllTalk. По текущей конфигурации основной проект обращается к сервису по адресу `http://127.0.0.1:7851`. Оставьте этот терминал работающим.

### Шаг 3. Запустите Нолу

В другом терминале перейдите в корень проекта и активируйте своё окружение Python 3.11:

```bash
cd VTuber
conda activate nola
# или: source .venv/bin/activate

python --version
python main.py
```

Если появится запрос VTube Studio, нажмите **Allow / Разрешить**. После запуска проверьте источник звука, распознавание речи, ответ LLM, озвучивание и движение модели.

Для остановки основного приложения обычно используется `Ctrl+C` в его терминале. AllTalk останавливается отдельно, в терминале, где он запущен.

<a id="ru-structure"></a>
## ✧ Структура проекта

```text
VTuber/
├── main.py                     # Точка запуска основного приложения
├── requirements.txt            # Python-зависимости проекта
├── token.txt                   # Локальный токен VTube Studio; не публиковать
├── assets/                     # Model images and demonstration videos
│   ├── Character KIRU23 | HOW LOOKS MODEL.png
│   ├── EU | Example.mp4
│   ├── RU | Пример.mp4
│   └── VTS | HOW TO ON API.png
├── alltalk_tts/                # AllTalk TTS
├── whisper_stt/                # Захват и распознавание речи
│   ├── whisper_config.py       # Устройство, язык и параметры аудио
│   ├── whisper_model.py
│   ├── vad_model.py
│   ├── transcribition.py
│   ├── microphone_detector.py
│   ├── speakers_detector.py
│   └── main_rt_whisper.py
├── llm/                        # Логика ответов и настройки LLM
├── .env                        # Локальный ключ DeepInfra; не показывать(дажжжж знакомым)
│   ├── llm_config.py           # Ключ, endpoint, промпт и история
│   ├── llm_answer.py
│   └── llm_main.py
├── tts/                        # Интеграция с AllTalk TTS
│   ├── config_tts.py           # Адрес, язык, голос и аудиобэкенд
│   ├── tts_logic.py
│   ├── tts_response.py
│   └── main_tts.py
└── vts_model/                  # Подключение и анимация в VTube Studio
    ├── api_parameters.py       # Адрес API и настройки плагина
    ├── authentication.py       # Подключение и авторизация
    ├── shared.py               # Блокировка WebSocket
    ├── send.py                 # Отправка параметров в VTube Studio
    ├── move.py                 # Функции управления параметрами модели
    ├── vts_main.py             # Параллельный запуск анимаций
    ├── blink_eye_animation/
    ├── move_eyes_x_animation/
    ├── move_eyes_y_animation/
    ├── move_head_x_animation/
    ├── move_head_y_animation/
    ├── move_head_z_animation/
    ├── mouth_smiling_for_tts/
    ├── mouth_puff/
    └── mouth_sadding_logic/
```

В дереве показаны основные файлы и каталоги; тесты и отдельные вспомогательные модули для краткости опущены. Наличие каталога анимации само по себе не означает, что она запускается в `vts_main.py`: фактический список определяется вызовами в `asyncio.gather`.

<a id="ru-troubleshooting"></a>
## ✧ Решение проблем

### `No matching distribution found for torch==2.5.1+cu121`

Проверьте версию Python, окружение и начало файла зависимостей:

```bash
python --version
python -m pip --version
head -5 requirements.txt
```

Для подготовленного файла нужны Python 3.11 и доступ к дополнительному индексу `https://download.pytorch.org/whl/cu121`. Используйте именно `python -m pip`, чтобы не вызвать `pip` из другого окружения.

### Ошибка сборки PyAudio или не найден `portaudio.h`

На Arch Linux установите системные зависимости и повторите установку:

```bash
sudo pacman -S --needed base-devel portaudio linux-api-headers
python -m pip install -r requirements.txt
```

### Нет соединения с VTube Studio

- Проверьте, что VTube Studio запущен, модель загружена и Public API включён.
- Сверьте адрес и порт с `vts_model/api_parameters.py`.
- Подтвердите доступ плагина в VTube Studio.
- Если VTube Studio работает в Wine/Proton или на другой машине, отдельно проверьте сетевую доступность API. `localhost` означает текущий сетевой контекст приложения.
- Если токен неверен или отозван, переименуйте старый `token.txt`, создайте пустой файл и повторите авторизацию. Не удаляйте токен, если он нужен другому приложению.

### Whisper ничего не слышит

- Выполните `pactl list short sources` и проверьте `get_microphone_id`.
- Убедитесь, что выбран именно нужный микрофон или монитор выхода.
- Проверьте уровень входного сигнала и доступ приложения к аудиоустройству.
- При захвате системного звука проверьте, не возникает ли петля с голосом Нолы.

### LLM не отвечает

- Проверьте наличие `KEY_FOR_LLM` в `.env`, не публикуя сам ключ.
- Убедитесь, что запуск выполняется из корня проекта и есть доступ к DeepInfra.
- Проверьте доступность выбранной модели, разрешения ключа и сообщения об ошибке API.
- Учтите, что в показанном `async def llm_response` используется синхронный `requests`: такой вызов может блокировать event loop и влиять на задержку. При оптимизации можно вынести запрос в поток или перейти на асинхронный HTTP-клиент.

### Нет голоса

- Проверьте, что AllTalk запущен и доступен по адресу из `alltalktts_url`.
- Проверьте имя WAV-файла, настройки XTTS v2 и сообщения AllTalk.
- Проверьте аудиобэкенд и устройство, указанные в `cable_name`.

### Модель не двигается или двигается неправильно

- Убедитесь, что подключена нужная модель и плагин авторизован.
- Сверьте ID и диапазоны параметров модели со значениями в `vts_model/move.py` и настройками анимаций.
- Проверьте сообщения приложения и VTube Studio: успешное соединение ещё не гарантирует, что все параметры модели принимаются.

<a id="ru-security"></a>
## ✧ Безопасность

Не добавляйте секреты и локальные окружения в публичный репозиторий. Минимальные правила для `.gitignore`:

```gitignore
.env
.venv/
token.txt
```

Правило `token.txt` без ведущего `/` также исключит одноимённые файлы во вложенных каталогах. Если секрет уже был опубликован, отзовите или замените его: добавление файла в `.gitignore` не удаляет его из истории Git.

---

**Нола** · Голос, характер и Live2D в одном экспериментальном пайплайне.

[↑ Choose language / Выбрать язык](#language)
