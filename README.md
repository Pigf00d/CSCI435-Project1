# CSCI435-Project1

### How to run this yourself
1. Clone the repository 
2. Run ```pip install -r requirements.txt``` to install dependencies 
3. Open ```theFix.py```
4. Change ```path``` to the directory where your .xml and .png files are stored 
5. Change ```resultsPath``` to the directory where you want the new annotated .png files to go
6. Run ```theFix.py```

#### The annotated .png files should in the directory that you indicated 

## Natural language description of my design decisions

I used the lxml library to create the xml tree because it seemed like the general consensus online was that this was the best way available in python. As far as drawing the rectangle: my initial compulsion was to use matplotlib but this ended up being a lot of extra work because of the arguments that a matplotlib rectangle needs. Therefore, I ended up using OpenCV because it was much more friendly to the way the given bounds were structured.
I made sure that there needed to be minimal action on the side of the user when they run it on their own machine. All they have to change is two lines of code, for the initial and final directories, and then the tool will function as needed.
