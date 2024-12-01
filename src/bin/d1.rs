use aoc2024::file_lines;
use itertools::{self, Itertools};

fn main() -> anyhow::Result<()> {
    let lines = file_lines("input/d1.txt")?;
    let (left, right): (Vec<_>, Vec<_>) = lines
        .map(|line| {
            let (l, r) = line.split_once(' ').unwrap();
            (
                l.trim().parse::<i64>().unwrap(),
                r.trim().parse::<i64>().unwrap(),
            )
        })
        .unzip();

    let part1 = left
        .iter()
        .sorted()
        .zip(right.iter().sorted())
        .map(|(l, &r)| (l).abs_diff(r))
        .sum::<u64>();

    let part2 = left
        .into_iter()
        .map(|l| l * right.iter().filter(|&&r| r == l).count() as i64)
        .sum::<i64>();

    println!("{}", part1);
    println!("{}", part2);

    Ok(())
}
