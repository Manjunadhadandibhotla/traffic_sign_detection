import tkinter as tk
from tkinter import *
from tkinter import filedialog, Button
from gtts import gTTS
from playsound import playsound

language = 'en'
# load the trained model to classify sign
import keras.models
import numpy
import top as top
from PIL import ImageTk, Image

model = keras.models.load_model('traffic_classifier.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Vehicle > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing vehicle > 3.5 tons'}

# initialise GUI
top = tk.Tk()
top.geometry("1000x1000")
top.title('Sign Detection of Image')
top.configure(background='#E1E8ED')

label = Label(top, background='#E1E8ED', font=('Comic Sans MS', 35, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict([image])[0]
    sign = classes[max(range(len(pred)), key=lambda x: pred[x - 1])]
    print(sign)
    label.configure(foreground='#FBBC05', text=sign)
    text_val = sign
    obj = gTTS(text=text_val, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3
    obj.save("exam.mp3")

    # Play the exam.mp3 file
    playsound("exam.mp3")


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=35, pady=10)
    classify_b.configure(background='#34A853', foreground='white', font=('Comic Sans MS', 15, 'bold'))
    classify_b.pack(side=RIGHT)
    classify_b.place(relx=0.80, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 3.25), (top.winfo_height() / 3.25)))
        im = ImageTk.PhotoImage(uploaded)
        print(file_path)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, pady=10)
upload.configure(background='#4285F4', foreground='white', font=('Comic Sans MS', 15, 'bold'))
upload.place(rely=0.46)

upload.pack(side=LEFT)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Know Your Traffic Sign", font=('Comic Sans MS', 40, 'bold'))
heading.configure(background='#E1E8ED', foreground='#F65314')
heading.pack()
top.mainloop()
