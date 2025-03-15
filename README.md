# Enigma Cipher Cracker
## Overview
This project is an Enigma machine cracker that attempts to decrypt messages encoded using the WWII-era German M3 Enigma machine. By leveraging known plaintext attacks and brute force techniques, the program determines the daily Enigma settings and deciphers intercepted ciphertexts.

## Features
- Brute Force Cracking: Iterates through all possible Enigma settings to find the correct configuration.
- Known-Plaintext Attack: Identifies the repeated key in intercepted messages to accelerate cracking.
- Simulated M3 Enigma Machine: Uses an external Enigma implementation to process encryption and decryption.
- Support for Multiple Reflectors & Rotors: Tests various Enigma configurations including different rotors, reflectors, and plugboard settings.

## How it Works
- The file enigmaCracker.py can be ran to decrypt message encoded using a real engima machine, or using the enigma simulator enigma.py.
- Once the program is ran all possible rotor and reflector combinations are used on the first 6 letters of the ciphertext.
- If the first 6 letters contain repetitions, the rest of the ciphertext is than decrypted using the previous machine settings and printed in the console.
- The user can then view these print statements, and find the one that displays the correct message and machine settings.
