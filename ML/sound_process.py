import httplib, urllib, base64
import wave

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Transfer-Encoding: chunked',
    'Content-type: audio/wav; codec=audio/pcm; samplerate=16000',
    'Ocp-Apim-Subscription-Key: 10e9e0fe1b6243489c4b762827844b59',

}

params = urllib.urlencode({
})

w = wave.open("test.wav", "rb")
binary_data = w.readframes(w.getnframes())
# Replace the example URL below with the URL of the image you want to analyze.
body = binary_data


    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
conn = httplib.HTTPSConnection('https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed')
conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
