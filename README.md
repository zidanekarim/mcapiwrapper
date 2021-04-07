# Minecraft API



This a simple package to wrap many APIs, including the Mojang and Hypixel ones


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

__Example__
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
