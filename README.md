## turn-based-strategy-game
### yeah (we still don't have a name)
## Scroll down to view v2.0.0 patch notes!

If you change the name of 'game2lib.py', the game will break.
The custom functions for this game are stored in here:
This means that game needs to read from 'game2lib.py' in order to work.

Thank you so much, and enjoy playing!
\- aly

-- GUIDE --

: Attacking :
- Attacking is simple. You choose it and you deal a random amount of damage within a predetermined range.
-  Defending is also simple. You choose it and your defence goes up. It's a bit broken, but not really.
-  The item list can be accessed, but does nothing. Maybe at a later date.
-  Passing. Luigi is with you on this one.
-- Stats --
alyssa the great
big man fidel car
Health: 608
Attack: 248
Speed: 12

-- KNOWN BUGS -- 
-  Passing, defending, or simply having high luck can give absurdly high stats
-  High defence doesn't negate damage properly
-  Speed is way too overpowered
- The item menu does nothing
	- If the game gets expanded or moved to Gamemaker Studio, this might be implemented. Might.
- The stats menu eats your turn. 
	- Yeah I just couldn't figure this one out, sorry.
- Typing a non integer (a number without letters) during your turn crashes the game
	- This means that, if you aren't using an IDE to run the game, the window will close instantly. Your game isn't corrupted.<br/>
-- EXTRA -- 
- If you need to contact me, my Discord handle is @.1aria.

# V2.0.0 PATCHLOG BABYY !!
## The game has been rewrote from scratch! This means that *game2lib.py* does not work with this version, and that many bug fixes and reworks have arrived! The new file should be called *gamev2.py*

**New features**
- Random name generation
- Armour and weapon choices
- Critical hits & Reworked Luck stat
- A fully functioning item menu
- Error handling and error codes

**Tweaks, Fixes & Changes**
- Attacking has been entirely reworked.
    - Critical Hits: Armour types are weak to certain weapons and will occasionally receive increased damage on attack. There is a base crit chance ranging from 15-30%, but weapons have a 40% crit chance when attacking armour that is weak to them!
    - Luck has been reworked: It is now a stat ranging from 1-8 (without buffs), with a luck/8 chance to receive reduced damage on attack. Luck no longer has an effect on your other stats; it can only reduce damage during the attack calculation.
    - Speed has been removed, meaning you no can longer dodge attacks entirely. I really liked the concept of this mechanic, and it highly affected the new version of the luck stat.
- Defending has been reworked too!
    - Defending now gives a base defence bonus of 20, with the bonus being reduced by 1 for each consecutive block. This will reduce your defence if you successfully block more than 20 times, allowing you to go into the negatives if you feel like it. Due to how to damage calculation works, negative defence increases the damage you take. I really like how this works, so I don't think I'm going to change it.
    - Defensive Blocks are broken when you are attacked, resetting your defence to its' original value and setting the Block defence bonus to 20.
- The item menu works now! However, some changes may be made in v2-full.
    - There are 4 items to choose from with mostly positive buffs, however, items that reduce your hp can kill you, so use them carefully!
    - A health potion (+90 hp)
    - A rock (1/3 chance for +20 def, 2/3 chance for reduce your defence and hurt you.)
    - A shard of glass (hurts you, but increases your damage)
    - A strange magical potion (this can do 1 of 5 things, with effects varying from basic to unique, helpful to downright game ending.)
- The stats menu has also been fixed, and no longer ends your turn.
    - It displays your stats, gear, class, and another special stat that will only be displayed under very rare circumstances.

**Removed features & Balancing**
- Speed has been removed as it was entirely far too overpowered. It was taken into consideration as previously mentioned while coding the new and improved Luck stat.
- The Species feature has been removed in favour of the stat altering Weapon and Armour features. 
- The pass function and its goofy consequences have been removed. No more 99999 speed/luck, no more millions of hp, no more thousands of attack power. The game is (hopefully) more balanced and less cheat code dependant!

**Known issues**
- Attack power is not perfectly balanced yet, and the knight class/sword weapon is the best offensive choice for this game. I will continue to tweak this and see where I get.
- The defend action may raise a TypeError, breaking future uses of this action until the program is restarted. However, the error handling I implemented SHOULD allow you to continue playing.
- Items can be used as many times as a player desires. I do not wish to write another 100 lines of code to add a larger pool of items, and since this is just a CLI fight simulator and not a real RPG game with an explorable world, I feel as though it may be more fun to leave this in its' current state.
- The stats menu should inform you of when a Brilliance Mixture is active, but this is currently untested.

# If you encounter any bugs, regardless of whether or not there is an error code, please let me know! Bugs happen, and as a solo developer I am more prone to oversights. If you do contact me or raise an issue on the repo, please list what you did leading up to the bug/crash and I'll make sure to look into it and fix it!