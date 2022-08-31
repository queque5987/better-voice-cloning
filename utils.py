import requests
import numpy as np
import json

urls = {
    "encoder-inference": "https://better-encoder.herokuapp.com/inference/",
    "encoder-preprocess": "https://better-encoder.herokuapp.com/preprocess/",
    "synthesizer": "https://better-synthesizer.herokuapp.com/inference/",
    "vocoder": "https://better-vocoder.herokuapp.com/inference/"
}

headers = {
        'Content-Type': 'application/json'
}

def get_response(url: str, data: dict):
    return requests.request("POST", url, headers=headers, data=json.dumps(data))

def get_wav(wav: list, sr: int, text: str):
    print("requesting embed to encoder . . .")
    response = get_response(urls["encoder-inference"], {"wav": wav, "sr": sr})
    embed = eval(response.json())['embed']

    return get_wav_embedding(embed, sr, text)

def get_wav_embedding(embed: list, sr: int, text: str):
    print("requesting spec to synthesizer . . .")
    response = get_response(urls["synthesizer"], {"embed": embed, "text": text})
    spec = eval(response.json())['spec']

    print("requesting wav to vocoder . . .")
    response = get_response(urls["vocoder"], {"spec": spec, "sr": sr})
    wav = eval(response.json())['wav']
    wav = np.array(wav)
    wav = np.pad(wav, (0, sr), mode="constant")
    wav = list(wav)

    print("requesting preprocessing to encoder . . .")
    response = get_response(urls["encoder-preprocess"], {"wav": wav, "sr": sr})
    return eval(response.json())['wav']