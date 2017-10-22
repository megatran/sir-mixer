# Author: Nhan Tran and Shewta
import mixer_secretkey
import pygame.image
import pygame.camera
import os
import re
import dropbox
import httplib, urllib, base64

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[-1])
cam.start()
img = cam.get_image()


temp_data_path = "/home/linaro/Documents/sirmixer/collected_data"
temp_pic_path = os.path.join(temp_data_path, "temporary_pic.png")
pygame.image.save(img, temp_pic_path)
pygame.camera.quit()

dbx = dropbox.Dropbox(mixer_secretkey.dropbox_api_key)
with open(temp_data_path+"/temporary_pic.png", 'rb') as f:
   dbx.files_upload(f.read(), "/temporary_pic.png", mode=dropbox.files.WriteMode.overwrite)

shared_link = dbx.sharing_create_shared_link("/temporary_pic.png")
dl_url = re.sub(r"\?dl\=0", "?dl=1", shared_link.url)
print(dl_url)

azure_api_key = mixer_secretkey.azure_headers

params = urllib.urlencode({})

body = "{ 'url': '" + dl_url + "' } "


try:
    # NOTE: You must use the same region in your REST call as you used to obtain your sub$
    #   For example, if you obtained your subscription keys from westcentralus, replace "$
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, azure_api_key)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))





