
Kivy Intro
==========

A series of short tutorials intended as an introduction to Kivy.

You'll first need to `install Kivy <https://kivy.org/#download>`_, but
from there should be able to dive straight in with these brief
tutorials.

These tutorials take a similar path to my `Kivy crash course
<http://inclem.net/pages/kivy-crash-course/>`_ videos and articles,
but are targeted more as quick text exercises to quickly get started
with Kivy.


1) Say Hello
------------

**Central themes:** Starting an App, getting Kivy running

It's compulsory that the introduction to any programming project
should contain a "Hello World!" application. Since Kivy is a GUI
framework, that means starting an application and displaying the words
on the screen. Start by adding each of the following lines to your
program::

  from kivy.app import App
  
This imports the :code:`App` class, something you'll be using in any
Kivy application. Your instance of this class will create the Kivy
window and serve as the top level of your application

.. code-block:: python
   
   from kivy.uix.label import Label
  
This introduces one of Kivy's most important components; the
Widget. Your entire application will be built with Widgets, each of
which does a single (relatively) small task. For instance, Label is a
Widget that displays some text, Button is (obviously) a button, and
Layouts are Widgets that contain other Widgets and lay them out in
some particular arrangement.

You can find the documentation for Label `here
<https://kivy.org/docs/api-kivy.uix.label.html>`__. We'll need this
later!.

In every Kivy application, your first task is to create an App
subclass as follows::

    class YourApp(App):
        def build(self):
        root_widget = Label(text='Hello world!')
        return root_widget

The :code:`build` method is the only important addition you have to
make, and is the usually the first entry point for your use of a Kivy
application. This method must instantiate and return what will be your
**root widget**, the top level widget of your Kivy application, which
will contain anything else you add.

The root widget will automatically fill the window, so in this case
the Label text will appear right in the middle.

In our case, the application will only ever need a single Widget; the
Label displaying our text. We set the text by simply passing it as an
argument. This works automatically because :code:`text` is a *Kivy
property* of the Label widget...but that doesn't matter right now.

Finally, add a line to start and run the Application::

    YourApp().run()
    
This *instantiates* and *runs* the instance of your App. Any Kivy
application is created and started with some variation of these
basic steps.

Now...run the code!

.. code-block:: 

   python your_filename.py

You should see a Window something like the following
image. Congratulations, you've written and run your first Kivy
application.

Full code
~~~~~~~~~

your_filename.py::

  from kivy.app import App
  from kivy.uix.label import Label
  
  class YourApp(App):
      def build(self):
      root_widget = Label(text='Hello world!')
      return root_widget
  
  YourApp().run()


2) A fancier appearance: Customising widgets using Properties
-------------------------------------------------------------

**Central themes:** Modifying Widget appearance, Kivy properties


It's great to say Hello World, but it looks pretty boring, and you'd
expect that you'd be able to customise the appearance of
text. Fortunately, you'd be right...so let's do it.

We'll continue modifying the code from last time, which was::

  from kivy.app import App
  from kivy.uix.label import Label
  
  class YourApp(App):
      def build(self):
      root_widget = Label(text='Hello world!')
      return root_widget
  
  YourApp().run()

The basic way to modify things in Kivy is to change *Kivy properties*
of the widgets. As far as we're concerned right now, we can set these
by passing arguments at instantiation, or by treating them as
attributes of the class. For instance, we could also have set the text
as follows::

    root_widget = Label()
    root_widget.text = 'Hello world!'
    
Let's set ourselves three goals:

- Make the text larger
- Italicise the text
- Colour "Hello" and "world!" differently
  
To customise the Label appearance, we must check the documentation to
find an appropriate Kivy property. For the text size, check the `Label
doc <https://kivy.org/docs/api-kivy.uix.label.html>`__ and find the
:code:`font_size` listing. It looks something like the following:
  
.. image:: font size
           
Following the documentation, this lets us set the font size in pixels,
and it defaults to ``'15sp'``. This is a special Kivy syntax, the sp
units automatically scale the font size according to the DPI of the
display and the user's font size setting (on some platforms); on
desktop on a non-hidpi display, it is just 15 pixels. For now let's
just set a simple pixel number::

    root_widget = Label(
        text='Hello world!',
        font_size=100)

You can run the code now to see the result.

To make the text italic, the procedure is the same. Check the `Label doc
<https://kivy.org/docs/api-kivy.uix.label.html>`__ and find the
:code:`italic` property entry. you'll see that this is a
BooleanProperty that defaults to False; just set it to True to enable
the underline::

    root_widget = Label(
        text='Hello world!',
        font_size=100,
        italic=True)

Finally, we want to colour ``Hello`` and ``world!``
differently. Things are a little different here as we can't use a
single property setting to modify the whole string, since the two
words should be treated differently.

Instead we enable the `markup property
<https://kivy.org/docs/api-kivy.uix.label.html#kivy.uix.label.Label.markup>`__::

    root_widget = Label(
        text='Hello world!',
        font_size=100,
        underline=True,
        markup=True)
        
You can now use Kivy's `markup syntax
<https://kivy.org/docs/api-kivy.uix.label.html#markup-text>`__ to
modify the text within the Label. Try the following::

   root_widget = Label(
       font_size=100,
       italic=True,
       markup=True)
   root_widget.text = '[color=#ff0000]Hello[/color] [color=#00ff00]world![/color]'
   
