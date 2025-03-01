use std::collections::{HashMap, HashSet};
use std::fs;

fn parse_rule(rule: &str) -> (i32, i32) {
    let parts: Vec<&str> = rule.trim().split('|').collect();
    (parts[0].parse::<i32>().unwrap(), parts[1].parse::<i32>().unwrap())
}

fn sort(nums: &mut Vec<i32>, rule_map: &HashMap<i32, HashSet<i32>>) {
    let all: HashSet<i32> = nums.iter().cloned().collect();
    let mut i = 0;

    while i < nums.len() {
        if let Some(after) = rule_map.get(&nums[i]) {
            let inter: HashSet<_> = after.intersection(&all).cloned().collect();

            for &e in &inter {
                if let Some(idx) = nums.iter().position(|&x| x == e) {
                    if idx < i {
                        i = idx;
                    }
                    let elem = nums.remove(idx);
                    nums.push(elem);
                }
            }
        }
        i += 1;
    }
}

fn main() {
    // Read input from file
    let input = fs::read_to_string("input/d5.txt").expect("Failed to read input file");
    let parts: Vec<&str> = input.split("\n\n").collect();
    let rules = parts[0];
    let updates = parts[1];

    // Parse rules
    let mut rule_map: HashMap<i32, HashSet<i32>> = HashMap::new();
    for rule in rules.lines() {
        let (before, after) = parse_rule(rule);
        rule_map.entry(before).or_insert_with(HashSet::new).insert(after);
    }

    let mut p1 = 0;
    let mut incorrect: Vec<Vec<i32>> = Vec::new();

    // Process updates
    for update in updates.lines() {
        let nums: Vec<i32> = update.split(',').map(|x| x.parse::<i32>().unwrap()).collect();
        let mut seen: HashSet<i32> = HashSet::new();
        let mut bad = false;

        for &num in &nums {
            if let Some(after) = rule_map.get(&num) {
                let inter: HashSet<_> = seen.intersection(after).cloned().collect();

                if !inter.is_empty() {
                    bad = true;
                    incorrect.push(nums.clone());
                    break;
                }
            }
            seen.insert(num);
        }

        if !bad {
            p1 += nums[nums.len() / 2];
        }
    }

    // Sort incorrect lists
    let mut sorted: Vec<Vec<i32>> = Vec::new();
    for mut update in incorrect {
        sort(&mut update, &rule_map);
        sorted.push(update);
    }

    let p2: i32 = sorted.iter().map(|nums| nums[nums.len() / 2]).sum();

    // Print results
    println!("{}", p1);
    println!("{}", p2);
}