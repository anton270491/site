from jinja2 import  Template

name='VVV'

tm=Template ("hello {{name}}")
msg=tm.render(name=name)

print(msg)
