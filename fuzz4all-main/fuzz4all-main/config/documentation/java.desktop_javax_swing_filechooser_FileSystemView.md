# Class FileSystemView

**Source:** `java.desktop\javax\swing\filechooser\FileSystemView.html`

### Class Description

```java
public abstract class
FileSystemView

extends
Object
```

FileSystemView is JFileChooser's gateway to the
file system. Since the JDK1.1 File API doesn't allow
access to such information as root partitions, file type
information, or hidden file bits, this class is designed
to intuit as much OS-specific file system information as
possible.

Java Licensees may want to provide a different implementation of
FileSystemView to better handle a given operating system.

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileSystemView()

Constructs a FileSystemView.

---

### Method Details

#### public static
FileSystemView
getFileSystemView()

Returns the file system view.

**Returns:**
- the file system view

---

#### public boolean isRoot​(
File
f)

Determines if the given file is a root in the navigable tree(s).
Examples: Windows 98 has one root, the Desktop folder. DOS has one root
per drive letter,

C:\

,

D:\

, etc. Unix has one root,
the

"/"

directory.

The default implementation gets information from the

ShellFolder

class.

**Parameters:**
- f

- a

File

object representing a directory

**Returns:**
- true

if

f

is a root in the navigable tree.

**See Also:**
- isFileSystemRoot(java.io.File)

---

#### public
Boolean
isTraversable​(
File
f)

Returns true if the file (directory) can be visited.
Returns false if the directory cannot be traversed.

**Parameters:**
- f

- the

File

**Returns:**
- true

if the file/directory can be traversed, otherwise

false

**See Also:**
- JFileChooser.isTraversable(java.io.File)

,

FileView.isTraversable(java.io.File)

**Since:**
- 1.4

---

#### public
String
getSystemDisplayName​(
File
f)

Name of a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays as "CD-ROM (M:)"

The default implementation gets information from the ShellFolder class.

**Parameters:**
- f

- a

File

object

**Returns:**
- the file name as it would be displayed by a native file chooser

**See Also:**
- JFileChooser.getName(java.io.File)

**Since:**
- 1.4

---

#### public
String
getSystemTypeDescription​(
File
f)

Type description for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "Desktop" folder
is described as "Desktop".

Override for platforms with native ShellFolder implementations.

**Parameters:**
- f

- a

File

object

**Returns:**
- the file type description as it would be displayed by a native file chooser
or null if no native information is available.

**See Also:**
- JFileChooser.getTypeDescription(java.io.File)

**Since:**
- 1.4

---

#### public
Icon
getSystemIcon​(
File
f)

Icon for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays a CD-ROM icon.

The default implementation gets information from the ShellFolder class.

**Parameters:**
- f

- a

File

object

**Returns:**
- an icon as it would be displayed by a native file chooser

**See Also:**
- JFileChooser.getIcon(java.io.File)

**Since:**
- 1.4

---

#### public boolean isParent​(
File
folder,

File
file)

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem. Folder could for example be the
"Desktop" folder which is not the same as file.getParentFile().

**Parameters:**
- folder

- a

File

object representing a directory or special folder
- file

- a

File

object

**Returns:**
- true

if

folder

is a directory or special folder and contains

file

.

**Since:**
- 1.4

---

#### public
File
getChild​(
File
parent,

String
fileName)

**Parameters:**
- parent

- a

File

object representing a directory or special folder
- fileName

- a name of a file or folder which exists in

parent

**Returns:**
- a File object. This is normally constructed with

new
File(parent, fileName)

except when parent and child are both
special folders, in which case the

File

is a wrapper containing
a

ShellFolder

object.

**Since:**
- 1.4

---

#### public boolean isFileSystem​(
File
f)

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

. Used by UI classes to decide if
a folder is selectable when doing directory choosing.

**Parameters:**
- f

- a

File

object

**Returns:**
- true

if

f

is a real file or directory.

**Since:**
- 1.4

---

#### public abstract
File
createNewFolder​(
File
containingDir)
throws
IOException

Creates a new folder with a default folder name.

**Parameters:**
- containingDir

- a

File

object denoting directory to contain the new folder

**Returns:**
- a

File

object denoting the newly created folder

**Throws:**
- IOException

- if new folder could not be created

---

#### public boolean isHiddenFile​(
File
f)

Returns whether a file is hidden or not.

**Parameters:**
- f

- a

File

object

**Returns:**
- true if the given

File

denotes a hidden file

---

#### public boolean isFileSystemRoot​(
File
dir)

Is dir the root of a tree in the file system, such as a drive
or partition. Example: Returns true for "C:\" on Windows 98.

**Parameters:**
- dir

- a

File

object representing a directory

**Returns:**
- true

if

f

is a root of a filesystem

**See Also:**
- isRoot(java.io.File)

**Since:**
- 1.4

---

#### public boolean isDrive​(
File
dir)

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

The default implementation has no way of knowing, so always returns false.

**Parameters:**
- dir

- a directory

**Returns:**
- false

always

**Since:**
- 1.4

---

#### public boolean isFloppyDrive​(
File
dir)

