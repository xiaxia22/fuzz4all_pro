# Interface Blob

**Source:** `java.sql\java\sql\Blob.html`

### Class Description

```java
public interface
Blob
```

The representation (mapping) in
the Java™ programming language of an SQL

BLOB

value. An SQL

BLOB

is a built-in type
that stores a Binary Large Object as a column value in a row of
a database table. By default drivers implement

Blob

using
an SQL

locator(BLOB)

, which means that a

Blob

object contains a logical pointer to the
SQL

BLOB

data rather than the data itself.
A

Blob

object is valid for the duration of the
transaction in which is was created.

Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getBlob

and

setBlob

allow a programmer to
access an SQL

BLOB

value.
The

Blob

interface provides methods for getting the
length of an SQL

BLOB

(Binary Large Object) value,
for materializing a

BLOB

value on the client, and for
determining the position of a pattern of bytes within a

BLOB

value. In addition, this interface has methods for updating
a

BLOB

value.

All methods on the

Blob

interface must be fully implemented if the
JDBC driver supports the data type.

**All Known Implementing Classes:** SerialBlob

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long length()
throws
SQLException

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

**Returns:**
- length of the

BLOB

in bytes

**Throws:**
- SQLException

- if there is an error accessing the
length of the

BLOB
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.2

---

#### byte[] getBytes​(long pos,
int length)
throws
SQLException

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes. This

byte

array contains up to

length

consecutive bytes starting at position

pos

.

**Parameters:**
- pos

- the ordinal position of the first byte in the

BLOB

value to be extracted; the first byte is at
position 1
- length

- the number of consecutive bytes to be copied; the value
for length must be 0 or greater

**Returns:**
- a byte array containing up to

length

consecutive bytes from the

BLOB

value designated
by this

Blob

object, starting with the
byte at position

pos

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value; if pos is less than 1 or length is
less than 0
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**See Also:**
- setBytes(long, byte[])

**Since:**
- 1.2

---

#### InputStream
getBinaryStream()
throws
SQLException

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

**Returns:**
- a stream containing the

BLOB

data

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**See Also:**
- setBinaryStream(long)

**Since:**
- 1.2

---

#### long position​(byte[] pattern,
long start)
throws
SQLException

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.
The search for

pattern

begins at position

start

.

**Parameters:**
- pattern

- the byte array for which to search
- start

- the position at which to begin searching; the
first position is 1

**Returns:**
- the position at which the pattern appears, else -1

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

or if start is less than 1
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.2

---

#### long position​(
Blob
pattern,
long start)
throws
SQLException

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins. The search begins at position

start

.

**Parameters:**
- pattern

- the

Blob

object designating
the

BLOB

value for which to search
- start

- the position in the

BLOB

value
at which to begin searching; the first position is 1

**Returns:**
- the position at which the pattern begins, else -1

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value or if start is less than 1
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.2

---

#### int setBytes​(long pos,
byte[] bytes)
throws
SQLException

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:**
- pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
- bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents

**Returns:**
- the number of bytes written

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**See Also:**
- getBytes(long, int)

**Since:**
- 1.4

---

#### int setBytes​(long pos,
byte[] bytes,
int offset,
int len)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:**
- pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
- bytes

- the array of bytes to be written to this

BLOB

object
- offset

- the offset into the array

bytes

at which
to start reading the bytes to be set
- len

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes

**Returns:**
- the number of bytes written

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**See Also:**
- getBytes(long, int)

**Since:**
- 1.4

---

#### OutputStream
setBinaryStream​(long pos)
throws
SQLException

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

.
The bytes written to the stream will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing to the stream, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:**
- pos

- the position in the

BLOB

value at which
to start writing; the first position is 1

**Returns:**
- a

java.io.OutputStream

object to which data can
be written

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**See Also:**
- getBinaryStream()

**Since:**
- 1.4

---

#### void truncate​(long len)
throws
SQLException

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:**
- len

- the length, in bytes, to which the

BLOB

value
that this

Blob

object represents should be truncated

**Throws:**
- SQLException

- if there is an error accessing the

BLOB

value or if len is less than 0
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.4

