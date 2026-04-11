# Class FileNameExtensionFilter

**Source:** `java.desktop\javax\swing\filechooser\FileNameExtensionFilter.html`

### Class Description

```java
public final class
FileNameExtensionFilter

extends
FileFilter
```

An implementation of

FileFilter

that filters using a
specified set of extensions. The extension for a file is the
portion of the file name after the last ".". Files whose name does
not contain a "." have no file name extension. File name extension
comparisons are case insensitive.

The following example creates a

FileNameExtensionFilter

that will show

jpg

files:

```java
FileFilter filter = new FileNameExtensionFilter("JPEG file", "jpg", "jpeg");
JFileChooser fileChooser = ...;
fileChooser.addChoosableFileFilter(filter);
```

**Since:** 1.6
**See Also:** FileFilter

,

JFileChooser.setFileFilter(javax.swing.filechooser.FileFilter)

,

JFileChooser.addChoosableFileFilter(javax.swing.filechooser.FileFilter)

,

JFileChooser.getFileFilter()

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileNameExtensionFilter​(
String
description,

String
... extensions)

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions. The returned

FileNameExtensionFilter

will accept all directories and any
file with a file name extension contained in

extensions

.

**Parameters:**
- description

- textual description for the filter, may be

null
- extensions

- the accepted file name extensions

**Throws:**
- IllegalArgumentException

- if extensions is

null

, empty,
contains

null

, or contains an empty string

**See Also:**
- accept(java.io.File)

---

### Method Details

#### public boolean accept​(
File
f)

Tests the specified file, returning true if the file is
accepted, false otherwise. True is returned if the extension
matches one of the file name extensions of this

FileFilter

, or the file is a directory.

**Specified by:**
- accept

in class

FileFilter

**Parameters:**
- f

- the

File

to test

**Returns:**
- true if the file is to be accepted, false otherwise

---

#### public
String
getDescription()

The description of this filter. For example: "JPG and GIF Images."

**Specified by:**
- getDescription

in class

FileFilter

**Returns:**
- the description of this filter

**See Also:**
- FileView.getName(java.io.File)

---

#### public
String
[] getExtensions()

Returns the set of file name extensions files are tested against.

**Returns:**
- the set of file name extensions files are tested against

---

#### public
String
toString()

Returns a string representation of the

FileNameExtensionFilter

.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

FileNameExtensionFilter

---

### Additional Sections

#### Class FileNameExtensionFilter

java.lang.Object

- javax.swing.filechooser.FileFilter
- - javax.swing.filechooser.FileNameExtensionFilter

javax.swing.filechooser.FileFilter

- javax.swing.filechooser.FileNameExtensionFilter

javax.swing.filechooser.FileNameExtensionFilter

```java
public final class
FileNameExtensionFilter

extends
FileFilter
```

An implementation of

FileFilter

that filters using a
specified set of extensions. The extension for a file is the
portion of the file name after the last ".". Files whose name does
not contain a "." have no file name extension. File name extension
comparisons are case insensitive.

The following example creates a

FileNameExtensionFilter

that will show

jpg

files:

```java
FileFilter filter = new FileNameExtensionFilter("JPEG file", "jpg", "jpeg");
JFileChooser fileChooser = ...;
fileChooser.addChoosableFileFilter(filter);
```

**Since:** 1.6
**See Also:** FileFilter

,

JFileChooser.setFileFilter(javax.swing.filechooser.FileFilter)

,

JFileChooser.addChoosableFileFilter(javax.swing.filechooser.FileFilter)

,

JFileChooser.getFileFilter()

public final class

FileNameExtensionFilter

extends

FileFilter

An implementation of

FileFilter

that filters using a
specified set of extensions. The extension for a file is the
portion of the file name after the last ".". Files whose name does
not contain a "." have no file name extension. File name extension
comparisons are case insensitive.

The following example creates a

FileNameExtensionFilter

that will show

jpg

files:

```java
FileFilter filter = new FileNameExtensionFilter("JPEG file", "jpg", "jpeg");
JFileChooser fileChooser = ...;
fileChooser.addChoosableFileFilter(filter);
```

The following example creates a

FileNameExtensionFilter

that will show

jpg

files:

```java
FileFilter filter = new FileNameExtensionFilter("JPEG file", "jpg", "jpeg");
JFileChooser fileChooser = ...;
fileChooser.addChoosableFileFilter(filter);
```

FileFilter filter = new FileNameExtensionFilter("JPEG file", "jpg", "jpeg");
JFileChooser fileChooser = ...;
fileChooser.addChoosableFileFilter(filter);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileNameExtensionFilter

​(

String

description,

String

... extensions)

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

accept

​(

File

f)

Tests the specified file, returning true if the file is
accepted, false otherwise.

String

getDescription

()

The description of this filter.

String

[]

getExtensions

()

Returns the set of file name extensions files are tested against.

String

toString

()

Returns a string representation of the

FileNameExtensionFilter

.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

FileNameExtensionFilter

​(

String

description,

String

... extensions)

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions.

---

#### Constructor Summary

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

accept

​(

File

f)

