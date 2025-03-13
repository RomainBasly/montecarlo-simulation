# Montecarlo Simulation

A tool used to estimate roughly the delivery date to a scrum project. 
For each ticket, it is based on three hypothesis for each ticket (pessimist, normal, optimist).

The idea is to get a delivery date in terms of sprint and for that we do a random calculus to see which delivery date seems likely. 

Exemple here with fake data on 72 tickets: 

```
backlog = [
    (3, 5, 8),
    (5, 8, 13),
    (1, 2, 3),
    (8, 13, 21),
    (3, 5, 8),
    (5, 8, 13),
    (1, 2, 3),
    (8, 13, 21)
] * 9 
```

<img width="953" alt="image" src="https://github.com/user-attachments/assets/4c271972-64af-4b4b-a999-8638907c078b" />

We have 95% chance of finishing the sprint between 19th and 20th sprint.
