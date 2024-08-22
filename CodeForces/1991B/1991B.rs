#[allow(unused_imports)]
use std::cmp::{max, min};
use std::io::{stdin, stdout, BufWriter, Write};

#[derive(Default)]
struct Scanner {
    buffer: Vec<String>,
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("oh no failed to parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("eep i failed to read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }
}

fn check_if_possible(n: usize, b: &Vec<i32>) -> bool {
    assert!(n >= 2);
    if n == 2 {
        return true;
    }
    for i in 0..(n - 3) {
        if (b[i] & !b[i + 1] & b[i + 2]) != 0 {
            return false;
        }
    }
    true
}

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());
    let t: i32 = scan.next();

    for _ in 0..t {
        let n: usize = scan.next();
        let b: Vec<i32> = (0..(n - 1)).map(|_| scan.next()).collect();
        if n == 2 {
            writeln!(out, "{} {}", b[0], b[0]).ok();
        } else if check_if_possible(n, &b) {
            write!(out, "{} ", b[0]).ok();
            for k in 1..(n - 1) {
                write!(out, "{} ", b[k - 1] | b[k]).ok();
            }
            write!(out, "{}\n", b[n - 2]).ok();
        } else {
            writeln!(out, "-1").ok();
        }
    }
}
