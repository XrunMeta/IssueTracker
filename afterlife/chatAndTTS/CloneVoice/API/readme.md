# CloneVoice Python API Wrapper

## 📌 Prerequisites

Make sure the **CloneVoice server** is already running at:

```
http://127.0.0.1:9988
```

You can use **either the precompiled version** or the **source build**.

---

## 🚀 Usage

```bash
python clone_api.py "Text Input" <language> <speed> "<Voice Model File Path>"
```

- `Text Input` — The text you want to synthesize.
- `language` — Either full name (`english`) or abbreviation (`en`).
- `speed` — Speaking rate (e.g. `1.0` = normal speed).
- `Voice Model File Path` — Full path to your `.wav` file.

---

## 📂 Example Commands

```bash
python clone_api.py "Hello friends, how are you today" english 1.0 "E:\XRun\Clone Voice\dataset-voice\english1.wav"
python clone_api.py "Hello friends, how are you today" en 1.0 "E:\XRun\Clone Voice\dataset-voice\english1.wav"
python clone_api.py "어느 봄날 오후, 민준이는 학교 수업을 마치고 천천히 집으로 걸어가고 있었다." ko 1.0 "E:\XRun\dataset-voice\Korean1.wav"
```

---

## 🌐 Supported Languages

| Language     | Code   |
|--------------|--------|
| Chinese      | zh-cn  |
| English      | en     |
| Japanese     | ja     |
| Korean       | ko     |
| Spanish      | es     |
| German       | de     |
| French       | fr     |
| Italian      | it     |
| Turkish      | tr     |
| Russian      | ru     |
| Portuguese   | pt     |
| Polish       | pl     |
| Dutch        | nl     |
| Arabic       | ar     |
| Hungarian    | hu     |
| Czech        | cs     |

Both full names and abbreviations are accepted (e.g., `english` or `en`).
