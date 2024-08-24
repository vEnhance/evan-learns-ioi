// {{{ vEnhance's Rust competitive programming template
// I/O scanner from https://codeforces.com/blog/entry/67391
// vim: fdm=marker foldlevel=0

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

#[allow(dead_code)]
fn join<T, U>(v: U) -> String
where
    U: AsRef<[T]>,
    T: std::string::ToString,
{
    v.as_ref()
        .iter()
        .map(|elm| elm.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}

// Copy of dbg! macro, but only when stomp is used and the flag debug is passed
// So we don't waste time printing to stderr when submitting to online judge
#[macro_export]
macro_rules! debug {
    () => {
        #[cfg(feature = "debug")]
        std::eprintln!("[{}:{}:{}]", std::file!(), std::line!(), std::column!())
    };
    ($val:expr $(,)?) => {
        #[cfg(feature = "debug")]
        match $val {
            tmp => {
                std::eprintln!("[{}:{}:{}] {} = {:#?}",
                    std::file!(), std::line!(), std::column!(), std::stringify!($val), &tmp);
                tmp
            }
        }
    };
    ($($val:expr),+ $(,)?) => {
        #[cfg(feature = "debug")]
        ($(std::dbg!($val)),+,)
    };
}
/* }}} */

const SMALL_CASES: [i64; 5] = [1, 2, 2, 3, 3];

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());

    let t: i64 = scan.next();
    #[allow(unused_labels)]
    'test_case_loop: for _test_case_number in 0..t {
        let n: usize = scan.next();

        if n <= 5 {
            writeln!(out, "{}", SMALL_CASES[n - 1]).ok();
            writeln!(out, "{}", join(&SMALL_CASES[0..n])).ok();
        } else {
            writeln!(out, "{}", 4).ok();
            let ans: Vec<usize> = (0..n).map(|x| (x % 4) + 1).collect();
            writeln!(out, "{}", join(&ans)).ok();
        }
    }
}