---

#### void free()
throws
SQLException

This method frees the

Blob

object and releases the resources that
it holds. The object is invalid once the

free

method is called.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

**Throws:**
- SQLException

- if an error occurs releasing
the Blob's resources
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.6

---

#### InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

**Parameters:**
- pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1.
- length

- the length in bytes of the partial value to be retrieved

**Returns:**
- InputStream

through which
the partial

Blob

value can be read.

**Throws:**
- SQLException

- if pos is less than 1 or if pos is greater
than the number of bytes in the

Blob

or if
pos + length is greater than the number of bytes
in the

Blob
- SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method

**Since:**
- 1.6

---

### Additional Sections

#### Interface Blob

**All Known Implementing Classes:** SerialBlob

```java
public interface
Blob
```

The representation (mapping) in
the Java™ programming language of an SQL

BLOB

value. An SQL

BLOB

is a built-in type
that stores a Binary Large Object as a column value in a row of
a database table. By default drivers implement

Blob

using
an SQL

locator(BLOB)

, which means that a

Blob

object contains a logical pointer to the
SQL

BLOB

data rather than the data itself.
A

Blob

object is valid for the duration of the
transaction in which is was created.

Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getBlob

and

setBlob

allow a programmer to
access an SQL

BLOB

value.
The

Blob

interface provides methods for getting the
length of an SQL

BLOB

(Binary Large Object) value,
for materializing a

BLOB

value on the client, and for
determining the position of a pattern of bytes within a

BLOB

value. In addition, this interface has methods for updating
a

BLOB

value.

All methods on the

Blob

interface must be fully implemented if the
JDBC driver supports the data type.

**Since:** 1.2

public interface

Blob

The representation (mapping) in
the Java™ programming language of an SQL

BLOB

value. An SQL

BLOB

is a built-in type
that stores a Binary Large Object as a column value in a row of
a database table. By default drivers implement

Blob

using
an SQL

locator(BLOB)

, which means that a

Blob

object contains a logical pointer to the
SQL

BLOB

data rather than the data itself.
A

Blob

object is valid for the duration of the
transaction in which is was created.

Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getBlob

and

setBlob

allow a programmer to
access an SQL

BLOB

value.
The

Blob

interface provides methods for getting the
length of an SQL

BLOB

(Binary Large Object) value,
for materializing a

BLOB

value on the client, and for
determining the position of a pattern of bytes within a

BLOB

value. In addition, this interface has methods for updating
a

BLOB

value.

All methods on the

Blob

interface must be fully implemented if the
JDBC driver supports the data type.

Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getBlob

and

setBlob

allow a programmer to
access an SQL

BLOB

value.
The

Blob

interface provides methods for getting the
length of an SQL

BLOB

(Binary Large Object) value,
for materializing a

BLOB

value on the client, and for
determining the position of a pattern of bytes within a

BLOB

value. In addition, this interface has methods for updating
a

BLOB

value.

All methods on the

Blob

interface must be fully implemented if the
JDBC driver supports the data type.

All methods on the

Blob

interface must be fully implemented if the
JDBC driver supports the data type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

free

()

This method frees the

Blob

object and releases the resources that
it holds.

InputStream

getBinaryStream

()

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

InputStream

getBinaryStream

​(long pos,
long length)

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

byte[]

getBytes

​(long pos,
int length)

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes.

long

length

()

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

long

position

​(byte[] pattern,
long start)

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.

long

position

​(

Blob

pattern,
long start)

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins.

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
int len)

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

​(long len)

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

free

()

This method frees the

Blob

object and releases the resources that
it holds.

InputStream

getBinaryStream

()

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

InputStream

getBinaryStream

​(long pos,
long length)

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

byte[]

getBytes

​(long pos,
int length)

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes.

long

length

()

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

long

position

​(byte[] pattern,
long start)

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.

long

position

​(

Blob

pattern,
long start)

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins.

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
int len)

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

​(long len)

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

---

#### Method Summary

This method frees the

Blob

object and releases the resources that
it holds.

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes.

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins.

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

============ METHOD DETAIL ==========

- Method Detail

- length

