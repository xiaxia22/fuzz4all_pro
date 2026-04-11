# Interface DosFileAttributes

**Source:** `java.base\java\nio\file\attribute\DosFileAttributes.html`

### Class Description

```java
public interface
DosFileAttributes

extends
BasicFileAttributes
```

File attributes associated with a file in a file system that supports
legacy "DOS" attributes.

Usage Example:

```java
Path file = ...
DosFileAttributes attrs = Files.readAttributes(file, DosFileAttributes.class);
```

**All Superinterfaces:** BasicFileAttributes

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isReadOnly()

Returns the value of the read-only attribute.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

**Returns:**
- the value of the read-only attribute

---

#### boolean isHidden()

Returns the value of the hidden attribute.

This attribute is often used to indicate if the file is visible to
users.

**Returns:**
- the value of the hidden attribute

---

#### boolean isArchive()

Returns the value of the archive attribute.

This attribute is typically used by backup programs.

**Returns:**
- the value of the archive attribute

---

#### boolean isSystem()

Returns the value of the system attribute.

This attribute is often used to indicate that the file is a component
of the operating system.

**Returns:**
- the value of the system attribute

---

### Additional Sections

#### Interface DosFileAttributes

**All Superinterfaces:** BasicFileAttributes

```java
public interface
DosFileAttributes

extends
BasicFileAttributes
```

File attributes associated with a file in a file system that supports
legacy "DOS" attributes.

Usage Example:

```java
Path file = ...
DosFileAttributes attrs = Files.readAttributes(file, DosFileAttributes.class);
```

**Since:** 1.7

public interface

DosFileAttributes

extends

BasicFileAttributes

File attributes associated with a file in a file system that supports
legacy "DOS" attributes.

Usage Example:

```java
Path file = ...
DosFileAttributes attrs = Files.readAttributes(file, DosFileAttributes.class);
```

Usage Example:

```java
Path file = ...
DosFileAttributes attrs = Files.readAttributes(file, DosFileAttributes.class);
```

Path file = ...
DosFileAttributes attrs = Files.readAttributes(file, DosFileAttributes.class);

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isArchive

()

Returns the value of the archive attribute.

boolean

isHidden

()

Returns the value of the hidden attribute.

boolean

isReadOnly

()

Returns the value of the read-only attribute.

boolean

isSystem

()

Returns the value of the system attribute.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isArchive

()

Returns the value of the archive attribute.

boolean

isHidden

()

Returns the value of the hidden attribute.

boolean

isReadOnly

()

Returns the value of the read-only attribute.

boolean

isSystem

()

Returns the value of the system attribute.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

---

#### Method Summary

Returns the value of the archive attribute.

Returns the value of the hidden attribute.

Returns the value of the read-only attribute.

Returns the value of the system attribute.

Methods declared in interface java.nio.file.attribute.

BasicFileAttributes

creationTime

,

fileKey

,

isDirectory

,

isOther

,

isRegularFile

,

isSymbolicLink

,

lastAccessTime

,

lastModifiedTime

,

size

---

#### Methods declared in interface java.nio.file.attribute. BasicFileAttributes

============ METHOD DETAIL ==========

- Method Detail

- isReadOnly

```java
boolean isReadOnly()
```

Returns the value of the read-only attribute.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

**Returns:** the value of the read-only attribute

- isHidden

```java
boolean isHidden()
```

Returns the value of the hidden attribute.

This attribute is often used to indicate if the file is visible to
users.

**Returns:** the value of the hidden attribute

- isArchive

```java
boolean isArchive()
```

Returns the value of the archive attribute.

This attribute is typically used by backup programs.

**Returns:** the value of the archive attribute

- isSystem

```java
boolean isSystem()
```

Returns the value of the system attribute.

This attribute is often used to indicate that the file is a component
of the operating system.

**Returns:** the value of the system attribute

Method Detail

- isReadOnly

```java
boolean isReadOnly()
```

Returns the value of the read-only attribute.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

**Returns:** the value of the read-only attribute

- isHidden

```java
boolean isHidden()
```

Returns the value of the hidden attribute.

This attribute is often used to indicate if the file is visible to
users.

**Returns:** the value of the hidden attribute

- isArchive

```java
boolean isArchive()
```

Returns the value of the archive attribute.

This attribute is typically used by backup programs.

**Returns:** the value of the archive attribute

- isSystem

```java
boolean isSystem()
```

Returns the value of the system attribute.

This attribute is often used to indicate that the file is a component
of the operating system.

**Returns:** the value of the system attribute

---

#### Method Detail

isReadOnly

```java
boolean isReadOnly()
```

Returns the value of the read-only attribute.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

**Returns:** the value of the read-only attribute

---

#### isReadOnly

boolean isReadOnly()

Returns the value of the read-only attribute.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

This attribute is often used as a simple access control mechanism
to prevent files from being deleted or updated. Whether the file system
or platform does any enforcement to prevent

read-only

files
from being updated is implementation specific.

isHidden

```java
boolean isHidden()
```

Returns the value of the hidden attribute.

This attribute is often used to indicate if the file is visible to
users.

**Returns:** the value of the hidden attribute

---

#### isHidden

boolean isHidden()

Returns the value of the hidden attribute.

This attribute is often used to indicate if the file is visible to
users.

This attribute is often used to indicate if the file is visible to
users.

isArchive

```java
boolean isArchive()
```

Returns the value of the archive attribute.

This attribute is typically used by backup programs.

**Returns:** the value of the archive attribute

---

#### isArchive

boolean isArchive()

Returns the value of the archive attribute.

This attribute is typically used by backup programs.

This attribute is typically used by backup programs.

isSystem

```java
boolean isSystem()
```

Returns the value of the system attribute.

This attribute is often used to indicate that the file is a component
of the operating system.

**Returns:** the value of the system attribute

---

#### isSystem

boolean isSystem()

Returns the value of the system attribute.

This attribute is often used to indicate that the file is a component
of the operating system.

This attribute is often used to indicate that the file is a component
of the operating system.

---

