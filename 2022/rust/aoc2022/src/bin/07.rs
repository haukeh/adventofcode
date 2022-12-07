use std::{collections::HashMap, fs, rc::Rc, cell::RefCell};

fn main() {
    let input = fs::read_to_string("input/07").unwrap();
    let stack:  Rc<RefCell<Vec<String>>> = Rc::new(RefCell::new(Vec::new()));
    let sizes: Rc<RefCell<HashMap<String, usize>>> = Rc::new(RefCell::new(HashMap::new()));
    let children: Rc<RefCell<HashMap<String, Vec<String>>>> = Rc::new(RefCell::new(HashMap::new()));

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
                let d = line.chars().skip(4).take_while(|c| !c.is_whitespace()).collect::<String>();
                if let Some(current) = stack.borrow().last() {
                    children.borrow_mut().entry(current.to_string()).or_default().push(d);
                }
            } else {
                let size = line
                    .chars()
                    .take_while(|c| c.is_numeric())
                    .collect::<String>()
                    .parse::<usize>()
                    .unwrap();
                    
                for dir in stack.borrow().iter() {                
                    let d = String::from(dir);
                    let mut s = sizes.borrow_mut();
                    let e = s.entry(d).or_default();
                    *(e) += size;
                }
            }
        }
    }
    println!("{:?}", sizes);
    let s = sizes.borrow();
    let dirs = s.iter().filter(|(_, &v)| v <= 100_000).collect::<Vec<_>>();

    println!("{:?}", dirs);

    let sum = dirs.iter().map(|(_, &v)| v).sum::<usize>();
    

    println!("{:?}", sum)
}

