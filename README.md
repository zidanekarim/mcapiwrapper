# Minecraft API

This a simple package to wrap many APIs, including the Mojang and Hypixel ones

Requires Python 3.7+

#Usage guide

Import the package with

```py
import mcapiwrapper
```

Or the preferred way

```py
from mcapiwrapper import hypixel
```

The second way allows you to save some lines writing the actual code. To actually use this, create a Bedwars, Skywars, or Hypixel object. You must pass in a username and api key for the hypixel-related objects

\***\*Example\*\***

```py
from mcapiwrapper import hypixel

object = hypixel.Bedwars("ThePotatoPowers", "yourapikeyhere")
```

To get information from this object, use the `stats()` method. Then, the object's attributes will be set

```py
from mcapiwrapper import hypixel

object = hypixel.Bedwars("ThePotatoPowers", "yourapikeyhere")
object.stats()
print(object.wins) #prints bedwars wins for ThePotatoPowers
```

## Skins

Create a **skin object** by first importing the skin file from the package `from mcapiwrapper import skin`
The class takes a username argument

The `skingrab` method will return a link with the user's skin. You can access this with the skin attribute

The `body` method will return a link with the user's body. You can access this with the body attribute

The `head` method will return a link with the user's head. You can access this with the head attribute

The `avatar` method will return a link with the user's head in 2D. You can access this with the avatar attribute

## Bedwars

As shown above, import hypixel from mcapiwrapper. Then, create a `Bedwars` object which takes a username and apikey parameter (in that order)

After the `stats` method is run, you can access all attributes of the Bedwars object. This includes:

- display (displayname)
- wins
- losses
- deaths
- kills
- coins
- final_kills
- final_deaths
- beds_destroyed
- beds_lost
- winstreak
- level

## Skywars

As shown above, import hypixel from mcapiwrapper. Then, create a `Skywars` object which takes a username and apikey parameter (in that order)

After the `stats` method is run, you can access all attributes of the Skywars object. This includes:

- wins
- losses
- deaths
- kills
- coins
- souls
- heads
- winstreak
- display

## Hypixel

As shown above, import hypixel from mcapiwrapper. Then, create a `Hypixel` object which takes a username and apikey parameter (in that order)

After the `stats` method is run, you can access all attributes of the Hypixel object. This includes:

- firstLogin
- lastLogin
- nameHistory
- display

## Contribute

- Source Code: https://github.com/ThePotatoPowers/mcapiwrapper/
- Issue Tracker: https://github.com/ThePotatoPowers/mcapiwrapper/issues

## Support

If you are having issues, please let me know @ zkarim7676@gmail.com

## License

The project is licensed under the MIT license.
