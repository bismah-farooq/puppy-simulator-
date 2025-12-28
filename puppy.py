#description: This class represents a puppy, that can be in different states and responds to playing and feeding.

from stateasleep import StateAsleep  

class Puppy:
    def __init__(self):
        """
        initializes the puppy in the asleep state and initializes the feed and play count to zero
        """
        self._state = StateAsleep()
        self._feeds = 0
        self._plays = 0

    def change_state(self, new_state):
        """
        changing the puppy's previous state to a new state 
        """
        self._state = new_state

    def give_food(self):
        """
        feeding the puppy 
        """
        return self._state.feeds(self)  # Return the result of feed()

    def throw_ball(self):
        """
        playing with the puppy 
        """
        return self._state.plays(self)  # Return the result of play()

    def inc_feeds(self):
        """
        incresing the food count of the puppy
        """
        self._feeds += 1

    def inc_plays(self):
        """
        increasing the play count of the puppy 
        """
        self._plays += 1

    def reset(self):
        """
        resetting the feeding and playing count 
        """
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        """
        Returns the number of times the puppy has been fed.
        """
        return self._feeds

    @property
    def plays(self):
        """
        Returns the number of times the puppy has played.
        """
        return self._plays
