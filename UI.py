from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from choose_image_func import choose_image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from ML import detect_gender

class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text

class RV():
    b = BoxLayout(orientation='vertical')
    t = TextInput(font_size=50,
                  size_hint_y=None,
                  height=100)

    f = FloatLayout()
    s = Scatter()

    l = Label(text="Hello !",
              font_size=50)

    f.add_widget(s)
    s.add_widget(l)

    b.add_widget(t)
    b.add_widget(f)
    t.bind(text=l.setter('text'))

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)

class TestApp(App):
    title = "Visual Question Answering"
    file_path = ''
    product_img = Image(source='bg.png')
    caption = ''
    answer = ''
    gender_text = StringProperty("")
    gender = None 

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

        self.file_path = choose_image()
        if(self.file_path!=None):
            self.product_img.source = self.file_path
            gender = detect_gender(self.file_path)
            self.gender_text = gender
            self.gender.text = gender

        else:
            print('No File Selected')


    def build(self):
        layout = BoxLayout(orientation='horizontal')
        left = BoxLayout(orientation='vertical')
        right = BoxLayout(orientation='vertical')
        image_layout = BoxLayout(orientation='vertical')
        choose_btn_layout = BoxLayout(orientation='vertical', size=(100,100),size_hint=(None, None))

        # choose_btn_layout.padding = [50,10,10,10]
        left.add_widget(image_layout)
        left.spacing=10
        left.padding = [10,10,10,10]

        image_layout.padding = [30,60,20,60]
        choose_image_btn = Button(text='Choose Image', size=(200,100),size_hint=(None,None))
        choose_image_btn.bind(on_press=self.callback)
        choose_btn_layout.padding = [220,10,10,10]

        self.product_img.allow_stretch = True
        self.product_img.keep_ratio = False
        self.product_img.size_hint_x = 0.95
        self.product_img.size_hint_y = 0.8

        image_layout.add_widget(self.product_img)
        choose_btn_layout.add_widget(choose_image_btn)
        left.add_widget(choose_btn_layout)
        l = Label(text=self.answer, font_size='20sp')
        def on_enter(value):
            l.text = str(value.text)
        self.gender = Label(text=self.gender_text, font_size='25sp')
        #textinput = TextInput(text='' ,multiline=False, height=100, font_size=25, size_hint_y=None)
        #textinput.bind(on_text_validate=on_enter)
        title = Label(text='Gender Prediction', font_size='20sp')
        right.add_widget(title)
        right.add_widget(self.gender)
        right.add_widget(l)
        layout.add_widget(left)
        layout.add_widget(right)
        return layout

if __name__ == "__main__":
    TestApp().run()
