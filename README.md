# Boat

This is a work in progress to create custom rc boat.

## Part List

This is all parts that I had and I am planning to use.

- Raspberry Pi Pico
- 20A ESC
- 2300KV Motor
- 12V Battery
- UBEC 12V to 5V converter
- Servos still researching

## DEV Setup

1. Install micropython on raspberry pi
2. Setup virtual environment for python and install requirements
3. Use rshell to do the rest

### Setup Virtual Environment

```bash
# Setup venv
python3 -m venv venv
source venv/bin/activate
# Install requirements
pip install -r requirements.txt
```

### shell

```bash
rshell
rshell ls
rshell
# ctrl-x seems to close repl
ls /pyboard

rshell repl
# sync src with pyboard
rshell rsync src/ /pyboard

# run specific file in repl
exec(open('test.py').read())
```

### Install Packages

```bash
# Install mip packages
rshell
repl
import mip
mip.install('umqtt.simple')
```
