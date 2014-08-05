import bpy
import urllib.request
from html.parser import HTMLParser

LABEL = "Check for updates"

URL        = 'http://www.blender.org/download/'
TAG        = "h1"
TAG_KEY    = "style"
TAG_VALUE  = "margin-top: 68px"

ROOT_DESCR = "Blender "
RELEASE    = "release"

MESSAGE_ERROR  = "Version can't be retrieved"
MESSAGE_OK     = "Blender is up to date"
MESSAGE_UPDATE = "New version available : "



bl_info = {
    "name": "Check for update",
    "description": "Check for new version of Blender, based on download page.",
    "author": "Julien Duroure",
    "version": (0, 2),
    "blender": (2, 69, 0),
    "location": "Help > Check for updates",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/System/Check_for_updates",
    "tracker_url": "https://projects.blender.org/tracker/index.php?func=detail&aid=37310&group_id=153&atid=467",
    "category": "System"}

# class for HTML parser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.version = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == TAG:
            for attr in attrs:
        #current flags for version in www page
                if attr[0] == TAG_KEY and attr[1] == TAG_VALUE:
                    self.flag = True
                
    def handle_data(self, data):
        if self.flag == True:
            if data.find('&') != -1:
                self.version = data[:data.find('&')]
            else:
                self.version = data
            
    def handle_endtag(self, tag):
        if self.flag == True:
            self.flag = False

# operator 
class NewVersionCheck(bpy.types.Operator):
    bl_label = LABEL 
    bl_idname = "wm.newversion_check"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.prop(self)
        

    def execute(self, context):
        try:
        # retrieve current version of Blender ( used by user )
            current_version_num = bpy.app.version
            current_char    = bpy.app.version_char
            current_version = str(current_version_num[0]) + '.' +str(current_version_num[1]) + str(current_char)

        # retrieve current version available on www
            parser = MyHTMLParser()
            f = urllib.request.urlopen(URL)
            data = f.read()
            parser.feed(str(data))
            if parser.version[:8] != ROOT_DESCR:
                raise Exception('HTML error')
            if current_version == parser.version[8:] and bpy.app.version_cycle == RELEASE:
                self.report({"INFO"}, MESSAGE_OK)
            else:
                self.report({"INFO"}, MESSAGE_UPDATE + parser.version)

        # if any problem (network or change on www page )
        except:
            self.report({"ERROR"}, MESSAGE_ERROR)

        return {'FINISHED'}

        
def add_to_menu(self, context):
    layout = self.layout
    layout.operator("wm.newversion_check",icon='BLENDER')
        
def register():
    bpy.utils.register_class(NewVersionCheck)
    bpy.types.INFO_MT_help.append(add_to_menu)        
        
def unregister():
    bpy.utils.unregister_class(NewVersionCheck)
    bpy.types.INFO_MT_help.remove(add_to_menu)

if __name__ == "__main__":
    register()