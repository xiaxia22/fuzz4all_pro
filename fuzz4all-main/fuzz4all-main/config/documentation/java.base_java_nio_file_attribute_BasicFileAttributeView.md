# Interface BasicFileAttributeView

**Source:** `java.base\java\nio\file\attribute\BasicFileAttributeView.html`

### Class Description

```java
public interface
BasicFileAttributeView

extends
FileAttributeView
```

A file attribute view that provides a view of a

basic set

of file
attributes common to many file systems. The basic set of file attributes
consist of

mandatory

and

optional

file attributes as
defined by the

BasicFileAttributes

interface.

The file attributes are retrieved from the file system as a

bulk
operation

by invoking the

readAttributes

method.
This class also defines the

setTimes

method to update the
file's time attributes.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view have the following names and types:

Supported attributes

Name

Type

"lastModifiedTime"

FileTime

"lastAccessTime"

FileTime

"creationTime"

FileTime

"size"

Long

"isRegularFile"

Boolean

"isDirectory"

Boolean

"isSymbolicLink"

Boolean

"isOther"

Boolean

"fileKey"

Object

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

**All Superinterfaces:** AttributeView

,

FileAttributeView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of the attribute view. Attribute views of this type
have the name

"basic"

.

**Specified by:**
- name

in interface

AttributeView

**Returns:**
- the name of the attribute view

---

#### BasicFileAttributes
readAttributes()
throws
IOException

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Returns:**
- the file attributes

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

---

#### void setTimes​(
FileTime
lastModifiedTime,

FileTime
lastAccessTime,

FileTime
createTime)
throws
IOException

Updates any or all of the file's last modified time, last access time,
and create time attributes.

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

**Parameters:**
- lastModifiedTime

- the new last modified time, or

null

to not change the
value
- lastAccessTime

- the last access time, or

null

to not change the value
- createTime

- the file's create time, or

null

to not change the value

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default provider, a security manager is
installed, its

checkWrite

method is invoked to check write access to the file

**See Also:**
- Files.setLastModifiedTime(java.nio.file.Path, java.nio.file.attribute.FileTime)

---

### Additional Sections

#### Interface BasicFileAttributeView

**All Superinterfaces:** AttributeView

,

FileAttributeView

**All Known Subinterfaces:** DosFileAttributeView

,

PosixFileAttributeView

```java
public interface
BasicFileAttributeView

extends
FileAttributeView
```

A file attribute view that provides a view of a

basic set

of file
attributes common to many file systems. The basic set of file attributes
consist of

mandatory

and

optional

file attributes as
defined by the

BasicFileAttributes

interface.

The file attributes are retrieved from the file system as a

bulk
operation

by invoking the

readAttributes

method.
This class also defines the

setTimes

method to update the
file's time attributes.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view have the following names and types:

Supported attributes

Name

Type

"lastModifiedTime"

FileTime

"lastAccessTime"

FileTime

"creationTime"

FileTime

"size"

Long

"isRegularFile"

Boolean

"isDirectory"

Boolean

"isSymbolicLink"

Boolean

"isOther"

Boolean

"fileKey"

Object

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

**Since:** 1.7

public interface

BasicFileAttributeView

extends

FileAttributeView

A file attribute view that provides a view of a

basic set

of file
attributes common to many file systems. The basic set of file attributes
consist of

mandatory

and

optional

file attributes as
defined by the

BasicFileAttributes

interface.

The file attributes are retrieved from the file system as a

bulk
operation

by invoking the

readAttributes

method.
This class also defines the

setTimes

method to update the
file's time attributes.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view have the following names and types:

Supported attributes

Name

Type

"lastModifiedTime"

FileTime

"lastAccessTime"

FileTime

"creationTime"

FileTime

"size"

Long

"isRegularFile"

Boolean

"isDirectory"

Boolean

"isSymbolicLink"

Boolean

"isOther"

Boolean

"fileKey"

Object

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

The file attributes are retrieved from the file system as a

bulk
operation

by invoking the

readAttributes

method.
This class also defines the

setTimes

method to update the
file's time attributes.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view have the following names and types:

Supported attributes

Name

Type

"lastModifiedTime"

FileTime

"lastAccessTime"

FileTime

"creationTime"

FileTime

"size"

Long

"isRegularFile"

Boolean

"isDirectory"

Boolean

"isSymbolicLink"

Boolean

"isOther"

Boolean

"fileKey"

Object

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view have the following names and types:

Supported attributes

Name

Type

"lastModifiedTime"

FileTime

"lastAccessTime"

FileTime

"creationTime"

FileTime

"size"

Long

"isRegularFile"

Boolean

"isDirectory"

Boolean

"isSymbolicLink"

Boolean

"isOther"

