use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

fn main() {
    println!("The total score for part 1 is: {}", part1());
    println!("The total score for part 2 is: {}", part2());
}

fn part1() -> u32 {
    let rock = HandShape {
        opponent_key: String::from("A"),
        shape_value: 1,
        beats: String::from("C")
    };

    let paper = HandShape {
        opponent_key: String::from("B"),
        shape_value: 2,
        beats: String::from("A")
    };

    let scissors = HandShape {
        opponent_key: String::from("C"),
        shape_value: 3,
        beats: String::from("B")
    };

    let rock_paper_scissors_scorebook = HashMap::from([
        (String::from("X"), rock),
        (String::from("Y"), paper),
        (String::from("Z"), scissors)
    ]);

    let mut total_score: u32 = 0;

    let file = File::open("input").unwrap();
    let reader = BufReader::new(file);

    for (_index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let player_shape: String = (&line[2..3]).to_string();
        let opponent_shape: String = (&line[0..1]).to_string();

        let shape_score: u32 = rock_paper_scissors_scorebook[&player_shape].shape_value.into();
        let round_score: u32 = round_score(&rock_paper_scissors_scorebook[&player_shape], &opponent_shape);
        total_score = total_score + shape_score + round_score;
    }

    total_score
}

fn part2() -> u32 {
    let mut total_score: u32 = 0;
    let file = File::open("input").unwrap();
    let reader = BufReader::new(file);

    for (_index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let outcome: String = (&line[2..3]).to_string();
        let opponent_shape: String = (&line[0..1]).to_string();

        let shape_score: u32 = shape_score(&outcome, &opponent_shape);
        let round_score: u32 = match outcome.as_str() {
            "Z" => 6,
            "Y" => 3,
            _ => 0
        };
        
        total_score = total_score + shape_score + round_score;
    }

    total_score
}

fn round_score(player: &HandShape, opponent: &String) -> u32 {
    match player {
        HandShape { beats, .. } if beats == opponent => 6,
        HandShape { opponent_key, .. } if opponent_key == opponent => 3,
        _ => 0
    }
}

fn shape_score(outcome: &String, opponent: &String) -> u32 {
    if outcome == "Y" {
        match opponent.as_str() {
            "A" => 1,
            "B" => 2,
            "C" => 3,
            _ => 0
        }
    } else if outcome == "X" {
        match opponent.as_str() {
            "A" => 3,
            "B" => 1,
            "C" => 2,
            _ => 0
        } 
    } else if outcome == "Z" {
        match opponent.as_str() {
            "A" => 2,
            "B" => 3,
            "C" => 1,
            _ => 0
        }
    } else {
        0
    }
}

struct HandShape {
    opponent_key: String,
    shape_value: u8,
    beats: String
}

