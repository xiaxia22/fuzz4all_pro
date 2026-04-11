# Interface DosFileAttributeView

**Source:** `java.base\java\nio\file\attribute\DosFileAttributeView.html`

### Class Description

```java
public interface
DosFileAttributeView

extends
BasicFileAttributeView
```

A file attribute view that provides a view of the legacy "DOS" file attributes.
These attributes are supported by file systems such as the File Allocation
Table (FAT) format commonly used in

consumer devices

.

A

DosFileAttributeView

is a

BasicFileAttributeView

that
additionally supports access to the set of DOS attribute flags that are used
to indicate if the file is read-only, hidden, a system file, or archived.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

, and in addition, the following attributes are
supported:

Supported attributes

Name

Type

readonly

Boolean

hidden

Boolean

system

Boolean

archive

Boolean

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

**All Superinterfaces:** AttributeView

,

BasicFileAttributeView

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

"dos"

.

**Specified by:**
- name

in interface

AttributeView
- name

in interface

BasicFileAttributeView

**Returns:**
- the name of the attribute view

---

#### DosFileAttributes
readAttributes()
throws
IOException

Description copied from interface:

BasicFileAttributeView

**Specified by:**
- readAttributes

in interface

BasicFileAttributeView

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

#### void setReadOnly​(boolean value)
throws
IOException

Updates the value of the read-only attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:**
- value

- the new value of the attribute

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### void setHidden​(boolean value)
throws
IOException

Updates the value of the hidden attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:**
- value

- the new value of the attribute

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### void setSystem​(boolean value)
throws
IOException

Updates the value of the system attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:**
- value

- the new value of the attribute

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### void setArchive​(boolean value)
throws
IOException

Updates the value of the archive attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:**
- value

- the new value of the attribute

**Throws:**
- IOException

- if an I/O error occurs
- SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

### Additional Sections

#### Interface DosFileAttributeView

**All Superinterfaces:** AttributeView

,

BasicFileAttributeView

,

FileAttributeView

```java
public interface
DosFileAttributeView

extends
BasicFileAttributeView
```

A file attribute view that provides a view of the legacy "DOS" file attributes.
These attributes are supported by file systems such as the File Allocation
Table (FAT) format commonly used in

consumer devices

.

A

DosFileAttributeView

is a

BasicFileAttributeView

that
additionally supports access to the set of DOS attribute flags that are used
to indicate if the file is read-only, hidden, a system file, or archived.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

, and in addition, the following attributes are
supported:

Supported attributes

Name

Type

readonly

Boolean

hidden

Boolean

system

Boolean

archive

Boolean

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

**Since:** 1.7

public interface

DosFileAttributeView

extends

BasicFileAttributeView

A file attribute view that provides a view of the legacy "DOS" file attributes.
These attributes are supported by file systems such as the File Allocation
Table (FAT) format commonly used in

consumer devices

.

A

DosFileAttributeView

is a

BasicFileAttributeView

that
additionally supports access to the set of DOS attribute flags that are used
to indicate if the file is read-only, hidden, a system file, or archived.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

, and in addition, the following attributes are
supported:

Supported attributes

Name

Type

readonly

Boolean

hidden

Boolean

system

Boolean

archive

Boolean

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

A

DosFileAttributeView

is a

BasicFileAttributeView

that
additionally supports access to the set of DOS attribute flags that are used
to indicate if the file is read-only, hidden, a system file, or archived.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

, and in addition, the following attributes are
supported:

Supported attributes

Name

Type

readonly

Boolean

hidden

Boolean

system

Boolean

archive

Boolean

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

Where dynamic access to file attributes is required, the attributes
supported by this attribute view are as defined by

BasicFileAttributeView

, and in addition, the following attributes are
supported:

Supported attributes

Name

Type

readonly

Boolean

hidden

Boolean

system

Boolean

archive

Boolean

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

The

getAttribute

method may
be used to read any of these attributes, or any of the attributes defined by

BasicFileAttributeView

as if by invoking the

readAttributes()

method.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

The

setAttribute

method may
be used to update the file's last modified time, last access time or create
time attributes as defined by

BasicFileAttributeView

. It may also be
used to update the DOS attributes as if by invoking the

setReadOnly

,

setHidden

,

setSystem

, and

setArchive

