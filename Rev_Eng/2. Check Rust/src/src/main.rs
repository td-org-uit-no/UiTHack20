use std::io::{self, Write};

struct Challenge {
    encryption_key: [u8;32],
    password: [u8;32],
    flag: [u8;32],
}

impl Challenge {
    fn new() -> Self {
        Challenge {
            encryption_key: [135, 62, 148, 201, 144, 220, 57, 145, 251, 196, 165, 85, 181, 201, 34, 95, 37, 23, 19, 47, 136, 253, 20, 127, 33, 142, 243, 93, 78, 160, 50, 9],
            password: [244, 75, 228, 172, 226, 131, 74, 244, 152, 182, 192, 33, 234, 185, 67, 44, 86, 96, 124, 93, 236, 162, 102, 22, 70, 230, 135, 2, 38, 197, 64, 108],
            flag: [210, 87, 192, 129, 241, 191, 82, 163, 203, 191, 196, 59, 218, 189, 74, 58, 87, 72, 117, 67, 233, 154, 75, 29, 72, 250, 150, 2, 58, 200, 87, 116],
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
        let expected_password = [244, 75, 228, 172, 226, 131, 74, 244, 152, 182, 192, 33, 234, 185, 67, 44, 86, 96, 124, 93, 236, 162, 102, 22, 70, 230, 135, 2, 38, 197, 64, 108];
        let expected_flag = [210, 87, 192, 129, 241, 191, 82, 163, 203, 191, 196, 59, 218, 189, 74, 58, 87, 72, 117, 67, 233, 154, 75, 29, 72, 250, 150, 2, 58, 200, 87, 116];
        assert_eq!(chall.encryption_key, expected_encryption_key);
        assert_eq!(chall.password, expected_password);
        assert_eq!(chall.flag, expected_flag);
    }

    #[test]
    fn test_decrypt_password() {
        let chall = Challenge::new();
        let expected_password = b"super_secret_password_right_here";

        assert_eq!(chall.decrypt_data(&chall.password), expected_password);
    }

    #[test]
    fn test_decrypt_flag() {
        let chall = Challenge::new();
        let expected_flag = b"UiTHack20{another_flag_bite_the}";

        assert_eq!(chall.decrypt_data(&chall.flag), expected_flag);
    }

    #[test]
    fn test_check_password() {
        let chall = Challenge::new();
        
        assert_eq!(chall.check_password("super_secret_password_right_here"), true);
        assert_eq!(chall.check_password("this_is_the_wrong_password"), false);
    }
}
