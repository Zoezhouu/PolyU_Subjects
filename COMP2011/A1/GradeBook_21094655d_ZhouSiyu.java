import java.security.SecureRandom;
import java.util.Arrays;
/**
 *
 * @author Yixin Cao (September 14, 2022)
 *
 * A class for grade book of COMP2011.
 *
 * There are two sessions, denoted as 1 and 2.
 * There are four possible grades, 'A', 'B', 'C', and 'D.' (The Grading System of PolyU, which can be found at https://www.polyu.edu.hk/en/gs/current-students/graduation-requirements/, is more complicated.)
 *
 * It needs to support two views.
 * First, the grades are displayed session by session. In each session, the students are listed in alphabetical order.
 * Second, the grades are displayed by grades, and for students with the same grade, students from session 1 are listed before session 2.
 *
 * Read the {@code Student} class carefully before you start.
 *
 * If your implementation is correct, elements of the same value should respect their original order,
 * e.g., for input {1.25, 0, 1.25, 2.5, 10, 2.5, 1.25, 5, 2.5}, the output should be
 * [0.0 (1), 1.25 (0), 1.25 (2), 1.25 (6), 2.5 (3), 2.5 (5), 2.5 (8), 5.0 (7), 10.0 (4)].
 */
public class GradeBook_21094655d_ZhouSiyu { // Please change!

    static class Student {
        String id;
        byte session; // 1 or 2
        char grade; // 'A', 'B', 'C', or 'D'

        public Student(String id, byte session) {
            this.id = id;
            this.session = session;
        }

        public void setGrade(char grade) {
            this.grade = grade;
        }
        public String toString () {
            return id + " (" +  session + "): " + grade;
        }
    }
    //Student: id(session)grade

    /**
     * Do not modify the signatures of this method.
     * For comparing two strings, you need the {String.compareTo()} method.
     * https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/String.html#compareTo(java.lang.String)
     * For this task, consider it as a single step (not true in general).
     *
     * I've discussed this question with the following students:
     *     1.
     *     2.
     *     3.
     *     ...
     *
     * I've sought help from the following Internet resources and books:
     *     1. https://stackoverflow.com/questions/52527626/java-selection-sorting-an-array-of-objects-by-an-int-key-and-displaying-in-table
     *     2. https://blog.csdn.net/gjt1234/article/details/124006183
     *     3. https://blog.csdn.net/weixin_52450702/article/details/124253459
     *     ...
     *
     * Running time: O( n^2 ). (n is the total number of students.)
     */
    public static void swap(Student[] a, int index1, int index2) {
        Student temp = a[index1];
        a[index1] = a[index2];
        a[index2] = temp;
        return;
    }

    public static void sessionView(Student[] a) {
        // displayed session by session
        // in each session, students are listed in alphabetical order

        //sort with id first
        //str1.compareTo(str2)
        int n = a.length;
        //selection sort
        for (int i = 0; i < n-1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if ((a[min].id).compareTo(a[j].id)>0)
                    min = j;
                swap(a, min, i);
            }
        }

        //then sort with session
        //selection sort
        for (int i = 0; i < n-1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (a[min].session > a[j].session)
                    min = j;
                swap(a, min, i);
            }
        }
    }

    /*
     *
     * Arrange the grade book by grades, 'A' first and 'D' last.
     * For the same grade, list students from session 1 before session 2.
     *
     * My approach is to deal with sessions first, then grades.
     * The main benefit is that I can reuse the code from <code>sessionView</code>.
     * Alternatively, one can use eight counts for the number of students in each session for a different grade,
     * the number of students from session 1 with grade 'A,'
     * the number of students from session 2 with grade 'A,'
     * the number of students from session 1 with grade 'B,' etc.
     * Yet another (better) way is to do it in place.
     * Try to think about how to do it. You may get some hints from step 1.
     */
    /**
     * 1. Do not modify the signatures of this method.
     *
     * I've discussed this question with the following students:
     *     1.
     *     2.
     *     3.
     *     ...
     *
     * I've sought help from the following Internet resources and books:
     *     1. https://www.javatpoint.com/post/java-character-compare-method
     *     2. https://blog.csdn.net/gjt1234/article/details/124006183
     *     3. https://blog.csdn.net/weixin_52450702/article/details/124253459
     *     4. https://javahungry.blogspot.com/2020/04/compare-characters-java.html
     *
     * Running time: O(n^2   ). (n is the total number of students.)
     */
    public static void gradeView(Student[] a) {
        sessionView(a);

        //already re-use sessionView() - sorted with session

        //sort with grades
        int n = a.length;

        //selection sort
        for (int i = 0; i < n-1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (a[min].grade > a[j].grade)
                    min = j;
                swap(a, min, i);
            }
        }
    }

    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();
        int n = 200;
        Student[] s = new Student[n];
        char[] g = {'A', 'B', 'C', 'D'};
        int id = 65536;
        for (int i = 0; i < n; i++) {
            id += random.nextInt(100);
            s[i] = new Student(String.valueOf(id), (byte)(id % 2 + 1));
            s[i].setGrade(g[random.nextInt(4)]);
        }
        System.out.println(Arrays.toString(s));
        sessionView(s);
        System.out.println("\nThe session view: ");
        System.out.println(Arrays.toString(s));
        gradeView(s);
        System.out.println("\nAfter sorting by grade: ");
        System.out.println(Arrays.toString(s));
    }
}
