# Chess Library

This holds game related files supplied to both server and client during their functioning.
Having these in one central place allows us to make sure we're making non-breaking changes by testing code interaction
within the efficient unit test domain, and not in API integration. API integration must also happen, but it's not of
concern to what happens in this library and should rather be handled by it's respective packages.

___

## List of actions performed in each round of a game of chess

### INPUT
    - prompt user for input
        - prompt user for source block name
        - prompt user for destination block name 
### VALIDATION
    - validate source block name notation
    - validate source block game rules
        - that there's an initial piece present
        - that that piece is owned by the current player
    - validate destination block name notation
    - validate destination block game rules
        - [ that the move is not an exception? ]
        - that the move is within the pieces move pattern
        - that the move is within the pieces range
        - that the move is not blocked by any other pieces 
### MOVE
    - check if the destination block name has a piece
        - remove destination block piece if necessary
    - add the initial piece to the destination block name
    - remove the initial piece from the source block name
### CHECK GAME CONDITIONS
    - pre-win conditions
        - check
        - [ castling? ] - Can't be done more than once
        - [ pawn double step? ] - Can't be done more than once, on initial movement of piece
    - win conditions [/game ending]
        - checkmate
        - stalemate
### STATE CHANGE
    - rotate current player