Now run the application again, :code:`python your_filename.py`. The
result should now look something like the following image.

.. image:: 2 result
           
.. note:: This is just a basic introduction to customising Kivy
          widgets, you can use similar methods to accomplish many
          different changes in many different scenarios. Kivy
          properties also have other important functionality, covered
          later in these tutorials.

           
Full code
~~~~~~~~~

The full code for this exercise was::

    from kivy.app import App
    from kivy.uix.label import Label

    class YourApp(App):

        def build(self):
            root_widget = Label(
                font_size=100,
                italic=True,
                markup=True)
            root_widget.text = '[color=#ff0000]Hello[/color] [color=#00ff00]world![/color]'
            return root_widget

    YourApp().run()
    

3) Building a full GUI
----------------------

**Central themes:** Adding Widgets to one another

The tutorals so far have covered the very basics of a Kivy
application; getting everything running, adding a Widget (the Label),
and doing some customisation.

Let's now *combine* some widgets to make a larger GUI. This tutorial
will solely cover joining the widgets together, not making them do
anything; this is covered in later tutorials.

.. note:: This tutorial will construct the GUI using entirely Python
          code. You can always do this with Python as described here,
          but normally we recommend using the easier, clearer and more
          concise `kv language
          <https://kivy.org/docs/guide/lang.html>`__ to construct
          widget trees. This will be covered fully in later tutorials.
          
Our new task will be to build a simple calculator app; we'll need
Buttons for each of the numbers and mathematical operations, and a
Label to display the result.

Let's start with a new basic app structure::

    from kivy.app import App

    class YourApp(App):

        def build(self):
            return None

    YourApp().run()

Right now, you can run the code but the window will be empty because
we didn't add any widgets. Let's do that now, but we no longer want
just a Label; our app will be made of multiple Widgets next to one
another. For this, we use Layout classes; let's start with the
following::

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout


    class YourApp(App):
        def build(self):
            layout = BoxLayout(orientation='vertical')
            b1 = Button(text='button 1')
            b2 = Button(text='button 2')

            layout.add_widget(b1)
            layout.add_widget(b2)

            return layout


    YourApp().run()
    
We're now instantiating three Widget classes; the BoxLayout and two
Buttons. Just like with the Label, each one can be customised by
passing properties. The only new one here is the :code:`orientation`
of the BoxLayout; passing :code:`'vertical'` means it will place its
children below one another. The Buttons are internally a Label with a
background image and touch behaviour (you can see this in the `Button
documentation
<https://kivy.org/docs/api-kivy.uix.button.html#kivy.uix.button.Button>`__,
check the 'Bases:'), so we can use the Label's text property just like
before.

After instantiating the widgets, we can *add* them to one another. You
can almost always add any widget instance to any other in exactly this
way. When you do so, the newly added widgets will appear on the
screen, and you'll be able to interact with them.  The widget you add
to is called the *parent widget*, and the added widget (in this case
the Buttons) is the *child widget*.

This code should give you something like the following image. You can
also now click the buttons to see their colour change; this behaviour
is automatic, they don't do anything else yet.

  .. image:: two buttons

Try setting the BoxLayout orientation to :code:`'horizontal'` to see
how it affects the result.

Resize the window, and note that the sizes and positions of the
buttons update automatically. This happens because the BoxLayout
repositions and resizes its children when its own size changes, and
because it is the root widget its own size tracks that of the
window. This is **very important**! If you replace the BoxLayout with
a plain Widget (:code:`from kivy.uix.widget import Widget`) this will
*not* happen, the Buttons will both have their default position and
size in the bottom left of the window. For this reason, you'll want to
use Layouts like BoxLayout all the time to automatically position
things, though you can also create your own automatic bindings (see
later tutorials on Kivy Properties).

With these basic ideas in hand, let's proceed to add Widgets
representing our entire calculator interface::

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label


    class YourApp(App):
        def build(self):
            root_widget = BoxLayout(orientation='vertical')

            output_label = Label(size_hint_y=1)  

            button_symbols = ('1', '2', '3', '+',
                              '4', '5', '6', '-',
                              '7', '8', '9', '.',
                              '0', '*', '/', '=')

            button_grid = GridLayout(cols=4, size_hint_y=2) 
            for symbol in button_symbols:
                button_grid.add_widget(Button(text=symbol))

            clear_button = Button(text='clear', size_hint_y=None,
                                  height=100)

            root_widget.add_widget(output_label)
            root_widget.add_widget(button_grid)
            root_widget.add_widget(clear_button)

            return root_widget


    YourApp().run()

This introduces a couple of new ideas; the GridLayout is a new layout
class that arranges its child widgets in (you guessed it) a
grid. We've set its :code:`cols` property to :code:`4`, which means
that every 4 widgets we add it will start a new row. Since we add 16
buttons altogether, that's 4 rows of 4.

The other new idea here is the :code:`size_hint_y` setting for the
output_label and button_grid. All widgets have a :code:`size_hint_x`
(horizontal) and :code:`size_hint_y` (vertical) that you can set. They
are used by Layout classes to set relative sizes; in this case, the
the one with :code:`size_hint_y=2` takes up twice as much vertical
space as the one with :code:`size_hint_y=1`.

