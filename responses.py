import random

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    image_url_1 = 'https://raw.githubusercontent.com/SkeletonDad/Abstract-Art/main/Abstract_gallery/Abstract_gallery/Abstract_image_.jpg'
    image_url_2 = 'https://raw.githubusercontent.com/SkeletonDad/Abstract-Art/main/Abstract_gallery_2/Abstract_gallery_2/Abstract_image_.jpg'
    
    
    if 'art' in lowered:
        url = random.choice([image_url_1, image_url_2])
        if url == image_url_1:
            image = url[:-4] + str(random.randint(0, 2781)) + '.jpg'
        else:
            image = url[:-4] + str(random.randint(2782, 2871)) + '.jpg'

        return image