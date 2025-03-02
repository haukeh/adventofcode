#!/usr/bin/env fish

if test (count $argv) -eq 0
    echo "Usage: ./run.sh <day_number>"
    exit 1
end

if not mvn -q compile
    echo "Compilation failed."
    exit 1
end

set day_number $argv[1]
set main_class "de.haukeh.aoc2016.Day$day_number"

mvn -q exec:java -Dexec.mainClass=$main_class