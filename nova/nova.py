import reflex as rx #Web Framework
from rxconfig import config #Website details

class State(rx.State): #Main Site Data
    _source_code: str = open(__file__, 'r').read() #Get source code

    @rx.event()
    def gotopage(self, url: str ='/#'): #function to redirect to a different page
        return rx.redirect(url)
class State4a(rx.State): #Site Data for Palendrome Checker
    text: str = '' #Text in text box
    text_edit: str = '' #Edited text to check
    out: str = '' #Output string
    space: bool = False #Checkboxs' Values
    case: bool = False
    @rx.event()
    def check(self):
        self.text_edit = self.text.lower() if self.case == False else self.text #Make text lowercase if not Case-Sensitive
        self.text_edit = self.text.replace(' ', '') if self.space == True else self.text_edit #Remove spaces if checked
        if self.text_edit[::-1] == self.text_edit: #[::-1] means reverse string, so check if string is the same reversed
            self.out = 'It\'s a palendrome!' #Make output text certain value based on if the condition is met
        else:
            self.out = ':('
        #print(self.case, self.space) #Dev Tool: Show checkboxs' value
    @rx.event() #Tells web framework that this is an event
    def clear(self):
        self.reset() #Reset all variables
class State4b(rx.State):
    start: int
    end: int
    index: int = 0
    @rx.event #Tells web framework that this is an event
    def clear(self):
        self.reset() #Reset all variables

def home() -> rx.Component: #Home Button
    return rx.button(
        "Home",
        on_click=rx.redirect("/#"),  # redirect to home page
        color_scheme="blue",
        position='top-left'
    )

@rx.page() #Tells web framework this is a page
def index() -> rx.Component: #Home page
    return rx.container(
        rx.color_mode.button(position="top-right"), #Light/Dark mode switch
        rx.vstack( #Coloum
            rx.heading("Hello World NOVA Project", size="9"), #Big Text
            rx.text(
                'Check out my projects below!', #Small Text
                size="5", #Makes it a little bigger
            ),
            rx.hstack( #Row
                rx.button('Source Code', on_click=State.gotopage('/source')), #Buttons!
                rx.button('Reading/Video Log', on_click=State.gotopage('/1')),
                rx.button('Coding Concepts', on_click=State.gotopage('/3/a')),
                rx.button('Palendrome Checker', on_click=State.gotopage('/4a'))
            ),
            spacing="5", #Spaces out buttons
            justify="center", #Makes it all centered
            min_height="85vh" #Puts all the stuff in the almost middle of the screen vertically
        ),
    )

def ui() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        home(),
        width='25vh'
    )

@rx.page(on_load=State4a.clear) #Clear page data on load
def r4a() -> rx.Component: #Palendrome Checker
    return rx.box(
        ui(),
        rx.center( #Center all components inside the '()'
            rx.vstack( #Coloum
                rx.heading('Requirnment 4a: Palendrome Checker'), #Big Text
                rx.hstack( #Row
                    rx.input(placeholder='Tacocat', value=State4a.text, on_change=State4a.set_text),
                    rx.button('Check', on_click=State4a.check())
                ),
                rx.hstack( #Row
                    rx.checkbox('Case-Sensitive', on_change=State4a.set_case),
                    rx.checkbox('Remove Spacing', on_change=State4a.set_space)
                ),
                rx.text(State4a.out), #Tiny Text
                align='center', #Center it!
                justify='center'
            )
        )
    )

def sidebar() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text('Table Of Contents:', size='5'),
            rx.separator(),
            rx.link("Local and Global Variables", href="/3/a"),
            rx.separator(),
            rx.link("Data Types and Formats", href="/3/bc"),
            rx.separator(),
            rx.link("Flow Instructions", href="/3/d"),
            rx.separator(),
            rx.link("Functions and Parameters", href="/3/ef"),
            rx.separator(),
            rx.link("Keys and Values", href="/3/g"),
            rx.separator(),
            rx.link("Universal Resource Locators (URLs)", href="/3/h"),
            rx.separator()
        ),
        width='25vh'
    )