Used by UI classes to decide whether to display a special icon
for a floppy disk. Implies isDrive(dir).

The default implementation has no way of knowing, so always returns false.

**Parameters:**
- dir

- a directory

**Returns:**
- false

always

**Since:**
- 1.4

---

#### public boolean isComputerNode​(
File
dir)

Used by UI classes to decide whether to display a special icon
for a computer node, e.g. "My Computer" or a network server.

The default implementation has no way of knowing, so always returns false.

**Parameters:**
- dir

- a directory

**Returns:**
- false

always

**Since:**
- 1.4

---

#### public
File
[] getRoots()

Returns all root partitions on this system. For example, on
Windows, this would be the "Desktop" folder, while on DOS this
would be the A: through Z: drives.

**Returns:**
- an array of

File

objects representing all root partitions
on this system

---

#### public
File
getHomeDirectory()

Returns the home directory.

**Returns:**
- the home directory

---

#### public
File
getDefaultDirectory()

Return the user's default starting directory for the file chooser.

**Returns:**
- a

File

object representing the default
starting folder

**Since:**
- 1.4

---

#### public
File
createFileObject​(
File
dir,

String
filename)

Returns a File object constructed in dir from the given filename.

**Parameters:**
- dir

- an abstract pathname denoting a directory
- filename

- a

String

representation of a pathname

**Returns:**
- a

File

object created from

dir

and

filename

---

#### public
File
createFileObject​(
String
path)

Returns a File object constructed from the given path string.

**Parameters:**
- path

-

String

representation of path

**Returns:**
- a

File

object created from the given

path

---

#### public
File
[] getFiles​(
File
dir,
boolean useFileHiding)

Gets the list of shown (i.e. not hidden) files.

**Parameters:**
- dir

- the root directory of files to be returned
- useFileHiding

- determine if hidden files are returned

**Returns:**
- an array of

File

objects representing files and
directories in the given

dir

. It includes hidden
files if

useFileHiding

is false.

---

#### public
File
getParentDirectory​(
File
dir)

Returns the parent directory of

dir

.

**Parameters:**
- dir

- the

File

being queried

**Returns:**
- the parent directory of

dir

, or

null

if

dir

is

null

---

#### public
File
[] getChooserComboBoxFiles()

Returns an array of files representing the values to show by default in
the file chooser selector.

**Returns:**
- an array of

File

objects.

**Throws:**
- SecurityException

- if the caller does not have necessary
permissions

**Since:**
- 9

---

#### public boolean isLink​(
File
file)

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

**Parameters:**
- file

- a file

**Returns:**
- whether this is a link

**Throws:**
- NullPointerException

- if

file

equals

null
- SecurityException

- if the caller does not have necessary
permissions

**See Also:**
- getLinkLocation(File)

**Since:**
- 9

---

#### public
File
getLinkLocation​(
File
file)
throws
FileNotFoundException

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.
Returns

null

if the specified file is not
a shell interpreted link.

**Parameters:**
- file

- a file

**Returns:**
- the linked file or

null

.

**Throws:**
- FileNotFoundException

- if the linked file does not exist
- NullPointerException

- if

file

equals

null
- SecurityException

- if the caller does not have necessary
permissions

**Since:**
- 9

---

#### protected
File
createFileSystemRoot​(
File
f)

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

**Parameters:**
- f

- a

File

object representing a file system root
directory, for example "/" on Unix or "C:\" on Windows.

**Returns:**
- a new

File

object

**Since:**
- 1.4

---

### Additional Sections

#### Class FileSystemView

java.lang.Object

- javax.swing.filechooser.FileSystemView

javax.swing.filechooser.FileSystemView

```java
public abstract class
FileSystemView

extends
Object
```

FileSystemView is JFileChooser's gateway to the
file system. Since the JDK1.1 File API doesn't allow
access to such information as root partitions, file type
information, or hidden file bits, this class is designed
to intuit as much OS-specific file system information as
possible.

Java Licensees may want to provide a different implementation of
FileSystemView to better handle a given operating system.

public abstract class

FileSystemView

extends

Object

FileSystemView is JFileChooser's gateway to the
file system. Since the JDK1.1 File API doesn't allow
access to such information as root partitions, file type
information, or hidden file bits, this class is designed
to intuit as much OS-specific file system information as
possible.

Java Licensees may want to provide a different implementation of
FileSystemView to better handle a given operating system.

Java Licensees may want to provide a different implementation of
FileSystemView to better handle a given operating system.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileSystemView

()

Constructs a FileSystemView.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

File

createFileObject

​(

File

dir,

String

filename)

Returns a File object constructed in dir from the given filename.

File

createFileObject

​(

String

path)

Returns a File object constructed from the given path string.

protected

File

createFileSystemRoot

​(

File

f)

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

abstract

File

createNewFolder

​(

File

containingDir)

Creates a new folder with a default folder name.

File

getChild

​(

File

parent,

String

fileName)

File

[]

getChooserComboBoxFiles

()

Returns an array of files representing the values to show by default in
the file chooser selector.

File

getDefaultDirectory

