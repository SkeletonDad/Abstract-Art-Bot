import random
import vars

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    image_url_1 = 'https://raw.githubusercontent.com/SkeletonDad/Abstract-Art/main/Abstract_gallery/Abstract_gallery/Abstract_image_.jpg'
    image_url_2 = 'https://raw.githubusercontent.com/SkeletonDad/Abstract-Art/main/Abstract_gallery_2/Abstract_gallery_2/Abstract_image_.jpg'
    
    art_responses = [
        'Here is some art!',
        'Behold, there is art!',
        'Witness this artistic creation!',
        'Here you\'ll find some artistic expression!',
        'Presenting a piece of art!',
        'Observe the beauty in this artwork!',
        'Enjoy this display of artistic flair!',
        'Delight in the presence of art!',
        'Take a look at this piece of artistry!',
        'Here\'s a glimpse of artistic wonder!',
        'Appreciate the art presented here!',
        'Marvel at the artistic composition!',
        'This is a manifestation of art!',
        'Explore the world of art!',
        'Discover the beauty within this artwork!',
        'Behold, a work of art!',
        'Experience the artistry in this!',
        'Witness the creativity captured in art!',
        'Here you can find some beautiful art!',
        'This is a showcase of artistic brilliance!',
        'Take a moment to appreciate this art!',
        'Delve into the world of creative expression!',
        'Here\'s a creation that embodies art!',
        'Behold this piece of visual art!',
        'Explore the artistic side of things!',
        'Appreciate the craftsmanship in this art!',
        'Here lies a piece of artistic inspiration!',
        'Take a glimpse into the world of artistry!',
        'Witness the beauty encapsulated in this art!',
        'Behold the artistic essence presented here!']

    if 'resume' in lowered and not vars.alert_alex:
            vars.alert_alex = True
            return 'I will resume messaging you now!'
    
    if 'art' in lowered:
        rep = random.choice(art_responses)
        url = random.choice([image_url_1, image_url_2])
        if url == image_url_1:
            image = url[:-4] + str(random.randint(0, 2781)) + '.jpg'
        else:
            image = url[:-4] + str(random.randint(2782, 2871)) + '.jpg'

        return f'{rep}\n{image}'
    
    if 'stop' in lowered and vars.alert_alex:
        vars.alert_alex = False
        return 'Ok, I won\'t message you until you say \'resume\''
    
    