use aoc2024::file_as_string;
use regex::{Captures, Regex};

enum Token {
    Do,
    Dont,
    Mul(i64, i64),
}

impl Token {
    pub fn parse(capture: Captures<'_>) -> Self {
        match capture.get(0).unwrap().as_str() {
            "do()" => Self::Do,
            "don't()" => Self::Dont,
            _ => {
                let left_op: i64 = capture.get(1).map(|n| n.as_str().parse().unwrap()).unwrap();
                let right_op: i64 = capture.get(2).map(|n| n.as_str().parse().unwrap()).unwrap();
                Self::Mul(left_op, right_op)
            }
        }
    }
}

fn main() -> anyhow::Result<()> {
    let text = file_as_string("input/d3.txt")?;
    let r = Regex::new(r"don't\(\)|do\(\)|mul\((\d+)\,(\d+)\)")?;
    let tokens: Vec<Token> = r.captures_iter(&text).map(|c| Token::parse(c)).collect();

    let mut p1: i64 = 0;
    let mut p2: i64 = 0;
    let mut on: bool = true;
    
    for t in tokens.iter() {
        match t {
            Token::Do => on = true,
            Token::Dont => on = false,
            Token::Mul(a, b) => {
                p1 += a * b;
                if on {
                    p2 += a * b;
                }
            }
        }
    }

    println!("{}", p1);
    println!("{}", p2);

    Ok(())
}
