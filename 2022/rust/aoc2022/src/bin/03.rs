use aoc2022::input_as_string;
use itertools::Itertools;
use std::collections::{HashMap, HashSet};
use std::fs;
use std::slice::Iter;
use itertools::Chunk;

fn main() {
    let values: HashMap<char, usize> = value_map();

    let input = fs::read_to_string("input/03").unwrap();
    let lines = input.lines().collect_vec();

    let p1 = part1(&lines, &values);
    let p2 = part2(&lines, &values);

    println!("{}", p1);
    println!("{}", p2);
}

fn part1(lines: &Vec<&str>, values: &HashMap<char, usize>) -> usize {
    let halves = lines.iter().map(|l| l.split_at(l.len() / 2)).collect_vec();
    let r = halves.iter().map(|(a, b)| find_dups(a, b)).collect_vec();

    r.iter()
        .map(|cs| {
            cs.iter()
                .map(|c| {
                    values
                        .get(c)
                        .expect(format!("{} should be there", c).as_str())
                })
                .sum::<usize>()
        })
        .sum()
}

fn part2(lines: &Vec<&str>, values: &HashMap<char, usize>) -> usize {
    let mut sum: usize = 0;
    for rucksack in &lines.iter().chunks(3) {
        sum += find_common(rucksack).iter().map(|elem| values[elem]).sum::<usize>()
    }
    sum
}

fn value_map() -> HashMap<char, usize> {
    let mut values: HashMap<char, usize> = HashMap::new();
    for (i, c) in ('a'..='z').enumerate() {
        values.insert(c, i + 1);
    }
    for (i, c) in ('A'..='Z').enumerate() {
        values.insert(c, i + 27);
    }
    values
}

fn find_common<'a>(items: Chunk<Iter<'a, &str>>) -> HashSet<char> {
    let mut seen: HashMap<char, usize> = HashMap::new();
    for l in items {
        for c in l.chars().sorted().dedup() {
            *seen.entry(c).or_default() += 1;
        }
    }
    seen.iter()
        .filter_map(|(c, cnt)| if *cnt == 3 { Some(*c) } else { None })
        .collect::<HashSet<_>>()
}

fn find_dups(a: &str, b: &str) -> HashSet<char> {
    let mut seen: HashMap<char, usize> = HashMap::new();
    for c in a.chars() {
        *seen.entry(c).or_default() += 1;
    }
    let mut res = HashSet::new();
    for c in b.chars() {
        if seen.contains_key(&c) {
            res.insert(c);
        }
    }
    res
}
