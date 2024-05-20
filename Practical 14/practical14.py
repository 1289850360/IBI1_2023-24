import xml.dom.minidom  
import datetime  
import xml.sax  
import matplotlib.pyplot as plt  
  
bio_dom = 0   
mole_dom = 0  
cell_dom = 0  
file_path = 'go_obo.xml'
start_time1 = datetime.datetime.now()  
DOMTree = xml.dom.minidom.parse(file_path)  
collection = DOMTree.documentElement  
TAG = collection.getElementsByTagName("term")  
for each_tag in TAG:  
    namespace = each_tag.getElementsByTagName("namespace")[0].firstChild.data  
    if namespace == "biological_process":  
        bio_dom += 1  
    elif namespace == "molecular_function":  
        mole_dom += 1  
    elif namespace == "cellular_component":  
        cell_dom += 1  
end_time1 = datetime.datetime.now()  
execution_time_dom = end_time1 - start_time1  
  
# DOM
plt.figure(figsize=(10, 5))  
plt.bar(['bio', 'mole', 'cell'], [bio_dom, mole_dom, cell_dom], label='DOM')  
plt.title('Namespace Counts using DOM')  
plt.xlabel('Namespace')  
plt.ylabel('Count')  
plt.legend()  
plt.show()  
plt.clf()  
  
# SAX  
bio_sax = 0  
mole_sax = 0  
cell_sax = 0  
  
class NamespaceHandler(xml.sax.ContentHandler):  
    def __init__(self):  
        self.in_term = False  
        self.current_namespace = ''  
  
    def startElement(self, tag, attrs):  
        if tag == 'term':  
            self.in_term = True  
        elif tag == 'namespace' and self.in_term:  
            self.current_namespace = ''
  
    def characters(self, content):  
        if tag == 'namespace' and self.in_term:  
            self.current_namespace += content.strip()  
  
    def endElement(self, tag):  
        if tag == 'namespace' and self.in_term:  
            if self.current_namespace in ('biological_process', 'molecular_function', 'cellular_component'):  
                if self.current_namespace == 'biological_process':  
                    bio_sax += 1  
                elif self.current_namespace == 'molecular_function':  
                    mole_sax += 1  
                elif self.current_namespace == 'cellular_component':  
                    cell_sax += 1  
            self.in_term = False  
   
  
start_time2 = datetime.datetime.now()  
handler = NamespaceHandler()  
parser = xml.sax.make_parser()  
parser.setContentHandler(handler)  
parser.parse(file_path)  
end_time2 = datetime.datetime.now()  
execution_time_sax = end_time2 - start_time2  
  
plt.figure(figsize=(10, 5))  
plt.bar(['bio', 'mole', 'cell'], [bio_sax, mole_sax, cell_sax], label='SAX', color='C1')  
plt.title('Namespace Counts using SAX')  
plt.xlabel('Namespace')  
plt.ylabel('Count')  
plt.legend()  
plt.show()  
  
print('DOM methods takes ', execution_time_dom)  
print('SAX methods takes', execution_time_sax)