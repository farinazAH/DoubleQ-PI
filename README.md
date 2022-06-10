# Double Q-PI

The algorithm is also known as DQPI. From the article:  

[**"Double Q-PI architecture for smart model-free control of canals"**]([https://www.sciencedirect.com/science/article/abs/pii/S0168169922002575?via%3Dihub])
As appears in Computers and Electronics in Agriculture.

Authors: Kazem Shahverdi - Farinaz Alamiyan-Harandi - J.M.Maestre
![alt text](https://github.com/farinazAH/DoubleQ-PI/blob/master/Canal_RL_Details.jpg)


The algorithm is based on Double Q-PID, also known as DQPID, From the article:  

[**"Double Q-learning algorithm for mobile robot control"**](https://www.sciencedirect.com/science/article/pii/S0957417419304749)

As appears in Expert Systems with Applications.

Authors: Ignacio Carlucho - Mariano De Paula - Gerardo Acosta 

## Requirements: 

- numpy 
- python 2.7 

## How to run: 

```
python main.py
```

In main.py there is a variable called platform. By assigning to this variable the available canal in the canal dictionary, the algorithm will run it accordingly, 
with the parameters configured in the dictionary.   


## References: 
- **"Double Q-PI architecture for smart model-free control of canals"** ([https://www.sciencedirect.com/science/article/abs/pii/S0168169922002575?via%3Dihub])
- **Incremental Q-learning strategy for adaptive PID control of mobile robots** Carlucho et al. [Link](https://www.sciencedirect.com/science/article/pii/S0957417417301513)
