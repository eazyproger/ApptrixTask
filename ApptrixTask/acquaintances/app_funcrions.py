from PIL import Image


def add_photo_watermark(input_image_path, email):
    base_image = Image.open(input_image_path)
    watermark = Image.open('acquaintances/avatars/watermark.png')
    output_image_path = 'acquaintances/avatars/' + email + '.png'
    watermark_position = (base_image.width - watermark.width, base_image.height - watermark.height)
    transparent = Image.new('RGBA', base_image.size, (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, watermark_position, mask=watermark)
    transparent.save(output_image_path)
    return output_image_path
