# Class SerialBlob

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SerialBlob.html`

### Class Description

```java
public class
SerialBlob

extends
Object

implements
Blob
,
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL

BLOB

value.

The

SerialBlob

class provides a constructor for creating
an instance from a

Blob

object. Note that the

Blob

object should have brought the SQL

BLOB

value's data over
to the client before a

SerialBlob

object
is constructed from it. The data of an SQL

BLOB

value can
be materialized on the client as an array of bytes (using the method

Blob.getBytes

) or as a stream of uninterpreted bytes
(using the method

Blob.getBinaryStream

).

SerialBlob

methods make it possible to make a copy of a

SerialBlob

object as an array of bytes or as a stream.
They also make it possible to locate a given pattern of bytes or a

Blob

object within a

SerialBlob

object
and to update or truncate a

Blob

object.

Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Blob

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerialBlob​(byte[] b)
throws
SerialException
,

SQLException

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

**Parameters:**
- b

- the

byte

array containing the data for the

Blob

object to be serialized

**Throws:**
- SerialException

- if an error occurs during serialization
- SQLException

- if a SQL errors occurs

---

#### public SerialBlob​(
Blob
blob)
throws
SerialException
,

SQLException

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

**Parameters:**
- blob

- the

Blob

object from which this

SerialBlob

object is to be constructed;
cannot be null.

**Throws:**
- SerialException

- if an error occurs during serialization
- SQLException

- if the

Blob

passed to this
to this constructor is a

null

.

**See Also:**
- Blob

---

### Method Details

#### public byte[] getBytes​(long pos,
int length)
throws
SerialException

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

**Specified by:**
- getBytes

in interface

Blob

**Parameters:**
- pos

- the ordinal position of the first byte in this

SerialBlob

object to be copied;
numbering starts at

1

; must not be less
than

1

and must be less than or equal
to the length of this

SerialBlob

object
- length

- the number of bytes to be copied

**Returns:**
- an array of bytes that is a copy of a region of this

SerialBlob

object, starting at the given
position and containing the given number of consecutive bytes

**Throws:**
- SerialException

- if the given starting position is out of bounds;
if

free

had previously been called on this object

**See Also:**
- Blob.setBytes(long, byte[])

---

#### public long length()
throws
SerialException

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

**Specified by:**
- length

in interface

Blob

**Returns:**
- a

long

indicating the length in bytes of this

SerialBlob

object's array of bytes

**Throws:**
- SerialException

- if an error occurs;
if

free

had previously been called on this object

---

#### public
InputStream
getBinaryStream()
throws
SerialException

Returns this

SerialBlob

object as an input stream.
Unlike the related method,

setBinaryStream

,
a stream is produced regardless of whether the

SerialBlob

was created with a

Blob

object or a

byte

array.

**Specified by:**
- getBinaryStream

in interface

Blob

**Returns:**
- a

java.io.InputStream

object that contains
this

SerialBlob

object's array of bytes

**Throws:**
- SerialException

- if an error occurs;
if

free

had previously been called on this object

**See Also:**
- setBinaryStream(long)

---

#### public long position​(byte[] pattern,
long start)
throws
SerialException
,

SQLException

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

**Specified by:**
- position

in interface

Blob

**Parameters:**
- pattern

- the pattern of bytes for which to search
- start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object

**Returns:**
- the position in this

SerialBlob

object
where the given pattern begins, starting at the specified
position;

-1

if the pattern is not found
or the given starting position is out of bounds; position
numbering for the return value starts at

1

**Throws:**
- SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
- SQLException

- if there is an error accessing the

BLOB

value from the database

---

#### public long position​(
Blob
pattern,
long start)
throws
SerialException
,

SQLException

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

**Specified by:**
- position

in interface

Blob

**Parameters:**
- pattern

- the

Blob

object for which to search;
- start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object

**Returns:**
- the position in this

SerialBlob

object
where the given

Blob

object begins, starting
at the specified position;

-1

if the pattern is
not found or the given starting position is out of bounds;
position numbering for the return value starts at

1

**Throws:**
- SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
- SQLException

- if there is an error accessing the

BLOB

value from the database

---

#### public int setBytes​(long pos,
byte[] bytes)
throws
SerialException
,

SQLException

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

**Specified by:**
- setBytes

