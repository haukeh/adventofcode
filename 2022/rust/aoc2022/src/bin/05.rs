use std::fs;
use itertools::Itertools;

fn main() {
    let input = fs::read_to_string("input/05_t").unwrap();
    let (c, ins) = input.split("\n\n").collect_tuple().unwrap();

    let rows = c.split('\n').map(|r| r.split(' ').collect::<Vec<_>>()).collect::<Vec<_>>();

    println!("{:?}", rows);
    println!("{:?}", ins);
}