Boolean

"fileKey"

Object

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

The

getAttribute

method may be
used to read any of these attributes as if by invoking the

readAttributes()

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

The

setAttribute

method may be
used to update the file's last modified time, last access time or create time
attributes as if by invoking the

setTimes

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

BasicFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setTimes

​(

FileTime

lastModifiedTime,

FileTime

lastAccessTime,

FileTime

createTime)

Updates any or all of the file's last modified time, last access time,
and create time attributes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns the name of the attribute view.

BasicFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setTimes

​(

FileTime

lastModifiedTime,

FileTime

lastAccessTime,

FileTime

createTime)

Updates any or all of the file's last modified time, last access time,
and create time attributes.

---

#### Method Summary

Returns the name of the attribute view.

Reads the basic file attributes as a bulk operation.

Updates any or all of the file's last modified time, last access time,
and create time attributes.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"basic"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
BasicFileAttributes
readAttributes()
throws
IOException
```

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Returns:** the file attributes
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

- setTimes

```java
void setTimes​(
FileTime
lastModifiedTime,

FileTime
lastAccessTime,

FileTime
createTime)
throws
IOException
```

Updates any or all of the file's last modified time, last access time,
and create time attributes.

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

**Parameters:** lastModifiedTime

- the new last modified time, or

null

to not change the
value
**Parameters:** lastAccessTime

- the last access time, or

null

to not change the value
**Parameters:** createTime

- the file's create time, or

null

to not change the value
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkWrite

method is invoked to check write access to the file
**See Also:** Files.setLastModifiedTime(java.nio.file.Path, java.nio.file.attribute.FileTime)

Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"basic"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
BasicFileAttributes
readAttributes()
throws
IOException
```

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Returns:** the file attributes
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

- setTimes

```java
void setTimes​(
FileTime
lastModifiedTime,

FileTime
lastAccessTime,

FileTime
createTime)
throws
IOException
```

Updates any or all of the file's last modified time, last access time,
and create time attributes.

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

**Parameters:** lastModifiedTime

- the new last modified time, or

null

to not change the
value
**Parameters:** lastAccessTime

- the last access time, or

null

to not change the value
**Parameters:** createTime

- the file's create time, or

null

to not change the value
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkWrite

method is invoked to check write access to the file
**See Also:** Files.setLastModifiedTime(java.nio.file.Path, java.nio.file.attribute.FileTime)

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"basic"

.

**Specified by:** name

in interface

AttributeView
**Returns:** the name of the attribute view

---

#### name

String

name()

Returns the name of the attribute view. Attribute views of this type
have the name

"basic"

.

readAttributes

```java
BasicFileAttributes
readAttributes()
throws
IOException
```

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Returns:** the file attributes
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

---

#### readAttributes

BasicFileAttributes

readAttributes()
throws

IOException

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

setTimes

```java
void setTimes​(
FileTime
lastModifiedTime,

FileTime
lastAccessTime,

FileTime
createTime)
throws
IOException
```

Updates any or all of the file's last modified time, last access time,
and create time attributes.

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

**Parameters:** lastModifiedTime

- the new last modified time, or

null

to not change the
value
**Parameters:** lastAccessTime

- the last access time, or

null

to not change the value
**Parameters:** createTime

- the file's create time, or

null

to not change the value
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkWrite

method is invoked to check write access to the file
**See Also:** Files.setLastModifiedTime(java.nio.file.Path, java.nio.file.attribute.FileTime)

---

#### setTimes

void setTimes​(

FileTime

lastModifiedTime,

FileTime

lastAccessTime,

FileTime

createTime)
throws

IOException

Updates any or all of the file's last modified time, last access time,
and create time attributes.

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

This method updates the file's timestamp attributes. The values are
converted to the epoch and precision supported by the file system.
Converting from finer to coarser granularities result in precision loss.
The behavior of this method when attempting to set a timestamp that is
not supported or to a value that is outside the range supported by the
underlying file store is not defined. It may or not fail by throwing an

IOException

.

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

If any of the

lastModifiedTime

,

lastAccessTime

,
or

createTime

parameters has the value

null

then the
corresponding timestamp is not changed. An implementation may require to
read the existing values of the file attributes when only some, but not
all, of the timestamp attributes are updated. Consequently, this method
may not be an atomic operation with respect to other file system
operations. Reading and re-writing existing values may also result in
precision loss. If all of the

lastModifiedTime

,

lastAccessTime

and

createTime

parameters are

null

then
this method has no effect.

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

Usage Example:

Suppose we want to change a file's last access time.

```java
Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);
```

Path path = ...
FileTime time = ...
Files.getFileAttributeView(path, BasicFileAttributeView.class).setTimes(null, time, null);

---

