# dum-e
Dusting off old Flask code to allow for remote editing of Arduino code that drives my robot arm.

The old workflow was as follows:
1) write new code on my laptop;
2) use curl to send file to raspberry pi (base) running flask;
3) file would be received;
4) file would be compiled;
5) arm is set into safe mode;
6) load is moved over;
7) arm is waiting for new commands.

Moving the scope to make this more of a universal type of code that can
be used to drive other similar robotic projects in my house.