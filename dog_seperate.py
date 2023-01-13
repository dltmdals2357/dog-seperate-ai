import os 
import wget
import requests
import shutil



dog_list = ['maltese', 'pomeranian', 'chihuahua', 'retriever/golden', 'poodle/toy' ]


def rmdir():
    
    for dog in dog_list:
        try:
            if dog == 'retriever/golden' or dog == 'poodle/toy':
                split = dog.split('/')
                shutil.rmtree(f'{split[0]}-{split[1]}')
            else:
                shutil.rmtree(f'{dog}')
        except:
            print('Cant find the folder')
            
def mkdir():
    for dog in dog_list:
        if dog == 'retriever/golden' or dog == 'poodle/toy':
            split = dog.split('/')
            os.mkdir(f'{split[0]}-{split[1]}')
        else:
            os.mkdir(dog)


rmdir()                             #folder reset
mkdir()


for dog in dog_list:
    url = f'https://dog.ceo/api/breed/{dog}/images'
    response = requests.get(url)
    if response.status_code == 200:
        img_link = response.json()['message']
        for img in img_link:
            split = img.split('/')
            try:
                if len(os.listdir(f'{split[4]}')) < 50:
                    wget.download(img, out=f"{split[4]}/img{len(os.listdir(f'{split[4]}'))+1}.png")
            except:
                print(" >>>>>>>> Error")
                break



for img in img_link:
    split = img.split('/')
    try:
        if len(os.listdir(f'{split[4]}')) < 50:
            wget.download(img, out=f"{split[4]}/img{len(os.listdir(f'{split[4]}'))+1}.png")
    except:
        print(" >>>>>>>> Error")
        break