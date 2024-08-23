import base64
import time

import pyfiglet
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
}


def text_to_ascii_art(text, font="standard"):
    # Create an instance of Figlet with the specified font
    ascii_art = pyfiglet.Figlet(font=font)

    # Render the text into ASCII art
    rendered_text = ascii_art.renderText(text)

    return rendered_text


# A generator function to stream ASCII art line by line
def ascii_stream(text: str):
    yield "\033[2J\033[H"
    for line in text.splitlines():
        yield line + "\n"
        time.sleep(0.3)  # Simulate a delay for streaming effect

    # Add a delay before clearing the screen
    time.sleep(0.5)
    yield "\033[2J\033[H"

    while True:
        for k, v in colors.items():
            yield v
            yield text
            time.sleep(0.3)
            yield "\033[2J\033[H"


@app.get("/{text}")
async def stream_ascii(text: str):
    ascii_art = text_to_ascii_art(base64.b64decode(text).decode("utf-8"))
    return StreamingResponse(ascii_stream(ascii_art), media_type="text/plain")
