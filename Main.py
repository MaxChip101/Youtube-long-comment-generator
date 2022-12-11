# Youtube longest comment generator
import time

commentlen = 3332 # 3332 is the maximum characters youtube can handle

print("< YouTube longest comment generator : By MaxChip101 >")
begginingletter = input("Input a beggining character: ")
endingletter = input("Input an ending character: ")
savefile = input("Save to directory: ")

open(str(savefile), "w")

l = 0

print("Writing...")

while commentlen > l:
    time.sleep(0)
    l += 1
    with open("longcomment.txt", "a") as f:
        if l < 2:
            f.write(begginingletter)
        else:
            f.write(" "+ "\n")
            if l > commentlen - 1:
                f.write(endingletter)


print("Done")
time.sleep(1)
print("Thanks for using my software")
