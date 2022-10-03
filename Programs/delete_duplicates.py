'''
README FOR THE PROGRAM
## [Delete duplicate files](./delete_copies.py)

### usage:
`python delete_copies.py <folder1> <folder2> <folder3> (and so on) <print/trash/delete>`

### Description
You can enter as many folders as you can, but the script checks for just the mentioned folder and its child folders, it does not include parent folder

last arguments explanation:

  `print` - just print the duplicate files

  `trash` - deletes all the duplicate files in the folder and sends them to trash/recycle bin
  
  `delete` - deletes the duplicate files permanently (can't be found in trash after this is executed, there is backup too in case this is just unfortunate command execution)
'''
try:
    import os
    import sys
    import hashlib
    import subprocess
    import send2trash
except:
    if sys.platform in ['win32', 'cygwin']:
        subprocess.check_output("python -m pip install --upgrade pip", shell=True)
        subprocess.check_output("python -m pip install send2trash", shell=True)
    else:
        subprocess.check_output("pip install --upgrade pip", shell=True)
        subprocess.check_outpue("pip install send2trash", shell=True)
    
def usage():
    print("[+] python file.py <folder1> <folder2> <folder3> delete -> to permanently delete the repeated files")
    print("[+] python file.py <folder1> <folder2> <folder3> trahs -> to send the repeated tiles to trash/recycle bin")
    print("[+] python file.py <folder1> <folder2> <folder3> print -> to just print the path of the repeated files")
    print("[+] You can enter as many folders as you can")
    sys.exit()

def printResults(files):
    print("[+] The following files are identical, names could differ but the file contents are identical")
    print("-------------------")
    for f in files:
        for i in f:
            print("\t{}".format(i))
        print("-------------------")

def trashFiles(files):
    for f in files:
        for i in f[1:]:
            print(f"[=] Trashing {i} file")
            send2trash.send2trash(i)
        print("-------------------")
        print(f"[+] {f[0]} duplicates of this file are send to trash.")
    print("[=] JOB DONE")

def deletePermanently(files):
    warnAgain = str(input("[-] Are you sure to delete these files(yes/no): "))
    while warnAgain.lower() not in ['yes', 'y', 'n', 'no']:
        warnAgain = str(input("[-] Are you sure to delete these files(yes/no): "))
    if warnAgain.lower() in ['yes', 'y']:
        print("[-] Deleting the duplicate files permanently...")
        for f in files:
            for i in f[1:]:
                print(f"[=] Deleting {i} file")
                os.remove(i)
            print("---------------")
            print(f"[=] {f[0]} duplicates are removes successfully...")
        print("[=] JOB DONE")
    else:
        print("[-] Exit from the program, no files are deleted..")

def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def findDuplicates(parentFolder):
    copies = {}
    for dirName, subDir, fileList in os.walk(parentFolder):
        print(f"Scanning {dirName}")
        for filename in fileList:
            path = os.path.join(dirName, filename)
            file_hash = hashfile(path)
            if file_hash in copies:
                copies[file_hash].append(path)
            else:
                copies[file_hash] = [path]
    return copies

def delete_empty_folder(folders):
    for i in folders:
        for dirname, folders, files in os.walk(i):
            for folder in folders:
                try:
                    path = os.path.join(dirname, folder)
                    os.rmdir(path)
                    print(f"[+] deleted empty folder {path}")
                except Exception as error:
                    continue

def joinDicts(parentDict, childDict):
    for key in childDict.keys():
        parentDict[key] = childDict[key] if key not in parentDict else parentDict[key] + childDict[key]

if __name__ == '__main__':
    if len(sys.argv)>2 and sys.argv[-1].lower() in ['trash', 'delete','print']:
        duplicate_files = {}
        folders = sys.argv[1:-1]
        for i in folders:
            if os.path.exists(i):
                joinDicts(duplicate_files, findDuplicates(i))
            else:
                print(f"[-] folder path {i} does not exists")
                sys.exit()
        duplicate_files = list(filter(lambda x : len(x)>1, duplicate_files.values()))
        if len(duplicate_files)<=0:
            print("[=] No duplicates found.....")
            sys.exit()
        else:
            print("[=] Duplicates found")
            if sys.argv[-1].lower() == 'print':
                printResults(duplicate_files)
            elif sys.argv[-1].lower() == 'trash':
                trashFiles(duplicate_files)
                delete_empty_folder(sys.argv[1:-1])
            elif sys.argv[-1].lower() == 'delete':
                deletePermanently(duplicate_files)
                delete_empty_folder(sys.argv[1:-1])
            sys.exit()
    else:
        usage()
