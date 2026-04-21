# Face Detection Project

Простая программа для обнаружения лиц на изображении с использованием OpenCV и каскадов Хаара.

##   Возможности

- Загрузка изображения по пути
- Поиск одного лица на фото
- Отображение результата с рамкой
- (в планах) поддержка нескольких лиц, видео, веб-камеры

## Установка

```bash
# Клонируем репозиторий
git clone https://github.com/ТВОЙ_НИКНЕЙМ/face-detection.git
cd face-detection

# Создаём окружение (рекомендуется)
conda create -n face_detection python=3.9
conda activate face_detection

# Устанавливаем зависимости
pip install -r requirements.txt
