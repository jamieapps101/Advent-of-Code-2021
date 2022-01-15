use std::{
    path::PathBuf,
    io::{
        BufReader,
        prelude::*
    },
    fs::File,
    boxed::Box,
};

const DATA_PATH: &str = "../data/input.txt";
const MAX_LINE_LEN: usize = 12;

fn read_data<P: Into<PathBuf>>(p: P) -> Option<Vec<[u8; MAX_LINE_LEN]>> {
    let f = if let Ok(f) = File::open(p.into()) {
        f
    } else {
        return None
    };
    let mut reader = BufReader::new(f);
    let mut data: Vec<[u8; MAX_LINE_LEN]> = Vec::new();
    let mut line = String::with_capacity(MAX_LINE_LEN+1);
    while let Ok(bytes) = reader.read_line(&mut line) {
        if bytes == 0 { break }
        let mut line_data = [0;MAX_LINE_LEN];
        line.chars().filter(|c| c != &'\n').enumerate().for_each( |(i,c)| {
            if c == '1' {
                line_data[i] = 1;
            }
        });
        data.push(line_data);
        line.clear();
    }
    Some(data)
}

#[derive(Debug,PartialEq)]
struct Branch {
    child: Option<Box<Node>>,
    count: usize
}

impl Branch {
    fn new() -> Self {
        Self {
            child: None,
            count: 0,
        }
    }
}

enum BranchSelector {
    Zero,
    One,
}

impl From<u8> for BranchSelector {
    fn from(f: u8) -> Self {
        match f {
            0 => Self::Zero,
            1 => Self::One,
            _ => panic!("Invalid branch selector")
        }
    }
}

impl From<usize> for BranchSelector {
    fn from(f: usize) -> Self {
        match f {
            0 => Self::Zero,
            1 => Self::One,
            _ => panic!("Invalid branch selector")
        }
    }
}

impl From<BranchSelector> for usize {
    fn from(b: BranchSelector) -> Self {
        match b {
            BranchSelector::Zero => 0,
            BranchSelector::One  => 1,
        }
    }
}

#[derive(Debug,PartialEq)]
struct Node { branches: [Branch; 2] }

impl Node {
    fn new() -> Self {
        Self {branches: [Branch::new(), Branch::new()]}
    }

    fn add_to_count<B: Into<BranchSelector>>(&mut self, branch: B) {
        let branch_index: usize = branch.into().into();
        self.branches[branch_index].count += 1;
    }

    fn get_count<B: Into<BranchSelector>>(&self, branch: B) -> usize {
        let branch_index: usize = branch.into().into();
        self.branches[branch_index].count
    }

    fn get_child_mut_ref<B: Into<BranchSelector>>(&mut self, branch: B) -> &mut Self {
        let branch_index: usize = branch.into().into();
        if self.branches[branch_index].child.is_none() {
            self.branches[branch_index].child = Some(Box::new(Node::new()));
        }
        let mut_box_ref = self.branches[branch_index].child.as_mut().unwrap();
        return mut_box_ref.as_mut();
    }

    fn get_child_ref<B: Into<BranchSelector>>(&self, branch: B) -> Option<&Self> {
        let branch_index: usize = branch.into().into();
        if self.branches[branch_index].child.is_none() {
            return None
        }
        let mut_box_ref = self.branches[branch_index].child.as_ref().unwrap();
        Some(mut_box_ref.as_ref())
    }
}

fn build_tree(data: Vec<[u8;MAX_LINE_LEN]>) -> Node {
    let mut tree = Node::new();
    data.iter().for_each(|line| build_branch(line,&mut tree, 0) );
    return tree;
}

fn build_branch(data: &[u8;MAX_LINE_LEN], base: &mut Node, index: usize) {
    if index < MAX_LINE_LEN {
        let current_bit = data[index];
        base.add_to_count(current_bit);
        let current_node = base.get_child_mut_ref(current_bit);
        build_branch(data, current_node, index+1);
    }
}

enum QueryMode {
    OxyMode,
    CoMode
}

fn query_tree(tree: &Node, mode:QueryMode, depth: usize) -> Vec<u8> {
    let this_bit = match mode {
        QueryMode::OxyMode => {
            if tree.get_count(1usize)>=tree.get_count(0usize) { 1 } else { 0 }
        },
        QueryMode::CoMode => {
            if tree.get_count(0usize)<=tree.get_count(1usize) { 0 } else { 1 }
        },
    };
    let mut return_vec = vec![this_bit];
    if depth != MAX_LINE_LEN-1 {
        println!("{depth}: {this_bit}:{},{}",tree.get_count(0usize),tree.get_count(1usize));
        let sub_tree = tree.get_child_ref(this_bit).unwrap();
        return_vec.extend(query_tree(sub_tree, mode, depth+1));
    }
    return return_vec;
}

/// Filter by most common value
fn get_oxy_gen_rating(tree: &Node) -> Vec<u8> {
    return query_tree(tree, QueryMode::OxyMode,0)
}

/// Filter by most common value
fn get_co2_scr_rating(tree: &Node) -> Vec<u8> {
    return query_tree(tree, QueryMode::CoMode,0)
}

fn binary_vec_to_int(input: Vec<u8>) -> u32 {
    let mut value: u32 = 0;
    for bit in input {
        value *= 2;
        if bit == 1 {
            value += 1
        }
    }
    return value
}


fn main() {
    println!("Starting");
    let data = read_data(DATA_PATH).unwrap();
    let tree = build_tree(data);
    println!("{} zeros in first position", tree.get_count(0usize));
    println!("{} ones in first position", tree.get_count(1usize));

    let og_rating_str = get_oxy_gen_rating(&tree);
    println!("og_rating_str: {og_rating_str:?}");
    println!("");
    let og_rating = binary_vec_to_int(og_rating_str);


    let cs_rating_str = get_co2_scr_rating(&tree);
    println!("cs_rating_str: {cs_rating_str:?}");
    println!("");
    let cs_rating = binary_vec_to_int(cs_rating_str);

    let life_support_rating = og_rating * cs_rating;
    println!("life_support_rating: {life_support_rating}")
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_read_data() {
        let data = read_data(DATA_PATH);
        assert!(data.is_some());
        let data = data.unwrap();
        assert_eq!(data[0],[0,1,0,1,0,0,1,1,0,1,1,1]);
        assert_eq!(data[1],[1,0,1,0,0,1,0,1,0,0,0,0]);
    }

    #[test]
    fn test_editing_trees() {
        let mut tree = Node::new();

        tree.add_to_count(0usize);
        let sub_tree = tree.get_child_mut_ref(0u8);

        sub_tree.add_to_count(1usize);
        let sub_sub_tree = sub_tree.get_child_mut_ref(1u8);

        sub_sub_tree.add_to_count(1usize);

        assert_eq!(tree.branches[0].count, 1);
        assert_eq!(tree.branches[1].count, 0);

        assert_eq!(tree.branches[1].child.as_ref(), None);
        assert_eq!(tree.branches[1].child.as_ref(), None);
        assert_eq!(tree.branches[0].child.as_ref().unwrap().branches[0].count, 0);
        assert_eq!(tree.branches[0].child.as_ref().unwrap().branches[1].count, 1);

        assert_eq!(tree.branches[0].child.as_ref().unwrap().branches[1].child.as_ref().unwrap().branches[1].count, 1);
    }

    #[test]
    fn test_assert_counts() {
        let data = read_data(DATA_PATH).unwrap();
        let tree = build_tree(data);
        assert_eq!(472, tree.get_count(0usize));
        assert_eq!(528, tree.get_count(1usize));
    }
}