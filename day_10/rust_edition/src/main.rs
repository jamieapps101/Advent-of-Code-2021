use std::{
    io::{BufRead,BufReader},
    path::Path,
    fs::File
};


const DATA_PATH: &str    = "../data/input.txt";
const DATA_WIDTH: usize  = 10;
const DATA_HEIGHT: usize = 10;
const FLASH_THRESH: u8   = 9;
const SIM_STEPS: usize   = 100;


fn read_file<P: AsRef<Path>>(path: P) -> [[Octopus; DATA_WIDTH]; DATA_HEIGHT] {
    let mut output = [[Octopus::default(); DATA_WIDTH]; DATA_HEIGHT];

    let f = File::open(path).unwrap();
    let mut reader = BufReader::new(f);

    let mut line_string = String::with_capacity(DATA_WIDTH);
    let line_index = 0;
    while let Ok(byte_count) = reader.read_line(&mut line_string) {
        if byte_count == 0 { break }
        for (char_index,c) in line_string.chars().enumerate() {
            if c == '\n' { continue }
            output[line_index][char_index].set_level(c.to_digit(10).unwrap() as u8);
        }
    }
    output
}

#[derive(Clone,Copy)]
struct Octopus {
    level: u8,
}

impl From<u8> for Octopus {
    fn from(level: u8) -> Self {
        Self { level }
    }
}

impl Default for Octopus {
    fn default() -> Self {
        Self { level: 0 }
    }
}

#[derive(PartialEq)]
enum FlashState { Flash, NonFlash }

impl Octopus {
    fn set_level(&mut self, new_level: u8) {
        self.level = new_level;
    }

    fn increment_level(&mut self) {
        self.level += 1;
    }

    fn flash(&mut self, threshold: u8) -> FlashState {
        if self.level >= threshold {
            self.level = 0;
            FlashState::Flash
        } else {
            FlashState::NonFlash
        }
    }
}


struct Octopi {
    octopi: [[Octopus; DATA_WIDTH]; DATA_HEIGHT],
}


impl Octopi {
    /// Load octopi feild data from file
    fn load_from<P: AsRef<Path>>(path: P) -> Self {
        Self { octopi: read_file(path) }
    }

    fn step_once(&mut self) -> Vec<(usize,usize)> {
        // first add one to each octopus in the grid
        for row in self.octopi {
            for mut octopus in row {
                octopus.increment_level();
            }
        }

        // work out which ones do a flash
        let mut flashers = Vec::new();
        let mut current_flashers = self.initiate_flash();
        while !current_flashers.is_empty() {
            flashers.append(&mut current_flashers);
            current_flashers = self.initiate_flash();
        }
        flashers
    }

    fn initiate_flash(&mut self) -> Vec<(usize,usize)> {
        let mut flashers = Vec::new();
        let max_rows = self.octopi.len();
        let max_cols = self.octopi[0].len();
        for row_index in 0..max_rows {
            for col_index in 0..max_cols {
                if self.octopi[row_index][col_index].flash(FLASH_THRESH) == FlashState::Flash {
                    // if we got a flasher, then go round and increment
                    // all the other octopi
                    flashers.push((row_index,col_index));
                }
            }
        }

        flashers.iter().for_each( |(r,c)| {
            let row_index = *r;
            let col_index = *c;
            for row_offset in [-1,0,1] {
                for col_offset in [-1,0,1] {
                    if col_offset == 0 || row_offset == 0 {
                        continue;
                    }
                    if (row_index == 0 && row_offset == -1) ||
                        (row_index == (max_rows-1) && row_offset == 1) ||
                        (col_index == 0 && col_offset == -1) ||
                        (col_index == (max_cols-1) && col_offset == 1) {
                            continue
                        }
                    let prop_row_index = ((row_index as i32)+row_offset) as usize;
                    let prop_col_index = ((col_index as i32)+col_offset) as usize;
                    self.octopi[prop_row_index][prop_col_index].increment_level();
                }
            }
        });
        flashers
    }
}

fn main() {
    println!("Hello, world!");
    let mut octopi = Octopi::load_from(DATA_PATH);

    for _i in 0..SIM_STEPS {
        let _flashers = octopi.step_once();
    }
}
