package hk.edu.polyu.comp.comp2021.assignment3.employee;

/**
 * Levels of salary.
 */
enum SalaryLevel {
    ENTRY(1), JUNIOR(1.25), SENIOR(1.5), EXECUTIVE(2);

    // Add missing code here.
    private double level;




    SalaryLevel(double d){
        level = d;
    }
    public double getScale(){
        return this.level;
    }
    public static double getEntry(){
        return SalaryLevel.ENTRY.getScale();
    }

    public static double getJunior(){
        return SalaryLevel.JUNIOR.getScale();
    }

    public static double getSenior(){
        return SalaryLevel.SENIOR.getScale();
    }

    public static double getExecutive(){
        return SalaryLevel.EXECUTIVE.getScale();
    }
}