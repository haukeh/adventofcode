package de.haukeh.aoc2016;

record Point(int x, int y) {

    public int distance(Point other) {
        return Math.abs(x - other.x) + Math.abs(y - other.y);
    }

    public Point add(Point other) {
        return new Point(x + other.x, y + other.y);
    }

    @Override
    public String toString() {
        return "(" + x + "," + y + ")";
    }
}
