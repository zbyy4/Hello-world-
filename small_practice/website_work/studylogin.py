from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout
from bokeh.models import widgets as wd, ColumnarDataSource
from bokeh.core.properties import value

# Login
btnLogin = wd.Button(label="Login")
btnReset = wd.Button(label="Reset")
name = wd.TextInput(title="Name",
    placeholder="enter name ....")
pwd = wd.TextInput(title="Password",
    placeholder="enter password ....")

login = layout( [
        [ wb(name) ],
        [ wb(pwd) ],
        [ wb(btnLogin), wb(btnReset) ]
    ] )

# Study
majors = wd.RadioButtonGroup(labels=["CSC", "STA",
    "MAT", "EIE", "ENE", "HSS", "SME"])
text = wd.Paragraph(text="Press button to start ...." )
answer = wd.Paragraph(text="")
btnRandom = wd.Button(label="Choose for me")

study = layout( [
        [ wb(majors, width=800) ],
        [ wb(text, btnRandom, answer) ]
    ] )

page1 = wd.Panel(child=login, title="login")
page2 = wd.Panel(child=study, title="Study")

tabs = wd.Tabs( tabs=[page1, page2] )

curdoc().add_root(tabs)