()

Return the user's default starting directory for the file chooser.

File

[]

getFiles

​(

File

dir,
boolean useFileHiding)

Gets the list of shown (i.e. not hidden) files.

static

FileSystemView

getFileSystemView

()

Returns the file system view.

File

getHomeDirectory

()

Returns the home directory.

File

getLinkLocation

​(

File

file)

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.

File

getParentDirectory

​(

File

dir)

Returns the parent directory of

dir

.

File

[]

getRoots

()

Returns all root partitions on this system.

String

getSystemDisplayName

​(

File

f)

Name of a file, directory, or folder as it would be displayed in
a system file browser.

Icon

getSystemIcon

​(

File

f)

Icon for a file, directory, or folder as it would be displayed in
a system file browser.

String

getSystemTypeDescription

​(

File

f)

Type description for a file, directory, or folder as it would be displayed in
a system file browser.

boolean

isComputerNode

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a computer node, e.g.

boolean

isDrive

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

boolean

isFileSystem

​(

File

f)

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

.

boolean

isFileSystemRoot

​(

File

dir)

Is dir the root of a tree in the file system, such as a drive
or partition.

boolean

isFloppyDrive

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a floppy disk.

boolean

isHiddenFile

​(

File

f)

Returns whether a file is hidden or not.

boolean

isLink

​(

File

file)

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

boolean

isParent

​(

File

folder,

File

file)

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem.

boolean

isRoot

​(

File

f)

Determines if the given file is a root in the navigable tree(s).

Boolean

isTraversable

​(

File

f)

Returns true if the file (directory) can be visited.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

FileSystemView

()

Constructs a FileSystemView.

---

#### Constructor Summary

Constructs a FileSystemView.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

File

createFileObject

​(

File

dir,

String

filename)

Returns a File object constructed in dir from the given filename.

File

createFileObject

​(

String

path)

Returns a File object constructed from the given path string.

protected

File

createFileSystemRoot

​(

File

f)

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

abstract

File

createNewFolder

​(

File

containingDir)

Creates a new folder with a default folder name.

File

getChild

​(

File

parent,

String

fileName)

File

[]

getChooserComboBoxFiles

()

Returns an array of files representing the values to show by default in
the file chooser selector.

File

getDefaultDirectory

()

Return the user's default starting directory for the file chooser.

File

[]

getFiles

​(

File

dir,
boolean useFileHiding)

Gets the list of shown (i.e. not hidden) files.

static

FileSystemView

getFileSystemView

()

Returns the file system view.

File

getHomeDirectory

()

Returns the home directory.

File

getLinkLocation

​(

File

file)

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.

File

getParentDirectory

​(

File

dir)

Returns the parent directory of

dir

.

File

[]

getRoots

()

Returns all root partitions on this system.

String

getSystemDisplayName

​(

File

f)

Name of a file, directory, or folder as it would be displayed in
a system file browser.

Icon

getSystemIcon

​(

File

f)

Icon for a file, directory, or folder as it would be displayed in
a system file browser.

String

getSystemTypeDescription

​(

File

f)

Type description for a file, directory, or folder as it would be displayed in
a system file browser.

boolean

isComputerNode

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a computer node, e.g.

boolean

isDrive

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

boolean

isFileSystem

​(

File

f)

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

.

boolean

isFileSystemRoot

​(

File

dir)

Is dir the root of a tree in the file system, such as a drive
or partition.

boolean

isFloppyDrive

​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a floppy disk.

boolean

isHiddenFile

​(

File

f)

Returns whether a file is hidden or not.

boolean

isLink

​(

File

file)

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

boolean

isParent

​(

File

folder,

File

file)

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem.

boolean

isRoot

​(

File

f)

Determines if the given file is a root in the navigable tree(s).

Boolean

isTraversable

​(

File

f)

Returns true if the file (directory) can be visited.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a File object constructed in dir from the given filename.

Returns a File object constructed from the given path string.

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

Creates a new folder with a default folder name.

Returns an array of files representing the values to show by default in
the file chooser selector.

Return the user's default starting directory for the file chooser.

Gets the list of shown (i.e. not hidden) files.

Returns the file system view.

Returns the home directory.

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.

Returns the parent directory of

dir

.

Returns all root partitions on this system.

Name of a file, directory, or folder as it would be displayed in
a system file browser.

Icon for a file, directory, or folder as it would be displayed in
a system file browser.

Type description for a file, directory, or folder as it would be displayed in
a system file browser.

Used by UI classes to decide whether to display a special icon
for a computer node, e.g.

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

.

Is dir the root of a tree in the file system, such as a drive
or partition.

Used by UI classes to decide whether to display a special icon
for a floppy disk.

Returns whether a file is hidden or not.

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem.

Determines if the given file is a root in the navigable tree(s).

Returns true if the file (directory) can be visited.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileSystemView

```java
public FileSystemView()
```

Constructs a FileSystemView.

============ METHOD DETAIL ==========

- Method Detail

- getFileSystemView

```java
public static
FileSystemView
getFileSystemView()
```

Returns the file system view.

