use itertools::Itertools;
use std::collections::HashSet;
use std::fs;

fn main() {
    let input = fs::read_to_string("input/06").unwrap();
    // let input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    let mut seen: Vec<char> = Vec::new();
    let mut cnt = 0;
    for c in input.chars() {
        cnt += 1;
        
        if seen.contains(&c) {
            let pos = seen.iter().position(|i| *i == c).unwrap();
            seen.drain(..=pos);
        }

        seen.push(c);

        if seen.len() == 14 {
            break;
        }
    }

    println!("{}", cnt);
}
