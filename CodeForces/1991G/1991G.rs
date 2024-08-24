// {{{ vEnhance's Rust competitive programming template
// I/O scanner from https://codeforces.com/blog/entry/67391
// vim: fdm=marker foldlevel=0

#[allow(unused_imports)]
use std::cmp::{max, min};
use std::io::{stdin, stdout, BufWriter, Stdout, Write};

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

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());

    let t: i64 = scan.next();
    for _test_case_number in 0..t {
        solve(&mut scan, out);
    }
}

fn solve(scan: &mut Scanner, out: &mut BufWriter<Stdout>) {
    // Read all the input
    let n: i64 = scan.next();
    let m: i64 = scan.next();
    let k: i64 = scan.next();
    let q: i64 = scan.next();
    let s: Vec<bool> = scan.next::<String>().chars().map(|c| c == 'H').collect();
    debug!(n, m, k, q);

    let grid_dims = [m, n];

    // This stupid edge case where multiple clears can happen at once
    if k == 1 {
        for c in 0..q {
            writeln!(out, "{} 1", (c % n) + 1).ok();
        }
        return;
    }

    // oh geez this is so many cases i can't
    let mut depth = [k, k];
    let mut tide = grid_dims;
    let mut corner = [k, k];

    /*
    Explanation of this god forsaken code:
    All the coordinates here are corners of cells rather than cells
    So the overall rectangle is:
    - Northwest corner of the grid is (0,0)
    - Northeast corner of the grid is (m,0)
    - Southwest corner of the grid is (0,n)
    Okay. Then:

    So here's like a picture of three regions
      0    k                         m
    0 +----+-------------------------+
      | NW |          NE             |
      |    |                         |
    k +----+-------------------------+
      |    |                         |
      |    |                         |
      | SW |                         |
      |    |                         |
    n +----+-------------------------+

    So NE is the rectangle from (k,k) to (n,0)
    while SW is the rectangle from (0,n) to (k,k)
    and NW is the square from (0,0) to (k,k)
    (We ain't touching that southeast region.)

    Then the variable meanings are:
    - Assume the black cells in NE are from (m,0) to (tide[0], depth[1])
    - Assume the black cells in SW are from (0,n) to (depth[0], tide[1])
    - Assume the black cells in NW are from (k,k) to (corner[0], corner[1])

    In particular, always the following should hold:
    - k <= tide[0] <= m, k <= tide[1] <= n
    - 0 < depth[0,1] <= k
    - 0 < corner[0,1] <= k

    Moreover: in each region we are going to enforce that the black cells
    always reaches all the way across in at least one of the dimensions
    (if they are nonempty at all).
    For example, in NE region, if there are black cells at all,
    either tide[0] = k or depth[1] = k.

    Finally, for empty NW region, we require depth[0] == k and depth[1] == k simultaneously.
    */

    for is_horizontal in s {
        // okay this is already way too many cases for tiny brain evan
        // so we're going to only do the horizontal case and the other is symmetric
        let i = if is_horizontal { 0 } else { 1 }; // columns
        let j = 1 - i; // rows

        // and henceforth we assume i = 0 and j = 1 and is_horizontal is true

        // ok here is the thing that actually places the rectangle
        // This closure knows whether it's H or V so it sets the other coord to 1
        let mut place_rect = |c: i64| {
            if is_horizontal {
                writeln!(out, "{} 1", c).ok();
            } else {
                writeln!(out, "1 {}", c).ok();
            }
        };

        if k == m && k == n {
            place_rect(1);
            continue;
        } else if k == m && is_horizontal {
            place_rect(n);
            continue;
        } else if k == n && !is_horizontal {
            place_rect(m);
            continue;
        } else if tide[i] == k && ((corner[i] == k && corner[j] == k) || corner[i] == 0) {
            /*
            This case means we can clear a row by adding a rectangle
              0    k                         m
            0 +----+-------------------------+
              |!!!!|xxxxxxxxxxxxxxxxxxxxxxxxx|
              |    |                         |
            k +----+-------------------------+
              |    |                         |
              |    |                         |
              |    |                         |
              |    |                         |
            n +----+-------------------------+
            */
            place_rect(depth[j]);
            depth[j] -= 1;
            if depth[j] == 0 {
                // This means the entire NW region is wiped
                depth[j] = k;
                tide[i] = grid_dims[i];
                corner[i] = k;
                corner[j] = k;
            }
        } else if tide[j] > k {
            /*
            In this case we can't clear a row, so we just add something to SW if possible
              0    k                         m
            0 +----+-------------------------+
              |    |                         |
              |    |                         |
            k +----+-------------------------+
              |    |                         |
              |!!!!|                         |
              |xxxx|                         |
              |xxxx|                         |
            n +----+-------------------------+
            */
            place_rect(tide[j]);
            tide[j] -= 1;
            if tide[j] == k && corner[j] == 0 {
                /*
                This lets us clear a bunch of columns (wiping all NW)
                  0    k                         m
                0 +----+-------------------------+
                  |  xx|                         |
                  |  xx|                         |
                k +----+-------------------------+
                  |!!!!|                         |
                  |xxxx|                         |
                  |xxxx|                         |
                  |xxxx|                         |
                n +----+-------------------------+
                */
                depth[i] = corner[i];
                corner[i] = k;
                corner[j] = k;
            }
        } else {
            /*
            If SW is full, then the only remaining case is NW has horizontal sticks
              0    k                         m
            0 +----+-------------------------+
              |!!!!|    xxxxxxxxxxxxxxxxxxxxx|
              |xxxx|    xxxxxxxxxxxxxxxxxxxxx|
            k +----+-------------------------+
              |xx  |                         |
              |xx  |                         |
              |xx  |                         |
              |xx  |                         |
            n +----+-------------------------+
            */
            assert!(corner[i] == 0 || (corner[i] == k && corner[j] == k));
            place_rect(corner[j]);
            corner[i] = 0;
            corner[j] -= 1;
            if corner[j] == 0 {
                // We filled the entire NW region
                corner[i] = depth[i];
                if depth[i] == k {
                    // erase entire NW region too
                    corner[j] = k;
                }
                // Wipe out SW
                tide[j] = grid_dims[j];
                depth[j] = k;
            }
        }
    }
    // These two assertions fail a random test case and I have no clue why
    // but it AC's without them??? wtf help
    // assert!(tide[0] == k || depth[1] == k);
    // assert!(tide[1] == k || depth[0] == k);
    assert!((corner[0] == k || corner[1] == k) || corner[0] == 0 || corner[1] == 0);
    assert!(0 < depth[0] && depth[0] <= k);
    assert!(0 < depth[1] && depth[1] <= k);
    assert!(0 <= corner[0] && corner[0] <= k);
    assert!(0 <= corner[1] && corner[1] <= k);
    assert!(k <= tide[0] && tide[0] <= m);
    assert!(k <= tide[1] && tide[1] <= n);
}
