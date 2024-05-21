import datetime
import matplotlib.pyplot as plt
import numpy as np
import xml.dom.minidom

# Parsing XML files
start = datetime.datetime.now()#count time beginning
doc = xml.dom.minidom.parse(r'C:\Users\12898\Documents\Github\IBI1_2023-24\Practical 14\go_obo.xml')
# Gets all go term elements
go_terms = doc.getElementsByTagName('term')
#print(go_terms)
# Initialize counter
bp_count = 0
mf_count = 0
cc_count = 0
# go through all the go term elements and count them
for go_term in go_terms:
    category=go_term.getElementsByTagName('namespace')[0].firstChild.data
    if category == 'biological_process':
        bp_count += 1
    elif category == 'molecular_function':
        mf_count += 1
    elif category == 'cellular_component':
        cc_count += 1

# print results
print(f"Biological Process (BP) GO terms: {bp_count}")
print(f"Molecular Function (MF) GO terms: {mf_count}")
print(f"Cellular Component (CC) GO terms: {cc_count}")
delta1 = (datetime.datetime.now() - start).total_seconds()#end timing
print(delta1, "seconds used for DOM api.")

#Using SAX to calculate GO term
import xml.sax

# Define a processor class
class GoHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.bp_count = 0
        self.mf_count = 0
        self.cc_count = 0
        self.current_category = ""
        self.in_namespace=False 

    def startElement(self, name, attrs):
        if name == 'namespace':
            #print(attrs)
            self.current_category = ""
            self.in_namespace = True
        
    def characters(self, content):
        if self.in_namespace:
            self.current_category+=content.strip()
# Collect and clean text content 
    def endElement(self, name):
        if name == 'namespace':
            self.in_namespace = False
        elif name == 'term':
            if self.current_category == 'biological_process':
                self.bp_count += 1
            elif self.current_category == 'molecular_function':
                self.mf_count += 1
            elif self.current_category == 'cellular_component':
                self.cc_count += 1
            self.current_category = ""

    def endDocument(self):
        print(f"Biological Process (BP) GO terms: {self.bp_count}")
        print(f"Molecular Function (MF) GO terms: {self.mf_count}")
        print(f"Cellular Component (CC) GO terms: {self.cc_count}")

# Create an XML parser and specify the processor
start = datetime.datetime.now()

parser = xml.sax.make_parser()
handler = GoHandler()
parser.setContentHandler(handler)

# Parsing XML files
parser.parse(r'C:\Users\12898\Documents\Github\IBI1_2023-24\Practical 14\go_obo.xml')
delta2 = (datetime.datetime.now() - start).total_seconds()#end timing
print(delta2, "seconds used for SAX api.")

terms_count = [bp_count, mf_count, cc_count]
x = [1,2,3]
plt.bar(x, terms_count, align='center', alpha=0.5)
plt.xticks(x,('bp','mf','cc'))
plt.show()