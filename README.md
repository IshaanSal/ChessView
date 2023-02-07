# ChessView
Based upon overhead visual of chess board, the program provides the exact board position of each piece.
-The goal of this project was to be able to develop an effective method of being able to scan each and every piece on the board
 and return its position on the board, based on the provided image.

**Instructions On How to Use:**
-To use the program, first setup your chessboard, with all the pieces in their initial positions. This is the initialization step.
-Then take an overhead photo of this chessboard setup, with preferrably overhead lighting, so as to reduce shadows.
-Then crop the corners of the image so the only things visible are the squares. (a sample image of what it should look is provided
 in chessPics/init1.5.png & chessPics/setup1.jpg). This is considered your "OriginalSetup" image.
-Now that the initial setup is captured a photo of the board at any point in the game can be utilized, as long as the edges are cropped the same
 way as the original image.
-When you have the previously mentioned images, open the file labeled 'InputValues.py"
-In this file, edit the variable "OriginalSetup" with the name of your initial image, and do the same for the variable "ParentImage"
 with whatever mid-game image you want.
 -Finally, you can simply run "ChessView.py" and the program should run successfully!

_Needed Dependencies_
-OpenCV
-Numpy
-PIL

**How it Works**
The program relies on a OpenCV function known as Template Matching. In essence, template matching takes a frame, of a certain pixel height and width,
and runs a 2-Dimensional convolution over a certain parent image. In simpler terms, it takes a small image frame, and slides it over a larger template,
while looking for a frame in the template image, that looks similar to the small image frame. Prior to this process occurs, both images must be imported
in grayscale format, meaning each pixel is simply given a value between 0 and 1, that indicates its darkness. This assists in calculating the similarity
between the small image frame as well as the template, since the frame in the template with the most similar grayscale pixels is ultimately returned.
When the user takes an image of the initial setup of the board, the file "boardDiv.py" uses iterative constructs to divide the board into 32 different images,
each being an image of a different chess piece. These images are then saved to the directory labeled "piecePics".
The file "pieceMatch.py" then utilizes template matching from the OpenCV library to run the function on every image of the pieces. This class then returns
two points, each containing the coordinates for the top left corner and bottom right corner of the matched image. The file "posEstimator.py" finally converts
these pixel coordinates into corresponding board pieces, finally returning the board position of every piece.
