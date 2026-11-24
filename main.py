#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — entry program.

Writes one line of office humour to /output/entry.txt (UTF-8, 1-200 chars).
The joke: an HR survey asks whether staff feel heard — and the submit
button is greyed out, so the survey itself will not let anyone answer.
The last beat redefines the setup; the reader supplies the reframe.
Gate: the file must hold exactly the joke, no trailing newline.
"""

LINE = "HR's survey asked if we feel heard. The submit button was greyed out."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    data = text.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "byte verification failed"
    print(f"entry.txt: {len(text)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
