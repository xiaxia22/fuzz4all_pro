# Class FileView

**Source:** `java.desktop\javax\swing\filechooser\FileView.html`

### Class Description

```java
public abstract class
FileView

extends
Object
```

FileView

defines an abstract class that can be implemented
to provide the filechooser with UI information for a

File

.
Each L&F

JFileChooserUI

object implements this
class to pass back the correct icons and type descriptions specific to
that L&F. For example, the Microsoft Windows L&F returns the
generic Windows icons for directories and generic files.
Additionally, you may want to provide your own

FileView

to

JFileChooser

to return different icons or additional
information using

JFileChooser.setFileView(javax.swing.filechooser.FileView)

.

JFileChooser

first looks to see if there is a user defined

FileView

, if there is, it gets type information from
there first. If

FileView

returns

null

for
any method,

JFileChooser

then uses the L&F specific
view to get the information.
So, for example, if you provide a

FileView

class that
returns an

Icon

for JPG files, and returns

null

icons for all other files, the UI's

FileView

will provide
default icons for all other files.

For an example implementation of a simple file view, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileView.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

**Direct Known Subclasses:** BasicFileChooserUI.BasicFileView

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileView()

*No description found.*

---

### Method Details

#### public
String
getName​(
File
f)

The name of the file. Normally this would be simply

f.getName()

.

**Parameters:**
- f

- a

File

object

**Returns:**
- a

String

representing the name of the file

---

#### public
String
getDescription​(
File
f)

A human readable description of the file. For example,
a file named

jag.jpg

might have a description that read:
"A JPEG image file of James Gosling's face".

**Parameters:**
- f

- a

File

object

**Returns:**
- a

String

containing a description of the file or

null

if it is not available.

---

#### public
String
getTypeDescription​(
File
f)

A human readable description of the type of the file. For
example, a

jpg

file might have a type description of:
"A JPEG Compressed Image File"

**Parameters:**
- f

- a

File

object

**Returns:**
- a

String

containing a description of the type of the file
or

null

if it is not available .

---

#### public
Icon
getIcon​(
File
f)

The icon that represents this file in the

JFileChooser

.

**Parameters:**
- f

- a

File

object

**Returns:**
- an

Icon

which represents the specified

File

or

null

if it is not available.

---

#### public
Boolean
isTraversable​(
File
f)

Whether the directory is traversable or not. This might be
useful, for example, if you want a directory to represent
a compound document and don't want the user to descend into it.

**Parameters:**
- f

- a

File

object representing a directory

**Returns:**
- true

if the directory is traversable,

false

if it is not, and

null

if the
file system should be checked.

**See Also:**
- FileSystemView.isTraversable(java.io.File)

---

### Additional Sections

#### Class FileView

java.lang.Object

- javax.swing.filechooser.FileView

javax.swing.filechooser.FileView

**Direct Known Subclasses:** BasicFileChooserUI.BasicFileView

```java
public abstract class
FileView

extends
Object
```

FileView

defines an abstract class that can be implemented
to provide the filechooser with UI information for a

File

.
Each L&F

JFileChooserUI

object implements this
class to pass back the correct icons and type descriptions specific to
that L&F. For example, the Microsoft Windows L&F returns the
generic Windows icons for directories and generic files.
Additionally, you may want to provide your own

FileView

to

JFileChooser

to return different icons or additional
information using

JFileChooser.setFileView(javax.swing.filechooser.FileView)

.

JFileChooser

first looks to see if there is a user defined

FileView

, if there is, it gets type information from
there first. If

FileView

returns

null

for
any method,

JFileChooser

then uses the L&F specific
view to get the information.
So, for example, if you provide a

FileView

class that
returns an

Icon

for JPG files, and returns

null

icons for all other files, the UI's

FileView

will provide
default icons for all other files.

For an example implementation of a simple file view, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileView.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

**See Also:** JFileChooser

public abstract class

FileView

extends

Object

FileView

defines an abstract class that can be implemented
to provide the filechooser with UI information for a

File

.
Each L&F

JFileChooserUI

object implements this
class to pass back the correct icons and type descriptions specific to
that L&F. For example, the Microsoft Windows L&F returns the
generic Windows icons for directories and generic files.
Additionally, you may want to provide your own

FileView

to

JFileChooser

to return different icons or additional
information using

JFileChooser.setFileView(javax.swing.filechooser.FileView)

.

JFileChooser

first looks to see if there is a user defined

FileView

, if there is, it gets type information from
there first. If

FileView

returns

null

for
any method,

JFileChooser

then uses the L&F specific
view to get the information.
So, for example, if you provide a

FileView

class that
returns an

Icon

for JPG files, and returns

null

icons for all other files, the UI's

FileView

will provide
default icons for all other files.

For an example implementation of a simple file view, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileView.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

JFileChooser

first looks to see if there is a user defined

FileView

, if there is, it gets type information from
there first. If

FileView

returns

null

for
any method,

JFileChooser

then uses the L&F specific
view to get the information.
So, for example, if you provide a

FileView

class that
returns an

Icon

for JPG files, and returns

null

icons for all other files, the UI's

FileView

will provide
default icons for all other files.

For an example implementation of a simple file view, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileView.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

For an example implementation of a simple file view, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileView.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileView

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

​(

File

f)

A human readable description of the file.

Icon

getIcon

​(

File

f)

The icon that represents this file in the

JFileChooser

.

String

getName

​(

File

f)

The name of the file.

String

getTypeDescription

