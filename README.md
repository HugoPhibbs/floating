# Etude 12: Floating

## Our approach

- We originally started this etude with Java, but Kate gave us the handy tip to instead to it in Python instead. This
  was due to the fact that using Python floats can avoid rounding errors that are possible with Java Doubles
- As arranged with stefanie we only implemented single precision in this etude due to our group size.

## Running the program
- To run the program enter: from within the **src** folder run the command 
```shell
python3 convert.py
``` 
- You will then be prompted to enter a file to read from. 
- After this enter in a file to write to with the suffix ".bin". 
- The converted floats will then be inside the newly created file. 


## Testing the program
- We tested our program using the test files given to us. Among with other manual tests.

## Python version
- Our program has been developed with Python 3.

## External libraries
- ctypes for writing python C types (this tip was kindly provided by Stefanie, danke!)
- binascii was used for converting IBM floats to python ones


