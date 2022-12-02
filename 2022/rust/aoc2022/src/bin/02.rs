use aoc2022::input_as_string;
use std::collections::HashMap;

fn main() {
    #[rustfmt::skip]
    let p1_scores = HashMap::from([
        ("A X", 4), ("A Y", 8), ("A Z", 3),
        ("B X", 1), ("B Y", 5), ("B Z", 9),
        ("C X", 7), ("C Y", 2), ("C Z", 6),
    ]);

    #[rustfmt::skip]
    let p2_scores = HashMap::from([
        ("A X", 3), ("A Y", 4), ("A Z", 8),
        ("B X", 1), ("B Y", 5), ("B Z", 9),
        ("C X", 2), ("C Y", 6), ("C Z", 7),
    ]);

    let mut part1 = 0;
    let mut part2 = 0;

    for r in input_as_string(02).lines().map(str::trim) {
        part1 += p1_scores[r];
        part2 += p2_scores[r];
    }

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