```java
long length()
throws
SQLException
```

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

**Returns:** length of the

BLOB

in bytes
**Throws:** SQLException

- if there is an error accessing the
length of the

BLOB
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- getBytes

```java
byte[] getBytes​(long pos,
int length)
throws
SQLException
```

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes. This

byte

array contains up to

length

consecutive bytes starting at position

pos

.

**Parameters:** pos

- the ordinal position of the first byte in the

BLOB

value to be extracted; the first byte is at
position 1
**Parameters:** length

- the number of consecutive bytes to be copied; the value
for length must be 0 or greater
**Returns:** a byte array containing up to

length

consecutive bytes from the

BLOB

value designated
by this

Blob

object, starting with the
byte at position

pos
**Throws:** SQLException

- if there is an error accessing the

BLOB

value; if pos is less than 1 or length is
less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBytes(long, byte[])

- getBinaryStream

```java
InputStream
getBinaryStream()
throws
SQLException
```

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

**Returns:** a stream containing the

BLOB

data
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBinaryStream(long)

- position

```java
long position​(byte[] pattern,
long start)
throws
SQLException
```

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.
The search for

pattern

begins at position

start

.

**Parameters:** pattern

- the byte array for which to search
**Parameters:** start

- the position at which to begin searching; the
first position is 1
**Returns:** the position at which the pattern appears, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- position

```java
long position​(
Blob
pattern,
long start)
throws
SQLException
```

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins. The search begins at position

start

.

**Parameters:** pattern

- the

Blob

object designating
the

BLOB

value for which to search
**Parameters:** start

- the position in the

BLOB

value
at which to begin searching; the first position is 1
**Returns:** the position at which the pattern begins, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- setBytes

```java
int setBytes​(long pos,
byte[] bytes)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

- setBytes

```java
int setBytes​(long pos,
byte[] bytes,
int offset,
int len)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to this

BLOB

object
**Parameters:** offset

- the offset into the array

bytes

at which
to start reading the bytes to be set
**Parameters:** len

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

- setBinaryStream

```java
OutputStream
setBinaryStream​(long pos)
throws
SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

.
The bytes written to the stream will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing to the stream, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

value at which
to start writing; the first position is 1
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBinaryStream()

- truncate

```java
void truncate​(long len)
throws
SQLException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** len

- the length, in bytes, to which the

BLOB

value
that this

Blob

object represents should be truncated
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if len is less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4

- free

```java
void free()
throws
SQLException
```

This method frees the

Blob

object and releases the resources that
it holds. The object is invalid once the

free

method is called.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

**Throws:** SQLException

- if an error occurs releasing
the Blob's resources
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

- getBinaryStream

```java
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1.
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which
the partial

Blob

value can be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater
than the number of bytes in the

Blob

or if
pos + length is greater than the number of bytes
in the

Blob
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

Method Detail

- length

```java
long length()
throws
SQLException
```

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

**Returns:** length of the

BLOB

in bytes
**Throws:** SQLException

- if there is an error accessing the
length of the

BLOB
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- getBytes

```java
byte[] getBytes​(long pos,
int length)
throws
SQLException
```

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes. This

byte

array contains up to

length

consecutive bytes starting at position

pos

.

**Parameters:** pos

- the ordinal position of the first byte in the

BLOB

value to be extracted; the first byte is at
position 1
**Parameters:** length

- the number of consecutive bytes to be copied; the value
for length must be 0 or greater
**Returns:** a byte array containing up to

length

consecutive bytes from the

BLOB

value designated
by this

Blob

object, starting with the
byte at position

pos
**Throws:** SQLException

- if there is an error accessing the

BLOB

value; if pos is less than 1 or length is
less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBytes(long, byte[])

- getBinaryStream

```java
InputStream
getBinaryStream()
throws
SQLException
```

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

**Returns:** a stream containing the

BLOB

data
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBinaryStream(long)

- position

```java
long position​(byte[] pattern,
long start)
throws
SQLException
```

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.
The search for

pattern

begins at position

start

.

**Parameters:** pattern

- the byte array for which to search
**Parameters:** start

- the position at which to begin searching; the
first position is 1
**Returns:** the position at which the pattern appears, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- position

```java
long position​(
Blob
pattern,
long start)
throws
SQLException
```

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins. The search begins at position

start

.

**Parameters:** pattern

- the

Blob

object designating
the

BLOB

value for which to search
**Parameters:** start

- the position in the

BLOB

value
at which to begin searching; the first position is 1
**Returns:** the position at which the pattern begins, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

- setBytes

```java
int setBytes​(long pos,
byte[] bytes)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