methods respectively.

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

DosFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setArchive

​(boolean value)

Updates the value of the archive attribute.

void

setHidden

​(boolean value)

Updates the value of the hidden attribute.

void

setReadOnly

​(boolean value)

Updates the value of the read-only attribute.

void

setSystem

​(boolean value)

Updates the value of the system attribute.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

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

DosFileAttributes

readAttributes

()

Reads the basic file attributes as a bulk operation.

void

setArchive

​(boolean value)

Updates the value of the archive attribute.

void

setHidden

​(boolean value)

Updates the value of the hidden attribute.

void

setReadOnly

​(boolean value)

Updates the value of the read-only attribute.

void

setSystem

​(boolean value)

Updates the value of the system attribute.

- Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

---

#### Method Summary

Returns the name of the attribute view.

Reads the basic file attributes as a bulk operation.

Updates the value of the archive attribute.

Updates the value of the hidden attribute.

Updates the value of the read-only attribute.

Updates the value of the system attribute.

Methods declared in interface java.nio.file.attribute.

BasicFileAttributeView

setTimes

---

#### Methods declared in interface java.nio.file.attribute. BasicFileAttributeView

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"dos"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
DosFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
**Returns:** the file attributes
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

- setReadOnly

```java
void setReadOnly​(boolean value)
throws
IOException
```

Updates the value of the read-only attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setHidden

```java
void setHidden​(boolean value)
throws
IOException
```

Updates the value of the hidden attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setSystem

```java
void setSystem​(boolean value)
throws
IOException
```

Updates the value of the system attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setArchive

```java
void setArchive​(boolean value)
throws
IOException
```

Updates the value of the archive attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

Method Detail

- name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"dos"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Returns:** the name of the attribute view

- readAttributes

```java
DosFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
**Returns:** the file attributes
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default provider, a security manager is
installed, its

checkRead

method is invoked to check read access to the file

- setReadOnly

```java
void setReadOnly​(boolean value)
throws
IOException
```

Updates the value of the read-only attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setHidden

```java
void setHidden​(boolean value)
throws
IOException
```

Updates the value of the hidden attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setSystem

```java
void setSystem​(boolean value)
throws
IOException
```

Updates the value of the system attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

- setArchive

```java
void setArchive​(boolean value)
throws
IOException
```

Updates the value of the archive attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### Method Detail

name

```java
String
name()
```

Returns the name of the attribute view. Attribute views of this type
have the name

"dos"

.

**Specified by:** name

in interface

AttributeView
**Specified by:** name

in interface

BasicFileAttributeView
**Returns:** the name of the attribute view

---

#### name

String

name()

Returns the name of the attribute view. Attribute views of this type
have the name

"dos"

.

readAttributes

```java
DosFileAttributes
readAttributes()
throws
IOException
```

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

**Specified by:** readAttributes

in interface

BasicFileAttributeView
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

DosFileAttributes

readAttributes()
throws

IOException

Description copied from interface:

BasicFileAttributeView

Reads the basic file attributes as a bulk operation.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

It is implementation specific if all file attributes are read as an
atomic operation with respect to other file system operations.

setReadOnly

```java
void setReadOnly​(boolean value)
throws
IOException
```

Updates the value of the read-only attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### setReadOnly

void setReadOnly​(boolean value)
throws

IOException

Updates the value of the read-only attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

setHidden

```java
void setHidden​(boolean value)
throws
IOException
```

Updates the value of the hidden attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### setHidden

void setHidden​(boolean value)
throws

IOException

Updates the value of the hidden attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

setSystem

```java
void setSystem​(boolean value)
throws
IOException
```

Updates the value of the system attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### setSystem

void setSystem​(boolean value)
throws

IOException

Updates the value of the system attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

setArchive

```java
void setArchive​(boolean value)
throws
IOException
```

Updates the value of the archive attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

**Parameters:** value

- the new value of the attribute
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- In the case of the default, and a security manager is installed,
its

checkWrite

method
is invoked to check write access to the file

---

#### setArchive

void setArchive​(boolean value)
throws

IOException

Updates the value of the archive attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

It is implementation specific if the attribute can be updated as an
atomic operation with respect to other file system operations. An
implementation may, for example, require to read the existing value of
the DOS attribute in order to update this attribute.

---