**Returns:** the file system view

- isRoot

```java
public boolean isRoot​(
File
f)
```

Determines if the given file is a root in the navigable tree(s).
Examples: Windows 98 has one root, the Desktop folder. DOS has one root
per drive letter,

C:\

,

D:\

, etc. Unix has one root,
the

"/"

directory.

The default implementation gets information from the

ShellFolder

class.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if

f

is a root in the navigable tree.
**See Also:** isFileSystemRoot(java.io.File)

- isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Returns true if the file (directory) can be visited.
Returns false if the directory cannot be traversed.

**Parameters:** f

- the

File
**Returns:** true

if the file/directory can be traversed, otherwise

false
**Since:** 1.4
**See Also:** JFileChooser.isTraversable(java.io.File)

,

FileView.isTraversable(java.io.File)

- getSystemDisplayName

```java
public
String
getSystemDisplayName​(
File
f)
```

Name of a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays as "CD-ROM (M:)"

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** the file name as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getName(java.io.File)

- getSystemTypeDescription

```java
public
String
getSystemTypeDescription​(
File
f)
```

Type description for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "Desktop" folder
is described as "Desktop".

Override for platforms with native ShellFolder implementations.

**Parameters:** f

- a

File

object
**Returns:** the file type description as it would be displayed by a native file chooser
or null if no native information is available.
**Since:** 1.4
**See Also:** JFileChooser.getTypeDescription(java.io.File)

- getSystemIcon

```java
public
Icon
getSystemIcon​(
File
f)
```

Icon for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays a CD-ROM icon.

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** an icon as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getIcon(java.io.File)

- isParent

```java
public boolean isParent​(
File
folder,

File
file)
```

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem. Folder could for example be the
"Desktop" folder which is not the same as file.getParentFile().

**Parameters:** folder

- a

File

object representing a directory or special folder
**Parameters:** file

- a

File

object
**Returns:** true

if

folder

is a directory or special folder and contains

file

.
**Since:** 1.4

- getChild

```java
public
File
getChild​(
File
parent,

String
fileName)
```

**Parameters:** parent

- a

File

object representing a directory or special folder
**Parameters:** fileName

- a name of a file or folder which exists in

parent
**Returns:** a File object. This is normally constructed with

new
File(parent, fileName)

except when parent and child are both
special folders, in which case the

File

is a wrapper containing
a

ShellFolder

object.
**Since:** 1.4

- isFileSystem

```java
public boolean isFileSystem​(
File
f)
```

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

. Used by UI classes to decide if
a folder is selectable when doing directory choosing.

**Parameters:** f

- a

File

object
**Returns:** true

if

f

is a real file or directory.
**Since:** 1.4

- createNewFolder

```java
public abstract
File
createNewFolder​(
File
containingDir)
throws
IOException
```

Creates a new folder with a default folder name.

**Parameters:** containingDir

- a

File

object denoting directory to contain the new folder
**Returns:** a

File

object denoting the newly created folder
**Throws:** IOException

- if new folder could not be created

- isHiddenFile

```java
public boolean isHiddenFile​(
File
f)
```

Returns whether a file is hidden or not.

**Parameters:** f

- a

File

object
**Returns:** true if the given

File

denotes a hidden file

- isFileSystemRoot

```java
public boolean isFileSystemRoot​(
File
dir)
```

Is dir the root of a tree in the file system, such as a drive
or partition. Example: Returns true for "C:\" on Windows 98.

**Parameters:** dir

- a

File

object representing a directory
**Returns:** true

if

f

is a root of a filesystem
**Since:** 1.4
**See Also:** isRoot(java.io.File)

- isDrive

```java
public boolean isDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- isFloppyDrive

```java
public boolean isFloppyDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a floppy disk. Implies isDrive(dir).

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- isComputerNode

