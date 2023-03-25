public class Test {
        private int a;
        private int b;
        private int c;

    public Test(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public String check() {
        double D = Math.pow(b, 2) - 4 * a * c;
        System.out.println("Дискриминант D = " + D);
        if (D > 0) {
            double x1 = (-b + Math.sqrt(D)) / (2 * a);
            double x2 = (-b - Math.sqrt(D)) / (2 * a);
            return "x1 = " + x1 + "\nx2 = " + x2;
        } else if (D == 0) {
            double x = -b / (2 * a);
            return "x = " + x;
        } else {
            return "Корней нет";
        }
    }
}
