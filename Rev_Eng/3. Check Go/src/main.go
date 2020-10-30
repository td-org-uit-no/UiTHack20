package main

import (
	"fmt"
)

type Challenge struct {
    // binascii.unhexlify("49c9ce50e936f450d1e8b7e52b98706248e87ead1d9845e3471ff2fb91a21f40")
    encryption_key []byte
    // PLAIN: "_this_password_is_not_super_easy"
    password []byte
    // PLAIN: "UiTHack20{_this_is_a_nice_flag_}"
    flag []byte
}

func (c *Challenge) decrypt_data(data []byte) []byte {
    if len(data) != len(c.encryption_key) {
        return []byte{}
    }

    dec := make([]byte, len(data))
    for i,v := range data {
        dec[i] = v ^ c.encryption_key[i]
    }
    return dec
}

func (c *Challenge) check_password(password string) bool {
    if string(c.decrypt_data(c.password)) == password {
        return true
    } else {
        return false
    }
}

func (c *Challenge) print_flag() {
    fmt.Println(string(c.decrypt_data(c.flag)))
}

func new_challenge() Challenge {
    return Challenge{
        encryption_key: []byte("I\xc9\xceP\xe96\xf4P\xd1\xe8\xb7\xe5+\x98pbH\xe8~\xad\x1d\x98E\xe3G\x1f\xf2\xfb\x91\xa2\x1f@"),
        password: []byte("\x16\xbd\xa69\x9ai\x841\xa2\x9b\xc0\x8aY\xfc/\x0b;\xb7\x10\xc2i\xc76\x967z\x80\xa4\xf4\xc3l9"),
        flag: []byte("\x1c\xa0\x9a\x18\x88U\x9fb\xe1\x93\xe8\x91C\xf1\x03=!\x9b!\xccB\xf6,\x80\"@\x94\x97\xf0\xc5@="),
    }
}

func main() {
    var password string
    fmt.Printf("Enter password: ")
    _, err := fmt.Scanln(&password)
    if err != nil {
        fmt.Println("Error: ", err)
        return
    }

    chall := new_challenge()
    if chall.check_password(password) {
        chall.print_flag()
    } else {
        fmt.Println("Wrong password :/")
    }
}
