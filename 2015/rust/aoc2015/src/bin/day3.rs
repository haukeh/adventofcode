extern crate core;

use std::collections::HashMap;
use std::fs::read_to_string;

#[derive(Eq, Hash, PartialEq, Copy, Clone, Debug)]
struct Point {
    x: i64,
    y: i64,
}

struct Santa {
    pos: Point,
    seen: HashMap<Point, usize>,
}

impl Santa {
    fn new(initial_pos: Point) -> Self {
        let mut hm = HashMap::new();
        hm.insert(initial_pos, 1);
        Santa {
            pos: initial_pos,
            seen: hm,
        }
    }

    fn handle(mut self, input: impl IntoIterator<Item=char>) -> Self {
        for c in input {
            match c {
                '>' => {
                    self.pos = Point { x: self.pos.x + 1, ..self.pos };
                    *self.seen.entry(self.pos).or_insert(0) += 1
                }
                '<' => {
                    self.pos = Point { x: self.pos.x - 1, ..self.pos };
                    *self.seen.entry(self.pos).or_insert(0) += 1
                }
                'v' => {
                    self.pos = Point { y: self.pos.y - 1, ..self.pos };
                    *self.seen.entry(self.pos).or_insert(0) += 1
                }
                '^' => {
                    self.pos = Point { y: self.pos.y + 1, ..self.pos };
                    *self.seen.entry(self.pos).or_insert(0) += 1
                }
                _ => {
                    panic!("invalid input character")
                }
            }
        }
        self
    }

    fn visited_houses(&self) -> usize {
        return self.seen.keys().count();
    }

    fn merge_results(mut self, other: Santa) -> Santa {
        self.seen.extend(other.seen);
        self
    }
}

fn main() {
    let input = read_to_string("input/d3.txt").unwrap();

    let sum = part1(input.as_str());

    println!("{}", sum);

    let sum2 = part2(input.as_str());

    println!("{}", sum2)
}

fn part1(input: &str) -> usize {
    let santa = Santa::new(Point { x: 0, y: 0 });
    return santa.handle(input.chars()).visited_houses();
}

fn part2(input: &str) -> usize {
    let santa = Santa::new(Point { x: 0, y: 0 })
        .handle(input.chars().step_by(2));
    let robo_santa = Santa::new(Point { x: 0, y: 0 })
        .handle(input.chars().skip(1).step_by(2));

    let both = santa.merge_results(robo_santa);
    return both.visited_houses();
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1_1() {
        assert_eq!(2, part1(">"))
    }

    #[test]
    fn ex2_1() {
        assert_eq!(4, part1("^>v<"))
    }

    #[test]
    fn ex3_1() {
        assert_eq!(2, part1("^v^v^v^v^v"))
    }

    #[test]
    fn ex1_2() {
        assert_eq!(3, part2("^v"))
    }

    #[test]
    fn ex2_2() {
        assert_eq!(3, part2("^>v<"))
    }

    #[test]
    fn ex3_2() {
        assert_eq!(11, part2("^v^v^v^v^v"))
    }
}
