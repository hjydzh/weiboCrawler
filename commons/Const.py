class _const(object):
    class ConstError(TypeError): pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError, "Changing const.%s" % key
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None
import sys
sys.modules[__name__] = _const()