Tests the specified file, returning true if the file is
accepted, false otherwise.

String

getDescription

()

The description of this filter.

String

[]

getExtensions

()

Returns the set of file name extensions files are tested against.

String

toString

()

Returns a string representation of the

FileNameExtensionFilter

.

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

wait

,

wait

,

wait

---

#### Method Summary

Tests the specified file, returning true if the file is
accepted, false otherwise.

The description of this filter.

Returns the set of file name extensions files are tested against.

Returns a string representation of the

FileNameExtensionFilter

.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FileNameExtensionFilter

```java
public FileNameExtensionFilter​(
String
description,

String
... extensions)
```

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions. The returned

FileNameExtensionFilter

will accept all directories and any
file with a file name extension contained in

extensions

.

**Parameters:** description

- textual description for the filter, may be

null
**Parameters:** extensions

- the accepted file name extensions
**Throws:** IllegalArgumentException

- if extensions is

null

, empty,
contains

null

, or contains an empty string
**See Also:** accept(java.io.File)

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
public boolean accept​(
File
f)
```

Tests the specified file, returning true if the file is
accepted, false otherwise. True is returned if the extension
matches one of the file name extensions of this

FileFilter

, or the file is a directory.

**Specified by:** accept

in class

FileFilter
**Parameters:** f

- the

File

to test
**Returns:** true if the file is to be accepted, false otherwise

- getDescription

```java
public
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images."

**Specified by:** getDescription

in class

FileFilter
**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

- getExtensions

```java
public
String
[] getExtensions()
```

Returns the set of file name extensions files are tested against.

**Returns:** the set of file name extensions files are tested against

- toString

```java
public
String
toString()
```

Returns a string representation of the

FileNameExtensionFilter

.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

FileNameExtensionFilter

Constructor Detail

- FileNameExtensionFilter

```java
public FileNameExtensionFilter​(
String
description,

String
... extensions)
```

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions. The returned

FileNameExtensionFilter

will accept all directories and any
file with a file name extension contained in

extensions

.

**Parameters:** description

- textual description for the filter, may be

null
**Parameters:** extensions

- the accepted file name extensions
**Throws:** IllegalArgumentException

- if extensions is

null

, empty,
contains

null

, or contains an empty string
**See Also:** accept(java.io.File)

---

#### Constructor Detail

FileNameExtensionFilter

```java
public FileNameExtensionFilter​(
String
description,

String
... extensions)
```

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions. The returned

FileNameExtensionFilter

will accept all directories and any
file with a file name extension contained in

extensions

.

**Parameters:** description

- textual description for the filter, may be

null
**Parameters:** extensions

- the accepted file name extensions
**Throws:** IllegalArgumentException

- if extensions is

null

, empty,
contains

null

, or contains an empty string
**See Also:** accept(java.io.File)

---

#### FileNameExtensionFilter

public FileNameExtensionFilter​(

String

description,

String

... extensions)

Creates a

FileNameExtensionFilter

with the specified
description and file name extensions. The returned

FileNameExtensionFilter

will accept all directories and any
file with a file name extension contained in

extensions

.

Method Detail

- accept

```java
public boolean accept​(
File
f)
```

Tests the specified file, returning true if the file is
accepted, false otherwise. True is returned if the extension
matches one of the file name extensions of this

FileFilter

, or the file is a directory.

**Specified by:** accept

in class

FileFilter
**Parameters:** f

- the

File

to test
**Returns:** true if the file is to be accepted, false otherwise

- getDescription

```java
public
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images."

**Specified by:** getDescription

in class

FileFilter
**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

- getExtensions

```java
public
String
[] getExtensions()
```

Returns the set of file name extensions files are tested against.

**Returns:** the set of file name extensions files are tested against

- toString

```java
public
String
toString()
```

Returns a string representation of the

FileNameExtensionFilter

.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

FileNameExtensionFilter

---

#### Method Detail

accept

```java
public boolean accept​(
File
f)
```

Tests the specified file, returning true if the file is
accepted, false otherwise. True is returned if the extension
matches one of the file name extensions of this

FileFilter

, or the file is a directory.

**Specified by:** accept

in class

FileFilter
**Parameters:** f

- the

File

to test
**Returns:** true if the file is to be accepted, false otherwise

---

#### accept

public boolean accept​(

File

f)

Tests the specified file, returning true if the file is
accepted, false otherwise. True is returned if the extension
matches one of the file name extensions of this

FileFilter

, or the file is a directory.

getDescription

```java
public
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images."

**Specified by:** getDescription

in class

FileFilter
**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

---

#### getDescription

public

String

getDescription()

The description of this filter. For example: "JPG and GIF Images."

getExtensions

```java
public
String
[] getExtensions()
```

Returns the set of file name extensions files are tested against.

**Returns:** the set of file name extensions files are tested against

---

#### getExtensions

public

String

[] getExtensions()

Returns the set of file name extensions files are tested against.

toString

```java
public
String
toString()
```

Returns a string representation of the

FileNameExtensionFilter

.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

FileNameExtensionFilter

---

#### toString

public

String

toString()

Returns a string representation of the

FileNameExtensionFilter

.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

---

