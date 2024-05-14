#!/bin/bash
while read -r line; do
 sudo rm -rf "$line"
done < <(locate timeshift)

