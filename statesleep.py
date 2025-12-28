#description: this class represents the asleep state of the puppy

from puppystate import PuppyState  
from stateeat import StateEat

class StateAsleep(PuppyState):
    def feeds(self, puppy):
        """
        the puppy is in asleepy state and then waking up for food 
        """
        puppy.change_state(StateEat())
        puppy.reset()
        return "The puppy wakes up and comes running to eat."

    def plays(self, puppy):
        """
        returns a string 
        """
        return "The puppy is asleep. it doesn't want to play right now"

