from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random
import string
import datetime

Window.clearcolor = (0.15, 0.15, 0.15, 1)

SERVICES = {
    "Discord Nitro": 16,
    "Steam Gift": 15,
    "Amazon Gift": 14,
    "Spotify Premium": 18,
    **{f"Popular Service {i}": random.randint(12, 24) for i in range(1, 997)}
}

def generate_code(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class CodeGenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.add_widget(Label(text='Select Service', size_hint=(1, None), height=30))
        self.spinner = Spinner(
            text='Discord Nitro',
            values=sorted(SERVICES.keys()),
            size_hint=(1, None),
            height=44
        )
        self.add_widget(self.spinner)
        self.add_widget(Label(text='Quantity', size_hint=(1, None), height=30))
        self.qty_input = TextInput(text='1', multiline=False, input_filter='int', size_hint=(1, None), height=44)
        self.add_widget(self.qty_input)
        self.gen_button = Button(text='Generate Codes', size_hint=(1, None), height=50)
        self.gen_button.bind(on_press=self.generate_codes)
        self.add_widget(self.gen_button)
        self.output = TextInput(readonly=True, background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1,1,1,1))
        self.add_widget(self.output)

    def generate_codes(self, instance):
        try:
            count = max(1, int(self.qty_input.text))
        except ValueError:
            count = 1
        service = self.spinner.text
        length = SERVICES.get(service, 16)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        codes = [f"[{timestamp}] {service}: {generate_code(length)}" for _ in range(count)]
        self.output.text = '\n'.join(codes)

class CodeGenApp(App):
    def build(self):
        return CodeGenLayout()

if __name__ == '__main__':
    CodeGenApp().run()