You can also override the size hint to set a manual width and/or
height for your Widget, but you must do this explicitly, as shown here
with the 'clear' button. By setting :code:`size_hint_y=None`, we
ensure that its :code:`height=100` is never overridden, this Button
will have a height of 100 pixels no matter what.

Your final code should look something like the image below. You can
resize the window to see all the components move around and resize
automatically, thanks to the use of Layouts for positioning.

.. image:: calculator gui

You are *strongly encouraged* to experiment with modifying this code
to see what happens. All the concepts used here are standard when
working with Kivy widget positioning.

The calculator GUI clearly doesn't do anything yet (although you can
click on the buttons due to their default behaviour). Adding some
functionality is covered in the next tutorial.


Full code
~~~~~~~~~

your_filename.py::

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label


    class YourApp(App):
        def build(self):
            root_widget = BoxLayout(orientation='vertical')

            output_label = Label(size_hint_y=1)  

            button_symbols = ('1', '2', '3', '+',
                              '4', '5', '6', '-',
                              '7', '8', '9', '.',
                              '0', '*', '/', '=')

            button_grid = GridLayout(cols=4, size_hint_y=2) 
            for symbol in button_symbols:
                button_grid.add_widget(Button(text=symbol))

            clear_button = Button(text='clear', size_hint_y=None,
                                  height=100)
                
            root_widget.add_widget(output_label)
            root_widget.add_widget(button_grid)
            root_widget.add_widget(clear_button)

            return root_widget


    YourApp().run()

    
4) Making the GUI do stuff: binding to events
---------------------------------------------

**Central themes:** Events and Kivy properties

We left the last tutorial with a calculator app GUI with some nice
automatic behaviour, but which doesn't actually do anything. Let's
change that; it's time to learn about *binding events*.

To refresh, the basic calculator GUI code was as follows. If you
modified it to experiment, feel free to continue with your modified
code, and try to change the instructions to fit your modifications::

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label


    class YourApp(App):
        def build(self):
            root_widget = BoxLayout(orientation='vertical')

            output_label = Label(size_hint_y=1)  

            button_symbols = ('1', '2', '3', '+',
                              '4', '5', '6', '-',
                              '7', '8', '9', '.',
                              '0', '*', '/', '=')

            button_grid = GridLayout(cols=4, size_hint_y=2) 
            for symbol in button_symbols:
                button_grid.add_widget(Button(text=symbol))

            clear_button = Button(text='clear', size_hint_y=None,
                                  height=100)

            root_widget.add_widget(output_label)
            root_widget.add_widget(button_grid)
            root_widget.add_widget(clear_button)

            return root_widget


    YourApp().run()
    
.. note:: This tutorial introduces some major new Kivy concepts. I
          recommend working through it even if you don't entirely
          follow what's going on, then going back to modify components
          and see how things change.

The plan now is that every one of these buttons should add their
symbol to the Label at the top, except '=' which should evaluate the
code and display the result. This is obviously an extremely basic
calculator, but the point here is to showcase some Kivy basics - if
you'd like to improve the interface, go ahead with trying to do so
along the way.

To make the buttons do something, we must *bind* to their events. This
is a generic Kivy concept; whenever you want one thing to trigger
another, you look for an event to bind to. Some widgets such as Button
have events indicating they have been clicked on, and every Kivy
property (such as all those used to customise Widgets so far) has an
associated event when it changes.

Let's start with a simple binding example::

    def print_button_text(self, instance):
        print(instance.text)
        for button in button_grid.children[1:]:  # note use of the
                                                 # `children` property
            button.bind(on_press=print_button_text)
     
If you run the code now, and click on any of the buttons, you should
see its text printed in the console (but not in the Kivy GUI).

The key concept here is the :code:`bind` method, which you can use
with any Widget, as well as several other Kivy objects (discussed in
later tutorials). This takes any number of keyword arguments, each
specifying an *event name* and a *function to call*; in this case the
event name is :code:`on_press`, and the function to be called is our
new :code:`print_button_text`. The :code:`bind` method makes sure that
whenever :code:`on_press` occurs, the function is called. It
automatically receives a single argument, the binded widget instance.

Also note that we've iterated over
:code:`button_grid.children[1:]`. The :code:`children` property is
available on any Widget, and holds a list of all the widgets added to
it, in reverse order. In this case, we use :code:`[1:]` to skip the
first element, '=', as we want to use this to evaluate the result.

.. note:: Button also has an :code:`on_release` event that is called
          when the user releases a click or touch. You can find more
          information in the `Button documentation
          <https://kivy.org/docs/api-kivy.uix.button.html>`__.

This binding idea is very normal in Kivy, and you'll quickly get used
to seeing it used in different ways, including some introduced later
in these tutorials. The kv markup language, also introduced later,
has special syntax designed to make it even simpler and clearer.

Anyway, all this does so far is print some text when the event occurs,
but we want to update the GUI. Let's change the bound function to
achieve that::

        def print_button_text(instance):
            output_label.text += instance.text

Run the code again. Now when you press the buttons, you should see the
text appear at the top of the screen, as in the screenshot below:

.. image:: button updated
           
         
At this point, a new problem presents itself; the font size of the
label is kind of small. We can use another event to have it update
automatically in response to the label's height::

        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height
        output_label.bind(height=resize_label_text)
        