```java
public boolean isComputerNode​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a computer node, e.g. "My Computer" or a network server.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- getRoots

```java
public
File
[] getRoots()
```

Returns all root partitions on this system. For example, on
Windows, this would be the "Desktop" folder, while on DOS this
would be the A: through Z: drives.

**Returns:** an array of

File

objects representing all root partitions
on this system

- getHomeDirectory

```java
public
File
getHomeDirectory()
```

Returns the home directory.

**Returns:** the home directory

- getDefaultDirectory

```java
public
File
getDefaultDirectory()
```

Return the user's default starting directory for the file chooser.

**Returns:** a

File

object representing the default
starting folder
**Since:** 1.4

- createFileObject

```java
public
File
createFileObject​(
File
dir,

String
filename)
```

Returns a File object constructed in dir from the given filename.

**Parameters:** dir

- an abstract pathname denoting a directory
**Parameters:** filename

- a

String

representation of a pathname
**Returns:** a

File

object created from

dir

and

filename

- createFileObject

```java
public
File
createFileObject​(
String
path)
```

Returns a File object constructed from the given path string.

**Parameters:** path

-

String

representation of path
**Returns:** a

File

object created from the given

path

- getFiles

```java
public
File
[] getFiles​(
File
dir,
boolean useFileHiding)
```

Gets the list of shown (i.e. not hidden) files.

**Parameters:** dir

- the root directory of files to be returned
**Parameters:** useFileHiding

- determine if hidden files are returned
**Returns:** an array of

File

objects representing files and
directories in the given

dir

. It includes hidden
files if

useFileHiding

is false.

- getParentDirectory

```java
public
File
getParentDirectory​(
File
dir)
```

Returns the parent directory of

dir

.

**Parameters:** dir

- the

File

being queried
**Returns:** the parent directory of

dir

, or

null

if

dir

is

null

- getChooserComboBoxFiles

```java
public
File
[] getChooserComboBoxFiles()
```

Returns an array of files representing the values to show by default in
the file chooser selector.

**Returns:** an array of

File

objects.
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

- isLink

```java
public boolean isLink​(
File
file)
```

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

**Parameters:** file

- a file
**Returns:** whether this is a link
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9
**See Also:** getLinkLocation(File)

- getLinkLocation

```java
public
File
getLinkLocation​(
File
file)
throws
FileNotFoundException
```

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.
Returns

null

if the specified file is not
a shell interpreted link.

**Parameters:** file

- a file
**Returns:** the linked file or

null

.
**Throws:** FileNotFoundException

- if the linked file does not exist
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

- createFileSystemRoot

```java
protected
File
createFileSystemRoot​(
File
f)
```

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

**Parameters:** f

- a

File

object representing a file system root
directory, for example "/" on Unix or "C:\" on Windows.
**Returns:** a new

File

object
**Since:** 1.4

Constructor Detail

- FileSystemView

```java
public FileSystemView()
```

Constructs a FileSystemView.

---

#### Constructor Detail

FileSystemView

```java
public FileSystemView()
```

Constructs a FileSystemView.

---

#### FileSystemView

public FileSystemView()

Constructs a FileSystemView.

Method Detail

- getFileSystemView

```java
public static
FileSystemView
getFileSystemView()
```

Returns the file system view.

**Returns:** the file system view

- isRoot

```java
public boolean isRoot​(
File
f)
```

Determines if the given file is a root in the navigable tree(s).
Examples: Windows 98 has one root, the Desktop folder. DOS has one root
per drive letter,

C:\

,

D:\

, etc. Unix has one root,
the

"/"

directory.

The default implementation gets information from the

ShellFolder

class.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if

f

is a root in the navigable tree.
**See Also:** isFileSystemRoot(java.io.File)

- isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Returns true if the file (directory) can be visited.
Returns false if the directory cannot be traversed.

**Parameters:** f

- the

File
**Returns:** true

if the file/directory can be traversed, otherwise

false
**Since:** 1.4
**See Also:** JFileChooser.isTraversable(java.io.File)

,

FileView.isTraversable(java.io.File)

- getSystemDisplayName

```java
public
String
getSystemDisplayName​(
File
f)
```

Name of a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays as "CD-ROM (M:)"

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** the file name as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getName(java.io.File)

- getSystemTypeDescription

```java
public
String
getSystemTypeDescription​(
File
f)
```

Type description for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "Desktop" folder
is described as "Desktop".

Override for platforms with native ShellFolder implementations.

**Parameters:** f

- a

File

object
**Returns:** the file type description as it would be displayed by a native file chooser
or null if no native information is available.
**Since:** 1.4
**See Also:** JFileChooser.getTypeDescription(java.io.File)

- getSystemIcon

```java
public
Icon
getSystemIcon​(
File
f)
```

Icon for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays a CD-ROM icon.

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** an icon as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getIcon(java.io.File)

- isParent

```java
public boolean isParent​(
File
folder,

File
file)
```

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem. Folder could for example be the
"Desktop" folder which is not the same as file.getParentFile().

**Parameters:** folder

- a

File

object representing a directory or special folder
**Parameters:** file

- a

File

object
**Returns:** true

if

folder

is a directory or special folder and contains

file

.
**Since:** 1.4

- getChild

```java
public
File
getChild​(
File
parent,

String
fileName)
```

**Parameters:** parent

- a

File

object representing a directory or special folder
**Parameters:** fileName

- a name of a file or folder which exists in

parent
**Returns:** a File object. This is normally constructed with

new
File(parent, fileName)

except when parent and child are both
special folders, in which case the

File

is a wrapper containing
a

ShellFolder

object.
**Since:** 1.4

- isFileSystem

```java
public boolean isFileSystem​(
File
f)
```

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

. Used by UI classes to decide if
a folder is selectable when doing directory choosing.

**Parameters:** f

- a

File

object
**Returns:** true

if

f

is a real file or directory.
**Since:** 1.4

- createNewFolder

```java
public abstract
File
createNewFolder​(
File
containingDir)
throws
IOException
```

Creates a new folder with a default folder name.

**Parameters:** containingDir

- a

File

object denoting directory to contain the new folder
**Returns:** a

File

object denoting the newly created folder
**Throws:** IOException

- if new folder could not be created

- isHiddenFile

```java
public boolean isHiddenFile​(
File
f)
```

Returns whether a file is hidden or not.

**Parameters:** f

- a

File

object
**Returns:** true if the given

File

denotes a hidden file

- isFileSystemRoot

```java
public boolean isFileSystemRoot​(
File
dir)
```

Is dir the root of a tree in the file system, such as a drive
or partition. Example: Returns true for "C:\" on Windows 98.

**Parameters:** dir

- a

File

object representing a directory
**Returns:** true

if

f

is a root of a filesystem
**Since:** 1.4
**See Also:** isRoot(java.io.File)

- isDrive

```java
public boolean isDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- isFloppyDrive

