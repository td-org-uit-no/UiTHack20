package main

import (
	"fmt"
)

type Challenge struct {
    // binascii.unhexlify("49c9ce50e936f450d1e8b7e52b98706248e87ead1d9845e3471ff2fb91a21f40")
    encryption_key []byte
    // PLAIN: "particularly_extensive_passwords"
    password []byte
    // PLAIN: "UiTHack20{gophers_are_secretive}"
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
        password: []byte("9\xa8\xbc$\x80U\x81<\xb0\x9a\xdb\x9ct\xfd\x08\x16-\x86\r\xc4k\xfd\x1a\x93&l\x81\x8c\xfe\xd0{3"),
        flag: []byte("\x1c\xa0\x9a\x18\x88U\x9fb\xe1\x93\xd0\x8a[\xf0\x15\x10;\xb7\x1f\xdfx\xc76\x86$m\x97\x8f\xf8\xd4z="),
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
