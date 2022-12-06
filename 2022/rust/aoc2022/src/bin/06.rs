use itertools::Itertools;
use std::collections::HashSet;
use std::fs;
use std::ops::Index;

fn main() {
    let input = fs::read_to_string("input/06").unwrap();
    let input = "bvwbjplbgvbhsrlpgdmjqwftvncz";

    let mut seen: Vec<char> = Vec::new();
    let mut cnt = 0;
    for c in input.chars() {
        cnt += 1;
        if seen.contains(&c) {
            seen.drain(c[..seen.in()])
        }

        seen.push(c);

        if seen.len() == 4 {
            break;
        }
        println!("cnt: {}, seen: {:?}", cnt, seen);
    }
    println!("{}", cnt - 1);
}
