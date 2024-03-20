from PIL import Image, ImageOps
import os

def create_collage_from_folders(folder_list, output_file):
    images = []
    
    # Получение списка изображений из указанных папок
    for folder_name in folder_list:
        folder_path = os.path.join(os.getcwd(), folder_name)
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(folder_path, filename)
                img = Image.open(image_path)
                images.append(img)

    # Инициализация параметров для создания коллажа
    max_images_in_row = 4
    outer_padding = 20
    inner_padding = 40
    background_color = (255, 255, 255)  # белый

    # Вычисление размеров коллажа
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    collage_width = max_width * max_images_in_row + (max_images_in_row - 1) * inner_padding + 2 * outer_padding
    collage_height = ((len(images) - 1) // max_images_in_row + 1) * (max_height + 2 * outer_padding) + 2 * outer_padding

    collage = Image.new("RGB", (collage_width, collage_height), background_color)

    index = 0
    x_offset = outer_padding
    y_offset = outer_padding

    # Создание коллажа
    for img in images:
        collage.paste(img, (x_offset, y_offset))
        x_offset += max_width + inner_padding
        index += 1

        if index % max_images_in_row == 0:
            x_offset = outer_padding
            y_offset += max_height + 2 * outer_padding

    # Сохранение коллажа в формате TIFF
    collage.save(output_file)

# Пример использования
folder_list = ['1388_12_Наклейки 3-D_3']
output_file = 'Result.tif'

create_collage_from_folders(folder_list, output_file)