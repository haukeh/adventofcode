use std::{cell::RefCell, collections::HashMap, fs, rc::Rc};

use itertools::Itertools;

fn main() {
    let input = fs::read_to_string("input/07").unwrap();
    let stack: Rc<RefCell<Vec<String>>> = Rc::new(RefCell::new(Vec::new()));
    let sizes: Rc<RefCell<HashMap<String, usize>>> = Rc::new(RefCell::new(HashMap::new()));

    for line in input.lines() {
        if line.starts_with("$") {
            let cmd = line.chars().skip(2).take(2).collect::<String>();
            match &cmd[..] {
                "cd" => {
                    let arg = line
                        .chars()
                        .skip(5)
                        .take_while(|c| c != &' ')
                        .collect::<String>();
                    if arg == ".." {
                        stack.borrow_mut().pop();
                    } else {
                        stack.borrow_mut().push(arg);
                    }
                }
                "ls" => {
                    continue;
                }
                _ => println!("Got other"),
            }
        } else {
            if line.starts_with("dir") {
                let d = line
                    .chars()
                    .skip(4)
                    .take_while(|c| !c.is_whitespace())
                    .collect::<String>();
                let path = stack.borrow().iter().join("/");
                sizes.borrow_mut().insert(path, 0);
            } else {
                let size = line
                    .chars()
                    .take_while(|c| c.is_numeric())
                    .collect::<String>()
                    .parse::<usize>()
                    .unwrap();
                let _ = stack.borrow().iter().fold("".to_string(), |acc, x| {
                    let p = if acc == "/" {
                        acc
                    } else {
                        format!("{}/{}", acc, x)
                    };
                    let mut si = sizes.borrow_mut();
                    println!("{}", p);
                    *si.entry(p.to_string()).or_default() += size;
                    p
                });
            }
        }
    }

    let s = sizes.borrow();
    let dirs = s.iter().filter(|(_, &v)| v <= 100_000).collect::<Vec<_>>();
    let p1 = dirs.iter().map(|(_, &v)| v).sum::<usize>();

    let root_size = s.get("/").unwrap();
    println!("{}", root_size);

    let p2 = s
        .iter()
        .filter(|(_, &v)| v != 0 && ((70000000 - 30000000) + v >= *root_size))
        .map(|(_, &v)| v)
        .min()
        .unwrap();

    println!("{:?}", p1);
    println!("{:?}", p2);
}
