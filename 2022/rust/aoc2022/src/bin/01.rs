use itertools::Itertools;

fn main() {
    let elves = aoc2022::input_as_string(1)
        .split("\n\n")
        .map(|l| l.lines().map(|i| i.parse::<u32>().unwrap()).sum::<u32>())
        .sorted()
        .rev()
        .collect_vec();

    let max = elves.first().unwrap();
    let top3: u32 = elves.iter().take(3).sum();

    println!("part1: {}", max);
    println!("part2: {}", top3);
}