```java
public boolean isFloppyDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a floppy disk. Implies isDrive(dir).

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- isComputerNode

```java
public boolean isComputerNode​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a computer node, e.g. "My Computer" or a network server.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

- getRoots

```java
public
File
[] getRoots()
```

Returns all root partitions on this system. For example, on
Windows, this would be the "Desktop" folder, while on DOS this
would be the A: through Z: drives.

**Returns:** an array of

File

objects representing all root partitions
on this system

- getHomeDirectory

```java
public
File
getHomeDirectory()
```

Returns the home directory.

**Returns:** the home directory

- getDefaultDirectory

```java
public
File
getDefaultDirectory()
```

Return the user's default starting directory for the file chooser.

**Returns:** a

File

object representing the default
starting folder
**Since:** 1.4

- createFileObject

```java
public
File
createFileObject​(
File
dir,

String
filename)
```

Returns a File object constructed in dir from the given filename.

**Parameters:** dir

- an abstract pathname denoting a directory
**Parameters:** filename

- a

String

representation of a pathname
**Returns:** a

File

object created from

dir

and

filename

- createFileObject

```java
public
File
createFileObject​(
String
path)
```

Returns a File object constructed from the given path string.

**Parameters:** path

-

String

representation of path
**Returns:** a

File

object created from the given

path

- getFiles

```java
public
File
[] getFiles​(
File
dir,
boolean useFileHiding)
```

Gets the list of shown (i.e. not hidden) files.

**Parameters:** dir

- the root directory of files to be returned
**Parameters:** useFileHiding

- determine if hidden files are returned
**Returns:** an array of

File

objects representing files and
directories in the given

dir

. It includes hidden
files if

useFileHiding

is false.

- getParentDirectory

```java
public
File
getParentDirectory​(
File
dir)
```

Returns the parent directory of

dir

.

**Parameters:** dir

- the

File

being queried
**Returns:** the parent directory of

dir

, or

null

if

dir

is

null

- getChooserComboBoxFiles

```java
public
File
[] getChooserComboBoxFiles()
```

Returns an array of files representing the values to show by default in
the file chooser selector.

**Returns:** an array of

File

objects.
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

- isLink

```java
public boolean isLink​(
File
file)
```

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

**Parameters:** file

- a file
**Returns:** whether this is a link
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9
**See Also:** getLinkLocation(File)

- getLinkLocation

```java
public
File
getLinkLocation​(
File
file)
throws
FileNotFoundException
```

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.
Returns

null

if the specified file is not
a shell interpreted link.

**Parameters:** file

- a file
**Returns:** the linked file or

null

.
**Throws:** FileNotFoundException

- if the linked file does not exist
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

- createFileSystemRoot

```java
protected
File
createFileSystemRoot​(
File
f)
```

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

**Parameters:** f

- a

File

object representing a file system root
directory, for example "/" on Unix or "C:\" on Windows.
**Returns:** a new

File

object
**Since:** 1.4

---

#### Method Detail

getFileSystemView

```java
public static
FileSystemView
getFileSystemView()
```

Returns the file system view.

**Returns:** the file system view

---

#### getFileSystemView

public static

FileSystemView

getFileSystemView()

Returns the file system view.

isRoot

```java
public boolean isRoot​(
File
f)
```

Determines if the given file is a root in the navigable tree(s).
Examples: Windows 98 has one root, the Desktop folder. DOS has one root
per drive letter,

C:\

,

D:\

, etc. Unix has one root,
the

"/"

directory.

The default implementation gets information from the

ShellFolder

class.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if

f

is a root in the navigable tree.
**See Also:** isFileSystemRoot(java.io.File)

---

#### isRoot

public boolean isRoot​(

File

f)

Determines if the given file is a root in the navigable tree(s).
Examples: Windows 98 has one root, the Desktop folder. DOS has one root
per drive letter,

C:\

,

D:\

, etc. Unix has one root,
the

"/"

directory.

The default implementation gets information from the

ShellFolder

class.

isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Returns true if the file (directory) can be visited.
Returns false if the directory cannot be traversed.

**Parameters:** f

- the

File
**Returns:** true

if the file/directory can be traversed, otherwise

false
**Since:** 1.4
**See Also:** JFileChooser.isTraversable(java.io.File)

,

FileView.isTraversable(java.io.File)

---

#### isTraversable

public

Boolean

isTraversable​(

File

f)

Returns true if the file (directory) can be visited.
Returns false if the directory cannot be traversed.

getSystemDisplayName

```java
public
String
getSystemDisplayName​(
File
f)
```

