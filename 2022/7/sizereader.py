# Challenge input
inputfile = open("input.txt", "r")

# Variables
currentpath, sizelist = [], []
filesystemdict, folderdict = {}, {}
depth = 0

#  Directory processor build the path the command is currently in.
def directoryprocessor(command, pathtoprocess):
    print("\n==== Directory Processor ====")
    if '..' in command:
        print("This goes up a directory!")
        currentdirectory = pathtoprocess[-1]
        # Delete last entry in the path to represent going up a directory
        pathtoprocess.pop()
        print(f"We are now in {currentdirectory}")
    else:
        # Grab directory from the input command
        x,x,currentdirectory = command.split()
        print(f"This goes to {currentdirectory}")
        # Append dir_ to make sure the difference between directory and file is known
        currentdirectory = 'dir_' + currentdirectory
        # Add the directory to the working path
        pathtoprocess.append(currentdirectory)
        print(f"We came here from {pathtoprocess}.")
    print(f"Returning the following path: {pathtoprocess}")
    return pathtoprocess

# Build the folder dictionary / directory structure
def dictbuilder(filesystemdict, currentpath):
    print("\n==== Dictionary Builder ====")
    # Copy list into a new list to avoid ID issues
    currentpathforwards = currentpath[:]
    print(f"We're currently going through {filesystemdict.keys()}")
    print(f'The current path is: {currentpathforwards}')
    # If the path still contains items we can still go deeper
    if len(currentpathforwards) > 0:
        # Grab the folder to enter
        folder = currentpathforwards[0]
        # See if the folder exists
        if folder in filesystemdict.keys():
            print("Directory found!")
            # Remove the directory as we'll enter it now to prevent a loop
            currentpathforwards.pop(0)
            # Enter the folder and repeat
            dictbuilder(filesystemdict.get(folder), currentpathforwards)
        else:
            # If the directory isn't in there yet, we'll create it - including an empty size key for later use
            print("Not in it, adding it...")
            filesystemdict.update({folder: {'deepsize': 0, 'size': 0}})
    else:
        print("Processed entire path.")
    return filesystemdict

# Add files to correct place in the dictionary
def fileprocessor(command, filesystemdict, currentpath):
    print("\n==== File Processor ====")
    print(f'{command.strip()} is in directory {currentpath[-1]}')
    # Copy currentpath into unique list to avoid ID issues
    currentpathforwards = currentpath[:]
    print(currentpathforwards)
    # Go to correct directory
    if len(currentpathforwards) > 1:
        # Grab the folder to enter
        newdict = currentpathforwards[0]
        print("Directory found!")
        # Remove the directory as we'll enter it now to prevent a loop 
        currentpathforwards.pop(0)
        # Enter run the processor again, but in the next folder
        fileprocessor(command, filesystemdict.get(newdict), currentpathforwards)
    # Check if in correct directory
    elif currentpath[-1] in filesystemdict.keys() and len(currentpathforwards) == 1:
        # Split the command into the filesize and filename elements
        filesize, filename = command.split()
        # Append file_ to file name
        filename = 'file_' + filename
        print("We're in the right folder!")
        # Merge the current directory with what I want to add so it doesn't overwrite
        merged = {**filesystemdict.get(currentpath[-1]), **{filename: int(filesize)}}
        # Add the merged contents back into the dictionary
        filesystemdict.update({currentpath[-1]: merged})
        # Call the size calculator as we now want to update the size value.
        sizecalculator(filesystemdict, currentpath)
    return filesystemdict

# Calculate size of every folder
def sizecalculator(filesystemdict, currentpath):
    print("\n==== Size Calculator ====")
    # Create unique list to prevent ID issues
    currentpathforwards = currentpath[:]
    # Check if we're in the deepest directory
    if currentpath[-1] in filesystemdict.keys():
        print(f"We're in the lowest undone folder! - {currentpath[-1]}")
        folder = filesystemdict.get(currentpath[-1])
        newsize = 0
        print(f"The current size is {folder.get('size')}")
        for filename, size in folder.items():
            # Ignore the key called size to avoid counting its current size again
            if 'size' == filename:
                continue
            print(f'{filename} - {size}')
            if type(size) == type(0):
                newsize = newsize + size
        print(f'The new size is {newsize}')
        filesystemdict[currentpath[-1]]['size'] = newsize
        newsize = 0
    # Go to the deepest directory
    if len(currentpathforwards) > 1:
        newdict = currentpathforwards[0]
        if newdict in filesystemdict.keys():
            print("Directory found!")
            currentpathforwards.pop(0)
            sizecalculator(filesystemdict.get(newdict), currentpathforwards)
    return filesystemdict

