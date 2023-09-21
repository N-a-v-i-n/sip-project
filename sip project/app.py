# from kivy.app import App 
# from kivy.uix.label import Label
# from kivy.core.window import Window

# # How to build a app

# Window.clearcolor=(1,1,1,1)  # changing backgroud color to white
# class Myapp(App):  # this class name will be the window title
#     def build(self):  # this is to build app
#         label=Label(text="Hello world",font_size="120sp",bold=True,italic=True,color=(1,0,0,1))
#         return label
# Myapp().run() 


# # how to make Button on Kivy
# from kivy.uix.button import Button
# class Buttoncls(App):
#     def build(self):
#         return Button(text="Click Me",size_hint=(1,0.3 ),pos_hint={'center_x':0.5 , 'center_y':0.5 },font_size='44sp',on_press=self.btn_click,on_release=self.release)
#     def btn_click(self,b1):
#         print("b1 : ",b1)
#         print("BTN CLICKED")
#     def release(self,r1):
#         print("r1 : ",r1)
#         print("BTN RELEASED")

# Buttoncls().run()

# # Adding Images 
# from kivy.uix.image import Image,AsyncImage #for importing img from internet a=then we go for AsyncImage

# class Image_app(App):
#     def build(self):
#         return Image(source=r"C:\Users\navin\OneDrive\Desktop\navin sign.png",size_hint=(None,None),width=100,height=100,pos_hint={'center_x':0.5 , 'center_y':0.5})
    
# Image_app().run()
 

# #  Box Layouts
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.core.window import Window

# Window.clearcolor=(1,1,1,1)
# Window.size=(400,700)


# class box_lay(App):
#     def build(self):
#         layout=BoxLayout(orientation='horizontal',spacing=10,padding=10)   # for adding multing btns we need to bind it with layout, and we can return
#         btn1=Button(text='BTN1')
#         btn2=Button(text='BTN2')
#         layout.add_widget(btn1)
#         layout.add_widget(btn2)
#         return layout
    
# box_lay().run()

# # Grid Layout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button

# class Grid_lay(App):
#     def build(self):
#         grid_layout=GridLayout(cols=2) # rows=2,row_force_default=True,row_default_height=40
#         btn1=Button(text="BTN1")
#         btn2=Button(text="BTN2")
#         btn3=Button(text="BTN3")
#         btn4=Button(text="BTN4")
#         btn5=Button(text="BTN5")
#         [grid_layout.add_widget(x) for x in [btn1,btn2,btn3,btn4,btn5]]
#         return grid_layout
    
# Grid_lay().run()

# # Anchor Layout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.anchorlayout import AnchorLayout


# class Anchar_lay(App):
#     def build(self):
#         anchor=AnchorLayout(anchor_x="right",anchor_y="bottom")
#         btn1=Button(text="BTN1",size_hint=(None,None ), width=100, height=200)
#         btn2=Button(text="BTN2")
#         btn3=Button(text="BTN3")
#         # input_1=TextInput(_hint_text="enter your name")
#         [anchor.add_widget(x) for x in [btn1]]
#         return anchor
    
# Anchar_lay().run()

# # Float Layout
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout


# class Float_lay(App):
#     def build(self):
#         float=FloatLayout()
#         btn1=Button(text="BTN1",size_hint=(None,None ), width=100, height=200,pos_hint={'center_x':0.5 , 'center_y':0.5 })
#         float.add_widget(btn1)
#         return float
    
# Float_lay().run()

# # Page Layout
# from kivy.uix.button import Button
# from kivy.uix.pagelayout import PageLayout


# class Page_lay(App):
#     def build(self):
#         page=PageLayout()
#         btn1=Button(text="BTN1",size_hint=(None,None ), width=100, height=200,pos_hint={'center_x':0.5 , 'center_y':0.5 })
#         btn2=Button(text="BTN2",size_hint=(None,None ), width=100, height=200,pos_hint={'center_x':0.5 , 'center_y':0.5 })

#         page.add_widget(btn1)
#         page.add_widget(btn2)

#         return page
    
# Page_lay().run()


# # Input_field
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput

