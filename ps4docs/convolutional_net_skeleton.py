from keras.models import *
from keras.layers import *
import keras
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

def get_x_y_data():
    negative_data = []
    with open('negativedata.txt') as f:
        for line in f:
            final_mat = np.zeros((4,len(line)-1,1))
            for i in range(len(line)):
                char = line[i]
                if char == 'a':
                    final_mat[:,i,:] = np.array([[1],[0],[0],[0]])
                if char == 'c':
                    final_mat[:,i,:] = np.array([[0],[1],[0],[0]])
                if char == 'g':
                    final_mat[:,i,:] = np.array([[0],[0],[1],[0]])
                if char == 't':
                    final_mat[:,i,:] = np.array([[0],[0],[0],[1]])
            negative_data.append(final_mat)

    positive_data = []
    with open('positivedata.txt') as f:

        for line in f:
            final_mat = np.zeros((4,len(line)-1,1))
            for i in range(len(line)):
                char = line[i]
                if char == 'a':
                    final_mat[:,i,:] = np.array([[1],[0],[0],[0]])
                if char == 'c':
                    final_mat[:,i,:] = np.array([[0],[1],[0],[0]])
                if char == 'g':
                    final_mat[:,i,:] = np.array([[0],[0],[1],[0]])
                if char == 't':
                    final_mat[:,i,:] = np.array([[0],[0],[0],[1]])
            positive_data.append(final_mat)

    x_train = np.array(negative_data + positive_data)
    y_train = np.array([0] * len(negative_data) + [1] * len(positive_data))
    y_train = keras.utils.to_categorical(y_train)

    return x_train, y_train

x_train, y_train = get_x_y_data()

#X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2
x_train

model = Sequential()
model.add(Conv2D(32, kernel_size=(4, 6), strides=(1, 1),
                 activation='relu',
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(1, 1)))#, strides=(2, 2)))
model.add(Flatten())
model.add(Dense(10, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.add(Activation(tf.nn.softmax))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01),
              metrics=['accuracy'],
              validation_split=0.1)

model.fit(x_train, y_train,
          epochs=3,
          verbose=1,
          validation_data=(x_test, y_test),
          callbacks=[history])

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])






