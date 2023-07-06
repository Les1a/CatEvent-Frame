from PIL import Image
import os

# root = './reconstruction_lightflash'


def cat_ef(root, output_path):
    # 设置两个图片文件夹路径
    image_folder_1 = os.path.join(root, 'events')
    image_folder_2 = root

    # 获取两个图片文件夹中的所有文件名
    image_files_1 = os.listdir(image_folder_1)
    image_files_2 = os.listdir(image_folder_2)

    # 创建一个字典，用于存储图片名后八位相同的图片
    image_dict = {}

    # 遍历第一个图片文件夹中的所有图片文件名
    for image_file in image_files_1:
        # 获取图片名后八位
        image_name_suffix = image_file[-12:]
        # 将该图片添加到字典中
        image_dict[image_name_suffix] = image_file

    # 遍历第二个图片文件夹中的所有图片文件名
    for image_file in image_files_2:
        # 获取图片名后八位
        image_name_suffix = image_file[-12:]
        # 如果该图片名后八位已经在字典中，则说明已经与第一个文件夹中的图片拼接完成，可以删除字典中的对应项
        if image_name_suffix in image_dict:
            # 打开当前图片
            current_image = Image.open(os.path.join(image_folder_2, image_file))
            # 打开字典中的图片
            dict_image = Image.open(os.path.join(image_folder_1, image_dict[image_name_suffix]))
            # 创建一个新的图片，将当前图片和字典中的图片拼接在一起
            result_image = Image.new('RGB', (current_image.width + dict_image.width, current_image.height))
            result_image.paste(current_image, (0, 0))
            result_image.paste(dict_image, (current_image.width, 0))
            # 将拼接后的图片保存到文件夹中
            result_image.save(os.path.join(output_path, image_name_suffix))
            del image_dict[image_name_suffix]
    print('Done!')
    image_dict.clear()


if __name__ == '__main__':
    rootpath = './reconstruction_lightflash'
    output = os.path.join(rootpath, 'cat_output')

    for dirs in os.listdir('./'):
        if os.path.isdir(os.path.join('./', dirs)) and dirs.startswith('re'):
            print(os.path.join('.', dirs), end=' ')
            cat_ef(rootpath, output)
