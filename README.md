# Puppy Simulator (State Pattern)

This project implements a Puppy Simulator using the State design pattern. The program allows a user to interact with a puppy by feeding it or playing with it. The puppy’s behavior changes depending on its current state.

## Description
The puppy can exist in one of three states:
- Asleep
- Eating
- Playing

The simulator begins with the puppy in the asleep state. User actions cause state transitions based on predefined rules. The State pattern is used to encapsulate state-specific behavior and ensure clean separation of logic.

## Behavior Rules
- The puppy starts in the asleep state.
- When asleep, the puppy can only be woken up by feeding it.
- When eating, the puppy can:
  - Continue eating until it gets full and falls asleep
  - Be distracted by playing, which changes its state to playing
- When playing, the puppy:
  - Can continue playing until it gets tired and falls asleep
  - Will ignore food while playing
- Playing with a sleeping puppy has no effect.
- Feeding a playing puppy has no effect.

## Files Included
main.py  
puppy.py  
puppy_state.py  
state_asleep.py  
state_eat.py  
state_play.py  

## Program Structure
- Puppy: The main object the user interacts with. Tracks state, feed count, and play count.
- PuppyState: An abstract interface defining feed and play methods.
- StateAsleep, StateEat, StatePlay: Concrete state classes that implement behavior for each state.
- Main: Displays a menu and allows the user to interact with the puppy.

## How to Run
Run the program from the terminal:
```text
python main.py
```
The user will be presented with a menu to:
1. Feed the puppy
2. Play with the puppy
3. Quit

The program continues until the user chooses to quit.

## Learning Objectives
- Understand and apply the State design pattern
- Practice object-oriented programming in Python
- Use interfaces and inheritance effectively
- Manage state transitions cleanly
- Validate user input and control program flow

## Notes
- All state logic is handled through state classes
- No global variables are used
- All attributes are accessed through methods
- The program has been tested to ensure correct state transitions
