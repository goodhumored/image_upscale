from keras import layers, models, losses

def build_sr_model(input_shape=(512, 512, 3)):
    """
    Создаём простую CNN для суперразрешения.
    
    :param input_shape: Размер входного изображения (ширина, высота, каналы).
    :return: Модель нейронной сети.
    """
    model = models.Sequential()

    # Первый сверточный слой
    model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(layers.Conv2D(256, (3, 3), activation='relu', padding='same'))

    # Восстановление изображения
    model.add(layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same'))

    model.compile(optimizer="adam", loss=losses.MeanSquaredError())

    return model

sr_model = build_sr_model()
sr_model.summary()