Note that the event here is named :code:`height`. This works because
the Label has a Kivy property named height (as do all Widgets, see the
`documentation
<https://kivy.org/docs/api-kivy.uix.widget.html#kivy.uix.widget.Widget.height>`__,
and all Kivy properties can be bound to as an event of the same name,
called when the property changes. In this case, you can now resize the
window, which causes the layouts in the Widget tree to automatically
resize their children, which in turn causes :code:`resize_label_text`
to automatically be called. 

We'll use one final binding to make the calculator interface actually
work; when the '=' button is pressed, we can evaluate the entire label
text as python code, and display the result.

.. note:: Using eval as a calculator like this is in general a
          terrible idea, used here only to avoid dwelling on the
          details rather than the Kivy principles.
            
.. code-block:: python

        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python syntax error!'
        button_grid.children[0].bind(on_press=evaluate_result)
        # Remember, button_grid.children[0] is the '=' button
        
Further, we can make the 'clear' button clear the label, so that you
can start a new calculation::

        def clear_label(instance):
            output_label.text = ''
        clear_button.bind(on_press=clear_label)

With this all in place, run the app again and...the calculator works!
Every button now does something, either adding its symbol to the
output label, evaluating the label's text as python code, or clearing
the result. You should be seeing something like the image below:

.. image:: calculator final

These core event binding concepts are central to working with Kivy
widgets, and come up in many different ways. Don't worry if you don't
remember all the details straight away, such as the way all properties
have events you can bind to, or the specific syntax; you can look all
this up in the documentation as linked throughout and indexed on the
`Kivy website <https://kivy.org/docs/api-kivy.html>`__. Later
tutorials also follow on to help cement this knowledge.

Full code
~~~~~~~~~

your_filename.py::

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label


    class YourApp(App):
        def build(self):
            root_widget = BoxLayout(orientation='vertical')

            output_label = Label(size_hint_y=1)  

            button_symbols = ('1', '2', '3', '+',
                              '4', '5', '6', '-',
                              '7', '8', '9', '.',
                              '0', '*', '/', '=')

            button_grid = GridLayout(cols=4, size_hint_y=2) 
            for symbol in button_symbols:
                button_grid.add_widget(Button(text=symbol))

            clear_button = Button(text='clear', size_hint_y=None,
                                  height=100)

            def print_button_text(instance):
                output_label.text += instance.text
            for button in button_grid.children[1:]:  # note use of the
                                                 # `children` property
                button.bind(on_press=print_button_text)

            def resize_label_text(label, new_height):
                label.font_size = 0.5*label.height
            output_label.bind(height=resize_label_text)

            def evaluate_result(instance):
                try:
                    output_label.text = str(eval(output_label.text))
                except SyntaxError:
                    output_label.text = 'Python syntax error!'
            button_grid.children[0].bind(on_press=evaluate_result)

            def clear_label(instance):
                output_label.text = ''
            clear_button.bind(on_press=clear_label)

            root_widget.add_widget(output_label)
            root_widget.add_widget(button_grid)
            root_widget.add_widget(clear_button)

            return root_widget


    YourApp().run()


5) A new App: basic paint
   
**Central themes:** Canvas instructions

The next couple of tutorials will move to a new application in order
to showcase some more of Kivy's core components. In this tutorial
we'll cover *canvas instructions*, Kivy's low level drawing API which
is always available. In the next two, we'll add touch/mouse
interaction to let you click to draw stuff, and then introduce *kv
language*, and show how it interacts with Python code to easily
produce guis without so much Python boilerplate.

To showcase Kivy's drawing API, our next app will be a simple drawing
application. We'll be making a widget gui to select a few different options
(colour, size etc.), and handling the mouse/touch interaction manually
to draw the result of user input.

We'll need to start with a new basic app template, as introduced in
the first couple of tutorials::

    from kivy.app import App


    class DrawingApp(App):
        def build(self):
            return None

    DrawingApp().run()
    
Before anything else, let's start by getting some basic drawing
working, with no other gui components. There isn't a Widget for
drawing already (there's no nice way to abstract all the options you
might want), so instead Kivy makes it easy to build your own Widget
class::

    from kivy.uix.widget import Width

    class DrawingWidget(Widget):
        pass
        
    class DrawingApp(App):
        def build(self):
            return DrawingWidget()

    DrawingApp().run()
            
You can run the app now, but the screen will just be black because
Widget (and therefore DrawingWidget) doesn't draw anything by default.
We're using Widget as the base class because we want to add it to the
screen, but don't need any extra behaviour beyond that.

Time to do our own drawing. Change your code to add the following::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 0, 0, 1)  # the arguments are red, blue,
                                   # green, alpha
                Rectangle(size=(300, 100),
                          pos=(300, 200))


    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()

If you run the app now, you'll see a red rectangle. Its position in
pixels will be 300 right and 200 up from the bottom left of the
screen; Kivy's coordinate system follows OpenGL in having its
coordinate origin there.

.. image:: example rectangle

This is the basic way of doing any kind of drawing, and with a
combination of canvas instructions (also called graphics instructions)
you can achieve any kind of gui result. In fact, anything you see
drawn with Kivy is ultimately using canvas instructions, including all
the built in widget classes!

