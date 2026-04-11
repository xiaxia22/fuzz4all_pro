# Class ProcessBuilder.Redirect

**Source:** `java.base\java\lang\ProcessBuilder.Redirect.html`

### Class Description

```java
public abstract static class
ProcessBuilder.Redirect

extends
Object
```

Represents a source of subprocess input or a destination of
subprocess output.

Each

Redirect

instance is one of the following:

- the special value

Redirect.PIPE

the special value

Redirect.INHERIT

the special value

Redirect.DISCARD

a redirection to read from a file, created by an invocation of

Redirect.from(File)

a redirection to write to a file, created by an invocation of

Redirect.to(File)

a redirection to append to a file, created by an invocation of

Redirect.appendTo(File)

Each of the above categories has an associated unique

Type

.

**Enclosing class:** ProcessBuilder

---

### Field Details

#### public static final
ProcessBuilder.Redirect
PIPE

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

This is the default handling of subprocess standard I/O.

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

---

#### public static final
ProcessBuilder.Redirect
INHERIT

Indicates that subprocess I/O source or destination will be the
same as those of the current process. This is the normal
behavior of most operating system command interpreters (shells).

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

---

#### public static final
ProcessBuilder.Redirect
DISCARD

Indicates that subprocess output will be discarded.
A typical implementation discards the output by writing to
an operating system specific "null file".

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

**Since:**
- 9

---

### Constructor Details

*No entries found.*

### Method Details

#### public abstract
ProcessBuilder.Redirect.Type
type()

Returns the type of this

Redirect

.

**Returns:**
- the type of this

Redirect

---

#### public
File
file()

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

**Returns:**
- the file associated with this redirect,
or

null

if there is no such file

---

#### public static
ProcessBuilder.Redirect
from​(
File
file)

Returns a redirect to read from the specified file.

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

**Parameters:**
- file

- The

File

for the

Redirect

.

**Returns:**
- a redirect to read from the specified file

---

#### public static
ProcessBuilder.Redirect
to​(
File
file)

Returns a redirect to write to the specified file.
If the specified file exists when the subprocess is started,
its previous contents will be discarded.

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

**Parameters:**
- file

- The

File

for the

Redirect

.

**Returns:**
- a redirect to write to the specified file

---

#### public static
ProcessBuilder.Redirect
appendTo​(
File
file)

Returns a redirect to append to the specified file.
Each write operation first advances the position to the
end of the file and then writes the requested data.
Whether the advancement of the position and the writing
of the data are done in a single atomic operation is
system-dependent and therefore unspecified.

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

**Parameters:**
- file

- The

File

for the

Redirect

.

**Returns:**
- a redirect to append to the specified file

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this

Redirect

for
equality. Returns

true

if and only if the two
objects are identical or both objects are

Redirect

instances of the same type associated with non-null equal

File

instances.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this

Redirect

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this

Redirect

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ProcessBuilder.Redirect

java.lang.Object

- java.lang.ProcessBuilder.Redirect

java.lang.ProcessBuilder.Redirect

**Enclosing class:** ProcessBuilder

```java
public abstract static class
ProcessBuilder.Redirect

extends
Object
```

Represents a source of subprocess input or a destination of
subprocess output.

Each

Redirect

instance is one of the following:

- the special value

Redirect.PIPE

the special value

Redirect.INHERIT

the special value

Redirect.DISCARD

a redirection to read from a file, created by an invocation of

Redirect.from(File)

a redirection to write to a file, created by an invocation of

Redirect.to(File)

a redirection to append to a file, created by an invocation of

Redirect.appendTo(File)

Each of the above categories has an associated unique

Type

.

**Since:** 1.7

public abstract static class

ProcessBuilder.Redirect

extends

Object

Represents a source of subprocess input or a destination of
subprocess output.

Each

Redirect

instance is one of the following:

- the special value

Redirect.PIPE

the special value

Redirect.INHERIT

the special value

Redirect.DISCARD

a redirection to read from a file, created by an invocation of

Redirect.from(File)

a redirection to write to a file, created by an invocation of

Redirect.to(File)

a redirection to append to a file, created by an invocation of

Redirect.appendTo(File)

Each of the above categories has an associated unique

Type

.

the special value

Redirect.PIPE

the special value

Redirect.INHERIT

the special value

Redirect.DISCARD

a redirection to read from a file, created by an invocation of

Redirect.from(File)

a redirection to write to a file, created by an invocation of

Redirect.to(File)

a redirection to append to a file, created by an invocation of

Redirect.appendTo(File)

Each of the above categories has an associated unique

Type

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ProcessBuilder.Redirect.Type

The type of a

ProcessBuilder.Redirect

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ProcessBuilder.Redirect

DISCARD

Indicates that subprocess output will be discarded.

static

ProcessBuilder.Redirect

INHERIT

Indicates that subprocess I/O source or destination will be the
same as those of the current process.

static

ProcessBuilder.Redirect

PIPE

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

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

static

ProcessBuilder.Redirect

appendTo

​(

File

file)

Returns a redirect to append to the specified file.

