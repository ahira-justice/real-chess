# real-chess

## What is real-chess?

real-chess is a chess game I wrote in python and pygame. It has no AI (player vs computer). Rather, it defines chess rules (movement, capture, check and check-mate) for white and black sides. I didn't get around to including more advanced aspects of the game like pawn promotion, en passant or draw/stalemate. It is playable as a somewhat limited chess game between two human opponents.

This is one of my earliest projects. That fact is clearly visible when you examine the project structure and its lack of proper file modularity. All code is functional and is stored in a single file. Perhaps you can see why I'm reluctant to add new features to 2000+ (2184) lines of code, all in a single file from 4+ years ago. I can already feel the hair-pulling frustration.

So, this is more of a _post-mortem_ than it is a readme.

This project is great because, beyond all the advanced software development concepts I've gone on to learn, at its heart is experimentation with algorithms; sometimes re-inventing the wheel, an understanding of how programs work on a fundamental level, and lots of learning by doing.

## chess_build.py

This was my first attempt at a solution. I had just finished [Al Sweigart's](https://github.com/asweigart) _Making Games with Python & Pygame_. What you'll see here was my attempt at rendering complex polygons in the 2D shape of the various chess pieces. I didn't get to finish the King, nor start the Queen. I abandoned this approach when I found free png chess piece sprites to use instead.

## real_chess_beta_version.pyw

This is the first playable version of the game. It has no movement validation or capture constraints, neither does it have check or check-mate. It's just a board with 16 pieces a side. You can play as you would a real-life physical chess game, where both parties know the game and enforce the rules on the other person. I completed this version in 3 weeks of coding, only going out of room for kitchen runs.

## real_chess_1.0.pyw

This version of the game is the _current and final_ one. It has seen many iterations. Plenty of spirited bursts of coding fervor, punctuated by drawn out hiatuses. The product is many lines of code that mean more to me than what they're worth in text.

## Maintenance

I have made some changes in the recent past to get the project ready for GitHub, and ensure it follows PEP8 guidelines to make it easier to follow (I invite you to read the code):grin::broken_heart:.

I stopped debugging and writting _new feature_ code for **real-chess** in February, 2016. For the whole of my freshman year in 2015, I left the project untended. I had started in July, 2014 and did blaze through to the beta-version **real_chess_beta_version.py**, in three weeks. The rest of that year saw me meet deeper algorithimic challenges than I could ever have predicted right off the bat. During the session break of early 2016, I made an attempt to finish what I had started. Here I learnt another lesson; the last 20% of a project might take 50% of the overall time. Getting back on board with the project after a year's absence was a lesson in proper documentation, descriptive naming and commenting. I was also beginning to regret the lack of seperate files at this point. I also suffered from _scope creep_.

Since moving on from the project, I can now look back at all the rookie mistakes I made, the design anti-patterns I fell into, and the data structures I had no idea existed. There is a part of me that hopes to finally bring the project to a finished point; refactoring, modularizing and adding final features. There is also another part of me that just wants to hold on to the nostalgia of the 2000+ line program, leaving it as a relic to my journey into software development.

Whatever I end up doing with the project, I hope **real-chess** is something casual chess players can enjoy.

## Dependencies
```sh
pip install pygame
```

Clone this repo and have a go at a mate.