The basic procedure always follows this one. First, open a :code:`with
self.canvas` block - this sets an internal variable that means all
graphics instructions are drawn to the canvas of the current
widget. All widgets have a canvas, you can draw on e.g. a Label or
BoxLayout if you want. Second, instantiate any graphics instructions;
in this case we use Color (which sets the colour of any following
instructions) and Rectangle (which draws a rectangle at the given
position). Any instructions you add later will be drawn on top of the
previous ones.

Try changing these arguments to modify what you see. The arguments to
Color are red, green, blue and alpha components (currently opaque
red). You can also try drawing other shapes by checking the `vertex
instruction documentation
<https://kivy.org/docs/api-kivy.graphics.vertex_instructions.html>`__
(vertex instructions are shapes, other instructions like Color are
claled context instructions and include e.g. translation and
rotation).

.. note:: As with several other things mentioned so far, canvas
          instructions have their own simple syntax for drawing in kv
          language, introduced in tutorial 7.

.. note:: You can also access :code:`self.canvas.before` and
          :code:`self.canvas.after`; everything in the former is drawn
          first, then everything in :code:`self.canvas`, then
          everything in :code:`self.canvas.after`. This helps you to
          draw in layers if necessary.

Let's now draw a Rectangle filling the whole DrawingWidget, serving as
the background of anything we draw::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                Rectangle(size=self.size,
                          pos=self.pos)


    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()

Surprise, it doesn't work right! Although we set the rectangle size to
self.size (the size of the DrawingWidget), and its pos to self.pos
(the pos of the DrawingWidget), it always appears in the bottom left
of the window and has size 100 pixels square. This is because
although the DrawingWidget fills the window (because it is the root
widget), its pos and size are not set until *after* its
:code:`__init__` method has finished.

.. note:: :code:`pos` and :code:`size` are two more Kivy properties
          that all widgets have. They give the position of the bottom
          left corner (in pixels) and the size of the Widget (also in
          pixels).

To solve this problem, we again use *event bindings*::

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size
            
This works just like in the previous tutorials; we've bound to the
:code:`pos` and :code:`size` of the widget, and made it so that
whenever they update the Rectangle is also updated. Remember, this is
possible because :code:`pos` and :code:`size` are Kivy properties,
which you can also bind to (the function is called when their value
changes). When run, your app should now look like the following:

.. image:: white background, red rectangle

This tutorial has introduced the basic use of *canvas instructions*,
including the notion of automatically updating them in response to gui
changes, thanks to event binding. This is an important building block
for building complex applications.

In the next tutorial we'll introduce mouse/touch input handling, so
that we can finally draw something dynamicall in response to user
input.


Full code
~~~~~~~~~

main.py::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size



    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()


6) Let's draw something
-----------------------

**Central themes:** Handling touch or mouse input, more canvas instructions

In this tutorial we'll directly add touch handling to the basic code
developed in tutorial 5, starting with the code from last time::

  
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
                Color(1, 0, 0, 1)  # note that we must reset the colour
                Rectangle(size=(300, 100),
                          pos=(300, 200))
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size



    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()

We've already seen some input interaction via the Button widget, where
we could bind to its :code:`on_press` event to have a function called
whenever the Button was clicked. This is great for a Button, but is
not a general way to handle interaction - it gives no indication of
the position of the touch, or any other information like the button
clicked on the mouse.

Kivy achieves general mouse/touch handling via the
:code:`on_touch_down`, :code:`on_touch_move` and :code:`on_touch_up`
methods of all Widget classes. Let's dive in with an example,
modifying our DrawingWidget::

    from random import random

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
                self.rect_colour = Color(1, 0, 0, 1)  # note that we must reset the colour
                Rectangle(size=(300, 100),
                          pos=(300, 200))
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size

        def on_touch_down(self, touch):
            self.rect_colour.rgb = (random(), random(), random())
            print('touch pos is {}'.format(touch.pos))
            
Note that the only changes are to set :code:`self.rect_colour`, and to
add the :code:`on_touch_down` method. Run the code now, and whenever
you click the screen you should see the colour of the rectangle change.

How does this work? The answer is that whenever a mouse click or touch
is registered, the root widget's :code:`on_touch_down` method is
called, with a :code:`touch` object holding information about the
touch: you can see this here, where we access the :code:`pos` of this
object to get the pixel coordinates of its position. Each widget
passes this touch object to all its children. For this reason, it's
important to call :code:`super(...)` if you want the touch to also be
passed to the current Widget's children, though as it happens that's
not actually important here.

Note that although these methods are called :code:`on_touch_...`, and
I've called the argument :code:`touch`, they relate to both mouse and
touch handling; these events are handled in exactly the same way,
except that the touch object may contain different information such as
the button clicked (in the case of the mouse). I'll switch to mostly
referring to this input as 'touch', but this always includes mouse
interaction too.

The other methods I mentioned, :code:`on_touch_move` and
:code:`on_touch_up`, work the same way; they are called whenever that
thing happens, though only when :code:`on_touch_down` has already
happened, you don't get events when moving the mouse without having
clicked. We can use this to achieve drawing. 

First, change the kivy.graphics import to include :code:`Line`::

    from kivy.graphics import Rectangle, Color, Line
    
Then, add modify :code:`on_touch_down` and :code:`on_touch_move` to
draw and update a Line each time::

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        with self.canvas:
            Color(random(), random(), random())
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
  
