def get_image(parsed_html):
    img = parsed_html.find('img')
    return img['src']
