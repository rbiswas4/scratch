from __future__ import absolute_import, print_function
from future.utils import with_metaclass
import abc

__all__ = ['BaseAbs', 'NewClass']
class BaseAbs(with_metaclass(abc.ABCMeta, object)):

    @abc.abstractproperty
    def X(self):
        pass

    @abc.abstractmethod
    def square(self, x):
        pass


class NewClass(with_metaclass(abc.ABCMeta, BaseAbs)):

    @abc.abstractmethod
    def quad(self, x):
       y = self.square(x)
       return y * y
