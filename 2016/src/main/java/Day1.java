package src.main.java;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class Day1 {

    record Point(int x, int y) {
        public int distance(Point other) {
            return Math.abs(x - other.x) + Math.abs(y - other.y);
        }
        
        @Override
        public final String toString() {
            return "(" + x + "," + y + ")";
        }
    }

    static final Point[] DIRS = { new Point(-1, 0), new Point(0, 1), new Point(1, 0), new Point(0, -1) };

    public static void main(String[] args) throws IOException {
        var input = List.of(Files.readString(Path.of("input/d1.txt")).strip().replace(" ", "").split(","));

        final Point start = new Point(0, 0);

        var p1 = moveDirections(input, start, 1, false).distance(start);
        var p2 = moveDirections(input, start, 1, true).distance(start);

        System.out.println(p1);
        System.out.println(p2);
    }

    static Point moveDirections(Iterable<String> instructions, Point start, int startDir, boolean p2) {
        int dir = startDir;
        Point pos = start;
        var seen = new HashSet<>();

        for (String instr : instructions) {
            int distance = Integer.parseInt(instr.substring(1));

            switch (instr.charAt(0)) {
            case 'L':
                dir = Math.floorMod(dir - 1, 4);
                break;
            case 'R':
                dir = Math.floorMod(dir + 1, 4);
                break;
            default:
                throw new IllegalStateException();
            }

            int dx = DIRS[dir].x;
            int dy = DIRS[dir].y;

            for (int i = 0; i < distance; i++) {
                pos = new Point(pos.x + dx, pos.y + dy);
                
                if (p2 && seen.contains(pos)) {
                    return pos;
                }

                seen.add(pos);
            }                
        }

        return pos;
    }
}