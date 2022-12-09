use std::{
    collections::{HashMap, HashSet},
    error::Error,
    fmt::Display,
    hash::Hash,
    mem::take,
    ops::{Add, AddAssign},
    str::FromStr,
};

use itertools::Itertools;
use regex::Regex;

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
struct Point {
    x: isize,
    y: isize,
}

impl Point {
    fn new(x: isize, y: isize) -> Self {
        Point { x, y }
    }

    fn step(&mut self, dir: &Dir) {
        match dir {
            Dir::Right => self.x += 1,
            Dir::Up => self.y += 1,
            Dir::Left => self.x -= 1,
            Dir::Down => self.y -= 1,
        }
    }

    fn follow(&mut self, other: &Point) {
        self.x += (other.x - self.x).signum();
        self.y += (other.y - self.y).signum();   
    }

    fn adjacent_to(&self, other: &Point) -> bool {
        let dx = self.x - other.x;
        let dy = self.y - other.y;
        let res = dx.abs() <= 1 && dy.abs() <= 1;
        res
    }
}

impl Default for Point {
    fn default() -> Self {
        Self {
            x: Default::default(),
            y: Default::default(),
        }
    }
}

impl Display for Point {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

enum Dir {
    Right,
    Up,
    Left,
    Down,
}

impl From<&str> for Dir {
    fn from(s: &str) -> Self {
        match s {
            "R" => Dir::Right,
            "U" => Dir::Up,
            "L" => Dir::Left,
            "D" => Dir::Down,
            _ => unreachable!(),
        }
    }
}

struct Move(Dir, isize);

fn parse(line: &str) -> Move {
    let re = Regex::new(r"(\w) (\d+)").unwrap();
    let cap = re.captures(line).unwrap();
    Move(Dir::from(&cap[1]), cap[2].parse::<isize>().unwrap())
}

fn main() {
    let input = include_str!("../../input/09").lines();
    let knots: usize = 9;
    let mut points = vec![Point::new(0, 0); knots + 1];
    let mut histories = HashSet::new();

    for Move(dir, amount) in input.map(parse) {
        println!("BEFORE: {:?}", points);
        for _ in 0..amount {
            points[0].step(&dir);

            for k in 1..points.len() {
                let head = points[k - 1];
                // println!("h: {:?} - t: {:?}", head, points[k]);
                if !points[k].adjacent_to(&head) {
                    // println!("at idx {} {:?} follows {:?}", k, points[k], head);
                    // println!("BEFORE: {:?}", points);
                    points[k].follow(&head);
                }
            }
            histories.insert(points[knots].clone());
        }
        println!("AFTER: {:?}", points);
        println!(
            "-------------------------------------------------------------------------------------"
        );
        // println!("TAILZ: {:?}", points[knots]);
        // println!("-------------------------------------------------------------------------------------");

        // println!("{:?}", points);
        // println!("head: {:?}", points[0]);
        // println!("tail: {:?}", points[knots]);
    }

    println!("{}", histories.len());
}