Name of a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays as "CD-ROM (M:)"

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** the file name as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getName(java.io.File)

---

#### getSystemDisplayName

public

String

getSystemDisplayName​(

File

f)

Name of a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays as "CD-ROM (M:)"

The default implementation gets information from the ShellFolder class.

getSystemTypeDescription

```java
public
String
getSystemTypeDescription​(
File
f)
```

Type description for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "Desktop" folder
is described as "Desktop".

Override for platforms with native ShellFolder implementations.

**Parameters:** f

- a

File

object
**Returns:** the file type description as it would be displayed by a native file chooser
or null if no native information is available.
**Since:** 1.4
**See Also:** JFileChooser.getTypeDescription(java.io.File)

---

#### getSystemTypeDescription

public

String

getSystemTypeDescription​(

File

f)

Type description for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "Desktop" folder
is described as "Desktop".

Override for platforms with native ShellFolder implementations.

getSystemIcon

```java
public
Icon
getSystemIcon​(
File
f)
```

Icon for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays a CD-ROM icon.

The default implementation gets information from the ShellFolder class.

**Parameters:** f

- a

File

object
**Returns:** an icon as it would be displayed by a native file chooser
**Since:** 1.4
**See Also:** JFileChooser.getIcon(java.io.File)

---

#### getSystemIcon

public

Icon

getSystemIcon​(

File

f)

Icon for a file, directory, or folder as it would be displayed in
a system file browser. Example from Windows: the "M:\" directory
displays a CD-ROM icon.

The default implementation gets information from the ShellFolder class.

isParent

```java
public boolean isParent​(
File
folder,

File
file)
```

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem. Folder could for example be the
"Desktop" folder which is not the same as file.getParentFile().

**Parameters:** folder

- a

File

object representing a directory or special folder
**Parameters:** file

- a

File

object
**Returns:** true

if

folder

is a directory or special folder and contains

file

.
**Since:** 1.4

---

#### isParent

public boolean isParent​(

File

folder,

File

file)

On Windows, a file can appear in multiple folders, other than its
parent directory in the filesystem. Folder could for example be the
"Desktop" folder which is not the same as file.getParentFile().

getChild

```java
public
File
getChild​(
File
parent,

String
fileName)
```

**Parameters:** parent

- a

File

object representing a directory or special folder
**Parameters:** fileName

- a name of a file or folder which exists in

parent
**Returns:** a File object. This is normally constructed with

new
File(parent, fileName)

except when parent and child are both
special folders, in which case the

File

is a wrapper containing
a

ShellFolder

object.
**Since:** 1.4

---

#### getChild

public

File

getChild​(

File

parent,

String

fileName)

isFileSystem

```java
public boolean isFileSystem​(
File
f)
```

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

. Used by UI classes to decide if
a folder is selectable when doing directory choosing.

**Parameters:** f

- a

File

object
**Returns:** true

if

f

is a real file or directory.
**Since:** 1.4

---

#### isFileSystem

public boolean isFileSystem​(

File

f)

Checks if

f

represents a real directory or file as opposed to a
special folder such as

"Desktop"

. Used by UI classes to decide if
a folder is selectable when doing directory choosing.

createNewFolder

```java
public abstract
File
createNewFolder​(
File
containingDir)
throws
IOException
```

Creates a new folder with a default folder name.

**Parameters:** containingDir

- a

File

object denoting directory to contain the new folder
**Returns:** a

File

object denoting the newly created folder
**Throws:** IOException

- if new folder could not be created

---

#### createNewFolder

public abstract

File

createNewFolder​(

File

containingDir)
throws

IOException

Creates a new folder with a default folder name.

isHiddenFile

```java
public boolean isHiddenFile​(
File
f)
```

Returns whether a file is hidden or not.

**Parameters:** f

- a

File

object
**Returns:** true if the given

File

denotes a hidden file

---

#### isHiddenFile

public boolean isHiddenFile​(

File

f)

Returns whether a file is hidden or not.

isFileSystemRoot

```java
public boolean isFileSystemRoot​(
File
dir)
```

Is dir the root of a tree in the file system, such as a drive
or partition. Example: Returns true for "C:\" on Windows 98.

**Parameters:** dir

- a

File

object representing a directory
**Returns:** true

if

f

is a root of a filesystem
**Since:** 1.4
**See Also:** isRoot(java.io.File)

---

#### isFileSystemRoot

public boolean isFileSystemRoot​(

File

dir)

Is dir the root of a tree in the file system, such as a drive
or partition. Example: Returns true for "C:\" on Windows 98.

isDrive

```java
public boolean isDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

---

#### isDrive

public boolean isDrive​(

File

dir)

Used by UI classes to decide whether to display a special icon
for drives or partitions, e.g. a "hard disk" icon.

The default implementation has no way of knowing, so always returns false.

isFloppyDrive

```java
public boolean isFloppyDrive​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a floppy disk. Implies isDrive(dir).

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

---

#### isFloppyDrive

public boolean isFloppyDrive​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a floppy disk. Implies isDrive(dir).

