# ALPACASgame

Game code for Evennia servers designed for use with ALPACASclient. This code is
meant to be a type of  "compatability layer" between the ALPACASclient software
and Evennia, and not a fully playable game.

This project uses portions of code from Evennia. Its license is included here as:
`evennia.LICENSE.txt`.

![This alpaca is not ALPACAS.](https://upload.wikimedia.org/wikipedia/commons/d/db/Alpaca_%2831562329701%29.jpg)

Image source: Alpaca, CC BY 2.0 Tony Hisgett from Birmingham, UK - obtained
from WikiMedia commons.


## Project Goals

- Usable by any Evennia server
    - Usable similar to `evennia --init mygame`
    - Install-able in existing Evennia games
- Add a robust portal service plugin specifically for ALPACASclient
    - Plaintext (insecure) WebSocket
    - Secure WebSocket
- Add special server plugins and inputfuncs for Point-And-Click features
- Add typeclasses that tie into Point-And-Click features
