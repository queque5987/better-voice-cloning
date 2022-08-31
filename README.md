Better-API (vocoder)
=============
https://github.com/queque5987/better-encoder    
https://github.com/queque5987/better-synthesizer-w   
https://github.com/queque5987/better-synthesizer   
https://github.com/queque5987/better-vocoder    

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
to install librosa : https://github.com/heroku/heroku-buildpack-apt   
source : https://fastapi.tiangolo.com/   

## Heroku
deployed with FastAPI   
https://dashboard.heroku.com/

### requirements.txt
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn
