from ursina import *

app = Ursina()
text_string = "lol"
Text.default_resolution = 1080 * Text.size
text_stuff = Text(text=text_string, origin=(0,0), backround=True)
def input(key):
    if key == 'a':
        print("a")
        text_stuff.text = '<default><image:file_icon> <red><image:file_icon> test '
        print('by', text_stuff.text)
window.fps_counter.enabled = False
print('....', Text.get_width('yes'))
app.run()
app.run()
app.run()
app.run()
app.run()
app.run()
app.run()