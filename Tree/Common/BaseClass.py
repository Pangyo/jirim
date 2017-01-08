'''
Created on 2016. 5. 15.

Information : BaseClass is SingleTon

@author: yunjae
'''

class BaseClass(object):

    # instance
    _instance = None
    
    # new instance
    def __new__(self, *args, **kwargs):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self, *args, **kwargs)
        return self._instance
    