# censor-bot
A Discord bot that filters out blacklisted words in messages.

**Setup:**

To run on Replit, enable the keep alive function (default enabled) to ensure that the bot does not lose connection. If you're looking to host it locally, you can remove the alive.py script and remove the function ```keepAlive()```. blacklisted.txt contains a list of all blacklisted words you want to block. A filtering engine works based off those words and removes any close variations of those words. Anything that slightly resembles a word on blacklisted will be removed (case-sensitive). The bot will DM a user on discord stating the message that the bot caught was blacklisted and the blacklisted word it caught in the message as well as the warning count of the user (amount of warnings received from blacklisted words).

**Customization:**

You can change the list of words in blacklisted.txt as well as the embed it's sending. 
