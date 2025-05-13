import importlib.util
import os
import inspect

class FunctionLoader:
    @staticmethod
    def load_functions_from_file(filepath):
        module_name = os.path.splitext(os.path.basename(filepath))[0]
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        funcs = {}
        for name, attr in inspect.getmembers(module, inspect.isfunction):
            if attr.__module__ == module_name:
                funcs[name] = attr
        return funcs

    @staticmethod
    def load_tests_from_config(config_path):
        import json
        with open(config_path) as f:
            cfg = json.load(f)
        return cfg.get("tests", [])