- setBytes

```java
int setBytes​(long pos,
byte[] bytes,
int offset,
int len)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to this

BLOB

object
**Parameters:** offset

- the offset into the array

bytes

at which
to start reading the bytes to be set
**Parameters:** len

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

- setBinaryStream

```java
OutputStream
setBinaryStream​(long pos)
throws
SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

.
The bytes written to the stream will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing to the stream, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

value at which
to start writing; the first position is 1
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBinaryStream()

- truncate

```java
void truncate​(long len)
throws
SQLException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** len

- the length, in bytes, to which the

BLOB

value
that this

Blob

object represents should be truncated
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if len is less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4

- free

```java
void free()
throws
SQLException
```

This method frees the

Blob

object and releases the resources that
it holds. The object is invalid once the

free

method is called.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

**Throws:** SQLException

- if an error occurs releasing
the Blob's resources
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

- getBinaryStream

```java
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1.
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which
the partial

Blob

value can be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater
than the number of bytes in the

Blob

or if
pos + length is greater than the number of bytes
in the

Blob
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

---

#### Method Detail

length

```java
long length()
throws
SQLException
```

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

**Returns:** length of the

BLOB

in bytes
**Throws:** SQLException

- if there is an error accessing the
length of the

BLOB
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

---

#### length

long length()
throws

SQLException

Returns the number of bytes in the

BLOB

value
designated by this

Blob

object.

getBytes

```java
byte[] getBytes​(long pos,
int length)
throws
SQLException
```

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes. This

byte

array contains up to

length

consecutive bytes starting at position

pos

.

**Parameters:** pos

- the ordinal position of the first byte in the

BLOB

value to be extracted; the first byte is at
position 1
**Parameters:** length

- the number of consecutive bytes to be copied; the value
for length must be 0 or greater
**Returns:** a byte array containing up to

length

consecutive bytes from the

BLOB

value designated
by this

Blob

object, starting with the
byte at position

pos
**Throws:** SQLException

- if there is an error accessing the

BLOB

value; if pos is less than 1 or length is
less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBytes(long, byte[])

---

#### getBytes

byte[] getBytes​(long pos,
int length)
throws

SQLException

Retrieves all or part of the

BLOB

value that this

Blob

object represents, as an array of
bytes. This

byte

array contains up to

length

consecutive bytes starting at position

pos

.

getBinaryStream

```java
InputStream
getBinaryStream()
throws
SQLException
```

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

**Returns:** a stream containing the

BLOB

data
**Throws:** SQLException

- if there is an error accessing the

BLOB

value
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2
**See Also:** setBinaryStream(long)

---

#### getBinaryStream

InputStream

getBinaryStream()
throws

SQLException

Retrieves the

BLOB

value designated by this

Blob

instance as a stream.

position

```java
long position​(byte[] pattern,
long start)
throws
SQLException
```

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.
The search for

pattern

begins at position

start

.

**Parameters:** pattern

- the byte array for which to search
**Parameters:** start

- the position at which to begin searching; the
first position is 1
**Returns:** the position at which the pattern appears, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

---

#### position

long position​(byte[] pattern,
long start)
throws

SQLException

Retrieves the byte position at which the specified byte array

pattern

begins within the

BLOB

value that this

Blob

object represents.
The search for

pattern

begins at position

start

.

position

```java
long position​(
Blob
pattern,
long start)
throws
SQLException
```

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins. The search begins at position

start

.

**Parameters:** pattern

- the

Blob

object designating
the

BLOB

value for which to search
**Parameters:** start

- the position in the

BLOB

value
at which to begin searching; the first position is 1
**Returns:** the position at which the pattern begins, else -1
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if start is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.2

