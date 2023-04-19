package hk.edu.polyu.comp.comp2021.assignment2.shape;

public class XYRectangle {
    private Point topLeft;
    private Point bottomRight;

    public Point getTopLeft() {
        return topLeft;
    }

    public Point getBottomRight() {
        return bottomRight;
    }

    public XYRectangle(Point p1, Point p2){
        if (p1.getX() > p2.getX()){
            this.topLeft = p2;
            this.bottomRight = p2;
        }
        if (p1.getX() < p2.getX()){
            this.topLeft = p1;
            this.bottomRight = p2;
        }

    }

    public String toString(){
        return String.format("<%s,%s>",topLeft,bottomRight);
    }

    public int area(){
        return (bottomRight.getX() - topLeft.getX()) * (topLeft.getY() - bottomRight.getY());

    }

    public XYRectangle rotateClockwise(){
        Point newTopLeft = new Point(topLeft.getX() - (topLeft.getY() - bottomRight.getY()), topLeft.getY());
        Point newBottomRight = new Point (topLeft.getX(),topLeft.getY()-(bottomRight.getX()-topLeft.getX()));

        return new XYRectangle(newTopLeft, newBottomRight);
    }

    public XYRectangle move(int deltaX, int deltaY){
        Point newTopLeft = new Point(topLeft.getX() + deltaX, topLeft.getY() + deltaY);
        Point newBottomRight = new Point(bottomRight.getX() + deltaX, bottomRight.getY() + deltaY);

        return new XYRectangle(newTopLeft,newBottomRight);

    }

    public boolean contains(Point p){
        if (p.getX() >= topLeft.getX()
                && p.getX() <= bottomRight.getX()
                && p.getY() >= bottomRight.getY()
                && p.getY() <= topLeft.getY()){
            return true;
        }
        return false;
    }

    public boolean contains(XYRectangle r){
        if (r.topLeft.getX() >= topLeft.getX()
                && r.topLeft.getY() <= topLeft.getY()
                && r.bottomRight.getX() <= bottomRight.getX()
                && r.bottomRight.getY() >= bottomRight.getY()){
            return true;
        }

        return false;

    }
    public Point midpoint(Point a, Point b){
        int midX = (a.getX() + b.getX())/2;
        int midY = (a.getY() + b.getY())/2;
        return new Point(midX, midY);
    }

    public int sideLengthX(XYRectangle a, XYRectangle b){
        int length = Math.abs(a.getTopLeft().getX() - a.getBottomRight().getX())
                + Math.abs(b.getTopLeft().getX() - b.getTopLeft().getX());
        return length;
    }

    public int sideLengthY(XYRectangle a, XYRectangle b){
        int length = Math.abs(a.getTopLeft().getY() - a.getBottomRight().getY())
                + Math.abs(b.getTopLeft().getY() - b.getTopLeft().getY());
        return length;
    }

    public boolean overlapsWith(XYRectangle r){

        // middle point of original rectangule and rectangule r
        Point midPointThis = midpoint(this.topLeft, this.bottomRight);
        Point midPointr = midpoint(r.topLeft, r.bottomRight);

        // combine together
        int lengthX = Math.abs(midPointr.getX() - midPointThis.getX());
        int lengthY = Math.abs(midPointr.getX() - midPointThis.getX());

        //length of original recgtangle and rectangle r
        int sideLengthX = sideLengthX(this, r);
        int sideLengthY = sideLengthX(this, r);

        if (lengthX <= sideLengthX && lengthY <=sideLengthY){
            return true;
        }
        return false;


    }
}

class Point{
    private int x;
    private int y;

    public Point(int x, int y) {
        set(x, y);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void set(int x, int y){
        this.x = x;
        this.y = y;
    }

    public String toString(){
        return "(" + getX() + "," + getY() + ")";
    }
}

