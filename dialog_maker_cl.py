import sys
import json
import os

messages = []

def check_command(command):
    global speaker
    global dialog
    global messages

    if command == "/exit":
        create_json()
        sys.exit(0)
    elif command == "/change_dialog":
        create_json()
        messages.clear()
        dialog = input_checked(f"({filepath}) Insert new dialog id: ")
    elif command == "/change_speaker":
        speaker = input_checked(f"({filepath}[{dialog}]) Insert a new speaker name: ")
    elif command == "/save":
        create_json()

def input_checked(*args):
    command = input(*args)
    check_command(command)
    return command

def set_speaker_text():
    global text
    global speaker

    while True:
        text = input_checked(f"({filepath}[{dialog}]) What {speaker} says?\n")
        if text not in ["/change_speaker", "/change_dialog"]:
            if text == "/done":
                break
            messages.append({"speaker": speaker, "text": text})
            print(messages)

def create_json():
    global dialog
    global filepath
    global messages

    data = {}

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    if dialog not in data:
        data[dialog] = []

    data[dialog].extend(messages)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dialogs save in {filepath}")

filepath = input_checked("Insert file path: ")
dialog = input_checked("Insert dialog id: ")
speaker = input_checked(f"({filepath}[{dialog}]) Insert speaker name: ")
set_speaker_text()
create_json()
