def get_image(parsed_html):
    img = parsed_html.find('img')
    if img is None:
        return ''
    return img['src']
