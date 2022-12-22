use std::fs::File;
use std::io::BufRead;

const SUSSY_WUSSY: &[&'static str] = &[
    "windows",
    "coin",
    "call us",
    "refund",
    "cancel",
    "btc",
    "geek",
    "squad",
    "trend",
    "micro",
    "mcafee",
    "antivirus",
    "hack",
    "microsoft",
    "support",
    "department",
    "tech",
    "norton",
];

enum ErrorType {
    IOError,
}

impl ErrorType {
    pub(crate) fn as_error<U, T: ToString>(self, message: T) -> Result<U> {
        return Err(Error::new(message, self));
    }
}

impl ToString for ErrorType {
    fn to_string(&self) -> String {
        match self {
            Self::IOError => "IOError",
        }
        .to_string()
    }
}

struct Error {
    message: String,
    error_type: ErrorType,
}

impl Error {
    pub(crate) fn new<T: ToString>(message: T, etype: ErrorType) -> Self {
        Error {
            message: message.to_string(),
            error_type: etype,
        }
    }
}

impl ToString for Error {
    fn to_string(&self) -> String {
        format!("[{}]: {}", self.error_type.to_string(), self.message)
    }
}

type Result<T> = std::result::Result<T, Error>;

fn rate_lines() -> Result<()> {
    let file = File::open("../../invoices.txt")
        .or_else(|_| ErrorType::IOError.as_error("Could not open invoices.txt"))?;
    let lines = std::io::BufReader::new(file).lines();

    for (i, line) in lines.enumerate() {
        let mut score = 0;
        if let Ok(line_str) = line {
            for sussy in SUSSY_WUSSY {
                if line_str.to_lowercase().contains(sussy) {
                    score += 1;
                }
            }
        }
        println!("line {} has a sussy wussy score of {}", i, score);
    }
    Ok(())
}

fn main() {
    println!("SussyWussy Meter");
    match rate_lines() {
        Ok(_) => {}
        Err(e) => eprintln!("{}", e.to_string()),
    };
}
