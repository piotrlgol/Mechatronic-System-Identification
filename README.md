# Mechatronic-System-Identification

This project is a graphical user interface for common transformations used in signal analysis. Currently available functions include:
- Displaying signal in time domain
- Displaying signal in frequency domain
- Performing short time fast fourier transform
- Performing continuous wavelet transform

## Installation
`pip install -r requirements.txt`

## Usage
To use the GUI simply run the `main.py`. To add signal go to menu > new, the window with options to define the signal will pop up. The app allows to either write the equation for the signal, or load a signal from a .mat file.
A signal in .mat file should contain time vector in a variable named 't', and amplitudeof the signal in variable named 'a'.
The function equation uses t as a time variable, it uses sin, cos, tan, log, exp, pi from numpy library and the rand(t) will create a random distribution vector with a length of t.

example:
`sin(2*pi*10*t) + rand(t)`

## Important!
The function equation uses `eval()` function, which is very dangerous if you accept strings to evaluate from untrusted input.
