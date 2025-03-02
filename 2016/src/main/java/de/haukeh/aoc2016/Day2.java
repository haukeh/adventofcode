package de.haukeh.aoc2016;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;

import static java.lang.System.out;

public class Day2 {

    private static final Map<Point, Character> P1_KEYS = Map.of(
            new Point(-1, -1), '1', new Point(0, -1), '2', new Point(1, -1), '3',
            new Point(-1, 0), '4', new Point(0, 0), '5', new Point(1, 0), '6',
            new Point(-1, 1), '7', new Point(0, 1), '8', new Point(1, 1), '9');

    private static final Map<Point, Character> P2_KEYS = Map.ofEntries(
            Map.entry(new Point(0, -2), '1'),
            Map.entry(new Point(-1, -1), '2'),
            Map.entry(new Point(0, -1), '3'),
            Map.entry(new Point(1, -1), '4'),
            Map.entry(new Point(-1, 0), '6'),
            Map.entry(new Point(-2, 0), '5'),
            Map.entry(new Point(0, 0), '7'),
            Map.entry(new Point(1, 0), '8'),
            Map.entry(new Point(2, 0), '9'),
            Map.entry(new Point(0, 1), 'B'),
            Map.entry(new Point(-1, 1), 'A'),
            Map.entry(new Point(1, 1), 'C'),
            Map.entry(new Point(0, 2), 'D')
    );

    private static final Map<Character, Point> DIRS = Map.of(
            'U', new Point(0, -1),
            'R', new Point(1, 0),
            'D', new Point(0, 1),
            'L', new Point(-1, 0));

    public static void main(String[] args) throws IOException, URISyntaxException {
        String p1 = run(P1_KEYS);
        String p2 = run(P2_KEYS);

        out.println(p1);
        out.println(p2);
    }

    private static String run(Map<Point, Character> grid) throws IOException {
        Point currentPos = new Point(0, 0);
        var ans = new StringBuilder();

        for (String line : Files.readAllLines(Util.inputPath(2))) {
            for (char c : line.toCharArray()) {
                var diff = DIRS.get(c);
                var next = currentPos.add(diff);
                if (grid.containsKey(next)) {
                    currentPos = next;
                }
            }
            ans.append(grid.get(currentPos));
        }

        return ans.toString();
    }
}
