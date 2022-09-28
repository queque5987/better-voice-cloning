import requests
import numpy as np
import json

urls = {
    "encoder-inference": "https://better-encoder.herokuapp.com/inference",
    "encoder-preprocess": "https://better-encoder.herokuapp.com/preprocess",
    "synthesizer": "https://better-synthesizer.herokuapp.com/inference",
    "vocoder": "https://better-vocoder.herokuapp.com/inference",
    ## backup server ##
    "encoder-inference2": "https://better-encoder-2.herokuapp.com/inference",
    "encoder-preprocess2": "https://better-encoder-2.herokuapp.com/preprocess",
    "synthesizer2": "https://better-synthesizer-2.herokuapp.com/inference",
    "vocoder2": "https://better-vocoder-2.herokuapp.com/inference"
}
response_urls = {
    "encoder-inference": "https://better-encoder.herokuapp.com/check",
    "encoder-preprocess": "https://better-encoder.herokuapp.com/check",
    "synthesizer": "https://better-synthesizer.herokuapp.com/check",
    "vocoder": "https://better-vocoder.herokuapp.com/check"
}

headers = {
        'Content-Type': 'application/json'
}

def get_response(url: str, data: dict):
    res = requests.request("GET", response_urls[url], headers=headers)
    print(res.text)
    if res.text != "\"service available\"":
        print("{} dose not repond \nchanging to {}".format(url, url+"2"))
        return requests.request("POST", urls[url+"2"], headers=headers, data=json.dumps(data))
    return requests.request("POST", urls[url], headers=headers, data=json.dumps(data))

def get_wav(wav: list, sr: int, text: str):
    print("requesting embed to encoder . . .")
    response = get_response("encoder-inference", {"wav": wav, "sr": sr})
    embed = eval(response.json())['embed']
    print("embed -----\n{}".format(embed))

    return get_wav_embedding(embed, sr, text)

def get_wav_embedding(embed: list, sr: int, text: str):
    print("requesting spec to synthesizer . . .")
    response = get_response("synthesizer", {"embed": embed, "text": text})
    spec = eval(response.json())['spec']

    print("requesting wav to vocoder . . .")
    response = get_response("vocoder", {"spec": spec, "sr": sr})
    wav = eval(response.json())['wav']
    wav = np.array(wav)
    wav = np.pad(wav, (0, sr), mode="constant")
    wav = list(wav)

    print("requesting preprocessing to encoder . . .")
    response = get_response("encoder-preprocess", {"wav": wav, "sr": sr})
    return eval(response.json())['wav']