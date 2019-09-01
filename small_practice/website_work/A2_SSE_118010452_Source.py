import pymssql
import string

from bokeh.io import show, curdoc, output_file
from bokeh.plotting import figure
from bokeh.layouts import widgetbox as wb, layout
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.core.properties import value


global idx1, idx2, idxc, content1, content2
idx1 = idx2 = 1
idxc = 0
content1 = content2 = ''

# Connect server
def connectSQLServer():

    attr = dict(
        server = '10.20.213.10',
        database = 'csc1002',
        user = 'csc1002',
        password = 'csc1002',
        port = 1433,
        as_dict = True
    )

    try:
        return pymssql.connect(**attr)
    except Exception as e:
        print(e)
        quit()


# Here are UI Controls widgets
GroupLetters = wd.RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
dept_input = wd.TextInput(value="", title="Department", placeholder="Seach department")
title_input = wd.TextInput(value="", title="Title", placeholder="Serach title")
options = wd.RadioGroup(labels=['and', 'or'], active=0, width=100, inline=True)
button_refresh = wd.Button(label="Refresh")
Group_choices = wd.RadioButtonGroup(name="Title",
    labels=['Begins with ...', '... contains ...', '... ends with'], active=1)
Department_choices = wd.RadioButtonGroup(name="Department", 
    labels=['Begins with ...', '... contains ...', '... ends with'], active=1)
Text_Instruction = wd.Paragraph(text="Option")

# Data used in Tab1
columns = [
    wd.TableColumn(field="id", title="Course ID"),
    wd.TableColumn(field="title", title="Title"),
    wd.TableColumn(field="dept", title="Department"),
    wd.TableColumn(field="credit", title="Credits"),
    wd.TableColumn(field="instructor", title="Instructor"),
]
data_table = wd.DataTable(columns=columns, source=ColumnDataSource(), width=800)

# Select the department
esql = "SELECT dept_name FROM lgu.department"
sqlConn_1 = connectSQLServer()
with sqlConn_1.cursor(as_dict=True) as cursor_1:
    cursor_1.execute(esql)
    departments = cursor_1.fetchall()
departmentlist = ['All']
for dept in departments:
    departmentlist.append(dept['dept_name'])
dept_select = wd.Select(title="Department:", value="All", options=departmentlist)

# Tab2
gpa = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']  # All possible grades
years = ['2015', '2016', '2017']                         # All possible years
colors = ['#c9d9d3', '#718dbf', '#e84d60']               # Set the colors for the bar

# Build up the figure
data = {}
data['gpa'] = []
for yr in years:
    data[yr] = []

source = ColumnDataSource(data=data)
chart = figure(x_range=gpa, plot_height=500, plot_width=800, title="GPA count by year",
        toolbar_location=None, tools="")

chart.vbar_stack(years, x="gpa", width=0.9, color=colors, source=source,
        legend=[value(x) for x in years])

chart.y_range.start = 0
chart.legend.location = "top_right"
chart.legend.orientation = "vertical"



# Callback functions
# Click the buttons to execute the functions.
def choose(idx):
    global idxc
    idxc = idx

def title_choose(idx=-1):
    global idx1
    idx1 = idx

def dept_choose(idx=-1):
    global idx2
    idx2 = idx

def title_change(attr,old,new):
    global content1
    content1 = new.strip()

def dept_change(attr,old,new):
    global content2
    content2 = new.strip()

# on_click and on_change callback
options.on_click(choose)
Group_choices.on_click(title_choose)
Department_choices.on_click(dept_choose)
title_input.on_change("value", title_change)
dept_input.on_change("value", dept_change)



# Select by letter.
def data_show(idx):
    letter = GroupLetters.labels[idx]
    tsql = "SELECT * FROM lgu.course where title like '{}%'".format(letter)
    sqlConn = connectSQLServer()
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        data={}
        data['id']=[row['course_id'] for row in rows]
        data['title']=[row['title'] for row in rows]
        data['dept']=[row['dept_name'] for row in rows]
        data['credit']=[row['credits'] for row in rows]
        data['instructor']=[row['instructor'] for row in rows]
    data_table.source.data = data


