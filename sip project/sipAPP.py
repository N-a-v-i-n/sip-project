from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivy.lang import Builder
from pyVoIP.VoIP import VoIPPhone, VoIPCall, InvalidStateError, CallState,PhoneStatus
from pyVoIP import RTP
import time
import wave,pyVoIP
from pyVoIP.SIP import SIPMessage
from kivy.storage.jsonstore import JsonStore
from kivy.uix.popup import Popup
from kivy.uix.label import Label
def close_application(self):
    App.get_running_app().stop()
    Window.close()
    
Window.size=(480,800)
Window.bind(on_request_close=close_application)
store=JsonStore("clientData.json")


class Home_screen(Screen):
   
    store_data_ref=[]
    def __init__(self, **kwargs):
        super(Home_screen, self).__init__(**kwargs)
        btns=self.buttons()
        screen=self.display()
        call_btn=self.action_btns()
        bind_elements=GridLayout(cols=1)
        bind_elements.add_widget(screen)
        bind_elements.add_widget(btns)
        bind_elements.add_widget(call_btn)
        self.add_widget(bind_elements)
        
    def data(self,val):
        Home_screen.store_data_ref.append(val.text)
        self.dis_screen.text="".join(map(lambda x:x,Home_screen.store_data_ref))
    def buttons(self):
        self.bind_elements=GridLayout(rows=4)
        btn_1=Button(text="1",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_2=Button(text="2",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_3=Button(text="3",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_4=Button(text="4",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_5=Button(text="5",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_6=Button(text="6",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_7=Button(text="7",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_8=Button(text="8",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_9=Button(text="9",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_star=Button(text="*",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_0=Button(text="0",size_hint=(None,None),width=200,height=100, on_release=self.data)
        btn_hash=Button(text="#",size_hint=(None,None),width=200,height=100, on_release=self.data)

        [self.bind_elements.add_widget(x) for x in [btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_star,btn_0,btn_hash,]]

        return self.bind_elements
    
    def display(self):
        self.dis_screen=TextInput(text="",size_hint=(None,None),width=600,height=100,font_size="30sp")

        return self.dis_screen
    def action_btns(self):
        
        def clear_screen(ref):
            self.dis_screen.text=""
            Home_screen.store_data_ref=list()

        # def Call(ref):
        #     client_cred=store.get('data')
        #     phone=VoIPPhone(str(client_cred["ServerIP"]),int(client_cred["ServerPort"]),str(client_cred["Username"]),str(client_cred["Userpassword"]),str(client_cred["ClientIP"]),int(client_cred["ClientPort"]), rtpPortLow=100000, rtpPortHigh=200000)
        #     print("calling...",self.dis_screen.text)
        #     phone.start()
        #     phone.call(int(self.dis_screen.text))

        
        def backspace(ref):
            try:
                Home_screen.store_data_ref.pop()
                self.dis_screen.text="".join(map(lambda x:x,Home_screen.store_data_ref))
            except:
                pass
        clear=Button(text='Clear',size_hint=(None,None),width=100,height=80,on_release=clear_screen)
        call=Button(text="Call",size_hint=(None,None),width=400,height=80, on_press=Login.call)
        backspace=Button(text='Back',size_hint=(None,None),width=100,height=80,on_release=backspace)
        bind_elements=GridLayout(rows=1)
        [bind_elements.add_widget(x) for x in [clear,call,backspace]]
        return bind_elements
    
        



        
                



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class entryScreen(Screen):
    def __init__(self, **kwargs):
        super(entryScreen, self).__init__(**kwargs)
        grid_lay=GridLayout(cols=1)
        login = Button(text='login')
        register = Button(text='register')
        grid_lay.add_widget(login)
        grid_lay.add_widget(register)
        self.add_widget(grid_lay)

        register.bind(on_press = self.register_screen_transition)
        login.bind(on_press = self.login_screen_transition)

    def register_screen_transition(self, *args):
        self.manager.current = 'register'
    def login_screen_transition(self, *args):
        self.manager.current = 'login'

class Login(Screen):        
    Phone_ref=""

    def __init__(self, **kwargs):
        super(Login,self).__init__(**kwargs)
        connections=GridLayout(rows=8,spacing=5)
        self.server_ip=TextInput(text="192.168.52.131",_hint_text="Server IP",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.server_proxy=TextInput(text="5060",_hint_text="Server Port",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.user_name=TextInput(text="500",_hint_text="Username",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.user_password=TextInput(text="123",_hint_text="Password",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.display_name=TextInput(text="500",_hint_text="Display name",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.client_ip=TextInput(text="192.168.52.1",_hint_text="Client IP",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        self.client_proxy=TextInput(text="6062",_hint_text="Client Port",font_size="20sp",size_hint=(None,None ), width=600,height=50)
        bind_fun_btns=GridLayout(rows=1)
        self.Connect=Button(text='Connect',size_hint=(None,None ),height=50, on_release=self.submit)
        self.Disconnect=Button(text='Disconnect',size_hint=(None,None ),height=50, on_release=self.disconnect)
        bind_fun_btns.add_widget(self.Connect)
        bind_fun_btns.add_widget(self.Disconnect)
        

       


        [connections.add_widget(x) for x in [self.server_ip,self.server_proxy,self.user_name,self.user_password,self.display_name,self.client_ip,self.client_proxy,bind_fun_btns]]

        self.btn=connections
        self.add_widget(self.btn)
        self.btn.bind(on_press = self.screen_transition)

        
    def disconnect(self, instance):
        try:
            self.phone.stop()
            self.Connect.text="Connect"
            self.Connect.width=100
            self.Connect.color="white"
        
        except:
            pass
        print("Disconnected ...")

    def call(self):
        print(Login.Phone_ref)
        phone=Login.Phone_ref
       
        phone.call(400)

        phone.callback()
        print("helloo")

        
      

    def submit(self,call_req="None",):
        ServerIP=self.server_ip.text
        ServerPort=self.server_proxy.text
        Username=self.user_name.text
        Userpassword=self.user_password.text
        Displayname=self.display_name.text
        ClientIP=self.client_ip.text
        ClientPort=self.client_proxy.text

        store.put("data",
            ServerIP=ServerIP, 
            ServerPort=ServerPort,
            Username=Username,
            Userpassword=Userpassword,
            Displayname=Displayname,
            ClientIP=ClientIP,
            ClientPort=ClientPort
        )


        try:
            phone=VoIPPhone(str(ServerIP),int(ServerPort),str(Username),str(Userpassword),str(ClientIP),int(ClientPort), rtpPortLow=100000, rtpPortHigh=200000)
            Login.Phone_ref=phone
            self.phone=phone
            
            print("staring")
            self.phone.start()
            print("started")
            self.Connect.text="Connected"
            self.Connect.width=150
            self.Connect.color="greenyellow"

        except Exception as err:
            def Close_pop(self,ref):
                popup.dismiss()
            print("error is : ",err)
            popup = Popup(title='Error',content=Label(text=f"{err}"),size_hint=(None,None ),width=600, height=300)
            btn_to_cancel=Button(text='Close')
            btn_to_cancel.bind(on_press=Close_pop)
            self.Connect.text="Connect"
            self.Connect.width=100
            self.Connect.color="white"
            popup.open()

        if self.Connect.text=="Connected":
            # self.phone.stop()
            self.manager.current = 'homescreen'

    def screen_transition(self, *args):
        self.manager.current = 'homescreen'

class Register(Screen):
    def __init__(self, **kwargs):
        super(Register,self).__init__(**kwargs)
        self.btn=Button(text='Register screen')
        self.add_widget(self.btn)
        self.btn.bind(on_press = self.screen_transition)
    def screen_transition(self, *args):
        self.manager.current = 'entryScreen'

class ScintillateSIP(App):

    def build(self):

       
        screen_manage=ScreenManagement(transition=FadeTransition())
        screen_manage.add_widget(entryScreen(name="entryScreen"))
        screen_manage.add_widget(Login(name="login"))
        screen_manage.add_widget(Register(name="register"))
        screen_manage.add_widget(Home_screen(name="homescreen"))
        

        return screen_manage


ScintillateSIP().run()