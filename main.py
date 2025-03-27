import asyncio
from pynput import keyboard
from transcriber import WhisperAPITranscriber
from table_interface import ConsoleTable
from key_listener import create_keylistener
from dotenv import load_dotenv
from utils import manual_type


async def main():
    load_dotenv()

    transcriber = WhisperAPITranscriber.create()
    hotkey = create_keylistener(transcriber)
    def for_canonical(f):
        return lambda k: f(l.canonical(k))
    l = keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release))
    l.start()
    async for transcription, audio_duration_ms in transcriber.get_transcriptions():
        manual_type(transcription.strip())


if __name__ == "__main__":
    asyncio.run(main())
