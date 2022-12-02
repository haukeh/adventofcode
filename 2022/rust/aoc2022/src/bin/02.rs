use crate::GameResult::{Draw, Loss, Win};
use crate::RPS::{Paper, Rock, Scissors};
use aoc2022::input_as_string;
use itertools::Itertools;
use std::str::FromStr;

fn main() {
    let input = input_as_string(02);
    let rounds = input
        .lines()
        .map(|l| {
            l.split_whitespace()
                .collect_tuple::<(&str, &str)>()
                .unwrap()
        })
        .collect::<Vec<_>>();

    let score = part1(&rounds);
    println!("Part 1: {}", score);
    let score = part2(&rounds);
    println!("Part 2: {}", score);
}

fn part1(rounds: &Vec<(&str, &str)>) -> usize {
    let s = rounds
        .iter()
        .map(|(a, b)| (RPS::from_str(a).unwrap(), RPS::from_str(b).unwrap()));

    let mut score: usize = 0;
    for (enemy, you) in s {
        score += you.play(enemy);
    }
    score
}

fn part2(rounds: &Vec<(&str, &str)>) -> usize {
    let s = rounds
        .into_iter()
        .map(|(a, b)| (RPS::from_str(*a).unwrap(), GameResult::from(*b)));

    let mut score: usize = 0;
    for (opponents_move, wanted_result) in s {
        score += run_step(wanted_result, opponents_move);
    }
    score
}

fn run_step(res: GameResult, enemy: RPS) -> usize {
    match enemy {
        Rock => match res {
            Win => Paper.value() + Win.value(),
            Loss => Scissors.value() + Loss.value(),
            Draw => Rock.value() + Draw.value(),
        },
        Paper => match res {
            Win => Scissors.value() + Win.value(),
            Loss => Rock.value() + Loss.value(),
            Draw => Paper.value() + Draw.value(),
        },
        Scissors => match res {
            Win => Rock.value() + Win.value(),
            Loss => Paper.value() + Loss.value(),
            Draw => Scissors.value() + Draw.value(),
        },
    }
}

#[derive(Debug)]
enum RPS {
    Rock,
    Paper,
    Scissors,
}

enum GameResult {
    Win,
    Loss,
    Draw,
}

impl GameResult {
    pub const fn value(self) -> usize {
        match self {
            Win => 6,
            Loss => 0,
            Draw => 3,
        }
    }
}

impl RPS {
    pub const fn value(self) -> usize {
        match self {
            Rock => 1,
            Paper => 2,
            Scissors => 3,
        }
    }

    pub fn play(self, other: RPS) -> usize {
        match self {
            Rock => match other {
                Rock => self.value() + 3,
                Paper => self.value() + 0,
                Scissors => self.value() + 6,
            },
            Paper => match other {
                Rock => self.value() + 6,
                Paper => self.value() + 3,
                Scissors => self.value() + 0,
            },
            Scissors => match other {
                Rock => self.value() + 0,
                Paper => self.value() + 6,
                Scissors => self.value() + 3,
            },
        }
    }
}

impl From<&str> for GameResult {
    fn from(s: &str) -> Self {
        match s {
            "X" => Loss,
            "Y" => Draw,
            "Z" => Win,
            _ => panic!("ouch"),
        }
    }
}

impl FromStr for RPS {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "A" | "X" => Ok(Rock),
            "B" | "Y" => Ok(Paper),
            "C" | "Z" => Ok(Scissors),
            _ => Err(()),
        }
    }
}
