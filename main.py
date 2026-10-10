
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class ShadowPanel(App):
    def build(self):
        Window.clearcolor = (0.06, 0.07, 0.08, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        layout.add_widget(Label(
            text="SHADOW PANEL",
            font_size=26,
            bold=True
        ))

        self.buttons = []

        options = [
            "Mostrar / ocultar painel",
            "Opção 1",
            "Opção 2",
            "Opção 3"
        ]

        for option in options:
            button = Button(
                text=option,
                font_size=18,
                size_hint_y=None,
                height=55,
                background_normal="",
                background_color=(0.1, 0.55, 0.25, 1)
            )
            button.bind(on_release=self.toggle_button)
            layout.add_widget(button)
            self.buttons.append(button)

        return layout

    def toggle_button(self, button):
        if button.background_color == [0.1, 0.55, 0.25, 1]:
            button.background_color = (0.65, 0.15, 0.15, 1)
            button.text = "ATIVADO: " + button.text
        else:
            button.background_color = (0.1, 0.55, 0.25, 1)
            button.text = button.text.replace("ATIVADO: ", "")

if __name__ == "__main__":
    ShadowPanel().run()
          
