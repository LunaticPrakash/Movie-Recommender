# Movie-Recommender
This project suggests you the list of movies based on the movie title that you have entered. It uses Count Vectorizer (Text-Feature Extraction tool) to find the relation between similar movies.

## Purpose :- 
To recommend/suggest similar movies to watch based on given movie.


## Description & Features :-

It usage Count-Vectorizer for finding similarities between movies.
The similarity is based on following factors :-

- Genres (Ex- Action, Adventure, Fantasy etc.)
- Keywords (Ex- Culture Clash, Future, Battle, Space etc.)
- Cast (Actors)
- Crews (Director)


 ## Output :- 
 
    - You can enter the movie title and number of similar movies you want.
   
   ![Output](https://github.com/LunaticPrakash/Movie-Recommender/blob/master/Output.png?raw=true)
   
   
## Requirements :- 

- Python3
- Pandas
- Scikit-Learn


## How to install Requirements :-

1. Python3 can be installed from their official site https://www.python.org/ . Or you can use anaconda environment.

2. Pandas can be installed by
```
conda install -c anaconda pandas
``` 
or
```
pip3 install pandas
```
3. Scikit-Learn can be installed by 
```
conda install -c anaconda scikit-learn
```
or
```
pip3 install -U scikit-learn
```

## Getting Started :-

- Download or clone repository.
- Launch your jupyter-notebook either from the same directory where this cloned repo is located or in the location from where that directory can be accessed.
- Browse to this repository in jupyter-notebook and open the file **Movie-Reccomender.ipynb**. Now you can run or edit the code.


## Bugs and Improvements :-

- No major known bugs.
- But when you will write 'Batman' in movie name it will throw an error.
Line (that throws error) -> sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
Error -> The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
Explaination -> This error is raised when a boolean array is used in a context that requires a simple True/False value. Here it appears to be the comparison required for sorting. A test like x<y produces a boolean array if x or y is a numpy array.

You can Comment your solution (if any) or open an pull request to solve this bug. Your advice will be highly appreciated.


## Dev :- Prakash Gupta

