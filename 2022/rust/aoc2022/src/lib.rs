use std::fs;

pub fn input_as_string(day: usize) -> String {
    fs::read_to_string(format!("input/{:02}", day)).unwrap()
}
