# sum of two complex numbers

num1=complex(input())
num2=complex(input())
real=(num1.real)+(num2.real)      # adding real parts of complex numbers
imag=(num1.imag)+(num2.imag)      # adding complex parts of complex numbers
real=int(real)
imag=int(imag)

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

print(complex(real,imag))         # printing final complex number
print("Real part is",real)        # printing real part of final complex number
print("Imaginary part is",imag)   # printing imaginary part of final complex number