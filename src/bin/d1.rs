use aoc2024::file_lines;
use itertools::{self, Itertools};

fn main() -> anyhow::Result<()> {
    let lines = file_lines("input/d1.txt")?;
    let mut left: Vec<i64> = Vec::new();
    let mut right: Vec<i64> = Vec::new();

    for line in lines {
        let values: Vec<&str> = line.split_whitespace().map(|x| x.trim()).collect();
        match values.as_slice() {
            [l, r] => {
                let numl = l.parse::<i64>()?;
                left.push(numl);
                let numr = r.parse::<i64>()?;
                right.push(numr);
            }
            _ => {
                panic!("error parsing lines");
            }
        }
    }

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