in interface

Blob

**Parameters:**
- pos

- the position in the SQL

BLOB

value at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
- bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents

**Returns:**
- the number of bytes written

**Throws:**
- SerialException

- if there is an error accessing the

BLOB

value; or if an invalid position is set; if an
invalid offset value is set;
if

free

had previously been called on this object
- SQLException

- if there is an error accessing the

BLOB

value from the database

**See Also:**
- getBytes(long, int)

---

#### public int setBytes​(long pos,
byte[] bytes,
int offset,
int length)
throws
SerialException
,

SQLException

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.
Writing starts at position

pos

in the

BLOB

value;

len

bytes from the given byte array are written.

**Specified by:**
- setBytes

in interface

Blob

**Parameters:**
- pos

- the position in the

BLOB

object at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
- bytes

- the array of bytes to be written to the

BLOB

value
- offset

- the offset in the

byte

array at which
to start reading the bytes. The first offset position is

0

; must not be less than

0

nor greater
than the length of the

byte

array
- length

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes

.

**Returns:**
- the number of bytes written

**Throws:**
- SerialException

- if there is an error accessing the

BLOB

value; if an invalid position is set; if an
invalid offset value is set; if number of bytes to be written
is greater than the

SerialBlob

length; or the combined
values of the length and offset is greater than the Blob buffer;
if

free

had previously been called on this object
- SQLException

- if there is an error accessing the

BLOB

value from the database.

**See Also:**
- getBytes(long, int)

---

#### public
OutputStream
setBinaryStream​(long pos)
throws
SerialException
,

SQLException

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

. This method forwards the

setBinaryStream()

call to the underlying

Blob

in
the event that this

SerialBlob

object is instantiated with a

Blob

. If this

SerialBlob

is instantiated with
a

byte

array, a

SerialException

is thrown.

**Specified by:**
- setBinaryStream

in interface

Blob

**Parameters:**
- pos

- the position in the

BLOB

value at which
to start writing

**Returns:**
- a

java.io.OutputStream

object to which data can
be written

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value
- SerialException

- if the SerialBlob in not instantiated with a

Blob

object that supports

setBinaryStream()

;
if

free

had previously been called on this object

**See Also:**
- getBinaryStream()

---

#### public void truncate​(long length)
throws
SerialException

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

**Specified by:**
- truncate

in interface

Blob

**Parameters:**
- length

- the length, in bytes, to which the

BLOB

value that this

Blob

object represents should be
truncated

**Throws:**
- SerialException

- if there is an error accessing the Blob value;
or the length to truncate is greater that the SerialBlob length;
if

free

had previously been called on this object

---

#### public
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

**Specified by:**
- getBinaryStream

in interface

Blob

**Parameters:**
- pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1
- length

- the length in bytes of the partial value to be retrieved

**Returns:**
- InputStream

through which the partial

Blob

value can
be read.

**Throws:**
- SQLException

- if pos is less than 1 or if pos is greater than the
number of bytes in the

Blob

or if pos + length is greater than
the number of bytes in the

Blob
- SerialException

- if the

free

method had been previously
called on this object

**Since:**
- 1.6

---

#### public void free()
throws
SQLException

This method frees the

SerialBlob

object and releases the
resources that it holds. The object is invalid once the

free

method is called.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

**Specified by:**
- free

in interface

Blob

**Throws:**
- SQLException

- if an error occurs releasing the Blob's resources

**Since:**
- 1.6

---

#### public boolean equals​(
Object
obj)

Compares this SerialBlob to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialBlob

object that represents the same sequence of bytes as this
object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to compare this

SerialBlob

against

**Returns:**
- true

if the given object represents a

SerialBlob

equivalent to this SerialBlob,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this

SerialBlob

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Returns a clone of this

SerialBlob

. The copy will contain a
reference to a clone of the internal byte array, not a reference
to the original internal byte array of this

SerialBlob

object.
The underlying

Blob

object will be set to null.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this SerialBlob

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SerialBlob

java.lang.Object

- javax.sql.rowset.serial.SerialBlob

javax.sql.rowset.serial.SerialBlob

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Blob

```java
public class
SerialBlob

extends
Object

implements
Blob
,
Serializable
,
Cloneable
```

A serialized mapping in the Java programming language of an SQL