Run the code again, and try clicking and dragging...you should see a
line! Each time you click and drag the line has a different colour, as
we add a new random Color instruction before its instruction each
time. We're updating it by adding the x and y value of the touch
position to the Line's points, every time the touch is moved.

.. image:: app with lines
           
You can also note that we only use :code:`with self.canvas` when the
Line is instantiated - not when it is updated. This is because we only
need to add the Line canvas instruction to the canvas once, after that
the gui will automatically be updated whenever the Line changes,
including if we modified e.g. its width. Try changing
:code:`self.line.width` in :code:`on_touch_move` and see what happens.
      
.. note:: This way of storing the line (in :code:`self.line`) isn't
          very robust if there are multiple simultaneous interactions,
          e.g. in a multitouch display. This is easy to resolve by
          storing the reference more cleverly, including in the touch
          object itself, but I've just ignored the issue here.

You could continue here by experimenting with other actions in
response to touches, such as drawing different things (e.g. a
Rectangle at the touch position rather than a Line) or doing more
complex modifications to existing instructions.

With the basic drawing apparatus set up, the next tutorial will
introduce the *kv markup language*, showing how a gui can easily be
constructed without some of the Python boilerplate that comes from
using a general purpose language for creating a gui. 


Full code
~~~~~~~~~

main.py::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color, Line

    from random import random

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
                self.rect_colour = Color(1, 0, 0, 1)  # note that we must reset the colour
                Rectangle(size=(300, 100),
                          pos=(300, 200))
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size

        def on_touch_down(self, touch):
            super(DrawingWidget, self).on_touch_down(touch)

            with self.canvas:
                Color(random(), random(), random())
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

        def on_touch_move(self, touch):
            self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()

    
7) Introducing kv language
--------------------------

**Central themes:** kv language, building a gui, integration with Python

The goal of this tutorial will be to build up a simple gui around the
DrawingWidget built in the last two tutorials. A nice simple goal
would be to let the user select the colour of the lines. Kivy actually
has a ColorPicker Widget for this purpose (see the `documentation
<https://kivy.org/docs/api-kivy.uix.colorpicker.html>`__), but we'll
skip that for now in order to continue demonstrating Kivy widget
construction.

.. note:: Since all Kivy widgets are built out of other Widgets and
          canvas instructions, you might like to think about how you'd
          build the ColorPicker from scratch.
          
Let's start with the code from last time, minus the now-unnecessary
red Rectangle::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color, Line

    from random import random

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)


        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size

        def on_touch_down(self, touch):
            super(DrawingWidget, self).on_touch_down(touch)

            with self.canvas:
                Color(random(), random(), random())
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

        def on_touch_move(self, touch):
            self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


    class DrawingApp(App):

        def build(self):
            root_widget = DrawingWidget()
            return root_widget

    DrawingApp().run()

I'll demonstrate adding the new gui components in two ways; first in 
pure Python as has been demonstrated in previous tutorials, and second
using kv language instead. So, here's a Python implementation of the
new features we want, beginning with importing the Widget classes
we'll need::

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.slider import Slider
    
Slider is a previously-unseen Widget displaying a draggable marker. We'll be using a
Slider for each primary colour (red, blue, green), and using this to
set the Color when a Line is drawn.

We can now update the build method of DrawingApp, replacing the root
widget and adding the new gui components::

    class DrawingApp(App):

        def build(self):
            root_widget = BoxLayout(orientation='vertical')

            drawing_widget = DrawingWidget()

            red_slider = Slider(min=0, max=1, value=0.5,
                                size_hint_y=None, height=80)
            green_slider = Slider(min=0, max=1, value=0.5,
                                size_hint_y=None, height=80)
            blue_slider = Slider(min=0, max=1, value=0.5,
                                size_hint_y=None, height=80)

            colour_row = BoxLayout(orientation='horizontal',
                                   size_hint_y=None, height=80)
            colour_label = Label(text='output colour:')
            colour_widget = Widget()

            # We draw a Rectangle on colour_widget exactly the same way as
            # with DrawingWidget, just without making a new class
            with colour_widget.canvas:
                output_colour = Color(red_slider.value,
                                      green_slider.value,
                                      blue_slider.value)
                output_rectangle = Rectangle()
            def update_colour_widget_rect(instance, value):
                output_rectangle.pos = colour_widget.pos
                output_rectangle.size = colour_widget.size
            colour_widget.bind(pos=update_colour_widget_rect,
                               size=update_colour_widget_rect)

            def update_colour_widget_colour(instance, value):
                output_colour.rgb = (red_slider.value,
                                     green_slider.value,
                                     blue_slider.value)
            red_slider.bind(value=update_colour_widget_colour)
            green_slider.bind(value=update_colour_widget_colour)
            blue_slider.bind(value=update_colour_widget_colour)

            root_widget.add_widget(drawing_widget)
            root_widget.add_widget(red_slider)
            root_widget.add_widget(green_slider)
            root_widget.add_widget(blue_slider)
            root_widget.add_widget(colour_row)

            colour_row.add_widget(colour_label)
            colour_row.add_widget(colour_widget)

            return root_widget
            
This is a lot of code to drop all at once, but read it carefully and
you'll see that it's only the same concepts already introduced: we
instantiate Widgets, add them to one another, and create bindings so
that things automatically happen when Kivy properties are changed. In
this case, we make use of the :code:`value` Kivy property of the
Slider widget, which gives its current value (changing automatically
when the slider is moved).

