# optimal-stopping-fun
I was reading Algorithms to Live By (Book by Brian Christian, and Thomas L. Griffiths) and wanted to try simulating some of the solutions to the optimal stopping problem.

The simulation code is a bit of a mess, threw it together in a couple of minutes for fun.

So at first I do the exact criteria as defined: [https://www2.math.upenn.edu/~kazdan/210/LectureNotes/secretary/Sec.pdf](https://www2.math.upenn.edu/~kazdan/210/LectureNotes/secretary/Sec.pdf)

This after 100000 tests, tends to result in around the optimal value 36.6

Then, we try some variations, like making the distribution normal or specifying to check for who gets on average the best picks.

Most notable is trying to obtain the best possible expected outcome on average. So instead of having the highest chance of getting the best pick exactly, we want the pick's score to be ranked the highest. This increases the damage that not finding the best pick at all in the later 13 does.
Without changing any other criteria, the stopping and leaping strategy tells us that we should go for around 13 or so, or closer to 1/e<sup>2</sup>.

More testing is required, and there could be some errors in the way its performed, because everything was thrown together but things are very interesting.

I didn't do much math to confirm any of the values like averaging the top 5, so this is just for fun. Maybe someone has already found this and has some math, I will need to do some more googling.
