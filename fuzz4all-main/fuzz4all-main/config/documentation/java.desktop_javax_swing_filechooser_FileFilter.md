# Class FileFilter

**Source:** `java.desktop\javax\swing\filechooser\FileFilter.html`

### Class Description

```java
public abstract class
FileFilter

extends
Object
```

FileFilter

is an abstract class used by

JFileChooser

for filtering the set of files shown to the user. See

FileNameExtensionFilter

for an implementation that filters using
the file name extension.

A

FileFilter

can be set on a

JFileChooser

to
keep unwanted files from appearing in the directory listing.
For an example implementation of a simple file filter, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileFilter.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

**Direct Known Subclasses:** BasicFileChooserUI.AcceptAllFileFilter

,

FileNameExtensionFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileFilter()

*No description found.*

---

### Method Details

#### public abstract boolean accept​(
File
f)

Whether the given file is accepted by this filter.

**Parameters:**
- f

- the File to test

**Returns:**
- true if the file is to be accepted

---

#### public abstract
String
getDescription()

The description of this filter. For example: "JPG and GIF Images"

**Returns:**
- the description of this filter

**See Also:**
- FileView.getName(java.io.File)

---

### Additional Sections

#### Class FileFilter

java.lang.Object

- javax.swing.filechooser.FileFilter

javax.swing.filechooser.FileFilter

**Direct Known Subclasses:** BasicFileChooserUI.AcceptAllFileFilter

,

FileNameExtensionFilter

```java
public abstract class
FileFilter

extends
Object
```

FileFilter

is an abstract class used by

JFileChooser

for filtering the set of files shown to the user. See

FileNameExtensionFilter

for an implementation that filters using
the file name extension.

A

FileFilter

can be set on a

JFileChooser

to
keep unwanted files from appearing in the directory listing.
For an example implementation of a simple file filter, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileFilter.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

**See Also:** FileNameExtensionFilter

,

JFileChooser.setFileFilter(javax.swing.filechooser.FileFilter)

,

JFileChooser.addChoosableFileFilter(javax.swing.filechooser.FileFilter)

public abstract class

FileFilter

extends

Object

FileFilter

is an abstract class used by

JFileChooser

for filtering the set of files shown to the user. See

FileNameExtensionFilter

for an implementation that filters using
the file name extension.

A

FileFilter

can be set on a

JFileChooser

to
keep unwanted files from appearing in the directory listing.
For an example implementation of a simple file filter, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileFilter.java

.
For more information and examples see

How to Use File Choosers

,
a section in

The Java Tutorial

.

A

FileFilter

can be set on a

JFileChooser

to
keep unwanted files from appearing in the directory listing.
For an example implementation of a simple file filter, see

yourJDK

/demo/jfc/FileChooserDemo/ExampleFileFilter.java

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

FileFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

accept

​(

File

f)

Whether the given file is accepted by this filter.

abstract

String

getDescription

()

The description of this filter.

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

FileFilter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

accept

​(

File

f)

Whether the given file is accepted by this filter.

abstract

String

getDescription

()

The description of this filter.

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

Whether the given file is accepted by this filter.

The description of this filter.

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

- FileFilter

```java
public FileFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
public abstract boolean accept​(
File
f)
```

Whether the given file is accepted by this filter.

**Parameters:** f

- the File to test
**Returns:** true if the file is to be accepted

- getDescription

```java
public abstract
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images"

**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

Constructor Detail

- FileFilter

```java
public FileFilter()
```

---

#### Constructor Detail

FileFilter

```java
public FileFilter()
```

---

#### FileFilter

public FileFilter()

Method Detail

- accept

```java
public abstract boolean accept​(
File
f)
```

Whether the given file is accepted by this filter.

**Parameters:** f

- the File to test
**Returns:** true if the file is to be accepted

- getDescription

```java
public abstract
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images"

**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

---

#### Method Detail

accept

```java
public abstract boolean accept​(
File
f)
```

Whether the given file is accepted by this filter.

**Parameters:** f

- the File to test
**Returns:** true if the file is to be accepted

---

#### accept

public abstract boolean accept​(

File

f)

Whether the given file is accepted by this filter.

getDescription

```java
public abstract
String
getDescription()
```

The description of this filter. For example: "JPG and GIF Images"

**Returns:** the description of this filter
**See Also:** FileView.getName(java.io.File)

---

#### getDescription

public abstract

String

getDescription()

The description of this filter. For example: "JPG and GIF Images"

---

