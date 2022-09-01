Better-API (Voice-cloning)
=============
|Name               |Link                                                |input                             |output                     |
|:------------------|:---------------------------------------------------|:---------------------------------|--------------------------:|
|voice-cloning      |https://github.com/queque5987/better-voice-cloning  |wav/wample_rate/<br>embedding/text|speech sound               |
|encoder            |https://github.com/queque5987/better-encoder        |wav/sample_rate                   |embedding                  |
|synthesizer        |https://github.com/queque5987/better-synthesizer    |embedding/text                    |mel-spectrogram            |
|synthesizer-model  |https://github.com/queque5987/better-synthesizer-w  |parameters in synthesizer         |mel-spectrogram per batch  |
|vocoder            |https://github.com/queque5987/better-vocoder        |mel-spectrogram                   |speech sound               | 

### Better-API generates a voice that cloning user's voice from a text.
    1.encoder recieves a user voice and gives an embedding to synthesizer.
    2.synthesizer recieves an embedding and a text to generate speech and gives mel spectrogram to vocoder.   
    3.vocoder recieves a mel spectrogram and gives generated wav file.   
       
*Encoder speaker embedding Model*   
*Synthesizer uses TACOTRON2 Model; it is on better-synthesizer-w API*   
*Vocoder uses waveRNN Model*   
    
## available on
https://better-voice-cloning.herokuapp.com/
## to inference, send request on
https://better-voice-cloning.herokuapp.com/inference-c/
https://better-voice-cloning.herokuapp.com/inference-w/

### Request JSON
   ***TODO***
### Response JSON
   ***TODO***
   
* * *
# used libraries
## Real-Time-Voice-Cloning
https://github.com/CorentinJ/Real-Time-Voice-Cloning

## FastAPI   
developed with FastAPI   
https://fastapi.tiangolo.com/   

## Heroku
deployed with FastAPI   
https://dashboard.heroku.com/

### requirements.txt
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn

-----
## 사용예시(Examples) 

## ColdStart(with wav file)

### input
    wav : list   
    sr : int   
    text : str   
### output
    wav : list   
    sr : int   
    
### on Python
```python
import requests
import json

url = "https://better-voice-cloning.herokuapp.com/inference-c"

wav_json = json.dumps({
    "wav": wav,
    "sr": sr,
    "text": text
})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=wav_json)
print(response.json())
```

### on JavaScript
```javascript
var obj = new Object();
obj.wav = wav;
obj.sr = sr;
obj.text = text;
var jsonString = JSON.stringify(obj)
var res = fetch('https://better-voice-cloning.herokuapp.com/inference-c', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json',
  },
  body: jsonString
}).then((response) => response.json()
).then(function(data){
  var res = JSON.parse(data)
  console.log(res.wav) // output
})
```

## WalmStart <br> (with embeddings from https://github.com/queque5987/better-encoder)

### input
    embed : list   
    sr : int   
    text : str   
### output
    wav : list   
    sr : int   
    
### on Python
```python
import requests
import json

url = "https://better-voice-cloning.herokuapp.com/inference-w"

wav_json = json.dumps({
    "embed": embed,
    "sr": sr,
    "text": text
})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=wav_json)
print(response.json())
```

### on JavaScript
```javascript
var obj = new Object();
obj.embed = embed;
obj.sr = sr;
obj.text = text;
var jsonString = JSON.stringify(obj)
var res = fetch('https://better-voice-cloning.herokuapp.com/inference-w', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json',
  },
  body: jsonString
}).then((response) => response.json()
).then(function(data){
  var res = JSON.parse(data)
  console.log(res.wav) // output
})
```
