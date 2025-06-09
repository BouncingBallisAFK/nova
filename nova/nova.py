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
                rx.tooltip(
                    rx.button('Reading/Video Log', on_click=State.gotopage('/1')),
                    content="Req. 1",
                ),
                rx.tooltip(
                    rx.button('Coding Concepts', on_click=State.gotopage('/3/a')),
                    content="Req. 3",
                ),
                rx.tooltip(
                    rx.button('Palendrome Checker', on_click=State.gotopage('/4a')),
                    content="Req. 4a",
                ),
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
                        rx.heading('Global Variables'),
                        rx.text('A Global variable is a variable that is acessable anywhere. For example:'),
                        rx.code_block('''var=0\nclass main:\n   var=1\n   def __init__(self):\n      print(var)\nmain()\n#Output:\n0''', language="python", show_line_numbers=True),
                        rx.separator(),
                        rx.heading('Local Variables'),
                        rx.text('A local variable is a variable that is only accessable inside it\'s class. Take that example from before:'),
                        rx.code_block('''var=0\nclass main:\n\tvar=1\n\tdef __init__(self):\n\t\tprint(var)\nmain()\n#Output:\n0''', language="python", show_line_numbers=True),
                        rx.text('Modify:'),
                        rx.code_block('''class main:\n\tvar=1\n\tdef __init__(self):\n\t\tprint(var)''', language="python", show_line_numbers=True),
                        rx.text('To:'),
                        rx.code_block('''class main:\n\tvar=1\n\tdef __init__(self):\n\tprint(self.var)''', language="python", show_line_numbers=True),
                        rx.text('So the full code:'),
                        rx.code_block('''var=0\nclass main:\n\tvar=1\n\tdef __init__(self):\n\t\tprint(self.var)\nmain()''', language="python", show_line_numbers=True),
                        rx.text('Outputs:'),
                        rx.code_block('1', language="bash"),
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
                    rx.vstack(
                        rx.heading('Data Types and Formats', size='8'),
                        rx.separator(),
                        rx.heading('Scalar Variables'),
                        rx.text('Scalar variables contain only one value. These include strings, integers, floats, booleans, '),
                        rx.separator(),
                        rx.heading('String'),
                        rx.text('In python, a string, or "str", is defined using single or double quotes. For example:'),
                        rx.code_block('\'Hello, World!\'\n"Hello, World!"'),
                        rx.separator(),
                        rx.heading('Escape Characters'),
                        rx.markdown('Escape characters are used to add extra things to strings.<br>`\\n` makes a new line in a string.<br>`\\\\` cancels out a backslash, so you can display a backslash like normal.<br>`\\\'` or `\\\"` to put single or double quotes when your string when the string is made with them.<br>For example: `\'aren\\\'t\'` `\"He said \\\"Hello!\\\"\"`<br>`\\r` acts as a carrige return.<br>`\\t` makes a tab.<br>`\\b` makes a backspace.<br>`\\ooo` adds a octal value as a character.<br>`\\xhh` adds a hex value as a character.'),
                        rx.separator(),
                        rx.heading('Multi-line String'),
                        rx.text('A multi-line string is show with three single quotes. For Example:'),
                        rx.code_block('\'\'\'Hello,\nWorld!\'\'\''),
                        rx.separator(),
                        rx.heading('F String'),
                        rx.text('An F string can include variables using curly brackets. It is shown using a string with an "f" or "F" before the first quote For example:'),
                        rx.code_block('a=1\nb=2\nc=a+b\nstring=f\'{a}+{b}={c}\''),
                        rx.separator(),
                        rx.heading('R String'),
                        rx.text('An R string disables escape characters. It is shown using a string with an "r" or "R" before the first quote For example:'),
                        rx.code_block('r\'\\home\\user\\Downloads\''),
                        rx.separator(),
                        rx.heading('Numbers'),
                        rx.text('Numbers in python are catagorized based on if they have a decimal point or not. With a decimal point, they are a float. Else, they are an integer.'),
                        rx.separator(),
                        rx.heading('Integer'),
                        rx.markdown('An integer, or "int", represents a positive or negative number WITHOUT a decimal point. Integers are written using `var=1`'),
                        rx.separator(),
                        rx.heading('Float'),
                        rx.markdown('A float, or "flt", represents a positive or negative number WITH a decimal point. Floats are written using `var=1.5`'),
                        rx.separator(),
                        rx.heading('Complex'),
                        rx.markdown('A complex represents a real and imaginary number with a unit. They are written using `var=3+5j`'),
                        rx.separator(),
                        rx.heading('Boolean'),
                        rx.markdown('A boolean, or "bool", represents true or false. They are written using `var=True` or `var=False`'),
                        rx.separator(),
                        rx.heading('NoneType'),
                        rx.markdown('A nonetype, or "None", represents nothing. They are written using `var=None`'),
                        rx.separator(),
                        rx.heading('Array'),
                        rx.markdown('Array variables contain more than one value. These include lists, tuples, sets, and dictionarys.'),
                        rx.separator(),
                        rx.heading('List'),
                        rx.markdown('Lists are unorgainzed sets of values. They are written by using `var=[\'Hello\', \'World!\', 2, True, None]`.'),
                        rx.separator(),
                        rx.heading('Using specific list values'),
                        rx.markdown('Grabbing a value from a list can be done by using `var[0]`, where `var` is the list and `0` is the value\'s id (Starting at zero).<br>Using this method, we can also edit specific values as well, using `var[0]=new_value`, where `var` and `0` are the same as before, but `new_value` is the value we want to assign the list.'),
                        rx.separator(),
                        rx.heading('Tuples'),
                        rx.markdown('Tuples are unorgainzed sets of values that are uneditable. They are written by using `var=(\'Hello\', \'World!\', 2, True, None)`'),
                        rx.separator(),
                        rx.heading('Sets'),
                        rx.markdown('Lists and Sets are almost the same, but a set can\'t have values they are the same. They are written using `var={\'Value\', \'A different value\'}`'),
                        rx.separator(),
                        rx.heading('Dictionarys'),
                        rx.markdown('Dictionarys and Sets are written the same except for one thing. Dictionarys have `key:value` pairs, for example `var={\'key\':\'value\', \'NOT the same key\':\'same/different value\'}`'),
                    )
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
#Add all pages
app = rx.App()
app.add_page(index, title='Home', route='/')
app.add_page(r1, title='Reading/Videos Log | 1', route='/1/')
app.add_page(r3a, title='Local and Global Variables | 3a', route='/3/a')
app.add_page(r3bc, title='Local and Global Variables | 3b & 3c', route='/3/bc')
app.add_page(r3d, title='Local and Global Variables | 3d', route='/3/d')
app.add_page(r4a, title='Palendrome Checker | 4a', route='/4a/')