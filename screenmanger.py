from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from helpers import username_helper
from helpers import password_helper

Window.size = (300, 500)

screen_helper = """
ScreenManager:
    LoginScreen:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<LoginScreen>:
    name: 'login'
    MDTextField:
        hint_text: "Enter username"
        helper_text: "all in lower case"
        helper_text_mode: "on_focus"
        icon_right: "language-python"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300 
    MDTextField:
        hint_text: "Enter password"
        helper_text: "all in lower case"
        helper_text_mode: "on_focus"
        icon_right: "language-python"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300 
    MDRectangleFlatButton:
        text: "Enter"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'menu'
            
<MenuScreen>:
    name: 'menu'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Mobile GUI'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation :8
                              
                    Widget:
           
                    BoxLayout
                        orientation: 'vertical'
                        spacing:'20dp'
                        padding:'8dp'
                        MDRectangleFlatButton:
                            text: 'User1'
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                        Image:
                            source: 'brain.png'
                            pos_hint: {'center_x':0.5,'center_y':0.8}
                        
                            
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding:'8dp'
                Image:
                    source: 'stickman.png'
                MDLabel:
                    text: ' Tester'
                    front_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: ' tester123@ntu.edu.sg'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            on_press: root.manager.current = 'profile'
                            IconLeftWidget:
                                icon: 'face-profile-woman'
                        OneLineIconListItem:
                            text: 'Upload'
                            on_press: root.manager.current = 'upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'   

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""
class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
