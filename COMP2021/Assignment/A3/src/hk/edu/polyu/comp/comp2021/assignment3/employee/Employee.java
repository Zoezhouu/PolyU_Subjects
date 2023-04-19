package hk.edu.polyu.comp.comp2021.assignment3.employee;

import static hk.edu.polyu.comp.comp2021.assignment3.employee.SalaryLevel.*;

/**
 * An employee in a company.
 */
public class Employee{
    protected SalaryLevel level;
    /**
     * Name of the employee.
     */
    String name;

    /**
     * Level of salary of the employee.
     */
    private SalaryLevel salaryLevel;

    public Employee() {
    }

    /**
     * Return the name of the employee.
     */
    public String getName(){
        return name;
    }

    /**
     * Return the salary level of the employee.
     */
    public SalaryLevel getSalaryLevel(){
        return salaryLevel;
    }

    /**
     * Set the salary level.
     */
    public void setSalaryLevel(SalaryLevel salaryLevel){
        this.salaryLevel = salaryLevel;
    }

    /**
     * Initialize an employee object.
     */
    public Employee(String name, SalaryLevel level){

        // Add missing code here.
        this.name = name;
        this.salaryLevel = level;
        
    }

    /**
     * Return the salary of the employee.
     */
    public double salary() {
        // The salary of an employee is computed as the multiplication
        // of the base salary (2000.0) and the scale of the employee's salary level.

        // Add missing code here.
        double scale = 0;
        if (this.salaryLevel == ENTRY){
            scale = getEntry();
        }
        else if(this.salaryLevel == JUNIOR){
            scale = getJunior();
        }
        else if (this.salaryLevel == SENIOR){
            scale = getSenior();
        }
        else if (this.salaryLevel == EXECUTIVE) {
            scale = getExecutive();
        }

        return BASE_SALARY * scale;

    }

    /**
     * Base salary of all employees.
     */
    public static final double BASE_SALARY = 2000.0;

}
