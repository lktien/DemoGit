import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import Text
from PIL import ImageTk, Image
import numpy
from keras.models import load_model
model=load_model('model.h5')
classes = {1: 'Bệnh bọ xít, cần bón cân đối hợp lí các chất dinh dưỡng',
           2: 'Bệnh châu chấu, cần phải phòng trừ gấp!',
           3: 'Bệnh đạo ôn, cần đến trạm BVTV để phòng trừ kịp thời',
           4: 'Bệnh khô vằn, phải diệt bệnh nhanh chóng, đến trạm BVTV để xử lí',
           5: 'Bệnh rầy nâu, đến trạm BVTV và tuân theo nguyên tắc 4 đúng',
           6: 'Bệnh sâu cuốn lá, cần sử dụng thiên địch hoặc thuốc BVTV hợp lí',
           7: 'Bệnh sâu đục thân, phải dùng bông tẩm thuốc Virtako 40WG,Ammate 150SC,...',
           8: 'Bệnh ốc bưu vàng, phải đến trạm BVTV để phòng trừ kịp thời',
           9: 'Bệnh sâu keo, cần trị bệnh kịp thời'}
top=tk.Tk()
top.geometry('800x600')
top.title('MÔ HÌNH NHẬN DIỆN BỆNH')
top.configure(background='#ffffff')

label=Label(top,background='#ffffff', font=('arial',15,'bold'))
sign_image=Label(top)

def classify(file_path):
  global label_packed
  image = Image.open(file_path)
  image = image.resize((30,30))
  image = numpy.expand_dims(image, axis=0)
  image = numpy.array(image)
  print(image.shape)
  
  pred_probabilities= model.predict(image)[0]
  pred = pred_probabilities.argmax(axis=-1)
  sign= classes[pred+1]
  print(sign)
  label.configure(foreground='#011638',text=sign)

def show_classify_button(file_path):
  classify_b=Button(top,text="NHẬN DIỆN",command=lambda: classify(file_path), padx= 10,pady=5)
  classify_b.configure(background='#c71b20', foreground= 'white', font = ('arial',10,'bold'))
  classify_b.place(relx=0.79,rely=0.46)

def upload_image():
  try:
    file_path=filedialog.askopenfilename()
    uploaded=Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
    im=ImageTk.PhotoImage(uploaded)

    sign_image.configure(image=im)
    sign_image.image=im
    label.configure(text='classes')
    show_classify_button(file_path)
  except:
    pass
upload = Button(top, text="NHẤN ĐỂ NHẬN DIỆN", command=upload_image, padx=10, pady=5)
upload.configure(background='#c71b20', foreground= 'white',font=('arial', 10,'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading= Label(top, text = "NHẬN DIỆN BỆNH TRÊN CÂY LÚA",pady=10, font=('arial',20,'bold'))
heading.configure(background='#ffffff', foreground='#364156')
heading1= Label(top, text = "CHO MÙA BỘI THU",pady=10, font=('arial',20,'bold'))
heading1.configure(background='#ffffff', foreground='#364156')
heading2= Label(top, text = "VÌ CUỘC SỐNG XANH-SẠCH-ĐẸP",pady=10, font=('arial',20,'bold'))
heading2.configure(background='#ffffff', foreground='#364156')

heading.pack()
heading1.pack()
heading2.pack()

top.mainloop()