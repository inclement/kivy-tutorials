
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

Brief explanations of what's going on are given along the way. I
recommend going through every one of these examples


1) Say Hello
------------

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
