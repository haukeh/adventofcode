package de.haukeh.aoc2016;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class Day1 {

    static final Point[] DIRS = {new Point(-1, 0), new Point(0, 1), new Point(1, 0), new Point(0, -1)};

    public static void main(String[] args) throws IOException {
        var input = List.of(Files.readString(Util.inputPath(1)).strip().replace(" ", "").split(","));

        final Point start = new Point(0, 0);

        var p1 = moveDirections(input, start, false).distance(start);
        var p2 = moveDirections(input, start, true).distance(start);

        System.out.println(p1);
        System.out.println(p2);
    }

    static Point moveDirections(Iterable<String> instructions, Point start, boolean p2) {
        int dir = 1;
        Point pos = start;
        var seen = new HashSet<>();

        for (String instr : instructions) {
            int distance = Integer.parseInt(instr.substring(1));

            dir = switch (instr.charAt(0)) {
                case 'L' -> Math.floorMod(dir - 1, 4);
                case 'R' -> Math.floorMod(dir + 1, 4);
                default -> throw new IllegalStateException();
            };

            int dx = DIRS[dir].x();
            int dy = DIRS[dir].y();

            for (int i = 0; i < distance; i++) {
                pos = new Point(pos.x() + dx, pos.y() + dy);

                if (p2 && seen.contains(pos)) {
                    return pos;
                }

                seen.add(pos);
            }
        }

        return pos;
    }
}