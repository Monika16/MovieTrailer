# Movie WebSite
Movie Website is a python project which displays some of my favourite movies and its details. 
It has information like :
- Movie Title
- Movie Story Line
- Movie's Poster Image
- Movie's Youtube trailer

## Files in Project
It has 3 python files :
1. **media.py** : Contains Movie Class with attributes: 
- Title
- Story Line
- Poster Image URL
- Youtube Movie Trailer URL
2. **entertainment_center.py** : Contains instances of the class Movie. The List of the instances are then passed to the `open_movies_page` function in fresh_tomatoes.py.
3. **fresh_tomatoes.py** : Contains the Page Layout i.e. HTML page layout and the function `open_movies_page` which displayes the poster image of the movie with its title. Function to open the webbrowser to show the youtube trailer of the Movie is also present.

## Execution of the Project
To execute the project i am currently using _**IDLE(Python GUI)**_. 
_Steps of Execution :_ 
1. Start IDLE.
2. Open the entertainment_center.py file in the GUI. (File - Open - select the path where it is stored).
3. Execute the Run Command by going to the Run option in the Main Menu or on Keyboard Click Ctrl+F5.
4. Fresh Tomatoes! HTML Page is opened in the Browser. It contains Movie Poster with its corresponding Movie Title. 
5. To view the Youtube trailer of a specific movie, just click on the Movie Poster of that Movie.