boolean

equals

​(

Object

obj)

Compares the specified object with this

Redirect

for
equality.

File

file

()

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

static

ProcessBuilder.Redirect

from

​(

File

file)

Returns a redirect to read from the specified file.

int

hashCode

()

Returns a hash code value for this

Redirect

.

static

ProcessBuilder.Redirect

to

​(

File

file)

Returns a redirect to write to the specified file.

abstract

ProcessBuilder.Redirect.Type

type

()

Returns the type of this

Redirect

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ProcessBuilder.Redirect.Type

The type of a

ProcessBuilder.Redirect

.

---

#### Nested Class Summary

The type of a

ProcessBuilder.Redirect

.

Field Summary

Fields

Modifier and Type

Field

Description

static

ProcessBuilder.Redirect

DISCARD

Indicates that subprocess output will be discarded.

static

ProcessBuilder.Redirect

INHERIT

Indicates that subprocess I/O source or destination will be the
same as those of the current process.

static

ProcessBuilder.Redirect

PIPE

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

---

#### Field Summary

Indicates that subprocess output will be discarded.

Indicates that subprocess I/O source or destination will be the
same as those of the current process.

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

ProcessBuilder.Redirect

appendTo

​(

File

file)

Returns a redirect to append to the specified file.

boolean

equals

​(

Object

obj)

Compares the specified object with this

Redirect

for
equality.

File

file

()

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

static

ProcessBuilder.Redirect

from

​(

File

file)

Returns a redirect to read from the specified file.

int

hashCode

()

Returns a hash code value for this

Redirect

.

static

ProcessBuilder.Redirect

to

​(

File

file)

Returns a redirect to write to the specified file.

abstract

ProcessBuilder.Redirect.Type

type

()

Returns the type of this

Redirect

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns a redirect to append to the specified file.

Compares the specified object with this

Redirect

for
equality.

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

Returns a redirect to read from the specified file.

Returns a hash code value for this

Redirect

.

Returns a redirect to write to the specified file.

Returns the type of this

Redirect

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

============ FIELD DETAIL ===========

- Field Detail

- PIPE

```java
public static final
ProcessBuilder.Redirect
PIPE
```

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

This is the default handling of subprocess standard I/O.

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

- INHERIT

```java
public static final
ProcessBuilder.Redirect
INHERIT
```

Indicates that subprocess I/O source or destination will be the
same as those of the current process. This is the normal
behavior of most operating system command interpreters (shells).

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

- DISCARD

```java
public static final
ProcessBuilder.Redirect
DISCARD
```

Indicates that subprocess output will be discarded.
A typical implementation discards the output by writing to
an operating system specific "null file".

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- type

```java
public abstract
ProcessBuilder.Redirect.Type
type()
```

Returns the type of this

Redirect

.

**Returns:** the type of this

Redirect

- file

```java
public
File
file()
```

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

**Returns:** the file associated with this redirect,
or

null

if there is no such file

- from

```java
public static
ProcessBuilder.Redirect
from​(
File
file)
```

Returns a redirect to read from the specified file.

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to read from the specified file

- to

```java
public static
ProcessBuilder.Redirect
to​(
File
file)
```

Returns a redirect to write to the specified file.
If the specified file exists when the subprocess is started,
its previous contents will be discarded.

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to write to the specified file

- appendTo

```java
public static
ProcessBuilder.Redirect
appendTo​(
File
file)
```

Returns a redirect to append to the specified file.
Each write operation first advances the position to the
end of the file and then writes the requested data.
Whether the advancement of the position and the writing
of the data are done in a single atomic operation is
system-dependent and therefore unspecified.

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to append to the specified file

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

Redirect

for
equality. Returns

true

if and only if the two
objects are identical or both objects are

Redirect

instances of the same type associated with non-null equal

File

instances.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

Redirect

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

Redirect
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- PIPE

```java
public static final
ProcessBuilder.Redirect
PIPE
```

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

This is the default handling of subprocess standard I/O.

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

- INHERIT

```java
public static final
ProcessBuilder.Redirect
INHERIT
```

Indicates that subprocess I/O source or destination will be the
same as those of the current process. This is the normal
behavior of most operating system command interpreters (shells).

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

- DISCARD

```java
public static final
ProcessBuilder.Redirect
DISCARD
```

Indicates that subprocess output will be discarded.
A typical implementation discards the output by writing to
an operating system specific "null file".

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

**Since:** 9

---

#### Field Detail

PIPE

```java
public static final
ProcessBuilder.Redirect
PIPE
```

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

This is the default handling of subprocess standard I/O.

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

---

#### PIPE

public static final

ProcessBuilder.Redirect

PIPE

Indicates that subprocess I/O will be connected to the
current Java process over a pipe.

This is the default handling of subprocess standard I/O.

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

It will always be true that

```java
Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE
```

Redirect.PIPE.file() == null &&
Redirect.PIPE.type() == Redirect.Type.PIPE

INHERIT

```java
public static final
ProcessBuilder.Redirect
INHERIT
```

