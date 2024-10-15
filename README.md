# usp-a5-24904308

In this assignment, we will write a Python program loosely inspired by Unix command pkginfo (a
command available in a few versions of Unix). Our Python program will read a file containing
information about the installed software packages and will generate output depending on the
command line.
These are the specifications for our Python program:
1.  It must be named pkginfo.py. 

2.  It must be invoked as:
    `python pkginfo.py option argument_file`
    
    In the command line above, `option` means one of the options described below, and
    `argument_file` means the chosen argument file, which can have any arbitrary name.
    
    The program must check that argument `argument_file` exists, is a file and is readable. If not, it
    must print an error message to the <ins>standard output</ins> and exit. The specifications for the
    `argument_file` and `option` arguments are given below.

3. File argument_file can have any arbitrary name. It must be a file of text with the following
format:
    a. The file consists of an arbitrary number of lines (including, possibly, zero lines).

    b. Each line must contain four fields **separated by commas.**

    c. The four fields are: `category`, `name`, `description`, `size in kilobytes`.

    d. The `category` and `name` fields are each a string of characters of arbitrary (yet
    reasonably limited) length. Acceptable characters include: lower and upper case
    letters, digits, underscore, dot.

    e. The `description` field is a string of characters of arbitrary (yet reasonably limited)
    length. Acceptable characters include: lower and upper case letters, digits,
    underscore, dot, ‘+’, ‘/’, ‘-’, space.

    f. The size in kilobytes field is an integer limited between 1 and 10000000.

    <ins>**Fundamental note**</ins>: our program is not expected to verify that file `argument_file` complies with
    the above specifications. <ins>It will only be tested with compliant files.</ins>

    The following example should be regarded as the reference specification for the format of file
    argument_file:
    ```
    system,SUNWdoc,Documentation Tools,1251
    application,SPROcpl,C++ Compiler,25477
    system,BRCMbnxe,Broadcom NIC Driver,5423
    newcat,madeup,a made up line,100000
    application,ecj,Eclipse JDT,75443
    ```

4. Our program can be invoked with option: `-a`. In this case, it must print the names of the
installed packages in the order in which they appear in the argument file, in this format:
    ```
    Installed packages:
    first name in appearance order
    second name in appearance order
    ...
    last name in appearance order
    ```
    
    Example with the example `argument_file` given above:
    
    Command line:
    `python pkginfo.py -a argument_file`
    
    Expected output:
    ```
    Installed packages:
    SUNWdoc
    SPROcpl
    BRCMbnxe
    madeup
    ecj
    ```
    
    In the case in which file argument_file is empty, our program must instead only print:

    `No packages installed`
5. Our program can be invoked with option: `-s`. In this case, it must print the total size in
kilobytes of all the installed packages, in this format:
    
    `Total size in kilobytes: total size in kilobytes of all the installed packages`

    Example with the example argument_file given above:

    Command line:
    `python pkginfo.py –s argument_file`

    Expected output:
    `Total size in kilobytes: 207594`
    
    In the case in which file argument_file is empty, our program must print:
    `Total size in kilobytes: 0`
6. Our program can be invoked with option: `-l name`. The **name** argument has the same format
as the name field in the argument file. In this case, our program must search for a package
with that name in the argument file, and if it finds it, print its information in this format:
    ```
    Package: name
    Category: category
    Description: description
    Size in kilobytes: size in kilobytes
    ```

    Example with the example `argument_file` given above:
    Command line:
    `python pkginfo.py –l ecj argument_file`

    Expected output:
    ```
    Package: ecj
    Category: application
    Description: Eclipse JDT
    Size in kilobytes: 75443
    ```
    In the case in which a package with name name is not present in argument_file, our program
    must print:
    `No installed package with this name`
    
    Example with the example `argument_file` given above:
    Command line:
    `python pkginfo.py –l not_there argument_fil`e
    
    Expected output:
    `No installed package with this name`

7. Our program can be invoked with option: `-v`. In this case, it must only print the student name,
surname, student ID and date of completion of our assignment, in a format `YYYY-MM-DD`.
<ins>Please note that argument `argument_file` is still required.</ins>

8. No options can be used simultaneously. This means that our program can only be invoked
with one of the options at a time.

9. If our program is invoked with any other syntax than those specified above, it must print a
message of our choice to the <ins>**standard output**</ins> and exit.
    
    Examples of incorrect syntax:
    ```
    python pkginfo.py -Z argument_file (this option doesn't exist)
    python pkginfo.py –a (it misses the argument file)
    python pkginfo.py -l argument_file (it misses an argument)
    ```

