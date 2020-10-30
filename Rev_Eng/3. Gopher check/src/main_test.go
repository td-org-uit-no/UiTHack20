package main

import (
	"bytes"
	"testing"
)

func TestNewChallenge(t *testing.T) {
    c := new_challenge()

    expected_encryption_key := []byte("I\xc9\xceP\xe96\xf4P\xd1\xe8\xb7\xe5+\x98pbH\xe8~\xad\x1d\x98E\xe3G\x1f\xf2\xfb\x91\xa2\x1f@")
    expected_password := []byte("9\xa8\xbc$\x80U\x81<\xb0\x9a\xdb\x9ct\xfd\x08\x16-\x86\r\xc4k\xfd\x1a\x93&l\x81\x8c\xfe\xd0{3")
    expected_flag := []byte("\x1c\xa0\x9a\x18\x88U\x9fb\xe1\x93\xd0\x8a[\xf0\x15\x10;\xb7\x1f\xdfx\xc76\x86$m\x97\x8f\xf8\xd4z=")

    if bytes.Equal(c.encryption_key, expected_encryption_key) == false ||
       bytes.Equal(c.password, expected_password) == false ||
       bytes.Equal(c.flag, expected_flag) == false {
           t.Error("Challenge is not what we expect it to be")
   }
}

func TestDecryptPassword(t *testing.T) {
    c := new_challenge()

    expected_password := []byte("particularly_extensive_passwords")

    if bytes.Equal(c.decrypt_data(c.password), expected_password) == false {
        t.Error("Password did not decrypt as expected")
    }
}

func TestDecryptFlag(t *testing.T) {
    c := new_challenge()

    expected_flag := []byte("UiTHack20{gophers_are_secretive}")

    if bytes.Equal(c.decrypt_data(c.flag), expected_flag) == false {
        t.Error("Flag did not decrypt as expected")
    }
}

func TestCheckPassword(t *testing.T) {
    c := new_challenge()

    if c.check_password("particularly_extensive_passwords") == false {
        t.Error("Password check failed. We supplied the correct password")
    }

    if c.check_password("_this_password_is_wrong") == true {
        t.Error("Password check failed. We supplied the wrong password but it did not fail")
    }
}