Indicates that subprocess I/O source or destination will be the
same as those of the current process. This is the normal
behavior of most operating system command interpreters (shells).

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

---

#### INHERIT

public static final

ProcessBuilder.Redirect

INHERIT

Indicates that subprocess I/O source or destination will be the
same as those of the current process. This is the normal
behavior of most operating system command interpreters (shells).

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

It will always be true that

```java
Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT
```

Redirect.INHERIT.file() == null &&
Redirect.INHERIT.type() == Redirect.Type.INHERIT

DISCARD

```java
public static final
ProcessBuilder.Redirect
DISCARD
```

Indicates that subprocess output will be discarded.
A typical implementation discards the output by writing to
an operating system specific "null file".

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

**Since:** 9

---

#### DISCARD

public static final

ProcessBuilder.Redirect

DISCARD

Indicates that subprocess output will be discarded.
A typical implementation discards the output by writing to
an operating system specific "null file".

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

It will always be true that

```java
Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE
```

Redirect.DISCARD.file() is the filename appropriate for the operating system
and may be null &&
Redirect.DISCARD.type() == Redirect.Type.WRITE

Method Detail

- type

```java
public abstract
ProcessBuilder.Redirect.Type
type()
```

Returns the type of this

Redirect

.

**Returns:** the type of this

Redirect

- file

```java
public
File
file()
```

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

**Returns:** the file associated with this redirect,
or

null

if there is no such file

- from

```java
public static
ProcessBuilder.Redirect
from​(
File
file)
```

Returns a redirect to read from the specified file.

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to read from the specified file

- to

```java
public static
ProcessBuilder.Redirect
to​(
File
file)
```

Returns a redirect to write to the specified file.
If the specified file exists when the subprocess is started,
its previous contents will be discarded.

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to write to the specified file

- appendTo

```java
public static
ProcessBuilder.Redirect
appendTo​(
File
file)
```

Returns a redirect to append to the specified file.
Each write operation first advances the position to the
end of the file and then writes the requested data.
Whether the advancement of the position and the writing
of the data are done in a single atomic operation is
system-dependent and therefore unspecified.

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to append to the specified file

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

Redirect

for
equality. Returns

true

if and only if the two
objects are identical or both objects are

Redirect

instances of the same type associated with non-null equal

File

instances.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this

Redirect

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

Redirect
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

type

```java
public abstract
ProcessBuilder.Redirect.Type
type()
```

Returns the type of this

Redirect

.

**Returns:** the type of this

Redirect

---

#### type

public abstract

ProcessBuilder.Redirect.Type

type()

Returns the type of this

Redirect

.

file

```java
public
File
file()
```

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

**Returns:** the file associated with this redirect,
or

null

if there is no such file

---

#### file

public

File

file()

Returns the

File

source or destination associated
with this redirect, or

null

if there is no such file.

from

```java
public static
ProcessBuilder.Redirect
from​(
File
file)
```

Returns a redirect to read from the specified file.

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to read from the specified file

---

#### from

public static

ProcessBuilder.Redirect

from​(

File

file)

Returns a redirect to read from the specified file.

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

It will always be true that

```java
Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ
```

Redirect.from(file).file() == file &&
Redirect.from(file).type() == Redirect.Type.READ

to

```java
public static
ProcessBuilder.Redirect
to​(
File
file)
```

Returns a redirect to write to the specified file.
If the specified file exists when the subprocess is started,
its previous contents will be discarded.

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to write to the specified file

---

#### to

public static

ProcessBuilder.Redirect

to​(

File

file)

Returns a redirect to write to the specified file.
If the specified file exists when the subprocess is started,
its previous contents will be discarded.

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

It will always be true that

```java
Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE
```

Redirect.to(file).file() == file &&
Redirect.to(file).type() == Redirect.Type.WRITE

appendTo

```java
public static
ProcessBuilder.Redirect
appendTo​(
File
file)
```

Returns a redirect to append to the specified file.
Each write operation first advances the position to the
end of the file and then writes the requested data.
Whether the advancement of the position and the writing
of the data are done in a single atomic operation is
system-dependent and therefore unspecified.

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

**Parameters:** file

- The

File

for the

Redirect

.
**Returns:** a redirect to append to the specified file

---

#### appendTo

public static

ProcessBuilder.Redirect

appendTo​(

File

file)

Returns a redirect to append to the specified file.
Each write operation first advances the position to the
end of the file and then writes the requested data.
Whether the advancement of the position and the writing
of the data are done in a single atomic operation is
system-dependent and therefore unspecified.

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

It will always be true that

```java
Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND
```

Redirect.appendTo(file).file() == file &&
Redirect.appendTo(file).type() == Redirect.Type.APPEND

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this

Redirect

for
equality. Returns

true

if and only if the two
objects are identical or both objects are

Redirect

instances of the same type associated with non-null equal

File

instances.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified object with this

Redirect

for
equality. Returns

true

if and only if the two
objects are identical or both objects are

Redirect

instances of the same type associated with non-null equal

File

instances.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this

Redirect

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this

Redirect
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this

Redirect

.

---

