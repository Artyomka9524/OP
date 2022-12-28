class Point<T> {

    T x;
    T y;

    public Point(T x, T y) {
        this.x = x;
        this.y = y;
    }

    public T getX() {
        return x;
    }

    public T getY() {
        return y;
    }

    public void showType() {
        System.out.println("Сейчас класс работает с типом "
                + x.getClass().getName());
    }

    @Override
    public String toString() {
        return "x = " + x + ", y = " + y + "\n";
    }
}

public class Task1 {

    public static void main(String args[]) {

        Point<Integer> p1 = new Point<>(45, 62
        );
        p1.showType();
        System.out.println(p1);

        Point<Double> p2 = new Point<>(10.5, 20.5);
        p2.showType();
        System.out.println(p2);

        Point<String> p3 = new Point<>("28 с половиной", "7 и три десятых");
        p3.showType();
        System.out.println(p3);

    }
}