---

#### position

long position​(

Blob

pattern,
long start)
throws

SQLException

Retrieves the byte position in the

BLOB

value
designated by this

Blob

object at which

pattern

begins. The search begins at position

start

.

setBytes

```java
int setBytes​(long pos,
byte[] bytes)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to the

BLOB

value that this

Blob

object represents
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

---

#### setBytes

int setBytes​(long pos,
byte[] bytes)
throws

SQLException

Writes the given array of bytes to the

BLOB

value that
this

Blob

object represents, starting at position

pos

, and returns the number of bytes written.
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

setBytes

```java
int setBytes​(long pos,
byte[] bytes,
int offset,
int len)
throws
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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

object at which
to start writing; the first position is 1
**Parameters:** bytes

- the array of bytes to be written to this

BLOB

object
**Parameters:** offset

- the offset into the array

bytes

at which
to start reading the bytes to be set
**Parameters:** len

- the number of bytes to be written to the

BLOB

value from the array of bytes

bytes
**Returns:** the number of bytes written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBytes(long, int)

---

#### setBytes

int setBytes​(long pos,
byte[] bytes,
int offset,
int len)
throws

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
The array of bytes will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing the array of bytes, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

setBinaryStream

```java
OutputStream
setBinaryStream​(long pos)
throws
SQLException
```

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

.
The bytes written to the stream will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing to the stream, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** pos

- the position in the

BLOB

value at which
to start writing; the first position is 1
**Returns:** a

java.io.OutputStream

object to which data can
be written
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if pos is less than 1
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4
**See Also:** getBinaryStream()

---

#### setBinaryStream

OutputStream

setBinaryStream​(long pos)
throws

SQLException

Retrieves a stream that can be used to write to the

BLOB

value that this

Blob

object represents. The stream begins
at position

pos

.
The bytes written to the stream will overwrite the existing bytes
in the

Blob

object starting at the position

pos

. If the end of the

Blob

value is reached
while writing to the stream, then the length of the

Blob

value will be increased to accommodate the extra bytes.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

truncate

```java
void truncate​(long len)
throws
SQLException
```

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

**Parameters:** len

- the length, in bytes, to which the

BLOB

value
that this

Blob

object represents should be truncated
**Throws:** SQLException

- if there is an error accessing the

BLOB

value or if len is less than 0
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.4

---

#### truncate

void truncate​(long len)
throws

SQLException

Truncates the

BLOB

value that this

Blob

object represents to be

len

bytes in length.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

Note:

If the value specified for

pos

is greater than the length+1 of the

BLOB

value then the
behavior is undefined. Some JDBC drivers may throw an

SQLException

while other drivers may support this
operation.

free

```java
void free()
throws
SQLException
```

This method frees the

Blob

object and releases the resources that
it holds. The object is invalid once the

free

method is called.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

**Throws:** SQLException

- if an error occurs releasing
the Blob's resources
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

---

#### free

void free()
throws

SQLException

This method frees the

Blob

object and releases the resources that
it holds. The object is invalid once the

free

method is called.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

After

free

has been called, any attempt to invoke a
method other than

free

will result in an

SQLException

being thrown. If

free

is called multiple times, the subsequent
calls to

free

are treated as a no-op.

getBinaryStream

```java
InputStream
getBinaryStream​(long pos,
long length)
throws
SQLException
```

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

**Parameters:** pos

- the offset to the first byte of the partial value to be
retrieved. The first byte in the

Blob

is at position 1.
**Parameters:** length

- the length in bytes of the partial value to be retrieved
**Returns:** InputStream

through which
the partial

Blob

value can be read.
**Throws:** SQLException

- if pos is less than 1 or if pos is greater
than the number of bytes in the

Blob

or if
pos + length is greater than the number of bytes
in the

Blob
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver
does not support this method
**Since:** 1.6

---

#### getBinaryStream

InputStream

getBinaryStream​(long pos,
long length)
throws

SQLException

Returns an

InputStream

object that contains
a partial

Blob

value, starting with the byte
specified by pos, which is length bytes in length.

---

