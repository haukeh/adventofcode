use std::collections::HashMap;

use itertools::Itertools;

fn main() {
    let mut lines = include_str!("../../input/10").split('\n');

    let mut tick: usize = 1;
    let mut sprite_pos: isize = 1;
    let mut current: Option<(usize, Instr)> = None;
    let mut buf = vec![vec!['.'; 40]; 6];
    let mut exit = false;
    loop {
        // println!("tick: {}, sprite: {}, running: {:?}", tick, sprite_pos, current);

        let mut exec = false;
    
        // println!("tick: {}, sprite: {}", tick, sprite_pos);

        let row = (tick as f64 / 40f64).ceil() as usize - 1;
        let col = (tick - 1) % 40;

        // println!("tick: {}, sprite: {}, row: {}, col: {}", tick, sprite_pos, row, col);

        // println!("({}, {}, {})", sprite_pos-1, sprite_pos, sprite_pos+1);

        if col as isize == sprite_pos -1 || col as isize == sprite_pos || col as isize == sprite_pos + 1 {
            buf[row][col] = '#';
        }

        match current {
            Some((t, Instr::Addx(_))) if t == tick => {
                exec = true;
            }
            Some(_) => {
                //
            }
            None => match lines.next().map(parse_instruction) {
                Some(Instr::Noop) => {
                    // ???
                }
                Some(i @ Instr::Addx(_)) => {
                    current = Some((tick + 1, i));
                }
                None => {
                    if current.is_none() {
                        exit = true;
                    }
                }
            },
        }

        if exec {
            if let Some((_, Instr::Addx(n))) = current.take() {
                sprite_pos += n;
            } else {
                println!("WAT");
            }
        }

        if exit {
            break;
        }
        
        if tick == 240 {
            tick = 0;
            draw(&buf);
            reset(&mut buf);
        } 
        
        tick += 1;
    }
}

fn draw(buf: &Vec<Vec<char>>) {
    let strbuf = buf.iter().map(String::from_iter).join("\n");
    print!("{}", strbuf);
}

fn reset(buf: &mut Vec<Vec<char>>) {
    for l in buf {
        for c in l {
            *c = '.'
        }
    }
}

#[derive(Debug)]
enum Instr {
    Addx(isize),
    Noop,
}

fn parse_instruction(s: &str) -> Instr {
    if s.trim() == "noop" {
        Instr::Noop
    } else {
        let addx = s.split(' ').collect::<Vec<_>>();
        Instr::Addx(addx[1].parse::<isize>().unwrap())
    }
}
