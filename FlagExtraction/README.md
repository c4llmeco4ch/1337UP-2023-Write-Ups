# Flag Extraction

## Category

Warmup

## Tools Used

Command-line tools

## Key Takeaways

- Getting to know some general file types and how to decompress them

## Question

They told me I just need to extract flag but I don't know what that means?!

_flag.rar_ is provided

## Process

At the beginning of the challenge, we are provided with a _.rar_ file. Much like decompressing the commonly understood _.zip_ format, we need to start by extracting the contents of this to move forward. A command-line tool for this is [unrar](https://linux.die.net/man/1/unrar), and we can see that the _e_ option will provide us with what we need to move forward.

```sh
[foo@bar FlagExtraction]$ unrar e flag.rar 

UNRAR 6.24 freeware      Copyright (c) 1993-2023 Alexander Roshal


Extracting from flag.rar

Extracting  flag.tar.xz                                               OK 
All OK
```

As shown from the above output, we are now left with a _.tar.xz_ extension, which can luckily be dealt with using the [tar](https://linux.die.net/man/1/tar) tool. A simple command, `tar -xf flag.tar.xz`, will move us onto the next step.

Extracting the _.xz_ file, we are now left with a _.bz2_ file, which can be dealt with using the [bzip2](https://linux.die.net/man/1/bzip2) tool. As should be old hat at this point, we just need to run the following command: `bzip2 -d flag.tar.bz2`.

Now, we are left with a simple _.tar_ file, which will provide with exactly the same command to move forward as with the _.xz_ file: `tar -xf flag.tar`.

Being now provided with a _.gz_ file, we can use the [gzip](https://linux.die.net/man/1/gzip) tool and run the familiar `gzip -d flag.tar.gz`.

Seeing as we are left with yet another _.tar_ file, we can simply repeat the command from above once more: `tar -xf flag.tar`

Getting near the end (one would hope), we are left with the much more simple _.zip_ file, and can simply extract that using [unzip](https://linux.die.net/man/1/unzip): `unzip flag.zip`.

![Uhh...](flag.gif)

Well...that's strange? We're left with a gif that seems to be a dead end. How do we proceed...?

Considering we are asked to "extract" the flag, that leads us to thinking about how we can extract data from a non-traditional file format when something might spring to mind: "What if we just try to 'print' the image?" And for that, we can use the [strings](https://linux.die.net/man/1/strings) tool. However, when we attempt to run `strings flag.gif`, we are met with an insane number of lines and simply cannot parse all of them. Luckily for us, [grep](https://linux.die.net/man/1/grep) can provide us the salvation we need with a simple pipe operator: `strings flag.gif | grep INTIGRITI`!

Running this last command, we are met with the flag, `INTIGRITI{fl46_3x7r4c710n_c0mpl373}`!