# Refresh botton
def refresh():
    global idx1, idx2, idxc, content1, content2
    tsql="SELECT * FROM lgu.course where"

    if content1 != '':
        if idx1 == 0:
            tsql += " title like '{}%'" .format(content1)
        elif idx1 == 1:
            tsql += " title like '%{}%'" .format(content1)
        elif idx1 == 2:
            tsql += " title like '%{}'" .format(content1)

    if  content1 != '' and content2 != '':
        if idxc == 0:
            tsql += " and" 
        elif idxc == 1:
            tsql += " or"

    if  content2 !='':
        if idx2 == 0:
            tsql += " dept_name like '{}%'" .format(content2)
        elif idx2 == 1:
            tsql += " dept_name like '%{}%'" .format(content2)
        elif idx2 == 2:
            tsql += " dept_name like '%{}'" .format(content2)
    
    sqlConn = connectSQLServer()
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        data={}
        data['id']=[row['course_id'] for row in rows]
        data['title']=[row['title'] for row in rows]
        data['dept']=[row['dept_name'] for row in rows]
        data['credit']=[row['credits'] for row in rows]
        data['instructor']=[row['instructor'] for row in rows]
    data_table.source.data = data

# Groupletterbuttons and refresh callbacks
GroupLetters.on_click(data_show)
button_refresh.on_click(refresh)



# Select Department and callback
# Click the department, the chart will refresh, it will show the GPA count by year.
def select_change(attr, old, new):
    tsql2015 = "select gpa, count(*) as nums from lgu.student where year='2015' "
    tsql2016 = "select gpa, count(*) as nums from lgu.student where year='2016' "
    tsql2017 = "select gpa, count(*) as nums from lgu.student where year='2017' "

    if new != 'All':
        tsql2015 += "and dept_name = '{}' ".format(new)
        tsql2016 += "and dept_name = '{}' ".format(new)
        tsql2017 += "and dept_name = '{}' ".format(new)
    
    tsql2015 += "group by gpa"
    tsql2016 += "group by gpa"
    tsql2017 += "group by gpa"

    sqlConn = connectSQLServer()
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql2015)
        gpa2015 = cursor.fetchall()
        cursor.execute(tsql2016)
        gpa2016 = cursor.fetchall()
        cursor.execute(tsql2017)
        gpa2017 = cursor.fetchall()
    
    grade2015 = []
    grade2016 = []
    grade2017 = []
    count2015 = []
    count2016 = []
    count2017 = []

    for row in gpa2015:
        grade2015.append(row['gpa'])
        count2015.append(row['nums'])
    for row in gpa2016:
        grade2016.append(row['gpa'])
        count2016.append(row['nums'])
    for row in gpa2017:
        grade2017.append(row['gpa'])
        count2017.append(row['nums'])
    
    new_data = {}
    new_data['gpa'] = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    new_data['2015'] = check(grade2015, count2015)
    new_data['2016'] = check(grade2016, count2016)
    new_data['2017'] = check(grade2017, count2017)
    
    source.data = new_data

dept_select.on_change("value", select_change)

# Deal with missing grades
# Some of students' grades are missing so we need to fill it with 0
def check(grade, count):
    standard = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    for i in range(9):
        if standard[i] not in grade:
            count.insert(i, 0)
    return count


# Pages Layout
layout_tab1 = layout(
    [
        [wb(GroupLetters, width=1000)],
        [wb(Group_choices, width=400), wb(Department_choices)],
        [wb(title_input), wb(Text_Instruction, options, width=100), wb(dept_input)],
        [wb(button_refresh,width=100)],
        [wb(data_table)]
    ]
)
layout_tab2 = layout(
    [
        [wb(dept_select), chart]
    ]
)

# Tabs layout
tab1 = wd.Panel(child=layout_tab1, title="Course Info")
tab2 = wd.Panel(child=layout_tab2, title="Statistics")
tabs = wd.Tabs(tabs=[tab1,tab2])


# Display
curdoc().add_root(tabs)