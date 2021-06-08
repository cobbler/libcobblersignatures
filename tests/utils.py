"""
Copyright 2020 Tom Bocklisch and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

See https://github.com/tmbo/questionary/blob/master/tests/utils.py
"""

import asyncio

from prompt_toolkit.input.defaults import create_pipe_input
from prompt_toolkit.output import DummyOutput

from questionary import prompt
from questionary.prompts import prompt_by_name
from questionary.utils import is_prompt_toolkit_3


class KI:
    """
    KI - KeyInputs
    Possible key inputs.
    """
    D = "\x1b[B"
    U = "\x1b[A"
    L = "\x1b[D"
    R = "\x1b[C"
    ENT = "\r"
    ESC = "\x1b"
    CONTROLC = "\x03"
    BACK = "\x7f"
    SPACE = " "
    TAB = "\x09"


def feed_cli_with_input(_type, message, texts, sleep_time=1, **kwargs):
    """
    Create a Prompt, feed it with the given user input and return the CLI
    object.

    You an provide multiple texts, the feeder will async sleep for `sleep_time`

    This returns a (result, Application) tuple.
    """

    if not isinstance(texts, list):
        texts = [texts]

    inp = create_pipe_input()

    try:
        prompter = prompt_by_name(_type)
        application = prompter(message, input=inp, output=DummyOutput(), **kwargs)

        if is_prompt_toolkit_3():
            loop = asyncio.new_event_loop()
            future_result = loop.create_task(application.unsafe_ask_async())

            for i, text in enumerate(texts):
                # noinspection PyUnresolvedReferences
                inp.send_text(text)

                if i != len(texts) - 1:
                    loop.run_until_complete(asyncio.sleep(sleep_time))
            result = loop.run_until_complete(future_result)
        else:
            for text in texts:
                inp.send_text(text)
            result = application.unsafe_ask()

        return result, application
    finally:
        inp.close()


def patched_prompt(questions, text, **kwargs):
    """Create a prompt where the input and output are predefined."""

    inp = create_pipe_input()

    try:
        # noinspection PyUnresolvedReferences
        inp.send_text(text)
        result = prompt(questions, input=inp, output=DummyOutput(), **kwargs)
        return result

    finally:
        inp.close()
