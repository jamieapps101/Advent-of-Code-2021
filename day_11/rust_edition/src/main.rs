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

/// helper function to read in data into nested arrays
fn read_file<P: AsRef<Path>>(path: P) -> [[Octopus; DATA_WIDTH]; DATA_HEIGHT] {
    let mut output = [[Octopus::default(); DATA_WIDTH]; DATA_HEIGHT];

    let f = File::open(path).unwrap();
    let mut reader = BufReader::new(f);

    let mut line_string = String::with_capacity(DATA_WIDTH);
    let mut line_index = 0;
    while let Ok(byte_count) = reader.read_line(&mut line_string) {
        if byte_count == 0 { break }
        for (char_index,c) in line_string.chars().enumerate() {
            if c == '\n' { continue }
            output[line_index][char_index].set_level(c.to_digit(10).unwrap() as u8);
        }
        line_string.clear();
        line_index+=1;
    }
    output
}

#[derive(Clone,Copy,Debug, PartialEq)]
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

#[derive(PartialEq,Debug)]
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

#[derive(Debug, PartialEq)]
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
        for row_index in 0..self.octopi.len() {
            for col_index in 0..self.octopi[0].len() {
                self.octopi[row_index][col_index].increment_level();
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
        let n = flashers.len();
        println!("n: {n}");
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

    let mut total_flashes = 0;
    for _i in 0..SIM_STEPS {
        let flashers = octopi.step_once();
        total_flashes += flashers.len();
    }

    println!("total_flashes: {total_flashes}");
}


#[cfg(test)]
mod test {
    use super::*;

    fn get_ref_data() -> [[Octopus; 10]; 10] {
        [
            [4.into(),4.into(),3.into(),8.into(),6.into(),2.into(),4.into(),2.into(),6.into(),2.into()],
            [6.into(),2.into(),6.into(),3.into(),2.into(),5.into(),1.into(),8.into(),6.into(),4.into()],
            [2.into(),6.into(),1.into(),8.into(),8.into(),1.into(),2.into(),4.into(),3.into(),4.into()],
            [2.into(),1.into(),3.into(),4.into(),2.into(),6.into(),4.into(),5.into(),6.into(),5.into()],
            [1.into(),8.into(),1.into(),5.into(),1.into(),3.into(),1.into(),2.into(),4.into(),7.into()],
            [2.into(),6.into(),1.into(),2.into(),4.into(),5.into(),7.into(),3.into(),2.into(),5.into()],
            [8.into(),5.into(),8.into(),5.into(),7.into(),6.into(),7.into(),5.into(),8.into(),4.into()],
            [7.into(),2.into(),1.into(),7.into(),1.into(),3.into(),4.into(),5.into(),5.into(),6.into()],
            [2.into(),8.into(),2.into(),5.into(),4.into(),5.into(),6.into(),5.into(),6.into(),3.into()],
            [8.into(),2.into(),4.into(),8.into(),4.into(),7.into(),3.into(),5.into(),8.into(),4.into()]
        ]
    }
    #[test]
    fn test_read_file() {
        let data = read_file(DATA_PATH);
        let ref_data = get_ref_data();
        for row_index in 0..data.len() {
            assert_eq!(
                data[row_index],
                ref_data[row_index]
            );
        }
    }


    #[test]
    fn create_octopi() {
        let octopi = Octopi::load_from(DATA_PATH);
        let ref_octopi = Octopi {octopi: get_ref_data()};
        assert_eq!(octopi, ref_octopi);
    }

    #[test]
    fn test_octopus_leveling() {
        let mut octopus = Octopus::default();
        assert_eq!(octopus.level,0);

        octopus.increment_level();
        assert_eq!(octopus.level,1);

        assert_eq!(octopus.flash(3), FlashState::NonFlash);

        octopus.increment_level();
        assert_eq!(octopus.level,2);

        assert_eq!(octopus.flash(3), FlashState::NonFlash);

        octopus.increment_level();
        assert_eq!(octopus.level,3);

        assert_eq!(octopus.flash(3), FlashState::Flash);
        assert_eq!(octopus.level,0);

        assert_eq!(octopus.flash(3), FlashState::NonFlash);

        octopus.increment_level();
        assert_eq!(octopus.level,1);
    }
}