package main

import (
	"bytes"
	"testing"
)

func TestNewChallenge(t *testing.T) {
    c := new_challenge()

    expected_encryption_key := []byte("I\xc9\xceP\xe96\xf4P\xd1\xe8\xb7\xe5+\x98pbH\xe8~\xad\x1d\x98E\xe3G\x1f\xf2\xfb\x91\xa2\x1f@")
    expected_password := []byte("\x16\xbd\xa69\x9ai\x841\xa2\x9b\xc0\x8aY\xfc/\x0b;\xb7\x10\xc2i\xc76\x967z\x80\xa4\xf4\xc3l9")
    expected_flag := []byte("\x1c\xa0\x9a\x18\x88U\x9fb\xe1\x93\xe8\x91C\xf1\x03=!\x9b!\xccB\xf6,\x80\"@\x94\x97\xf0\xc5@=")

    if bytes.Equal(c.encryption_key, expected_encryption_key) == false ||
       bytes.Equal(c.password, expected_password) == false ||
       bytes.Equal(c.flag, expected_flag) == false {
           t.Error("Challenge is not what we expect it to be")
   }
}

func TestDecryptPassword(t *testing.T) {
    c := new_challenge()

    expected_password := []byte("_this_password_is_not_super_easy")

    if bytes.Equal(c.decrypt_data(c.password), expected_password) == false {
        t.Error("Password did not decrypt as expected")
    }
}

func TestDecryptFlag(t *testing.T) {
    c := new_challenge()

    expected_flag := []byte("UiTHack20{_this_is_a_nice_flag_}")

    if bytes.Equal(c.decrypt_data(c.flag), expected_flag) == false {
        t.Error("Flag did not decrypt as expected")
    }
}

func TestCheckPassword(t *testing.T) {
    c := new_challenge()

    if c.check_password("_this_password_is_not_super_easy") == false {
        t.Error("Password check failed. We supplied the correct password")
    }

    if c.check_password("_this_password_is_wrong") == true {
        t.Error("Password check failed. We supplied the wrong password but it did not fail")
    }
}
