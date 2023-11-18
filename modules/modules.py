"""
Initialize the modules (__init__) to get the relevant info of what to do with them:

The loaded modules must return a tuple of 4 elements
1st: a list of tab names where to be shown if ui component,
2nd:  the area where to include the Ai and area to include the process to be done within the module
3rd and 4th: two funcions: one named "__call__" and another named "show"
if no function, create one with the return being the same as the imput or a pass function    
    3rd: show: will be user to show the UI component of the module in the specified TAB & AREA, 
            def show(*args):
                pass
    4th: Call will be used to process a dictionay of parameters or a specific parameter, depending on where is to be included
            def __call__(*args):
                return args
ATT: not implemented the area zones, fixed.
tabs names:["txt2img","hires"] --


"""
class Borg20:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state



class preProcess_modules(Borg20):
    #import json
    all_modules=None
    _loaded=False


    def __init__(self):
        Borg20.__init__(self)
        if not self._loaded:
            self.__initclass__()

    def __str__(self): 
        import json
        return json.dumps(self.__dict__)

    def __initclass__(self):
        self.all_modules=self._launch_preprocess_modules()
        self._loaded=True

    def check_available_modules(self,tab_name):
        list_modules=[]
        for module in self.all_modules:
            if tab_name in module[0]:
                list_modules.append(module)
        available_modules=list_modules

        return available_modules #do not use a class var, it will provide always the functions for the last UI tab loaded



    def _launch_preprocess_modules(*args,**kwargs):
        from importlib import import_module
        #lista=['wilcards','styles']
        lista=['wildcards_module','styles_module']
        modules_data=[]

        for elemento in lista:
            my_modulo=import_module('modules.'+elemento, package="StylesModule")
            info=my_modulo.__init__("External Module %s Loaded" % elemento )
            functions=(my_modulo.show,my_modulo.__call__)
            modules_data.append(info+functions)

        return modules_data



if __name__ == "__main__":
    print("This is the module loader and is not intended to run as standalone")
    pass
else:
    __name__ = "ExternalModuleLoader"