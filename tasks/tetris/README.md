# Tetris

Implement a simple "text-mode" version of the Tetris game. Specification:

* game supports only 5 blocks:

```
****
```

```
*
*
**
```

```
 *
 *
**
```

```
 *
**
*
```

```
**
**
```

* blocks fall down on a 20x20 board
* the game starts with a random piece appearing at the top of the board
* the user is prompted to make a move:

    * a (return): move block left
    * d (return): move block right
    * q (return): rotate piece counter clockwise
    * e (return): rotate piece clockwise

* in case of invalid move user is prompted once again for valid choice (no game update)
* if the move is valid block is transformed according to user's input and drops one level down
* after every move the screen is redrawn
* when the current position of the block doesn't allow any valid move (i.e. no valid move, block reaches bottom of the board) 
a new blocks is placed at the top of the board
* when no move is available for the new block the game ends