Run the code and you should see something like the image below. You
can update the colour in the bottom right by moving the sliders. Cool.

.. image:: code with sliders
           
A problem now becoming obvious is that all this code is kind of
verbose, and also it can be a little unclear what is happening -
Widget instantiation is in a different place to where the Widgets are
added to one another, which is different again to where their events
are bound. You can mitigate this with a careful app structure and
following whatever coding conventions you like, but some of it is
unavoidable given how Python works.

It's for this reason that Kivy comes with *kv language*, a simple but
powerful language specifically designed for creating Kivy widget
trees. If learning a new language sounds worrying...don't be
concerned! Kv doesn't have much special syntax and is targeted
specifically at Kivy widgets, and much of the code you write is
actually normal Python (we'll see that soon).

All of the kv language stuff discussed below is `documented on the
Kivy website <https://kivy.org/docs/guide/lang.html>`__; I'll cover
the basics, but you can find more information there.

First, get rid of *all* the Python code from above, and replace the
root widget return with the following::

    class Interface(BoxLayout):
        pass

    class DrawingApp(App):

        def build(self):
            root_widget = Interface()
            return root_widget

kv language works by writing *rules* for Widget classes, which will be
automatically applied every time you instantiate one. We can use kv
for almost everything added to the app so far, but this time we'll
construct the gui step by step to see how each part is added with the
new kv syntax. We'll be writing a kv rule for the new
:code:`Interface` class.

To start using kv language, write the following code in a file named
``drawing.kv``. This name comes from the name
of the App class, minus the App at the end if present, and in
lowercase (e.g. if you named your App :code:`MySuperKivyApp` you'd
need to name the file ``mysuperkivy.kv``). This is only necessary if
you want the file to be automatically loaded, you can also `load files
or string manually
<https://kivy.org/docs/guide/lang.html#how-to-load-kv>`__. Our first
kv code is::

    <Interface>:
        orientation: 'vertical'
        Label:
            text: 'label added with kv'
            font_size: 50

Run the code again, and you should see the a Label with the given
text, as the kv file is automatically loaded and its
:code:`<Interface>` rule applied.
      
.. image:: example of label added with kv
     
This demonstrates the core rules of kv syntax. A *kv rule* is created
with the :code:`<WidgetName>:` syntax. You can make a rule for *any*
widget, including built in ones (Kivy internally has a `large kv file
<https://github.com/kivy/kivy/blob/master/kivy/data/style.kv>`__), and
if you make multiple rules for the same Widget then all of them are
applied one by one.

Below the rule creation, we indent by 4 spaces and define values for
Kivy properties of the widget, and add child widgets. Lines like
:code:`orientation: 'vertical'` set Kivy properties just like we did
previously in the Python code. Note that everything to the right of
the colon is *normal Python code* - that doesn't matter here, but for
instance we could equally well write :code:`orientation: ''.join(['v',
'e', 'r', 't', 'i', 'c', 'a', 'l'])` and it would be exactly the
same. You can set any Kivy property of a widget in this way, finding
the available options in the documentation as previously discussed.

We can also add child widgets by writing the widget name with a colon,
then indenting by a further 4 spaces, as is done here with the
:code:`Label`. After this you can keep going as deep as you like,
setting properties or adding more child widgets.

We can use these pieces of syntax to construct the previous Python
interface entirely in kv::

    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:
  
This hasn't yet set up the event binding, but the full widget tree has
been constructed entirely using the kv syntax described above. The
immediate advantage of this is that kv language directly expresses the
widget tree - there are no longer separate steps for instantiating
Widgets, setting their properties and adding them to one
another. Instead, you get to see everything at once.

This gui doesn't yet have the behaviour of the Python one (i.e. having
the sliders control output colour), but in the interest of keeping
these tutorials relatively short, I'll stop here for now. In the next
tutorial will see how kv language also makes event binding very easy.
  

Full code
~~~~~~~~~

main.py::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color, Line

    from random import random

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)

        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size

        def on_touch_down(self, touch):
            super(DrawingWidget, self).on_touch_down(touch)

            if not self.collide_point(*touch.pos):
                return

            with self.canvas:
                Color(random(), random(), random())
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

        def on_touch_move(self, touch):
            if not self.collide_point(*touch.pos):
                return

            self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


    class Interface(BoxLayout):
        pass

    class DrawingApp(App):

        def build(self):
            root_widget = Interface()
            return root_widget

    DrawingApp().run()

drawing.kv::
    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:
            

8) More kv language
-------------------

**Central themes:** Event binding and canvas instructions in kv
language

This tutorial directly follows on from the previous, so start by
retrieving the previous code, as below:

main.py::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color, Line

    from random import random

    class DrawingWidget(Widget):
        def __init__(self):
            super(DrawingWidget, self).__init__()

            with self.canvas:
                Color(1, 1, 1, 1)
                self.rect = Rectangle(size=self.size,
                                      pos=self.pos)
            self.bind(pos=self.update_rectangle,
                      size=self.update_rectangle)

        def update_rectangle(self, instance, value):
            self.rect.pos = self.pos
            self.rect.size = self.size

        def on_touch_down(self, touch):
            super(DrawingWidget, self).on_touch_down(touch)

            if not self.collide_point(*touch.pos):
                return

            with self.canvas:
                Color(random(), random(), random())
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

        def on_touch_move(self, touch):
            if not self.collide_point(*touch.pos):
                return

            self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


    class Interface(BoxLayout):
        pass

    class DrawingApp(App):

        def build(self):
            root_widget = Interface()
            return root_widget

    DrawingApp().run()