BLOB

value.

The

SerialBlob

class provides a constructor for creating
an instance from a

Blob

object. Note that the

Blob

object should have brought the SQL

BLOB

value's data over
to the client before a

SerialBlob

object
is constructed from it. The data of an SQL

BLOB

value can
be materialized on the client as an array of bytes (using the method

Blob.getBytes

) or as a stream of uninterpreted bytes
(using the method

Blob.getBinaryStream

).

SerialBlob

methods make it possible to make a copy of a

SerialBlob

object as an array of bytes or as a stream.
They also make it possible to locate a given pattern of bytes or a

Blob

object within a

SerialBlob

object
and to update or truncate a

Blob

object.

Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

**Since:** 1.5
**See Also:** Serialized Form

public class

SerialBlob

extends

Object

implements

Blob

,

Serializable

,

Cloneable

A serialized mapping in the Java programming language of an SQL

BLOB

value.

The

SerialBlob

class provides a constructor for creating
an instance from a

Blob

object. Note that the

Blob

object should have brought the SQL

BLOB

value's data over
to the client before a

SerialBlob

object
is constructed from it. The data of an SQL

BLOB

value can
be materialized on the client as an array of bytes (using the method

Blob.getBytes

) or as a stream of uninterpreted bytes
(using the method

Blob.getBinaryStream

).

SerialBlob

methods make it possible to make a copy of a

SerialBlob

object as an array of bytes or as a stream.
They also make it possible to locate a given pattern of bytes or a

Blob

object within a

SerialBlob

object
and to update or truncate a

Blob

object.

Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

The

SerialBlob

class provides a constructor for creating
an instance from a

Blob

object. Note that the

Blob

object should have brought the SQL

BLOB

value's data over
to the client before a

SerialBlob

object
is constructed from it. The data of an SQL

BLOB

value can
be materialized on the client as an array of bytes (using the method

Blob.getBytes

) or as a stream of uninterpreted bytes
(using the method

Blob.getBinaryStream

).

SerialBlob

methods make it possible to make a copy of a

SerialBlob

object as an array of bytes or as a stream.
They also make it possible to locate a given pattern of bytes or a

Blob

object within a

SerialBlob

object
and to update or truncate a

Blob

object.

Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

SerialBlob

methods make it possible to make a copy of a

SerialBlob

object as an array of bytes or as a stream.
They also make it possible to locate a given pattern of bytes or a

Blob

object within a

SerialBlob

object
and to update or truncate a

Blob

object.

Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

---

#### Thread safety

A SerialBlob is not safe for use by multiple concurrent threads. If a
SerialBlob is to be used by more than one thread then access to the SerialBlob
should be controlled by appropriate synchronization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerialBlob

​(byte[] b)

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

SerialBlob

​(

Blob

blob)

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialBlob

.

boolean

equals

​(

Object

obj)

Compares this SerialBlob to the specified object.

void

free

()

This method frees the

SerialBlob

object and releases the
resources that it holds.

InputStream

getBinaryStream

()

Returns this

SerialBlob

object as an input stream.

InputStream

getBinaryStream

​(long pos,
long length)

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

byte[]

getBytes

​(long pos,
int length)

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

int

hashCode

()

Returns a hash code for this

SerialBlob

.

long

length

()

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

long

position

​(byte[] pattern,
long start)

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

long

position

​(

Blob

pattern,
long start)

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

OutputStream

setBinaryStream

​(long pos)

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents.

int

setBytes

​(long pos,
byte[] bytes)

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

int

setBytes

​(long pos,
byte[] bytes,
int offset,
int length)

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.

void

truncate

​(long length)

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

- Methods declared in class java.lang.

Object

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

Constructor Summary

Constructors

Constructor

Description

SerialBlob

​(byte[] b)

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

SerialBlob

​(

Blob

blob)

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

---

#### Constructor Summary

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this

SerialBlob

.

boolean

equals

​(

Object

obj)

Compares this SerialBlob to the specified object.

void

free

()

This method frees the

SerialBlob

object and releases the
resources that it holds.

InputStream

getBinaryStream

()

Returns this

SerialBlob

object as an input stream.

InputStream

getBinaryStream

​(long pos,
long length)

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

byte[]

getBytes

​(long pos,
int length)

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

