# censor-bot
A Discord bot that filters out blacklisted words in messages.

**Setup:**

To run on Replit, enable the keep alive function (default enabled) to ensure that the bot does not lose connection. If you're looking to host it locally, you can remove the alive.py script and remove the function ```keepAlive()```. blacklisted.txt contains a list of all blacklisted words you want to block. A filtering engine works based off those words and removes any close variations of those words. Anything that slightly resembles a word on blacklisted will be removed (case-sensitive). The bot will DM a user on discord stating the message that the bot caught was blacklisted and the blacklisted word it caught in the message as well as the warning count of the user (amount of warnings received from blacklisted words).

**Customization:**

You can change the list of words in blacklisted.txt as well as the embed it's sending. 

![Screen Shot 2022-03-16 at 11 43 35 AM](https://user-images.githubusercontent.com/100868154/158664278-c9142e5e-dd62-4a64-bfe7-42d29e34a93d.png)
![Screen Shot 2022-03-16 at 11 43 43 AM](https://user-images.githubusercontent.com/100868154/158664344-a289f278-e751-4059-9f6c-56469be2381e.png)
![Screen Shot 2022-03-16 at 11 44 15 AM](https://user-images.githubusercontent.com/100868154/158664359-136082ea-c832-4d50-9613-3f9a2bfec4be.png)
