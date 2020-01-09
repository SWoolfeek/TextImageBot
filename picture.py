from PIL import Image, ImageDraw, ImageFont

def create_picture(text, b_color, t_color, user_id,width = 1080, height = 720):
    text, font_size, top_indent = text_transform(text, height, width)

    # Drawing empty Image
    image = Image.new('RGBA', (width, height), (b_color))
    draw = ImageDraw.Draw(image)
    # Set font
    font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-liberation/LiberationSerif-Bold.ttf", font_size)

    # Choosing left indent by length of first paragraph
    first_paragraph = text.split('\n')[0]
    left_indent = (width - (font.getsize(first_paragraph))[0]) / 2

    # Drawing text on Image
    draw.text((left_indent, top_indent), text, font=font, fill=t_color, align='center')
    picture_name = str(user_id)+".png"
    image.save(picture_name)
    return picture_name


# Transforming text, and choosing a font size
def text_transform(text, height, width, font_size=50):
    original = text
    text_list = text.split('\n')
    result = []

    # I use it to check width of paragraphs
    font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-liberation/LiberationSerif-Bold.ttf", font_size)

    width_mod = width - 202  # Modified width by subtraction minimal indent * 2 ## If image would by smaller then 1080-720, it would bad(
    # Dividing every paragraphs if they larger then they could be
    for i in text_list:
        if width_mod - (font.getsize(i))[0] < 0:
            counter = (width_mod // font_size) * 2
            separator = i[:counter].rfind(' ')
            # Checking if text is long, and without spaces
            if separator < 0:
                result.append(i)
            else:
                # Create new sentence and check, does it fit
                sentence = i[:separator] + '\n' + i[separator + 1:]
                prepared_text, _, _ = text_transform(sentence, height, width, font_size)

                result.append(prepared_text)
        else:
            result.append(i)
    result = '\n'.join(result)
    return paragraphs(result, original, height, width, font_size)


# Here`s checking does text fit by height, if no, change the font size and repeat
def paragraphs(text, original, height, width, font_size=50):
    top_indent = (height - 2 * font_size)
    paragraph_counts = text.count('\n')
    if top_indent < font_size * paragraph_counts:
        return text_transform(original, height, width, font_size - 5)
    return text, font_size, (50 + (top_indent - font_size * paragraph_counts)) // 2
