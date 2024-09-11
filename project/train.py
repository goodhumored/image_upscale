import numpy as np
from keras._tf_keras.keras.preprocessing.image import img_to_array, load_img
from keras.src.callbacks import ModelCheckpoint
import os
from model import sr_model

def load_dataset(compressed_dir, original_dir, target_size=(512, 512)):
    """
    Загрузка сжатых и оригинальных изображений для обучения.
    
    :param compressed_dir: Папка с сжатыми изображениями.
    :param original_dir: Папка с оригинальными изображениями.
    :param target_size: Размеры изображений для входа в модель.
    :return: Массивы с входами (сжатые изображения) и целями (оригинальные).
    """
    X, Y = [], []
    
    for img_name in os.listdir(compressed_dir):
        compressed_img_path = os.path.join(compressed_dir, img_name)
        original_img_name = img_name.split('_compressed_')[0] + ".jpg"
        original_img_path = os.path.join(original_dir, original_img_name)
        
        if os.path.exists(original_img_path):
            compressed_img = load_img(compressed_img_path, target_size=target_size)
            original_img = load_img(original_img_path, target_size=target_size)
            
            X.append(img_to_array(compressed_img) / 255.0)
            Y.append(img_to_array(original_img) / 255.0)
    
    return np.array(X), np.array(Y)

# Define checkpoint callback
checkpoint = ModelCheckpoint(
    "weights-improvement-{epoch:02d}.keras",   # Path to save the model
    save_best_only=False,      # Save only the best model (based on the monitored metric, but optional here)
    save_weights_only=False,  # Save the entire model (set to True if you want to save only weights)
    mode='auto',             # Auto mode selects the right mode based on the metric
    verbose=1                # Verbosity mode (0 or 1)
)

# Папки с сжатыми и оригинальными изображениями
compressed_images_folder = "compressed_images"
original_images_folder = "original_images_resized"

# Загрузка датасета
X_train, Y_train = load_dataset(compressed_images_folder, original_images_folder)

# Обучение модели
sr_model.fit(X_train, Y_train, epochs=50, batch_size=4, callbacks=[checkpoint],)

# Сохранение обученной модели
sr_model.save("model256_50_epochs.h5")
