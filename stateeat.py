#description: this class represents the eating state of the puppy

from puppystate import PuppyState 
import stateasleep
import stateplay

class StateEat(PuppyState):
    def feeds(self, puppy):
        """
        handles the feeding state of the puppy, when it is eating 
        """
        puppy.inc_feeds()
        if puppy.feeds >= 2:
            puppy.change_state(stateasleep.StateAsleep())
            puppy.reset()
            return "The puppy ate so much it fell asleep!"
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    
    def plays(self, puppy):
        """
        handles the playing state of the puppy 
        """
        puppy.change_state(stateplay.StatePlay())
        # puppy.reset()
        return "The puppy looks up from its food and chases the ball you threw."