​(

File

f)

A human readable description of the type of the file.

Boolean

isTraversable

​(

File

f)

Whether the directory is traversable or not.

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

FileView

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescription

​(

File

f)

A human readable description of the file.

Icon

getIcon

​(

File

f)

The icon that represents this file in the

JFileChooser

.

String

getName

​(

File

f)

The name of the file.

String

getTypeDescription

​(

File

f)

A human readable description of the type of the file.

Boolean

isTraversable

​(

File

f)

Whether the directory is traversable or not.

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

A human readable description of the file.

The icon that represents this file in the

JFileChooser

.

The name of the file.

A human readable description of the type of the file.

Whether the directory is traversable or not.

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

- FileView

```java
public FileView()
```

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName​(
File
f)
```

The name of the file. Normally this would be simply

f.getName()

.

**Parameters:** f

- a

File

object
**Returns:** a

String

representing the name of the file

- getDescription

```java
public
String
getDescription​(
File
f)
```

A human readable description of the file. For example,
a file named

jag.jpg

might have a description that read:
"A JPEG image file of James Gosling's face".

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the file or

null

if it is not available.

- getTypeDescription

```java
public
String
getTypeDescription​(
File
f)
```

A human readable description of the type of the file. For
example, a

jpg

file might have a type description of:
"A JPEG Compressed Image File"

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the type of the file
or

null

if it is not available .

- getIcon

```java
public
Icon
getIcon​(
File
f)
```

The icon that represents this file in the

JFileChooser

.

**Parameters:** f

- a

File

object
**Returns:** an

Icon

which represents the specified

File

or

null

if it is not available.

- isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Whether the directory is traversable or not. This might be
useful, for example, if you want a directory to represent
a compound document and don't want the user to descend into it.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if the directory is traversable,

false

if it is not, and

null

if the
file system should be checked.
**See Also:** FileSystemView.isTraversable(java.io.File)

Constructor Detail

- FileView

```java
public FileView()
```

---

#### Constructor Detail

FileView

```java
public FileView()
```

---

#### FileView

public FileView()

Method Detail

- getName

```java
public
String
getName​(
File
f)
```

The name of the file. Normally this would be simply

f.getName()

.

**Parameters:** f

- a

File

object
**Returns:** a

String

representing the name of the file

- getDescription

```java
public
String
getDescription​(
File
f)
```

A human readable description of the file. For example,
a file named

jag.jpg

might have a description that read:
"A JPEG image file of James Gosling's face".

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the file or

null

if it is not available.

- getTypeDescription

```java
public
String
getTypeDescription​(
File
f)
```

A human readable description of the type of the file. For
example, a

jpg

file might have a type description of:
"A JPEG Compressed Image File"

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the type of the file
or

null

if it is not available .

- getIcon

```java
public
Icon
getIcon​(
File
f)
```

The icon that represents this file in the

JFileChooser

.

**Parameters:** f

- a

File

object
**Returns:** an

Icon

which represents the specified

File

or

null

if it is not available.

- isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Whether the directory is traversable or not. This might be
useful, for example, if you want a directory to represent
a compound document and don't want the user to descend into it.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if the directory is traversable,

false

if it is not, and

null

if the
file system should be checked.
**See Also:** FileSystemView.isTraversable(java.io.File)

---

#### Method Detail

getName

```java
public
String
getName​(
File
f)
```

The name of the file. Normally this would be simply

f.getName()

.

**Parameters:** f

- a

File

object
**Returns:** a

String

representing the name of the file

---

#### getName

public

String

getName​(

File

f)

The name of the file. Normally this would be simply

f.getName()

.

getDescription

```java
public
String
getDescription​(
File
f)
```

A human readable description of the file. For example,
a file named

jag.jpg

might have a description that read:
"A JPEG image file of James Gosling's face".

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the file or

null

if it is not available.

---

#### getDescription

public

String

getDescription​(

File

f)

A human readable description of the file. For example,
a file named

jag.jpg

might have a description that read:
"A JPEG image file of James Gosling's face".

getTypeDescription

```java
public
String
getTypeDescription​(
File
f)
```

A human readable description of the type of the file. For
example, a

jpg

file might have a type description of:
"A JPEG Compressed Image File"

**Parameters:** f

- a

File

object
**Returns:** a

String

containing a description of the type of the file
or

null

if it is not available .

---

#### getTypeDescription

public

String

getTypeDescription​(

File

f)

A human readable description of the type of the file. For
example, a

jpg

file might have a type description of:
"A JPEG Compressed Image File"

getIcon

```java
public
Icon
getIcon​(
File
f)
```

The icon that represents this file in the

JFileChooser

.

**Parameters:** f

- a

File

object
**Returns:** an

Icon

which represents the specified

File

or

null

if it is not available.

---

#### getIcon

public

Icon

getIcon​(

File

f)

The icon that represents this file in the

JFileChooser

.

isTraversable

```java
public
Boolean
isTraversable​(
File
f)
```

Whether the directory is traversable or not. This might be
useful, for example, if you want a directory to represent
a compound document and don't want the user to descend into it.

**Parameters:** f

- a

File

object representing a directory
**Returns:** true

if the directory is traversable,

false

if it is not, and

null

if the
file system should be checked.
**See Also:** FileSystemView.isTraversable(java.io.File)

---

#### isTraversable

public

Boolean

isTraversable​(

File

f)

Whether the directory is traversable or not. This might be
useful, for example, if you want a directory to represent
a compound document and don't want the user to descend into it.

---

