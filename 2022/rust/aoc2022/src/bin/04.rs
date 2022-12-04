use itertools::Itertools;
use std::fs;
use std::ops::{Range, RangeInclusive};

fn main() {
    let input = fs::read_to_string("input/04").unwrap();
    let mut p1 = 0u32;
    let mut p2 = 0u32;

    let pairs = input.lines().map(|l| {
        l.trim()
            .split(['-', ','])
            .map(|a| a.parse::<u32>().unwrap())
            .collect_tuple::<(_, _, _, _)>()
            .unwrap()
    });

    for (start_a, end_a, start_b, end_b) in pairs {
        if (start_a >= start_b && end_a <= end_b) || (start_b >= start_a && end_b <= end_a) {
            p1 += 1;
        }
        if !(end_a < start_b || start_a > end_b) {
            p2 += 1;
        }
    }

    println!("{:?}", p1);
    println!("{:?}", p2);
}
