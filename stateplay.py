from puppystate import PuppyState 
import stateasleep
import stateplay

class StatePlay(PuppyState):
    def feeds(self, puppy):
        """
        handles the feeding state of the puppy.
        """
        return "The puppy is too busy playing with the ball to eat right now."
    
    def plays(self, puppy):
        """
        handles the playing state of the puppy, when it is playing too much
        """
        puppy.inc_plays()
        if puppy.plays >= 2:
            puppy.change_state(stateasleep.StateAsleep())
            # puppy.reset()
            return "The puppy played so much it fell asleep!"
        return "You throw the ball again and the puppy excitedly chases it."
