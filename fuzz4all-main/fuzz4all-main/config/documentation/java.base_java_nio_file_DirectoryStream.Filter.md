# Interface DirectoryStream.Filter<T>

**Source:** `java.base\java\nio\file\DirectoryStream.Filter.html`

### Class Description

```java
@FunctionalInterface

public static interface
DirectoryStream.Filter<T>
```

An interface that is implemented by objects that decide if a directory
entry should be accepted or filtered. A

Filter

is passed as the
parameter to the

Files.newDirectoryStream(Path,DirectoryStream.Filter)

method when opening a directory to iterate over the entries in the
directory.

**Type Parameters:** T

- the type of the directory entry

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean accept​(
T
entry)
throws
IOException

Decides if the given directory entry should be accepted or filtered.

**Parameters:**
- entry

- the directory entry to be tested

**Returns:**
- true

if the directory entry should be accepted

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Interface DirectoryStream.Filter<T>

**Type Parameters:** T

- the type of the directory entry

**Enclosing interface:** DirectoryStream

<

T

>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public static interface
DirectoryStream.Filter<T>
```

An interface that is implemented by objects that decide if a directory
entry should be accepted or filtered. A

Filter

is passed as the
parameter to the

Files.newDirectoryStream(Path,DirectoryStream.Filter)

method when opening a directory to iterate over the entries in the
directory.

**Since:** 1.7

@FunctionalInterface

public static interface

DirectoryStream.Filter<T>

An interface that is implemented by objects that decide if a directory
entry should be accepted or filtered. A

Filter

is passed as the
parameter to the

Files.newDirectoryStream(Path,DirectoryStream.Filter)

method when opening a directory to iterate over the entries in the
directory.

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

T

entry)

Decides if the given directory entry should be accepted or filtered.

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

T

entry)

Decides if the given directory entry should be accepted or filtered.

---

#### Method Summary

Decides if the given directory entry should be accepted or filtered.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
boolean accept​(
T
entry)
throws
IOException
```

Decides if the given directory entry should be accepted or filtered.

**Parameters:** entry

- the directory entry to be tested
**Returns:** true

if the directory entry should be accepted
**Throws:** IOException

- If an I/O error occurs

Method Detail

- accept

```java
boolean accept​(
T
entry)
throws
IOException
```

Decides if the given directory entry should be accepted or filtered.

**Parameters:** entry

- the directory entry to be tested
**Returns:** true

if the directory entry should be accepted
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

accept

```java
boolean accept​(
T
entry)
throws
IOException
```

Decides if the given directory entry should be accepted or filtered.

**Parameters:** entry

- the directory entry to be tested
**Returns:** true

if the directory entry should be accepted
**Throws:** IOException

- If an I/O error occurs

---

#### accept

boolean accept​(

T

entry)
throws

IOException

Decides if the given directory entry should be accepted or filtered.

---

