import sys
import importlib

processors = dict()

class AnnotationProcessor(object):

    @staticmethod
    def forName(name: str):
        result = processors.get(name, None)
        if result is not None:
            return result
        simpleName = name[1:] + "Processor"
        fullName = ".".join(__name__.split(".")[:-1]) + "." + simpleName
        module = sys.modules.get(fullName, None)
        if module is None:
            try:
                module = importlib.import_module(fullName)
            except Exception as e:
                return None
        if module is None:
            return None
        else:
            processor = module.__dict__.get(simpleName)()
            processors[name] = processor
            return processor


    def processCategory(self, annotation, context, declaration):
        raise Exception("Mssing override!")
