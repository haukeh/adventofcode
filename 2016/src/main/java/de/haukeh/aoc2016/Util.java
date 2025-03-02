package de.haukeh.aoc2016;

import java.net.URISyntaxException;
import java.nio.file.Path;

public class Util {
    public static Path inputPath(int day) {
        try {
            return Path.of(Day2.class.getClassLoader().getResource("input/d" + day + ".txt").toURI());
        } catch (URISyntaxException e) {
            throw new RuntimeException(e);
        }
    }
}