int

hashCode

()

Returns a hash code for this

SerialBlob

.

long

length

()

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

long

position

​(byte[] pattern,
long start)

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

long

position

​(

Blob

pattern,
long start)

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

OutputStream

setBinaryStream

​(long pos)

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents.

int

setBytes

​(long pos,
byte[] bytes)

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

int

setBytes

​(long pos,
byte[] bytes,
int offset,
int length)

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.

void

truncate

​(long length)

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

- Methods declared in class java.lang.

Object

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

Returns a clone of this

SerialBlob

.

Compares this SerialBlob to the specified object.

This method frees the

SerialBlob

object and releases the
resources that it holds.

Returns this

SerialBlob

object as an input stream.

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Returns a hash code for this

SerialBlob

.

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents.

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SerialBlob

```java
public SerialBlob​(byte[] b)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

**Parameters:** b

- the

byte

array containing the data for the

Blob

object to be serialized
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if a SQL errors occurs

- SerialBlob

```java
public SerialBlob​(
Blob
blob)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

**Parameters:** blob

- the

Blob

object from which this

SerialBlob

object is to be constructed;
cannot be null.
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if the

Blob

passed to this
to this constructor is a

null

.
**See Also:** Blob

============ METHOD DETAIL ==========

- Method Detail

- getBytes

```java
public byte[] getBytes​(long pos,
int length)
throws
SerialException
```

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

**Specified by:** getBytes

in interface

Blob
**Parameters:** pos

- the ordinal position of the first byte in this

SerialBlob

object to be copied;
numbering starts at

1

; must not be less
than

1

and must be less than or equal
to the length of this

SerialBlob

object
**Parameters:** length

- the number of bytes to be copied
**Returns:** an array of bytes that is a copy of a region of this

SerialBlob

object, starting at the given
position and containing the given number of consecutive bytes
**Throws:** SerialException

- if the given starting position is out of bounds;
if

free

had previously been called on this object
**See Also:** Blob.setBytes(long, byte[])

- length

```java
public long length()
throws
SerialException
```

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

**Specified by:** length

in interface

Blob
**Returns:** a

long

indicating the length in bytes of this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object

- getBinaryStream

```java
public
InputStream
getBinaryStream()
throws
SerialException
```

Returns this

SerialBlob

object as an input stream.
Unlike the related method,

setBinaryStream

,
a stream is produced regardless of whether the

SerialBlob

was created with a

Blob

object or a

byte

array.

**Specified by:** getBinaryStream

in interface

Blob
**Returns:** a

java.io.InputStream

object that contains
this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object
**See Also:** setBinaryStream(long)

- position

