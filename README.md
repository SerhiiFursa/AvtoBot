Bot AvtoBot is a bot for the Telegram messenger that helps you find the car on OtoMoto.com. 
With its help, you can subscribe to updates that match your criteria and receive notifications about new ads.

Link to bot - https://t.me/avtoAutoBot

Link to a video with an example using the bot [![AvtoBot Youtube]](https://www.youtube.com/watch?v=Fcn1BJy_CS0)


How the bot works from the user side:

  - the user creates a request by choosing the criteria for the car ads (make, model, transmission type, year (from-to), mileage (from-to), price (from-to)).

  - after creating the request, the bot will check for suitable ads on the OtoMoto.com website and as soon as it finds a new ad, it will send it to the user.

  - one user = one request


How the bot works from the technical side

  - after the user finishes creating the request, a URL is created based on the selected criteria for suitable cars. The presence or absence of certain criteria affects the structure of the link, so if the user doesn't care about, for example, the minimum price, the minimum allowable price on the site will be added to the criterion to use the same link template. The only exception is the transmission type, so two link templates are allowed - one for selecting the transmission type and one for not selecting it.

  - the program visits the link and saves the ID of the newest ad (this is needed so that the bot can send ads that were added after the user's request was created). The situation where there are no ads is also taken into account.

  - then the program adds the following data to the database: user ID, ID of the newest ad, make, model, transmission type, minimum year, maximum year, minimum mileage, maximum mileage, minimum price, maximum price, URL.

  - every 3 minutes, the bot visits the users' links and sends new ads if any are found (in this case, the old ad ID is replaced with the ID of the newer ad).


Also, using commands or the main menu, the user can:

-- delete an existing request;

-- read the instructions for use;

-- submit a complaint or suggestion;

-- support the project financially by following the appropriate link.
