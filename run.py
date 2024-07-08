#invoice_number = 'KA-B1-77166244'
#month = 'Jul'
#year = '2022'
#invoice_date = '01/07/2022'
#due_date = '15/07/2022'
#end_date = '31/07/2022'
#number_of_days = '31'

import yaml
from pathlib import Path
import os

#from html2image import Html2Image

with open('input.yaml') as fh:
    data = yaml.unsafe_load(fh)

from mako.template import Template

#hti = Html2Image()


Path('output').mkdir(parents=True,exist_ok=True)
mytemplate = Template(filename='act.html')
plan = 'Act Storm Internet'
rental = 1185
gst = 0.09*rental
total = rental + 2*gst
due_rental = total*1.12
total_gst = gst*2

def make_precision(rental,gst,total,due_rental,total_gst):
    rental = "{:.2f}".format(rental)
    gst = "{:.2f}".format(gst)
    total = "{:.2f}".format(total)
    due_rental = "{:.2f}".format(due_rental)
    total_gst = "{:.2f}".format(total_gst)

    return rental,gst,total,due_rental,total_gst

rental,gst,total,due_rental,total_gst = make_precision(rental,gst,total,due_rental,total_gst)

for d in data:
    bill = mytemplate.render(
            invoice_number=d['invoice_number'],
            month=d['month'],
            year=d['year'],
            invoice_date=d['invoice_date'],
            due_date=d['due_date'],
            end_date=d['end_date'],
            number_of_days=d['number_of_days'],
            PLAN=plan,
            rental=rental,
            gst=gst,
            total=total,
            due_rental=due_rental,
            total_gst=total_gst
    )
    ofname = f'output/{d["invoice_number"]}-{d["month"]}-{d["year"]}'

    with open(ofname+'.html','w') as fh:
        fh.write(bill)

    #hti.screenshot(html_file=ofname+'.html')
    #os.system(f'mv screenshot.png {ofname}.png')

    #from PIL import Image

    #image_1 = Image.open(ofname+'.png')
    #im_1 = image_1.convert('RGB')
    #im_1.save(ofname+'.pdf')