# Calculate size of every folder, including the folders it contains
def totalsizecalculator(filesystemdict, magicmath):
    print("\n==== Total Size Calculator ====")
    # print(filesystemdict)
    newdeepsize = 0
    currentsize = 0
    folderfound = False
    for key, value in filesystemdict.items():
        print(f"{key} - {value}")
        # Grab current folder size value
        if key == "size":
            currentsize = value
        # Check if there is a folder within the current folder
        if type(value) is dict:
            folder = value
            folderfound = True
            print("Folder has been found!")
        # Dig deeper if we know there is a contained folder
        if folderfound:
            print("Directory found in unprocessed folder, entering...")
            x, magicmath = totalsizecalculator(folder, magicmath)
            newdeepsize = newdeepsize + magicmath
            folder["deepsize"] = magicmath
    # If we are at the deepest, return the size for calculation higher up
    if not folderfound:
        print("Arrived at deepest unprocessed directory, returning size...")
        filesystemdict["deepsize"] = filesystemdict.get("size")
        print(f"Deepsize is now {filesystemdict.get('deepsize')}")
        magicmath = filesystemdict.get('deepsize')
        return filesystemdict, magicmath
    else:
        # Add the currentsize to the new deepsize value so that it also counts itself
        newdeepsize = newdeepsize + currentsize
        return filesystemdict, newdeepsize

# Pretty print the contents of the megadict, collect list of all directory sizes
def structureprinter(filesystemdict, depth, folderdict, sizelist):
    # ==== Folder Structure Printer ====
    depth = depth + 1
    for folder, size in filesystemdict.items():
        if "dir_" in folder:
            if depth == 1:
                print(f"{folder} - {size.get('deepsize')}")
                sizelist.append(size.get('deepsize'))
            else:
                print("|" + "-"*depth + f"{folder} - {size.get('deepsize')}")
                sizelist.append(size.get('deepsize'))
            folderdict[folder] = size.get('deepsize')
            folderdict, sizelist = structureprinter(size, depth, folderdict, sizelist)
    return folderdict, sizelist

# Build the directory structure
for command in inputfile: 
    print("\n==== Main Loop ====")
    # Check if it is user input
    print(f"Currently processing: {command.strip()}")
    # Send directory command to directory processor to add to dictionary if needed
    if '$ cd' in command:
        currentpath = directoryprocessor(command, currentpath)
        filesystemdict = dictbuilder(filesystemdict, currentpath)
    # Ignore ls command
    elif '$ ls' in command:
        print("ls command... ignoring")
    # Ignore dir's, all taken care of in the directoryprocessor
    elif 'dir' in command:
        print("Directory... ignoring")
    # Only remaining items are files, send to the fileprocessor to add to the dictionary and tally up the sizes
    else:
        print("DEBUG: Calling fileprocessor")
        filesystemdict = fileprocessor(command, filesystemdict, currentpath)

# Calculate the final size
filesystemdict, x = totalsizecalculator(filesystemdict, 0)

# Variables for the Part 1 answer
print("\n==== Folder Structure Printer ====")
folderdict, sizelist = structureprinter(filesystemdict, depth, folderdict, sizelist)
sizesum = 0

# Get Part 1 answer
for size in sizelist:
    if size <= 100000:
        sizesum = sizesum + size
print(f"\nThe sum of all directories below size 100000 is {sizesum}")

# Get Part 2 answer
totaldiskspace = 70000000
requireddiskspace = 30000000
useddiskspace = max(sizelist)
freediskspace = totaldiskspace - useddiskspace
difftotarget = requireddiskspace - freediskspace
possibletargets = []
print(f"\nUsed space: {useddiskspace}")
print(f"Free space: {freediskspace}")
print(f"Target    : {requireddiskspace}")
print(f"Difference: {difftotarget}")
print(f"Currently the free disk space is {freediskspace}, this is less than the required {requireddiskspace}.")
print("Looking for best directory to clean...")

for size in sizelist:
    if freediskspace + size >= requireddiskspace:
        possibletargets.append(size)

print(f"Most efficient target is {min(possibletargets)}\n")

print(filesystemdict)