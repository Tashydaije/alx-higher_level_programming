#!/bin/bash
# Sends a POST request to a URL argument, and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD" -L