# class Input_field(App):
#     def build(self):
#         input_1=TextInput(_hint_text="enter your name")
#         prperties=['_cursor_blink', '_cursor_visual_height', '_cursor_visual_pos', '_editable', '_hint_text', '_hint_text_lines', '_ime_composition', '_ime_cursor', '_keyboard', '_lines', 'allow_copy', 'auto_indent', 'background_active', 'background_color', 'background_disabled_normal', 'background_normal', 'base_direction', 'border', 'center', 'center_x', 'center_y', 'children', 'cls', 'cursor', 'cursor_blink', 'cursor_col', 'cursor_color', 'cursor_pos', 'cursor_row', 'cursor_width', 'disabled', 'disabled_foreground_color', 'do_wrap', 'focus', 'focus_next', 'focus_previous', 'focused', 'font_context', 'font_family', 'font_name', 'font_size', 'foreground_color', 'halign', 'handle_image_left', 'handle_image_middle', 'handle_image_right', 'height', 'hint_text', 'hint_text_color', 'ids', 'input_filter', 'input_type', 'is_focusable', 'keyboard', 'keyboard_mode', 'keyboard_suggestions', 'line_height', 'line_spacing', 'lines_to_scroll', 'minimum_height', 'motion_filter', 'multiline', 'opacity', 'padding', 'padding_x', 'padding_y', 'parent', 'password', 'password_mask', 'pos', 'pos_hint', 'readonly', 'replace_crlf', 'right', 'scroll_distance', 'scroll_from_swipe', 'scroll_timeout', 'scroll_x', 'scroll_y', 'selection_color', 'selection_from', 'selection_text', 'selection_to', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'tab_width', 'text', 'text_language', 'text_validate_unfocus', 'top', 'unfocus_on_touch', 'use_bubble', 'use_handles', 'width', 'write_tab', 'x', 'y']
#         return input_1
    
# Input_field().run()


# # Kv Language
 

# class KV_langAPP(App):
#     pass 

## create a filename same as classname, but in {small_letters.kv} and write coding
## Label:
##   text:"helloKivy"
    
# KV_langAPP().run()
 


# # Screen Switching
# from kivy.uix.button import Button
# from kivy.uix.screenmanager import ScreenManager,Screen

# class Home_screen(Screen):
#     pass
# class Product_screen(Screen):
#     pass

# class Manager(ScreenManager):
#     pass

# class Screen(App):
#     def build(self): 
#         pass

# ## create a filename same as classname, but in {small_letters.kv} and write coding

# ## Manager:
# ## Home_screen:
# ## Product_screen:

# ## <Home_screen>:
# ##     name:"Home"
# ##     Button:
# ##         text:"Homebtn"
# ##         on_press:
# ##             app.root.current="Product"
# ##             root.manager.transition.direction="left"

# ## <Product_screen>:
# ##     name: "Product"
# ##     Button:
# ##         text:"Productbtn"
# ##         on_press:
# ##             app.root.current="Home"
# ##             root.manager.transition.direction="right"
    
# Screen().run()



# # Builder Method  :- this will load the kv_language with the code 

# from kivy.lang import Builder
# mydoc="""
# Label:
#     text:"hello kivy"

# """
# class builder(App):
#     def build(self):
#         build=Builder.load_string(mydoc)
#         return build
# builder().run()

# ###########################################


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Window.size=(480,800)

    

class ScintillateSIP(App):
        store_data_ref=[]
        def data(self,val):
            ScintillateSIP.store_data_ref.append(val.text)
            self.dis_screen.text="".join(map(lambda x:x,ScintillateSIP.store_data_ref))
            
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
                ScintillateSIP.store_data_ref=list()
            def backspace(ref):
                try:
                    ScintillateSIP.store_data_ref.pop()
                    self.dis_screen.text="".join(map(lambda x:x,ScintillateSIP.store_data_ref))
                except:
                    pass
            clear=Button(text='Clear',size_hint=(None,None),width=100,height=80,on_release=clear_screen)
            call=Button(text="Call",size_hint=(None,None),width=400,height=80)
            backspace=Button(text='Back',size_hint=(None,None),width=100,height=80,on_release=backspace)
            bind_elements=GridLayout(rows=1)
            [bind_elements.add_widget(x) for x in [clear,call,backspace]]
            return bind_elements


   
        def build(self):
            btns=self.buttons()
            screen=self.display()
            call_btn=self.action_btns()
            bind_elements=GridLayout(cols=1)
            bind_elements.add_widget(screen)
            bind_elements.add_widget(btns)
            bind_elements.add_widget(call_btn)
            # popup.open()
            return bind_elements




ScintillateSIP().run()