```java
public long position​(byte[] pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the pattern of bytes for which to search
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given pattern begins, starting at the specified
position;

-1

if the pattern is not found
or the given starting position is out of bounds; position
numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

- position

```java
public long position​(
Blob
pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the

Blob

object for which to search;
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given

Blob

object begins, starting
at the specified position;

-1

if the pattern is
not found or the given starting position is out of bounds;
position numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

- setBytes

```java
public int setBytes​(long pos,
byte[] bytes)
throws
SerialException
,

SQLException
```

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the SQL

BLOB

value at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; or if an invalid position is set; if an
invalid offset value is set;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database
**See Also:** getBytes(long, int)

- setBytes

```java
public int setBytes​(long pos,
byte[] bytes,
int offset,
int length)
throws
SerialException
,

SQLException
```

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.
Writing starts at position

pos

in the

BLOB

value;

len

bytes from the given byte array are written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

object at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value
**Parameters:** offset

- the offset in the

byte

array at which
to start reading the bytes. The first offset position is

0

; must not be less than

0

nor greater
than the length of the

byte

array
**Parameters:** length

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes

.
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; if an invalid position is set; if an
invalid offset value is set; if number of bytes to be written
is greater than the

SerialBlob

length; or the combined
values of the length and offset is greater than the Blob buffer;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database.
**See Also:** getBytes(long, int)

- setBinaryStream

```java
public
OutputStream
setBinaryStream​(long pos)
throws
SerialException
,

SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

. This method forwards the

setBinaryStream()

call to the underlying

Blob

in
the event that this

SerialBlob

object is instantiated with a

Blob

. If this

SerialBlob

is instantiated with
a

byte

array, a

SerialException

is thrown.

**Specified by:** setBinaryStream

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

value at which
to start writing
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SerialException

- if the SerialBlob in not instantiated with a

Blob

object that supports

setBinaryStream()

;
if

free

had previously been called on this object
**See Also:** getBinaryStream()

- truncate

```java
public void truncate​(long length)
throws
SerialException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

**Specified by:** truncate

in interface

Blob
**Parameters:** length

- the length, in bytes, to which the

BLOB

value that this

Blob

object represents should be
truncated
**Throws:** SerialException

- if there is an error accessing the Blob value;
or the length to truncate is greater that the SerialBlob length;
if

free

had previously been called on this object

- getBinaryStream

```java
public
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

**Specified by:** getBinaryStream

in interface

Blob
**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which the partial

Blob

value can
be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater than the
number of bytes in the

Blob

or if pos + length is greater than
the number of bytes in the

Blob
**Throws:** SerialException

- if the

free

method had been previously
called on this object
**Since:** 1.6

- free

```java
public void free()
throws
SQLException
```

This method frees the

SerialBlob

object and releases the
resources that it holds. The object is invalid once the

free

method is called.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

**Specified by:** free

in interface

Blob
**Throws:** SQLException

- if an error occurs releasing the Blob's resources
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialBlob to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialBlob

object that represents the same sequence of bytes as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialBlob

against
**Returns:** true

if the given object represents a

SerialBlob

equivalent to this SerialBlob,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialBlob

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialBlob

. The copy will contain a
reference to a clone of the internal byte array, not a reference
to the original internal byte array of this

SerialBlob

object.
The underlying

Blob

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialBlob
**See Also:** Cloneable

Constructor Detail

- SerialBlob

```java
public SerialBlob​(byte[] b)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

**Parameters:** b

- the

byte

array containing the data for the

Blob

object to be serialized
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if a SQL errors occurs

- SerialBlob

```java
public SerialBlob​(
Blob
blob)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

**Parameters:** blob

- the

Blob

object from which this

SerialBlob

object is to be constructed;
cannot be null.
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if the

Blob

passed to this
to this constructor is a

null

.
**See Also:** Blob

---

#### Constructor Detail

SerialBlob

```java
public SerialBlob​(byte[] b)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

**Parameters:** b

- the

byte

array containing the data for the

Blob

object to be serialized
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if a SQL errors occurs

---

#### SerialBlob

public SerialBlob​(byte[] b)
throws

SerialException

,

SQLException

Constructs a

SerialBlob

object that is a serialized version of
the given

byte

array.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

The new

SerialBlob

object is initialized with the data from the

byte

array, thus allowing disconnected

RowSet

objects to establish serialized

Blob

objects without
touching the data source.

SerialBlob

```java
public SerialBlob​(
Blob
blob)
throws
SerialException
,

SQLException
```

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

**Parameters:** blob

- the

Blob

object from which this

SerialBlob

object is to be constructed;
cannot be null.
**Throws:** SerialException

- if an error occurs during serialization
**Throws:** SQLException

- if the

Blob

passed to this
to this constructor is a

null

.
**See Also:** Blob

---

#### SerialBlob

public SerialBlob​(

Blob

blob)
throws

SerialException

,

SQLException

Constructs a

SerialBlob

object that is a serialized
version of the given

Blob

object.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

The new

SerialBlob

object is initialized with the
data from the

Blob

object; therefore, the

Blob

object should have previously brought the
SQL

BLOB

value's data over to the client from
the database. Otherwise, the new

SerialBlob

object
will contain no data.

Method Detail

- getBytes

```java
public byte[] getBytes​(long pos,
int length)
throws
SerialException
```

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

**Specified by:** getBytes

in interface

Blob
**Parameters:** pos

- the ordinal position of the first byte in this

SerialBlob

object to be copied;
numbering starts at

1

; must not be less
than

1

and must be less than or equal
to the length of this

SerialBlob

object
**Parameters:** length

- the number of bytes to be copied
**Returns:** an array of bytes that is a copy of a region of this

SerialBlob

object, starting at the given
position and containing the given number of consecutive bytes
**Throws:** SerialException

- if the given starting position is out of bounds;
if

free

had previously been called on this object
**See Also:** Blob.setBytes(long, byte[])

- length

```java
public long length()
throws
SerialException
```

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

**Specified by:** length

in interface

Blob
**Returns:** a

long

indicating the length in bytes of this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object

- getBinaryStream

```java
public
InputStream
getBinaryStream()
throws
SerialException
```

Returns this

SerialBlob

object as an input stream.
Unlike the related method,

setBinaryStream

,
a stream is produced regardless of whether the

SerialBlob

was created with a

Blob

object or a

byte

array.

**Specified by:** getBinaryStream

in interface

Blob
**Returns:** a

java.io.InputStream

object that contains
this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object
**See Also:** setBinaryStream(long)

- position

```java
public long position​(byte[] pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the pattern of bytes for which to search
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given pattern begins, starting at the specified
position;

-1

if the pattern is not found
or the given starting position is out of bounds; position
numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

- position

```java
public long position​(
Blob
pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the

Blob

object for which to search;
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given

Blob

object begins, starting
at the specified position;

-1

if the pattern is
not found or the given starting position is out of bounds;
position numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

- setBytes

```java
public int setBytes​(long pos,
byte[] bytes)
throws
SerialException
,

SQLException
```

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the SQL

BLOB

value at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; or if an invalid position is set; if an
invalid offset value is set;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database
**See Also:** getBytes(long, int)

- setBytes

```java
public int setBytes​(long pos,
byte[] bytes,
int offset,
int length)
throws
SerialException
,

SQLException
```

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.
Writing starts at position

pos

in the

BLOB

value;

len

bytes from the given byte array are written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

object at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value
**Parameters:** offset

- the offset in the

byte

array at which
to start reading the bytes. The first offset position is

0

; must not be less than

0

nor greater
than the length of the

byte

array
**Parameters:** length

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes

.
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; if an invalid position is set; if an
invalid offset value is set; if number of bytes to be written
is greater than the

SerialBlob

length; or the combined
values of the length and offset is greater than the Blob buffer;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database.
**See Also:** getBytes(long, int)

- setBinaryStream

```java
public
OutputStream
setBinaryStream​(long pos)
throws
SerialException
,

SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

. This method forwards the

setBinaryStream()

call to the underlying

Blob

in
the event that this

SerialBlob

object is instantiated with a

Blob

. If this

SerialBlob

is instantiated with
a

byte

array, a

SerialException

is thrown.

**Specified by:** setBinaryStream

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

value at which
to start writing
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SerialException

- if the SerialBlob in not instantiated with a

Blob

object that supports

setBinaryStream()

;
if

free

had previously been called on this object
**See Also:** getBinaryStream()

- truncate

```java
public void truncate​(long length)
throws
SerialException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

**Specified by:** truncate

in interface

Blob
**Parameters:** length

- the length, in bytes, to which the

BLOB

value that this

Blob

object represents should be
truncated
**Throws:** SerialException

- if there is an error accessing the Blob value;
or the length to truncate is greater that the SerialBlob length;
if

free

had previously been called on this object

- getBinaryStream

```java
public
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

**Specified by:** getBinaryStream

in interface

Blob
**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which the partial

Blob

value can
be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater than the
number of bytes in the

Blob

or if pos + length is greater than
the number of bytes in the

Blob
**Throws:** SerialException

- if the

free

method had been previously
called on this object
**Since:** 1.6

- free

```java
public void free()
throws
SQLException
```

This method frees the

SerialBlob

object and releases the
resources that it holds. The object is invalid once the

free

method is called.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

**Specified by:** free

in interface

Blob
**Throws:** SQLException

- if an error occurs releasing the Blob's resources
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialBlob to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialBlob

object that represents the same sequence of bytes as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialBlob

against
**Returns:** true

if the given object represents a

SerialBlob

equivalent to this SerialBlob,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialBlob

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a clone of this

SerialBlob

. The copy will contain a
reference to a clone of the internal byte array, not a reference
to the original internal byte array of this

SerialBlob

object.
The underlying

Blob

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialBlob
**See Also:** Cloneable

---

#### Method Detail

getBytes

```java
public byte[] getBytes​(long pos,
int length)
throws
SerialException
```

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

**Specified by:** getBytes

in interface

Blob
**Parameters:** pos

- the ordinal position of the first byte in this

SerialBlob

object to be copied;
numbering starts at

1

; must not be less
than

1

and must be less than or equal
to the length of this

SerialBlob

object
**Parameters:** length

- the number of bytes to be copied
**Returns:** an array of bytes that is a copy of a region of this

SerialBlob

object, starting at the given
position and containing the given number of consecutive bytes
**Throws:** SerialException

- if the given starting position is out of bounds;
if

free

had previously been called on this object
**See Also:** Blob.setBytes(long, byte[])

---

#### getBytes

public byte[] getBytes​(long pos,
int length)
throws

SerialException

Copies the specified number of bytes, starting at the given
position, from this

SerialBlob

object to
another array of bytes.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

Note that if the given number of bytes to be copied is larger than
the length of this

SerialBlob

object's array of
bytes, the given number will be shortened to the array's length.

length

```java
public long length()
throws
SerialException
```

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

**Specified by:** length

in interface

Blob
**Returns:** a

long

indicating the length in bytes of this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object

---

#### length

public long length()
throws

SerialException

Retrieves the number of bytes in this

SerialBlob

object's array of bytes.

getBinaryStream

```java
public
InputStream
getBinaryStream()
throws
SerialException
```

Returns this

SerialBlob

object as an input stream.
Unlike the related method,

setBinaryStream

,
a stream is produced regardless of whether the

SerialBlob

was created with a

Blob

object or a

byte

array.

**Specified by:** getBinaryStream

in interface

Blob
**Returns:** a

java.io.InputStream

object that contains
this

SerialBlob

object's array of bytes
**Throws:** SerialException

- if an error occurs;
if

free

had previously been called on this object
**See Also:** setBinaryStream(long)

---

#### getBinaryStream

public

InputStream

getBinaryStream()
throws

SerialException

Returns this

SerialBlob

object as an input stream.
Unlike the related method,

setBinaryStream

,
a stream is produced regardless of whether the

SerialBlob

was created with a

Blob

object or a

byte

array.

position

```java
public long position​(byte[] pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the pattern of bytes for which to search
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given pattern begins, starting at the specified
position;

-1

if the pattern is not found
or the given starting position is out of bounds; position
numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

---

#### position

public long position​(byte[] pattern,
long start)
throws

SerialException

,

SQLException

Returns the position in this

SerialBlob

object where
the given pattern of bytes begins, starting the search at the
specified position.

position

```java
public long position​(
Blob
pattern,
long start)
throws
SerialException
,

SQLException
```

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

**Specified by:** position

in interface

Blob
**Parameters:** pattern

- the

Blob

object for which to search;
**Parameters:** start

- the position of the byte in this

SerialBlob

object from which to begin
the search; the first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object
**Returns:** the position in this

SerialBlob

object
where the given

Blob

object begins, starting
at the specified position;

-1

if the pattern is
not found or the given starting position is out of bounds;
position numbering for the return value starts at

1
**Throws:** SerialException

- if an error occurs when serializing the blob;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database

---

#### position

public long position​(

Blob

pattern,
long start)
throws

SerialException

,

SQLException

Returns the position in this

SerialBlob

object where
the given

Blob

object begins, starting the search at the
specified position.

setBytes

```java
public int setBytes​(long pos,
byte[] bytes)
throws
SerialException
,

SQLException
```

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the SQL

BLOB

value at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; or if an invalid position is set; if an
invalid offset value is set;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database
**See Also:** getBytes(long, int)

---

#### setBytes

public int setBytes​(long pos,
byte[] bytes)
throws

SerialException

,

SQLException

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.

setBytes

```java
public int setBytes​(long pos,
byte[] bytes,
int offset,
int length)
throws
SerialException
,

SQLException
```

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.
Writing starts at position

pos

in the

BLOB

value;

len

bytes from the given byte array are written.

**Specified by:** setBytes

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

object at which
to start writing. The first position is

1

;
must not be less than

1

nor greater than
the length of this

SerialBlob

object.
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value
**Parameters:** offset

- the offset in the

byte

array at which
to start reading the bytes. The first offset position is

0

; must not be less than

0

nor greater
than the length of the

byte

array
**Parameters:** length

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes

.
**Returns:** the number of bytes written
**Throws:** SerialException

- if there is an error accessing the

BLOB

value; if an invalid position is set; if an
invalid offset value is set; if number of bytes to be written
is greater than the

SerialBlob

length; or the combined
values of the length and offset is greater than the Blob buffer;
if

free

had previously been called on this object
**Throws:** SQLException

- if there is an error accessing the

BLOB

value from the database.
**See Also:** getBytes(long, int)

---

#### setBytes

public int setBytes​(long pos,
byte[] bytes,
int offset,
int length)
throws

SerialException

,

SQLException

Writes all or part of the given

byte

array to the

BLOB

value that this

Blob

object represents
and returns the number of bytes written.
Writing starts at position

pos

in the

BLOB

value;

len

bytes from the given byte array are written.

setBinaryStream

```java
public
OutputStream
setBinaryStream​(long pos)
throws
SerialException
,

SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

. This method forwards the

setBinaryStream()

call to the underlying

Blob

in
the event that this

SerialBlob

object is instantiated with a

Blob

. If this

SerialBlob

is instantiated with
a

byte

array, a

SerialException

is thrown.

**Specified by:** setBinaryStream

in interface

Blob
**Parameters:** pos

- the position in the

BLOB

value at which
to start writing
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SerialException

- if the SerialBlob in not instantiated with a

Blob

object that supports

setBinaryStream()

;
if

free

had previously been called on this object
**See Also:** getBinaryStream()

---

#### setBinaryStream

public

OutputStream

setBinaryStream​(long pos)
throws

SerialException

,

SQLException

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

. This method forwards the

setBinaryStream()

call to the underlying

Blob

in
the event that this

SerialBlob

object is instantiated with a

Blob

. If this

SerialBlob

is instantiated with
a

byte

array, a

SerialException

is thrown.

truncate

```java
public void truncate​(long length)
throws
SerialException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

**Specified by:** truncate

in interface

Blob
**Parameters:** length

- the length, in bytes, to which the

BLOB

value that this

Blob

object represents should be
truncated
**Throws:** SerialException

- if there is an error accessing the Blob value;
or the length to truncate is greater that the SerialBlob length;
if

free

had previously been called on this object

---

#### truncate

public void truncate​(long length)
throws

SerialException

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

getBinaryStream

```java
public
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

**Specified by:** getBinaryStream

in interface

Blob
**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which the partial

Blob

value can
be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater than the
number of bytes in the

Blob

or if pos + length is greater than
the number of bytes in the

Blob
**Throws:** SerialException

- if the

free

method had been previously
called on this object
**Since:** 1.6

---

#### getBinaryStream

public

InputStream

getBinaryStream​(long pos,
long length)
throws

SQLException

Returns an

InputStream

object that contains a partial

Blob

value, starting with the byte specified by pos, which is
length bytes in length.

free

```java
public void free()
throws
SQLException
```

This method frees the

SerialBlob

object and releases the
resources that it holds. The object is invalid once the

free

method is called.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

**Specified by:** free

in interface

Blob
**Throws:** SQLException

- if an error occurs releasing the Blob's resources
**Since:** 1.6

---

#### free

public void free()
throws

SQLException

This method frees the

SerialBlob

object and releases the
resources that it holds. The object is invalid once the

free

method is called.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

If

free

is called multiple times, the
subsequent calls to

free

are treated as a no-op.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this SerialBlob to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialBlob

object that represents the same sequence of bytes as this
object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to compare this

SerialBlob

against
**Returns:** true

if the given object represents a

SerialBlob

equivalent to this SerialBlob,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this SerialBlob to the specified object. The result is

true

if and only if the argument is not

null

and is a

SerialBlob

object that represents the same sequence of bytes as this
object.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

SerialBlob

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

SerialBlob

.

clone

```java
public
Object
clone()
```

Returns a clone of this

SerialBlob

. The copy will contain a
reference to a clone of the internal byte array, not a reference
to the original internal byte array of this

SerialBlob

object.
The underlying

Blob

object will be set to null.

**Overrides:** clone

in class

Object
**Returns:** a clone of this SerialBlob
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this

SerialBlob

. The copy will contain a
reference to a clone of the internal byte array, not a reference
to the original internal byte array of this

SerialBlob

object.
The underlying

Blob

object will be set to null.

---

