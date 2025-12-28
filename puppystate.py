#description: it is a abstact base class defining the state of the puppy 

import abc 

class PuppyState(abc.ABC):
    @abc.abstractmethod
    def feeds(self,puppy):
        """
        handles feeding the puppy 
        """
        pass

    @abc.abstractmethod
    def plays(self,puppy):
        """
        handles playing with the puppy 
        """
        pass