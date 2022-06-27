extern crate core;

use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input/d1.txt").unwrap();

    part1(input.as_str());
    part2(input.as_str());
}

fn part1(input: &str) -> () {
    let mut i = 0;

    for c in input.chars() {
        match c {
            '(' => i += 1,
            ')' => i -= 1,
            _ => panic!("wrong input")
        }
    }

    println!("{}", i)
}

fn part2(input: &str) -> () {
    let mut i = 0;

    for (idx, c) in input.chars().enumerate() {
        match c {
            '(' => i += 1,
            ')' => i -= 1,
            _ => panic!("wrong input")
        }

        if i == -1 {
            println!("{}", idx + 1);
            break;
        }
    }
}
