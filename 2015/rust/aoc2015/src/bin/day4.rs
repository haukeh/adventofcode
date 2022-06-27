use std::ptr::hash;
use md5::{Md5, Digest};

fn main() {
    let input = "bgvyzdsv";
    let mut hasher = Md5::new();
    let mut i = 0;

    loop {
        i += 1;

        let next = format!("{}{}", input, i);
        let _ = &hasher.update(next);
        let res = &hasher.finalize_reset();
        let hex = format!("{:X}", res);

        if &hex[..6] == "000000" {
            println!("i: {}, Hash: {}", i, hex);
            break;
        }
    }
}