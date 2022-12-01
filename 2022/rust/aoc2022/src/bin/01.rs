use std::fs::File;
use std::io::{BufRead, BufReader};
use std::cmp::Reverse;

fn main() {
    let f = File::open("input/01").unwrap();
    let l =
        BufReader::new(f).lines()
            .map(|l| l.unwrap())
            .collect::<Vec<_>>();
    let e = l.split(|l| l == "")
        .collect::<Vec<_>>();

    let mut elves = e.into_iter().map(|e| e.iter().map(|i| i.parse::<u32>().unwrap()).sum::<u32>()).collect::<Vec<_>>();

    let max = elves.iter().max().unwrap().clone();

    elves.sort_by_key(|w| Reverse(*w));
    let top3 = e.iter().take(3).sum::<u32>();

    println!("part1: {}", max);
    println!("part2: {}", top3);
}