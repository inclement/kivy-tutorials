
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

This code should give you something like the following:

  .. image:: two buttons

