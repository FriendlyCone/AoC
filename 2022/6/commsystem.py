# Challenge input
inputfile = open("input.txt", "r").read()

# Variables
datastream = [*inputfile]

# Variables for beginning and end of scan range
setstart = 0
# Choose if looking for start-of-packet or start-of-message marker
markertype = input('What marker type are we looking for?\n1: start-of-packet\n2: start-of-message\nChoose type: ')
if markertype == "2":
    message ="start-of-message"
    setend = 14
else:
    message ="start-of-packet"
    setend = 4

for stream in datastream:
    currentset = datastream[setstart:setend]
    print("".join(currentset))
    uniqueset = set(currentset)
    if len(uniqueset) == len(currentset):
        print(f"Found {message} marker at {setend}")
        break
    if setend == 4095:
        print(f"Found no markers.")
        break
    setstart = setstart+1
    setend = setend+1