def r1() -> rx.Component:
    return rx.box(
        ui(),
        rx.heading('Requirnment 1: Reading/Vidoes'),
        rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell('Date/Time'),
            rx.table.column_header_cell('Book/Video'),
            rx.table.column_header_cell('Length (min.)'),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell('Sat Jun 7, 7:30'),
            rx.table.cell('Python for Kids 2nd Edition by Jason R. Briggs'),
            rx.table.cell('30'),
        )
    ),
    width="100%",
)
    )
def r3a() -> rx.Component:
    return rx.box(
        ui(),
        rx.hstack(
            sidebar(),
            rx.center(
                rx.container(
                    rx.vstack(
                        rx.heading('NOTICE: THE FOLLOWING APPLIES TO THE PROGRAMMING LANGUAGE PYTHON. IT CAN BE FOUND AT:', size='8'),
                        rx.link('https://python.org/', href='https://python.org/', size='7'),
                        rx.separator(),
                        rx.heading('Local and Global Variables', size='8'),
                        rx.separator(),
                        rx.heading('Global Variables', size='6'),
                        rx.text('A Global variable is a variable that is acessable anywhere. For example:'),
                        rx.code_block('''var=0\nclass main:\n   var=1\n   def __init__(self):\n      print(var)\nmain()\n#Output:\n0''', language="python", show_line_numbers=True),
                        rx.separator(),
                        rx.heading('Local Variables', size='6'),
                        rx.text('A local variable is a variable that is only accessable inside it\'s class. Take that example from before:'),
                        rx.code_block('''var=0\nclass main:\n   var=1\n   def __init__(self):\n      print(var)\nmain()\n#Output:\n0''', language="python", show_line_numbers=True),
                        rx.text('Modify:'),
                        rx.code_block('''class main:\n   var=1\n   def __init__(self):\n      print(var)''', language="python", show_line_numbers=True),
                        rx.text('To:'),
                        rx.code_block('''class main:\n   var=1\n   def __init__(self):\n      print(self.var)''', language="python", show_line_numbers=True),
                        rx.text('So the full code:'),
                        rx.code_block('''var=0\nclass main:\n   var=1\n   def __init__(self):\n      print(self.var)\nmain()''', language="python", show_line_numbers=True),
                        rx.text('Outputs:'),
                        rx.code_block('1', language="bash"),
                        rx.separator(),
                        rx.link("Next: Data Types and Formats ->", href="/3/bc"),
                    ),
                    justify='left'
                ),
                width='75vw'
            )
        )
    )
def r3bc() -> rx.Component:
    return rx.box(
        ui(),
        rx.hstack(
            sidebar(),
            rx.center(
                rx.container(
                    rx.heading('Data Types and Formats'),
                ),
                width='75vw'
            )
        )
    )
def r3d() -> rx.Component:
    return rx.box(
        ui(),
        rx.hstack(
            sidebar(),
            rx.center(
                rx.container(
                    rx.heading('Flow Instructions'),
                ),
                width='75vw'
            )
        )
    )
            
            
    

@rx.page() #Tells web framework this is a page
def source() -> rx.Component: #Source code page
    return rx.box(
        ui(),
        rx.center( #Center all the stuff in the '()'
            rx.vstack( #Coloum
                rx.heading('Source Code:'), #Big Text
                rx.code_block(State._source_code, language="python", show_line_numbers=True), #Code
                align='center'
            ),
        )
    )
#Add all pages
app = rx.App()
app.add_page(index, title='Home', route='/')
app.add_page(r1, title='Reading/Videos Log | 1', route='/1/')
app.add_page(r3a, title='Local and Global Variables | 3a', route='/3/a')
app.add_page(r3bc, title='Local and Global Variables | 3b & 3c', route='/3/bc')
app.add_page(r3d, title='Local and Global Variables | 3d', route='/3/d')
app.add_page(r4a, title='Palendrome Checker | 4a', route='/4a/')
app.add_page(source, title='Source Code', route='/source/')