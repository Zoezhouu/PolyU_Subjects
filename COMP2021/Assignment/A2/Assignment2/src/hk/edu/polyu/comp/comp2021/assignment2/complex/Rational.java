package hk.edu.polyu.comp.comp2021.assignment2.complex;

public class Rational {
    // Task 1: add the missing fields
    public int numerator, denominator;


    //common divisor
//    static int greatestCommonDivisor(int a, int b){
//        return (a % b ==0) ? b : greatestCommonDivisor(b, a%b);
//    }

    public Rational(int numerator, int denominator) {
        // Task 2: complete the constructor
        this.numerator = numerator;
        this.denominator = denominator;

    }

    public Rational add(Rational other) {
        // Task 2: complete the method
        // numerator by addition
        // numerator = numerator1 * denominator2 + numerator2 * denominator1
        int nAdd = this.numerator * other.denominator + this.denominator * other.numerator;
        // denominator by addition
        // denominator multiply each other
        int dAdd = this.denominator * other.denominator;

        return new Rational(nAdd,dAdd);
    }

    public Rational subtract(Rational other) {
        // Task 2: complete the method
        // numerator by subtraction
        // numerator = numerator1 * denominator2 + numerator2 * denominator1
        int nSub = this.numerator * other.denominator - this.denominator * other.numerator;
        // denominator by subtraction
        // denominator multiply each other
        int dSub = this.denominator * other.denominator;

        return new Rational(nSub, dSub);
    }

    public Rational multiply(Rational other) {
        // Task 2: complete the method

        // numerator by multiplication
        // numerator multiply each other
        int nMul = this.numerator * other.numerator;
        // denominator by multiplication
        // denominator multiply each other
        int dMul = this.denominator * other.denominator;

        return new Rational (nMul, dMul);
    }

    public Rational divide(Rational other) {
        // Task 2: complete the method
        // numerator by division
        // numerator = numerator1 * denominator2
        int nDiv = this.numerator * other.denominator;
        // denominator by division
        // denominator = denominator1 * numerator2
        int dDiv = this.denominator * other.numerator;

        // consider situation of calculated denominator < 0
        // denominator may be smaller than 0, then expression may be different with normal expression of fraction
        if (dDiv < 0){
            nDiv = -nDiv;
            dDiv = -dDiv;
        }


        return new Rational(nDiv, dDiv);
    }

    public String toString() {
        // Task 2: complete the method

        // convert number to string in format provided
        return String.format("%d/%d", numerator, denominator);

    }

    public void simplify() {
        // Task 2: complete the method

        int temp;
        // divide numerator and denominator by common divisor
        if (numerator <= denominator){
            temp = numerator;
        }
        else {
            temp = denominator;
        }

        for (int i = 1; i <= temp; i++){
            if (numerator % i == 0 && denominator % i == 0){
                numerator /= i;
                denominator /= i;
                i = 1;
            }

        }



    }

    // ==================================

}
