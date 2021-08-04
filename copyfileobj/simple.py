import requests
import shutil

image_url  = 'https://i.imgur.com/2SbwzTP.jpg'
image_path = image_url.split("/")[-1]
print(image_path)
r = requests.get(image_url, stream = True)

if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    with open(image_path,'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ',image_path)
