from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


class MyWidget(Widget):
    pass


class MyApp(App):
    def build(self):
        self.title = 'Математический тренажёр'
        self.icon = 'логотип.jpg'
        Window.size = (1000, 600)

        layout = FloatLayout()
        widget = MyWidget()
        self.button_play = Button(text="Play", font_size="30", font_name="CodecPro-ExtraBold.ttf", size_hint=(None, None),
                             width=350, height=150,
                             pos_hint={'center_x': .5, 'center_y': .5})

        self.button_quit = Button(text="Quit", font_size="30", font_name="CodecPro-ExtraBold.ttf",
                             size_hint=(None, None), width=200, height=100,
                             pos_hint={'center_x': 0.5, 'center_y': 0.3})

        self.button_play.bind(on_press=self.show_difficulty_menu)
        self.button_quit.bind(on_press=self.quit_app)

        layout.add_widget(widget)
        layout.add_widget(self.button_play)
        layout.add_widget(self.button_quit)

        with widget.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=widget.pos, size=widget.size)
        widget.bind(pos=self.update_rect, size=self.update_rect)
        return layout

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return super().on_touch_down(touch)


    def update_rect(self, widget, *args):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=widget.pos, size=widget.size)

    def quit_app(self, instance):
        App.get_running_app().stop()

    def show_difficulty_menu(self, instance):
        # Создаём новый Layout
        layout = FloatLayout()
        # Добавляем кнопку для лёгкого уровня
        button_easy = Button(text="Easy", font_size="30", font_name="CodecPro-ExtraBold.ttf",
                             size_hint=(None, None), width=300, height=100,
                             pos_hint={'center_x': .5, 'center_y': .7})
        layout.add_widget(button_easy)
        # Добавляем кнопку для среднего уровня
        button_medium = Button(text="Medium", font_size="30", font_name="CodecPro-ExtraBold.ttf",
                               size_hint=(None, None), width=300, height=100,
                               pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(button_medium)
        # Добавляем кнопку для сложного уровня
        button_hard = Button(text="Hard", font_size="30", font_name="CodecPro-ExtraBold.ttf",
                             size_hint=(None, None), width=300, height=100,
                             pos_hint={'center_x': .5, 'center_y': .3})
        layout.add_widget(button_hard)
        # Добавляем Layout на главный экран
        self.root.add_widget(layout)
        # Удаляем кнопку Play и Quit с главного экрана
        self.root.remove_widget(instance)
        self.root.remove_widget(self.button_quit)


if __name__ == '__main__':
    MyApp().run()
