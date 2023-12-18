import imageio
import os
import re

def create_gif(directory, file_pattern, output_name, fps=5):
    print("Создание GIF...")
    try:
        file_list = [os.path.join(directory, filename) for filename in os.listdir(directory) if re.match(file_pattern, filename)]
        if not file_list:
            raise ValueError("Нет файлов, соответствующих заданному шаблону")

        file_list.sort(key=lambda x: int(re.search(r'\d+', x).group()))

        images = [imageio.imread(filename) for filename in file_list]

        imageio.mimsave(os.path.join(directory, output_name), images, fps=fps)
        print("GIF создан успешно.")
    except Exception as e:
        print(f"Ошибка при создании GIF: {e}")

def create_mp4(directory, file_pattern, output_name, fps=5):
    print("Создание MP4...")
    try:
        file_list = [os.path.join(directory, filename) for filename in os.listdir(directory) if re.match(file_pattern, filename)]
        if not file_list:
            raise ValueError("Нет файлов, соответствующих заданному шаблону")

        file_list.sort(key=lambda x: int(re.search(r'\d+', x).group()))

        with imageio.get_writer(os.path.join(directory, output_name), fps=fps, format='mp4') as writer:
            for filename in file_list:
                image = imageio.imread(filename)
                writer.append_data(image)
        print("MP4 создан успешно.")
    except Exception as e:
        print(f"Ошибка при создании MP4: {e}")

# Основная часть кода
directory = 'images'
file_pattern = r'loss_plot_epoch_\d+.png'
fps = 30

create_gif(directory, file_pattern, 'output_animation.gif', fps)
create_mp4(directory, file_pattern, 'output_video.mp4', fps)