drawing.kv::
    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:


The first thing to do is draw the coloured Rectangle that the final
Widget uses to display an output colour, and for this we need to know
how to draw canvas instructions in kv language. The syntax is as below::

        Widget:
            canvas:
                Color:
                    rgb: 0, 1, 0  # using a fixed colour for now
                Rectangle:
                    size: self.size
                    pos: self.pos
                    
Run the code, and you'll see another of kv language's most important
features; *automatic event binding*. In the original Python code of
tutorial 7 we needed an extra :code:`.bind(...)` call to make the
be updated to always be placed within its Widget. In kv language this
is not necessary, the dependency on :code:`self.size` and
:code:`self.pos` is automatically detected, and a binding
automatically created!

This is also the generic syntax for canvas instructions; first add
:code:`canvas:` (or :code:`canvas.before` or :code:`canvas.after`),
then, indent by 4 spaces, and add canvas instructions much like you
would Widgets. However, note that canvas instructions are *not*
widgets.

The only thing now missing from the original Python interface
implementation in tutorial 7 is having the Sliders automatically
update the output colour rectangle. Change the :code:`<Interface>:`
rule to the following::

    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        Slider:
            id: red_slider
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            id: green_slider
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        Slider:
            id: blue_slider
            min: 0
            max: 1
            value: 0.5
            size_hint_y: None
            height: 80
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:
                canvas:
                    Color:
                        rgb: red_slider.value, green_slider.value, blue_slider.value
                    Rectangle:
                        size: self.size
                        pos: self.pos

There are actually only two changes here; we gave each Slider an
:code:`id: ` declaration, and in the canvas Color referred to the
sliders with this name. Giving a widget an id is just like naming it
in Python so that you can refer to it elsewhere.

Thanks to kv's automatic binding, this is all we need to do to have
the Color update automatically whenever a slider value changes. Run
the code, and you should see that things work exactly as they did in
the original Python interface.

We can finish this tutorial with a couple of extra kv
conveniences. First, just as we added an automatically updating
Rectangle in the Widget kv, we can do the same for the background of
the DrawingWidget. Delete the :code:`__init__` and
:code:`update_rectangle` methods in the Python DrawingWidget code, and
add a new rule in the kv file::

    <DrawingWidget>:
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size

Second, you might have noticed that there's a lot of code duplication
in each of the Slider rules - we set the same :code:`min`,
:code:`max`, initial :code:`value`, :code:`size_hint_y`and
:code:`height` for every one. As is normal in Python, it would be
natural to abstract this in a new class, so as to set each value only
once. You can probably already see how to do this with what we've
learned so far (make a new :code:`class YourSlider(Slider):` in the
Python and add a new :code:`<YourSlider>:` rule in the kv), but I'll
note that you can even do this entirely in kv::

    <ColourSlider@Slider>:
        min: 0
        max: 1
        value: 0.5
        size_hint_y: None
        height: 80


    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        ColourSlider:
            id: red_slider
        ColourSlider:
            id: green_slider
        ColourSlider:
            id: blue_slider
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:
                canvas:
                    Color:
                        rgb: red_slider.value, green_slider.value, blue_slider.value
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        
The new :code:`<ColourSlider@Slider>:` rule defines a *dynamic class*,
a Python class kv rule without a corresponding Python code
definition. This is convenient if you want to do something repeatedly
only in kv, and never access it from Python.

At this point, we've reached feature parity with the original Python
code, and seen all the basics of kv language. In the next tutorial
we'll finish off the original purpose of all these sliders; letting
the user set the colour of line that is drawn by the DrawingWidget.

Full code
~~~~~~~~~

main.py::

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.slider import Slider

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.slider import Slider

    from kivy.uix.widget import Widget
    from kivy.graphics import Rectangle, Color, Line

    from random import random

    class DrawingWidget(Widget):
        def on_touch_down(self, touch):
            super(DrawingWidget, self).on_touch_down(touch)

            if not self.collide_point(*touch.pos):
                return

            with self.canvas:
                Color(random(), random(), random())
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

        def on_touch_move(self, touch):
            if not self.collide_point(*touch.pos):
                return

            self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


    class Interface(BoxLayout):
        pass

    class DrawingApp(App):

        def build(self):
            root_widget = Interface()
            return root_widget

    DrawingApp().run()

drawing.kv::

    <DrawingWidget>:
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size

    <ColourSlider@Slider>:
        min: 0
        max: 1
        value: 0.5
        size_hint_y: None
        height: 80


    <Interface>:
        orientation: 'vertical'
        DrawingWidget:
        ColourSlider:
            id: red_slider
        ColourSlider:
            id: green_slider
        ColourSlider:
            id: blue_slider
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
            Label:
                text: 'output colour:'
            Widget:
                canvas:
                    Color:
                        rgb: red_slider.value, green_slider.value, blue_slider.value
                    Rectangle:
                        size: self.size
                        pos: self.pos
