# Interface FilenameFilter

**Source:** `java.base\java\io\FilenameFilter.html`

### Class Description

```java
@FunctionalInterface

public interface
FilenameFilter
```

Instances of classes that implement this interface are used to
filter filenames. These instances are used to filter directory
listings in the

list

method of class

File

, and by the Abstract Window Toolkit's file
dialog component.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean accept​(
File
dir,

String
name)

Tests if a specified file should be included in a file list.

**Parameters:**
- dir

- the directory in which the file was found.
- name

- the name of the file.

**Returns:**
- true

if and only if the name should be
included in the file list;

false

otherwise.

---

### Additional Sections

#### Interface FilenameFilter

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
FilenameFilter
```

Instances of classes that implement this interface are used to
filter filenames. These instances are used to filter directory
listings in the

list

method of class

File

, and by the Abstract Window Toolkit's file
dialog component.

**Since:** 1.0
**See Also:** FileDialog.setFilenameFilter(java.io.FilenameFilter)

,

File

,

File.list(java.io.FilenameFilter)

@FunctionalInterface

public interface

FilenameFilter

Instances of classes that implement this interface are used to
filter filenames. These instances are used to filter directory
listings in the

list

method of class

File

, and by the Abstract Window Toolkit's file
dialog component.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

accept

​(

File

dir,

String

name)

Tests if a specified file should be included in a file list.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

accept

​(

File

dir,

String

name)

Tests if a specified file should be included in a file list.

---

#### Method Summary

Tests if a specified file should be included in a file list.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
boolean accept​(
File
dir,

String
name)
```

Tests if a specified file should be included in a file list.

**Parameters:** dir

- the directory in which the file was found.
**Parameters:** name

- the name of the file.
**Returns:** true

if and only if the name should be
included in the file list;

false

otherwise.

Method Detail

- accept

```java
boolean accept​(
File
dir,

String
name)
```

Tests if a specified file should be included in a file list.

**Parameters:** dir

- the directory in which the file was found.
**Parameters:** name

- the name of the file.
**Returns:** true

if and only if the name should be
included in the file list;

false

otherwise.

---

#### Method Detail

accept

```java
boolean accept​(
File
dir,

String
name)
```

Tests if a specified file should be included in a file list.

**Parameters:** dir

- the directory in which the file was found.
**Parameters:** name

- the name of the file.
**Returns:** true

if and only if the name should be
included in the file list;

false

otherwise.

---

#### accept

boolean accept​(

File

dir,

String

name)

Tests if a specified file should be included in a file list.

---

