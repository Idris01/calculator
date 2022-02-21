# Minicalculator
The Minicalculator is a basic utility calculator the for basic arithmetic operation

## Installation
The minicalculator can be installed from the PYPI library using 

```
pip install minicalculator
```

## Usage
Sample Usage is as follows showing some of the functionalities.

```
from mini_calculator.calculator import Calculator

calc = Calculator()

>>> calc.add(5)
5.0
>>> calc.multiply(3)
15.0
>>> calc.divide(5)
3
>>> calc.reset()
>>> calc.answer
0.0
>>> calc.root(4) # square root of 4
2.0
```
## Testing
The functionality [test](./test.py) an be run using the following command

``` 
python -m unittest test.py

```

## Runninig Inside Container (Docker)
To run inside a Docker container using the [Dockerfile](./Dockerfile)
```
docker build -t <tag-name> .

```
and to run the container

``` 
docker run -it --rm <tag-name>
```