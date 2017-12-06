import random
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import agentframework
import matplotlib.animation
import tkinter

import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs) 

 
import csv #to read csv file that has the environment
f = open('in.csv', newline='') 
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    for item in row:
        rowlist.append(item)
        
    environment.append(rowlist)
f.close() 


def distance_between(agent0, agent1):
        return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5



num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# Make the agents.
for i in range(num_of_agents):
     y = int(td_ys[i].text)
     x = int(td_xs[i].text)
     agents.append(agentframework.Agent(environment, agents, y, x)) 
     



       
def update (frame_number): 
    fig.clear() 
    matplotlib.pyplot.imshow(environment)
    
    for j in range(num_of_iterations):
        random.shuffle (agents) #to shuffle the agents
    for i in range(num_of_agents):
       agents[i].move ()
       agents[i].eat() 
       agents[i].share_with_neighbours(neighbourhood)
      
    for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i].x,agents[i].y)


def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			
        a = a + 1


def run():
     animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
     matplotlib.pyplot.xlim(0, 99)
     matplotlib.pyplot.ylim(0, 99)
     matplotlib.pyplot.imshow(environment)
     canvas.show() 



root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()




#print (agents[0].x,agents[0].y)
