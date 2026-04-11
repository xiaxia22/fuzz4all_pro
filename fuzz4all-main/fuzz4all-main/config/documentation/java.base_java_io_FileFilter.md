# Interface FileFilter

**Source:** `java.base\java\io\FileFilter.html`

### Class Description

```java
@FunctionalInterface

public interface
FileFilter
```

A filter for abstract pathnames.

Instances of this interface may be passed to the

listFiles(FileFilter)

method
of the

File

class.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean accept​(
File
pathname)

Tests whether or not the specified abstract pathname should be
included in a pathname list.

**Parameters:**
- pathname

- The abstract pathname to be tested

**Returns:**
- true

if and only if

pathname

should be included

---

### Additional Sections

#### Interface FileFilter

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
FileFilter
```

A filter for abstract pathnames.

Instances of this interface may be passed to the

listFiles(FileFilter)

method
of the

File

class.

**Since:** 1.2

@FunctionalInterface

public interface

FileFilter

A filter for abstract pathnames.

Instances of this interface may be passed to the

listFiles(FileFilter)

method
of the

File

class.

Instances of this interface may be passed to the

listFiles(FileFilter)

method
of the

File

class.

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

pathname)

Tests whether or not the specified abstract pathname should be
included in a pathname list.

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

pathname)

Tests whether or not the specified abstract pathname should be
included in a pathname list.

---

#### Method Summary

Tests whether or not the specified abstract pathname should be
included in a pathname list.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
boolean accept​(
File
pathname)
```

Tests whether or not the specified abstract pathname should be
included in a pathname list.

**Parameters:** pathname

- The abstract pathname to be tested
**Returns:** true

if and only if

pathname

should be included

Method Detail

- accept

```java
boolean accept​(
File
pathname)
```

Tests whether or not the specified abstract pathname should be
included in a pathname list.

**Parameters:** pathname

- The abstract pathname to be tested
**Returns:** true

if and only if

pathname

should be included

---

#### Method Detail

accept

```java
boolean accept​(
File
pathname)
```

Tests whether or not the specified abstract pathname should be
included in a pathname list.

**Parameters:** pathname

- The abstract pathname to be tested
**Returns:** true

if and only if

pathname

should be included

---

#### accept

boolean accept​(

File

pathname)

Tests whether or not the specified abstract pathname should be
included in a pathname list.

---

