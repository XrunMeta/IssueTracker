- Make sure CloneVoice server is already running on http://127.0.0.1:9988
    You can use either preCompiled version or SourceBuild version

- How to usage
    python clone_api.py "Text Input" language speed "Voice Model Target Path"

- Example usage
    python clone_api.py "Hello friends, how are you today" english 1.0 "E:\XRun\Clone Voice\dataset-voice\english1.wav"

    python clone_api.py "Hello friends, how are you today" en 1.0 "E:\XRun\Clone Voice\dataset-voice\english1.wav"

    python clone_api.py "어느 봄날 오후, 민준이는 학교 수업을 마치고 천천히 집으로 걸어가고 있었다." ko 1.0 "E:\XRun\dataset-voice\Korean1.wav"

-   SUPPORTED_LANGUAGES = {
        "chinese": "zh-cn", "zh-cn": "zh-cn",
        "english": "en", "en": "en",
        "japanese": "ja", "ja": "ja",
        "korean": "ko", "ko": "ko",
        "spanish": "es", "es": "es",
        "german": "de", "de": "de",
        "french": "fr", "fr": "fr",
        "italian": "it", "it": "it",
        "turkish": "tr", "tr": "tr",
        "russian": "ru", "ru": "ru",
        "portuguese": "pt", "pt": "pt",
        "polish": "pl", "pl": "pl",
        "dutch": "nl", "nl": "nl",
        "arabic": "ar", "ar": "ar",
        "hungarian": "hu", "hu": "hu",
        "czech": "cs", "cs": "cs"
    }