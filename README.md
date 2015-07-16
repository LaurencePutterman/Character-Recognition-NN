# Character-Recognition-NN
Neural network that can be programmed to recognize a single character drawn into a matrix

Uses kivy for the GUI and numpy for the matrices and linear algebra functions. 

Adapted from http://iamtrask.github.io/2015/07/12/basic-python-network/

TO USE: 

Draw a desired character in the matrix by clicking the boxes. Type a 1 or a 0 in the box to indicate whether the drawn character should be recognized as a positive match for the desired character or a negative match. Press enter in the box, then click add. 

Do this a couple of times, drawing in variations of positive matches and negative matches. The more you enter, the more accurate the network will be. Make sure that the number of times you click Add matches the number of times you pressed enter in the box. 

When you're done adding test cases, click Learn.

Now, try drawing a character. It should output your result in the terminal.