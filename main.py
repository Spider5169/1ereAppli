# This is a sample Python script.
import kivy
from kivy.lang import Builder

kivy.require('2.1.0')
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.uix.label import Label            #texte titre
from kivy.uix.gridlayout import GridLayout  #la fenetre est une grille
from kivy.uix.textinput import TextInput    #zone de text a saisir
from kivy.uix.widget import Widget          #fenetre ou on doit definir position

class LoginScreen(GridLayout):

    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Nom Utilisateur"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Mot de Passe"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text="Bienvenue dans l'application"))
        self.entree = Builder.load_string('''
Button :
    text: 'Entrer dans O Fit'
''')
        self.add_widget(self.entree)

class Main_page(GridLayout):

    def __init__(self, **kwargs):
        super(Main_page, self).__init__(**kwargs)
        self.rows = 3
        self.add_widget(Label(text = "O FIT"))
        self.login = Builder.load_string('''
Button :
    text: 'Connectez-vous'
    on_release :
        login()
''')
        self.add_widget(self.login)
        self.new_client = Builder.load_string('''
Button :
    text: 'Inscrivez-vous'
''')
        self.add_widget(self.new_client)


class OFitApp(App):

    def build(self):
        return Main_page()
        # return Label(text="Bienvenue dans l'application")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    OFitApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
