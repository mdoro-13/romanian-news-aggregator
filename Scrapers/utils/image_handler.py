def get_image(parsed_html, src_name = 'src'):
    img = parsed_html.find('img')
    if img is None:
        return ''
    return img[src_name]
