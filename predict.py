import cv2
import numpy as np
from keras.models import load_model
import sys

def predict_drone(image_path):
    try:
        model = load_model('drone_detection_model.h5')
    except Exception as e:
        print(f"Ошибка загрузки модели: {e}")
      
    original_image = cv2.imread(image_path)
    if original_image is None:
        print("Не удалось прочитать изображение")
        return

    orig_h, orig_w = original_image.shape[:2]

    image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = image.reshape(1, 224, 224, 3)

    prediction = model.predict(image)[0]
    
    xmin, ymin, xmax, ymax = prediction
    xmin = int(xmin * orig_w)
    ymin = int(ymin * orig_h)
    xmax = int(xmax * orig_w)
    ymax = int(ymax * orig_h)

    cv2.rectangle(original_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
    cv2.imwrite('result.jpg', original_image)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        predict_drone(sys.argv[1])
    else:
        print("Использование: python predict.py path_to_image.jpg")
