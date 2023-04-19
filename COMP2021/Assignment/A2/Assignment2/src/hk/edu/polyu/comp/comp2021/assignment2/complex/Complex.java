package hk.edu.polyu.comp.comp2021.assignment2.complex;

public class Complex {

    // Task 3: add the missing fields
    private Rational real, imag;
    public int numerator, denominator;


    public Complex(Rational real, Rational imag) {
        // Task 4: complete the constructor
        this.real = real;
        this.imag = imag;
    }




    public Complex add(Complex other) {
        // Task 4: complete the method

        // real-part numerator by addition
        int rnAdd = this.real.numerator * other.real.denominator + this.real.denominator * other.real.numerator;
        // real-part denominator by addition
        int rdAdd = this.real.denominator * other.real.denominator;
        // imagnary-part numerator by addition
        int inAdd = this.imag.numerator * other.imag.denominator + this.imag.denominator * other.imag.numerator;
        // imaginary-part denominator by addition
        int idAdd = this.imag.denominator * other.imag.denominator;

        //real-part number and imaginary-part number
        Rational realAdd = new Rational(rnAdd, rdAdd);
        Rational imagAdd = new Rational(inAdd, idAdd);
        return new Complex(realAdd, imagAdd);
    }

    public Complex subtract(Complex other) {
        // Task 4: complete the method

        // real-part numerator by subtraction
        int rnSub = this.real.numerator * other.real.denominator - this.real.denominator * other.real.numerator;
        // real-part denominator by subtraction
        int rdSub = this.real.denominator * other.real.denominator;
        // imagnary-part numerator by subtraction
        int inSub = this.imag.numerator * other.imag.denominator - this.imag.denominator * other.imag. numerator;
        // imaginary-part denominator by subtraction
        int idSub = this.imag.denominator * other.imag.denominator;

        //real-part number and imaginary-part number
        Rational realSub = new Rational(rnSub, rdSub);
        Rational imagSub = new Rational(inSub, idSub);
        return new Complex(realSub, imagSub);
    }

    public Complex multiply(Complex other) {
        // Task 4: complete the method

        // complex this = (a/A)+(b/B)i
        // complex other = (c/C)+(d/D)i
        int a = this.real.numerator;
        int b = this.imag.numerator;
        int c = other.real.numerator;
        int d = other.imag.numerator;
        int A = this.real.denominator;
        int B = this.imag.denominator;
        int C = other.real.denominator;
        int D = other.imag.denominator;

        // real-part numerator by multiplication
        int rnMul = a * c * B * D - b * d * A * C;
        //real-part denominator by multiplication
        int rdMul = A * B * C * D;
        // imaginary-part numerator by multiplication
        int inMul = b * c * A * D + a * d * B * C;
        // imaginary-part denominator by multiplication
        int idMul = A * B * C * D;

        // real-part number and imaginary-part number;
        Rational realMul = new Rational(rnMul, rdMul);
        Rational imagMul = new Rational(inMul, idMul);
        return new Complex(realMul, imagMul);
    }

    public Complex divide(Complex other) {
        // Task 4: complete the method
        // you may assume 'other' is never equal to '0+/-0i'.

        // (a/A)+(b/B)i
        // (c/C)+(d/D)i
        int a = this.real.numerator;
        int b = this.imag.numerator;
        int c = other.real.numerator;
        int d = other.imag.numerator;
        int A = this.real.denominator;
        int B = this.imag.denominator;
        int C = other.real.denominator;
        int D = other.imag.denominator;

        // real-part numerator by division
        int rnDiv = ( B * D * a * c + b * d * A * C ) * C * D;
        //real-part denominator by division
        int rdDiv = ( c * c * D * D + d * d * C * C ) * A * B;
        // imaginary-part numerator by division
        int inDiv = ( b * c * A * D - a * d * B * C ) * C * D;
        // imaginary-part denominator by division
        int idDiv = ( c * c * D * D + d * d * C * C ) * A * B;



        // real-part number and imaginary-part number;
        Rational realDiv = new Rational(rnDiv,rdDiv);
        Rational imagDiv = new Rational(inDiv, rdDiv);
        return new Complex(realDiv, imagDiv);
    }

    public void simplify() {
        // Task 4: complete the method
        int temp1, temp2;
        if (real.numerator <= real.denominator){
            temp1 = real.numerator;
        }
        else{
            temp1 = real.denominator;
        }
        if (real.numerator < 0){
            temp2 = -temp1;
        }
        else{
            temp2 = temp1;
        }

        //divide numerator and denominator by common divisor
        for (int i = 1; i <= temp2; i++){
            if (real.numerator % i == 0 && real.denominator % i == 0){
                real.numerator /= i;
                real.denominator /= i;
                i = 1;
            }




        }

        int temp3, temp4;
        if (imag.numerator <= imag.denominator){
            temp3 = imag.numerator;
        }
        else{
            temp3 = imag.denominator;
        }
        if (imag.numerator < 0){
            temp4 = -temp3;
        }
        else{
            temp4 = temp3;
        }
        for (int i = 1; i <= temp4; i++) {
            if (imag.numerator % i == 0 && imag.denominator % i == 0) {
                imag.numerator /= i;
                imag.denominator /= i;
                i = 1;
            }
        }




    }

    public String toString() {
        // Task 4: complete the method
        return String.format("(%s,%s)", real, imag);
    }

    // ==================================

}
