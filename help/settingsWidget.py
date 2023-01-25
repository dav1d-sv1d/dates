class Settings:

    def settings_label(

            self,
            widgets=None,
            text=None,
            alignment=None,
            font=None,
            bold=None

    ):

        for widget in widgets:
            widget.setText(text[widget]["text"])
            widget.setAlignment(alignment[widget]["alignment"])
            font_w = font[widget]["font"]
            font_w.setBold(True)
            widget.setFont(font_w)

    def settings_widget(

            self,
            widget=None,
            text=None,
            alignment=None,
            font=None,
            font_size=None,


    ):
        pass