The default implementation has no way of knowing, so always returns false.

isComputerNode

```java
public boolean isComputerNode​(
File
dir)
```

Used by UI classes to decide whether to display a special icon
for a computer node, e.g. "My Computer" or a network server.

The default implementation has no way of knowing, so always returns false.

**Parameters:** dir

- a directory
**Returns:** false

always
**Since:** 1.4

---

#### isComputerNode

public boolean isComputerNode​(

File

dir)

Used by UI classes to decide whether to display a special icon
for a computer node, e.g. "My Computer" or a network server.

The default implementation has no way of knowing, so always returns false.

getRoots

```java
public
File
[] getRoots()
```

Returns all root partitions on this system. For example, on
Windows, this would be the "Desktop" folder, while on DOS this
would be the A: through Z: drives.

**Returns:** an array of

File

objects representing all root partitions
on this system

---

#### getRoots

public

File

[] getRoots()

Returns all root partitions on this system. For example, on
Windows, this would be the "Desktop" folder, while on DOS this
would be the A: through Z: drives.

getHomeDirectory

```java
public
File
getHomeDirectory()
```

Returns the home directory.

**Returns:** the home directory

---

#### getHomeDirectory

public

File

getHomeDirectory()

Returns the home directory.

getDefaultDirectory

```java
public
File
getDefaultDirectory()
```

Return the user's default starting directory for the file chooser.

**Returns:** a

File

object representing the default
starting folder
**Since:** 1.4

---

#### getDefaultDirectory

public

File

getDefaultDirectory()

Return the user's default starting directory for the file chooser.

createFileObject

```java
public
File
createFileObject​(
File
dir,

String
filename)
```

Returns a File object constructed in dir from the given filename.

**Parameters:** dir

- an abstract pathname denoting a directory
**Parameters:** filename

- a

String

representation of a pathname
**Returns:** a

File

object created from

dir

and

filename

---

#### createFileObject

public

File

createFileObject​(

File

dir,

String

filename)

Returns a File object constructed in dir from the given filename.

createFileObject

```java
public
File
createFileObject​(
String
path)
```

Returns a File object constructed from the given path string.

**Parameters:** path

-

String

representation of path
**Returns:** a

File

object created from the given

path

---

#### createFileObject

public

File

createFileObject​(

String

path)

Returns a File object constructed from the given path string.

getFiles

```java
public
File
[] getFiles​(
File
dir,
boolean useFileHiding)
```

Gets the list of shown (i.e. not hidden) files.

**Parameters:** dir

- the root directory of files to be returned
**Parameters:** useFileHiding

- determine if hidden files are returned
**Returns:** an array of

File

objects representing files and
directories in the given

dir

. It includes hidden
files if

useFileHiding

is false.

---

#### getFiles

public

File

[] getFiles​(

File

dir,
boolean useFileHiding)

Gets the list of shown (i.e. not hidden) files.

getParentDirectory

```java
public
File
getParentDirectory​(
File
dir)
```

Returns the parent directory of

dir

.

**Parameters:** dir

- the

File

being queried
**Returns:** the parent directory of

dir

, or

null

if

dir

is

null

---

#### getParentDirectory

public

File

getParentDirectory​(

File

dir)

Returns the parent directory of

dir

.

getChooserComboBoxFiles

```java
public
File
[] getChooserComboBoxFiles()
```

Returns an array of files representing the values to show by default in
the file chooser selector.

**Returns:** an array of

File

objects.
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

---

#### getChooserComboBoxFiles

public

File

[] getChooserComboBoxFiles()

Returns an array of files representing the values to show by default in
the file chooser selector.

isLink

```java
public boolean isLink​(
File
file)
```

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

**Parameters:** file

- a file
**Returns:** whether this is a link
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9
**See Also:** getLinkLocation(File)

---

#### isLink

public boolean isLink​(

File

file)

Returns whether the specified file denotes a shell interpreted link which
can be obtained by the

getLinkLocation(File)

.

getLinkLocation

```java
public
File
getLinkLocation​(
File
file)
throws
FileNotFoundException
```

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.
Returns

null

if the specified file is not
a shell interpreted link.

**Parameters:** file

- a file
**Returns:** the linked file or

null

.
**Throws:** FileNotFoundException

- if the linked file does not exist
**Throws:** NullPointerException

- if

file

equals

null
**Throws:** SecurityException

- if the caller does not have necessary
permissions
**Since:** 9

---

#### getLinkLocation

public

File

getLinkLocation​(

File

file)
throws

FileNotFoundException

Returns the regular file referenced by the specified link file if
the specified file is a shell interpreted link.
Returns

null

if the specified file is not
a shell interpreted link.

createFileSystemRoot

```java
protected
File
createFileSystemRoot​(
File
f)
```

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

**Parameters:** f

- a

File

object representing a file system root
directory, for example "/" on Unix or "C:\" on Windows.
**Returns:** a new

File

object
**Since:** 1.4

---

#### createFileSystemRoot

protected

File

createFileSystemRoot​(

File

f)

Creates a new

File

object for

f

with correct
behavior for a file system root directory.

---

