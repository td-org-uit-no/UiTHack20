use std::io::{self, Write};

struct Challenge {
    encryption_key: [u8;32],
    password: [u8;32],
    flag: [u8;32],
}

impl Challenge {
    fn new() -> Self {
        Challenge {
            encryption_key: [135, 62, 148, 201, 144, 220, 57, 145, 251, 196,
                             165, 85, 181, 201, 34, 95, 37, 23, 19, 47, 136,
                             253, 20, 127, 33, 142, 243, 93, 78, 160, 50, 9],
            password: [230, 93, 224, 188, 241, 176, 85, 232, 164, 178, 192, 39,
                       204, 150, 70, 54, 67, 113, 122, 76, 253, 145, 96, 32, 81,
                       239, 128, 46, 57, 207, 64, 109],
            flag: [210, 87, 192, 129, 241, 191, 82, 163, 203, 191, 199, 60, 219,
                   168, 80, 54, 64, 100, 76, 88, 225, 137, 124, 32, 82, 235, 144,
                   47, 43, 212, 65, 116],

        }
    }

    fn check_password(&self, password: &str) -> bool {
        self.decrypt_data(&self.password) == password.as_bytes()
    }

    fn decrypt_data(&self, data: &[u8]) -> Vec<u8> {
        self.encryption_key.iter().zip(data).map(|(x,y)| x^y).collect()
    }

    fn print_flag(&self) {
        if let Ok(flag) = String::from_utf8(self.decrypt_data(&self.flag)) {
            println!("Flag: {}", flag);
        } else {
            println!("Unable to convert decrypted flag to string");
        }
    }
}

fn main() {
    print!("Password: ");
    let _ = io::stdout().flush();
    let mut password = String::new();
    match io::stdin().read_line(&mut password) {
        Ok(_) => {
            let chall = Challenge::new();
            if chall.check_password(password.trim_end()) {
                chall.print_flag();
            } else {
                println!("Wrong password :/")
            }
        }
        Err(error) => println!("Error: {}", error),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_expected_chall() {
        let chall = Challenge::new();
        let expected_encryption_key = [135, 62, 148, 201, 144, 220, 57, 145, 251, 196, 165, 85, 181, 201, 34, 95, 37, 23, 19, 47, 136, 253, 20, 127, 33, 142, 243, 93, 78, 160, 50, 9];
        let expected_password = [230, 93, 224, 188, 241, 176, 85, 232, 164, 178, 192, 39, 204, 150, 70, 54, 67, 113, 122, 76, 253, 145, 96, 32, 81, 239, 128, 46, 57, 207, 64, 109];
        let expected_flag = [210, 87, 192, 129, 241, 191, 82, 163, 203, 191, 199, 60, 219, 168, 80, 54, 64, 100, 76, 88, 225, 137, 124, 32, 82, 235, 144, 47, 43, 212, 65, 116];
        assert_eq!(chall.encryption_key, expected_encryption_key);
        assert_eq!(chall.password, expected_password);
        assert_eq!(chall.flag, expected_flag);
    }

    #[test]
    fn test_decrypt_password() {
        let chall = Challenge::new();
        let expected_password = b"actually_very_difficult_password";

        assert_eq!(chall.decrypt_data(&chall.password), expected_password);
    }

    #[test]
    fn test_decrypt_flag() {
        let chall = Challenge::new();
        let expected_flag = b"UiTHack20{binaries_with_secrets}";

        assert_eq!(chall.decrypt_data(&chall.flag), expected_flag);
    }

    #[test]
    fn test_check_password() {
        let chall = Challenge::new();
        
        assert_eq!(chall.check_password("actually_very_difficult_password"), true);
        assert_eq!(chall.check_password("this_is_the_wrong_password"), false);
    }
}
