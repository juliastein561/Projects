#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:19:29 2021
@author: Shannon Duvall
Crack the code!  Implement a rotating substitution cipher
"""
"""
Project 3
@author: Julia Stein, MWF 2:00

NOTE: If you want to check if the decoded provided message is correct, 
      first input d/D for 'decode', then input p/P for 'provided message.'
      
      If you would like to check if your encoded message is correct, you can 
      copy the encoded output and input it through the decode function, it will 
      be in lower case because the alphabet list has only lower case letters.
"""

global final_message
# I'm not sure why I had to put this here and inside
# the main function, but it made the error go away.


def main():
    my_key = "qwertyuiopasdfghjklzxcvbnm"
    my_message = ("ehglnnan qslhmhl vjp xqxoeww mft tkkngxepcva hchrbvs feq znb vy fsmp, ecmz, "
                  "mvds gez evzso. hte eoztszjgxd ke fqquojtstl brbsyogo; vsp nqedgny moip lv "
                  "zcuq jd wgfgbkfoiwf uhbn gez evzso pwx wggtiznn qhqnylxepp eqnn.")
    global final_message
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    input_decode_encode = input("Would you like to decode or encode a message? Input either d/D or e/E: ")
    while input_decode_encode != 'D'.lower() and input_decode_encode != 'E'.lower():
        input_decode_encode = input("Input is invalid. Please input either d/D or e/E: ")
    if input_decode_encode == 'D'.lower():
        print('------- 🍎📇Lets decode!📇🍎-------')
        input_decode_message_type = input("Would you like to decode the message provided or decode your own message?\n"
                                          "     Input either p/P for 'provided message' or y/Y for 'your message': ")
        if input_decode_message_type == 'P'.lower():
            print("The provided message is decoded below.")
            final_message = decode(my_message, my_key, alphabet)
        if input_decode_message_type == 'Y'.lower():
            input_personal_decoded_message = input("What message would you like to decode?: ")
            final_message = decode(input_personal_decoded_message, my_key, alphabet)
    elif input_decode_encode == 'E'.lower():
        print('------- 📇🍎Lets encode!🍎📇-------')
        input_personal_encoded_message = input("What message would you like to encode?: ")
        final_message = encode(input_personal_encoded_message, my_key, alphabet)
    print(final_message)


def decode(my_message, my_key, alphabet):
    print('     The decoded message is: ', end='')
    decoded_message = ''
    my_key_list = []
    for char in my_key:
        my_key_list.append(char)
    key_to_alphabet = {}
    for char in my_message:
        for i in range(len(my_key)):
            key_to_alphabet.update({my_key_list[i]: alphabet[i]})
        if char in key_to_alphabet:
            decoded_message += key_to_alphabet[char]
            my_key_list.append(my_key_list[0])
            my_key_list.remove(my_key_list[0])
        else:
            decoded_message += char
    return decoded_message


def encode(input_personal_encoded_message, my_key, alphabet):
    input_personal_encoded_message = input_personal_encoded_message.lower()
    # I changed all the characters in the string to be lower case because if the character is upper
    # case, it isn't in the alphabet I made and is just appended to the encoded message, and it would
    # be obvious to the 'hacker' what those letters are due to them not being actually encrypted.

    encoded_message = ''
    print('     The encoded message is: ', end='')
    my_key_list = []
    for char in my_key:
        my_key_list.append(char)
    alphabet_to_key = {}
    for char in input_personal_encoded_message:
        for i in range(len(alphabet)):
            alphabet_to_key.update({alphabet[i]: my_key_list[i]})
        if char in alphabet_to_key:
            encoded_message += alphabet_to_key[char]
            my_key_list.append(my_key_list[0])
            my_key_list.remove(my_key_list[0])
        else:
            encoded_message += char
    return encoded_message


# Don't change this line of code:
if __name__ == '__main__':
    main()