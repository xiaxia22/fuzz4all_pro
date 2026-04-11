# Class Inflater

**Source:** `java.base\java\util\zip\Inflater.html`

### Class Description

```java
public class
Inflater

extends
Object
```

This class provides support for general purpose decompression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class inflates sequences of ZLIB compressed bytes. The input byte
sequence is provided in either byte array or byte buffer, via one of the

setInput()

methods. The output byte sequence is written to the
output byte array or byte buffer passed to the

deflate()

methods.

The following code fragment demonstrates a trivial compression
and decompression of a string using

Deflater

and

Inflater

.

```java
try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}
```

**API Note:** To release resources used by this

Inflater

, the

end()

method
should be called explicitly. Subclasses are responsible for the cleanup of resources
acquired by the subclass. Subclasses that override

finalize()

in order
to perform cleanup should be modified to use alternative cleanup mechanisms such
as

Cleaner

and remove the overriding

finalize

method.
**Implementation Requirements:** If this

Inflater

has been subclassed and the

end

method has been
overridden, the

end

method will be called by the finalization when the
inflater is unreachable. But the subclasses should not depend on this specific
implementation; the finalization is not reliable and the

finalize

method
is deprecated to be removed.
**Since:** 1.1
**See Also:** Deflater

---

### Field Details

*No entries found.*

### Constructor Details

#### public Inflater​(boolean nowrap)

Creates a new decompressor. If the parameter 'nowrap' is true then
the ZLIB header and checksum fields will not be used. This provides
compatibility with the compression format used by both GZIP and PKZIP.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

**Parameters:**
- nowrap

- if true then support GZIP compatible compression

---

#### public Inflater()

Creates a new decompressor.

---

### Method Details

#### public void setInput​(byte[] input,
int off,
int len)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:**
- input

- the input data bytes
- off

- the start offset of the input data
- len

- the length of the input data

**See Also:**
- needsInput()

---

#### public void setInput​(byte[] input)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:**
- input

- the input data bytes

**See Also:**
- needsInput()

---

#### public void setInput​(
ByteBuffer
input)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

**Parameters:**
- input

- the input data bytes

**See Also:**
- needsInput()

**Since:**
- 11

---

#### public void setDictionary​(byte[] dictionary,
int off,
int len)

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:**
- dictionary

- the dictionary data bytes
- off

- the start offset of the data
- len

- the length of the data

**See Also:**
- needsDictionary()

,

getAdler()

---

#### public void setDictionary​(byte[] dictionary)

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:**
- dictionary

- the dictionary data bytes

**See Also:**
- needsDictionary()

,

getAdler()

---

#### public void setDictionary​(
ByteBuffer
dictionary)

Sets the preset dictionary to the bytes in the given buffer. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:**
- dictionary

- the dictionary data bytes

**See Also:**
- needsDictionary()

,

getAdler()

**Since:**
- 11

---

#### public int getRemaining()

Returns the total number of bytes remaining in the input buffer.
This can be used to find out what bytes still remain in the input
buffer after decompression has finished.

**Returns:**
- the total number of bytes remaining in the input buffer

---

#### public boolean needsInput()

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:**
- true if no data remains in the input buffer

---

#### public boolean needsDictionary()

Returns true if a preset dictionary is needed for decompression.

**Returns:**
- true if a preset dictionary is needed for decompression

**See Also:**
- setDictionary(byte[], int, int)

---

#### public boolean finished()

Returns true if the end of the compressed data stream has been
reached.

**Returns:**
- true if the end of the compressed data stream has been
reached

---

#### public int inflate​(byte[] output,
int off,
int len)
throws
DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:**
- output

- the buffer for the uncompressed data
- off

- the start offset of the data
- len

- the maximum number of uncompressed bytes

**Returns:**
- the actual number of uncompressed bytes

**Throws:**
- DataFormatException

- if the compressed data format is invalid

**See Also:**
- needsInput()

,

needsDictionary()

---

#### public int inflate​(byte[] output)
throws
DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:**
- output

- the buffer for the uncompressed data

**Returns:**
- the actual number of uncompressed bytes

**Throws:**
- DataFormatException

- if the compressed data format is invalid

**See Also:**
- needsInput()

,

needsDictionary()

---

#### public int inflate​(
ByteBuffer
output)
throws
DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:**
- output

- the buffer for the uncompressed data

**Returns:**
- the actual number of uncompressed bytes

**Throws:**
- DataFormatException

- if the compressed data format is invalid
- ReadOnlyBufferException

- if the given output buffer is read-only

**See Also:**
- needsInput()

,

needsDictionary()

**Since:**
- 11

---

#### public int getAdler()

Returns the ADLER-32 value of the uncompressed data.

**Returns:**
- the ADLER-32 value of the uncompressed data

---

#### public int getTotalIn()

Returns the total number of compressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:**
- the total number of compressed bytes input so far

---

#### public long getBytesRead()

Returns the total number of compressed bytes input so far.

**Returns:**
- the total (non-negative) number of compressed bytes input so far

**Since:**
- 1.5

---

#### public int getTotalOut()

Returns the total number of uncompressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:**
- the total number of uncompressed bytes output so far

---

#### public long getBytesWritten()

Returns the total number of uncompressed bytes output so far.

**Returns:**
- the total (non-negative) number of uncompressed bytes output so far

**Since:**
- 1.5

---

#### public void reset()

Resets inflater so that a new set of input data can be processed.

---

#### public void end()

Closes the decompressor and discards any unprocessed input.

This method should be called when the decompressor is no longer
being used. Once this method is called, the behavior of the
Inflater object is undefined.

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()

Closes the decompressor when garbage is collected.

**Overrides:**
- finalize

in class

Object

**See Also:**
- WeakReference

,

PhantomReference

**Implementation Requirements:**
- If this

Inflater

has been subclassed and the

end

method
has been overridden, the

end

method will be called when the
inflater is unreachable.

---

### Additional Sections

#### Class Inflater

java.lang.Object

- java.util.zip.Inflater

java.util.zip.Inflater

```java
public class
Inflater

extends
Object
```

This class provides support for general purpose decompression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class inflates sequences of ZLIB compressed bytes. The input byte
sequence is provided in either byte array or byte buffer, via one of the

setInput()

methods. The output byte sequence is written to the
output byte array or byte buffer passed to the

deflate()

methods.

The following code fragment demonstrates a trivial compression
and decompression of a string using

Deflater

and

Inflater

.

```java
try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}
```

**API Note:** To release resources used by this

Inflater

, the

end()

method
should be called explicitly. Subclasses are responsible for the cleanup of resources
acquired by the subclass. Subclasses that override

finalize()

in order
to perform cleanup should be modified to use alternative cleanup mechanisms such
as

Cleaner

and remove the overriding

finalize

method.
**Implementation Requirements:** If this

Inflater

has been subclassed and the

end

method has been
overridden, the

end

method will be called by the finalization when the
inflater is unreachable. But the subclasses should not depend on this specific
implementation; the finalization is not reliable and the

finalize

method
is deprecated to be removed.
**Since:** 1.1
**See Also:** Deflater

public class

Inflater

extends

Object

This class provides support for general purpose decompression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class inflates sequences of ZLIB compressed bytes. The input byte
sequence is provided in either byte array or byte buffer, via one of the

setInput()

methods. The output byte sequence is written to the
output byte array or byte buffer passed to the

deflate()

methods.

The following code fragment demonstrates a trivial compression
and decompression of a string using

Deflater

and

Inflater

.

```java
try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}
```

This class inflates sequences of ZLIB compressed bytes. The input byte
sequence is provided in either byte array or byte buffer, via one of the

setInput()

methods. The output byte sequence is written to the
output byte array or byte buffer passed to the

deflate()

methods.

The following code fragment demonstrates a trivial compression
and decompression of a string using

Deflater

and

Inflater

.

```java
try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}
```

The following code fragment demonstrates a trivial compression
and decompression of a string using

Deflater

and

Inflater

.

```java
try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}
```

try {
// Encode a String into bytes
String inputString = "blahblahblah€€";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);

// Decompress the bytes
Inflater decompresser = new Inflater();
decompresser.setInput(output, 0, compressedDataLength);
byte[] result = new byte[100];
int resultLength = decompresser.inflate(result);
decompresser.end();

// Decode the bytes into a String
String outputString = new String(result, 0, resultLength, "UTF-8");
} catch (java.io.UnsupportedEncodingException ex) {
// handle
} catch (java.util.zip.DataFormatException ex) {
// handle
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Inflater

()

Creates a new decompressor.

Inflater

​(boolean nowrap)

Creates a new decompressor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

end

()

Closes the decompressor and discards any unprocessed input.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

boolean

finished

()

Returns true if the end of the compressed data stream has been
reached.

int

getAdler

()

Returns the ADLER-32 value of the uncompressed data.

long

getBytesRead

()

Returns the total number of compressed bytes input so far.

long

getBytesWritten

()

Returns the total number of uncompressed bytes output so far.

int

getRemaining

()

Returns the total number of bytes remaining in the input buffer.

int

getTotalIn

()

Returns the total number of compressed bytes input so far.

int

getTotalOut

()

Returns the total number of uncompressed bytes output so far.

int

inflate

​(byte[] output)

Uncompresses bytes into specified buffer.

int

inflate

​(byte[] output,
int off,
int len)

Uncompresses bytes into specified buffer.

int

inflate

​(

ByteBuffer

output)

Uncompresses bytes into specified buffer.

boolean

needsDictionary

()

Returns true if a preset dictionary is needed for decompression.

boolean

needsInput

()

Returns true if no data remains in the input buffer.

void

reset

()

Resets inflater so that a new set of input data can be processed.

void

setDictionary

​(byte[] dictionary)

Sets the preset dictionary to the given array of bytes.

void

setDictionary

​(byte[] dictionary,
int off,
int len)

Sets the preset dictionary to the given array of bytes.

void

setDictionary

​(

ByteBuffer

dictionary)

Sets the preset dictionary to the bytes in the given buffer.

void

setInput

​(byte[] input)

Sets input data for decompression.

void

setInput

​(byte[] input,
int off,
int len)

Sets input data for decompression.

void

setInput

​(

ByteBuffer

input)

Sets input data for decompression.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Inflater

()

Creates a new decompressor.

Inflater

​(boolean nowrap)

Creates a new decompressor.

---

#### Constructor Summary

Creates a new decompressor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

end

()

Closes the decompressor and discards any unprocessed input.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

boolean

finished

()

Returns true if the end of the compressed data stream has been
reached.

int

getAdler

()

Returns the ADLER-32 value of the uncompressed data.

long

getBytesRead

()

Returns the total number of compressed bytes input so far.

long

getBytesWritten

()

Returns the total number of uncompressed bytes output so far.

int

getRemaining

()

Returns the total number of bytes remaining in the input buffer.

int

getTotalIn

()

Returns the total number of compressed bytes input so far.

int

getTotalOut

()

Returns the total number of uncompressed bytes output so far.

int

inflate

​(byte[] output)

Uncompresses bytes into specified buffer.

int

inflate

​(byte[] output,
int off,
int len)

Uncompresses bytes into specified buffer.

int

inflate

​(

ByteBuffer

output)

Uncompresses bytes into specified buffer.

boolean

needsDictionary

()

Returns true if a preset dictionary is needed for decompression.

boolean

needsInput

()

Returns true if no data remains in the input buffer.

void

reset

()

Resets inflater so that a new set of input data can be processed.

void

setDictionary

​(byte[] dictionary)

Sets the preset dictionary to the given array of bytes.

void

setDictionary

​(byte[] dictionary,
int off,
int len)

Sets the preset dictionary to the given array of bytes.

void

setDictionary

​(

ByteBuffer

dictionary)

Sets the preset dictionary to the bytes in the given buffer.

void

setInput

​(byte[] input)

Sets input data for decompression.

void

setInput

​(byte[] input,
int off,
int len)

Sets input data for decompression.

void

setInput

​(

ByteBuffer

input)

Sets input data for decompression.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Closes the decompressor and discards any unprocessed input.

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

Returns true if the end of the compressed data stream has been
reached.

Returns the ADLER-32 value of the uncompressed data.

Returns the total number of compressed bytes input so far.

Returns the total number of uncompressed bytes output so far.

Returns the total number of bytes remaining in the input buffer.

Uncompresses bytes into specified buffer.

Returns true if a preset dictionary is needed for decompression.

Returns true if no data remains in the input buffer.

Resets inflater so that a new set of input data can be processed.

Sets the preset dictionary to the given array of bytes.

Sets the preset dictionary to the bytes in the given buffer.

Sets input data for decompression.

Methods declared in class java.lang.

Object

clone

,

equals

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

- Inflater

```java
public Inflater​(boolean nowrap)
```

Creates a new decompressor. If the parameter 'nowrap' is true then
the ZLIB header and checksum fields will not be used. This provides
compatibility with the compression format used by both GZIP and PKZIP.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

**Parameters:** nowrap

- if true then support GZIP compatible compression

- Inflater

```java
public Inflater()
```

Creates a new decompressor.

============ METHOD DETAIL ==========

- Method Detail

- setInput

```java
public void setInput​(byte[] input,
int off,
int len)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the input data
**Parameters:** len

- the length of the input data
**See Also:** needsInput()

- setInput

```java
public void setInput​(byte[] input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**See Also:** needsInput()

- setInput

```java
public void setInput​(
ByteBuffer
input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

**Parameters:** input

- the input data bytes
**Since:** 11
**See Also:** needsInput()

- setDictionary

```java
public void setDictionary​(byte[] dictionary,
int off,
int len)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsDictionary()

,

getAdler()

- setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** needsDictionary()

,

getAdler()

- setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets the preset dictionary to the bytes in the given buffer. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**Since:** 11
**See Also:** needsDictionary()

,

getAdler()

- getRemaining

```java
public int getRemaining()
```

Returns the total number of bytes remaining in the input buffer.
This can be used to find out what bytes still remain in the input
buffer after decompression has finished.

**Returns:** the total number of bytes remaining in the input buffer

- needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if no data remains in the input buffer

- needsDictionary

```java
public boolean needsDictionary()
```

Returns true if a preset dictionary is needed for decompression.

**Returns:** true if a preset dictionary is needed for decompression
**See Also:** setDictionary(byte[], int, int)

- finished

```java
public boolean finished()
```

Returns true if the end of the compressed data stream has been
reached.

**Returns:** true if the end of the compressed data stream has been
reached

- inflate

```java
public int inflate​(byte[] output,
int off,
int len)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of uncompressed bytes
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

- inflate

```java
public int inflate​(byte[] output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

- inflate

```java
public int inflate​(
ByteBuffer
output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**Throws:** ReadOnlyBufferException

- if the given output buffer is read-only
**Since:** 11
**See Also:** needsInput()

,

needsDictionary()

- getAdler

```java
public int getAdler()
```

Returns the ADLER-32 value of the uncompressed data.

**Returns:** the ADLER-32 value of the uncompressed data

- getTotalIn

```java
public int getTotalIn()
```

Returns the total number of compressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes input so far

- getBytesRead

```java
public long getBytesRead()
```

Returns the total number of compressed bytes input so far.

**Returns:** the total (non-negative) number of compressed bytes input so far
**Since:** 1.5

- getTotalOut

```java
public int getTotalOut()
```

Returns the total number of uncompressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes output so far

- getBytesWritten

```java
public long getBytesWritten()
```

Returns the total number of uncompressed bytes output so far.

**Returns:** the total (non-negative) number of uncompressed bytes output so far
**Since:** 1.5

- reset

```java
public void reset()
```

Resets inflater so that a new set of input data can be processed.

- end

```java
public void end()
```

Closes the decompressor and discards any unprocessed input.

This method should be called when the decompressor is no longer
being used. Once this method is called, the behavior of the
Inflater object is undefined.

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to use
alternative cleanup mechanisms and remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable,

Closes the decompressor when garbage is collected.

**Overrides:** finalize

in class

Object
**Implementation Requirements:** If this

Inflater

has been subclassed and the

end

method
has been overridden, the

end

method will be called when the
inflater is unreachable.
**See Also:** WeakReference

,

PhantomReference

Constructor Detail

- Inflater

```java
public Inflater​(boolean nowrap)
```

Creates a new decompressor. If the parameter 'nowrap' is true then
the ZLIB header and checksum fields will not be used. This provides
compatibility with the compression format used by both GZIP and PKZIP.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

**Parameters:** nowrap

- if true then support GZIP compatible compression

- Inflater

```java
public Inflater()
```

Creates a new decompressor.

---

#### Constructor Detail

Inflater

```java
public Inflater​(boolean nowrap)
```

Creates a new decompressor. If the parameter 'nowrap' is true then
the ZLIB header and checksum fields will not be used. This provides
compatibility with the compression format used by both GZIP and PKZIP.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

**Parameters:** nowrap

- if true then support GZIP compatible compression

---

#### Inflater

public Inflater​(boolean nowrap)

Creates a new decompressor. If the parameter 'nowrap' is true then
the ZLIB header and checksum fields will not be used. This provides
compatibility with the compression format used by both GZIP and PKZIP.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

Note: When using the 'nowrap' option it is also necessary to provide
an extra "dummy" byte as input. This is required by the ZLIB native
library in order to support certain optimizations.

Inflater

```java
public Inflater()
```

Creates a new decompressor.

---

#### Inflater

public Inflater()

Creates a new decompressor.

Method Detail

- setInput

```java
public void setInput​(byte[] input,
int off,
int len)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the input data
**Parameters:** len

- the length of the input data
**See Also:** needsInput()

- setInput

```java
public void setInput​(byte[] input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**See Also:** needsInput()

- setInput

```java
public void setInput​(
ByteBuffer
input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

**Parameters:** input

- the input data bytes
**Since:** 11
**See Also:** needsInput()

- setDictionary

```java
public void setDictionary​(byte[] dictionary,
int off,
int len)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsDictionary()

,

getAdler()

- setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** needsDictionary()

,

getAdler()

- setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets the preset dictionary to the bytes in the given buffer. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**Since:** 11
**See Also:** needsDictionary()

,

getAdler()

- getRemaining

```java
public int getRemaining()
```

Returns the total number of bytes remaining in the input buffer.
This can be used to find out what bytes still remain in the input
buffer after decompression has finished.

**Returns:** the total number of bytes remaining in the input buffer

- needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if no data remains in the input buffer

- needsDictionary

```java
public boolean needsDictionary()
```

Returns true if a preset dictionary is needed for decompression.

**Returns:** true if a preset dictionary is needed for decompression
**See Also:** setDictionary(byte[], int, int)

- finished

```java
public boolean finished()
```

Returns true if the end of the compressed data stream has been
reached.

**Returns:** true if the end of the compressed data stream has been
reached

- inflate

```java
public int inflate​(byte[] output,
int off,
int len)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of uncompressed bytes
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

- inflate

```java
public int inflate​(byte[] output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

- inflate

```java
public int inflate​(
ByteBuffer
output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**Throws:** ReadOnlyBufferException

- if the given output buffer is read-only
**Since:** 11
**See Also:** needsInput()

,

needsDictionary()

- getAdler

```java
public int getAdler()
```

Returns the ADLER-32 value of the uncompressed data.

**Returns:** the ADLER-32 value of the uncompressed data

- getTotalIn

```java
public int getTotalIn()
```

Returns the total number of compressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes input so far

- getBytesRead

```java
public long getBytesRead()
```

Returns the total number of compressed bytes input so far.

**Returns:** the total (non-negative) number of compressed bytes input so far
**Since:** 1.5

- getTotalOut

```java
public int getTotalOut()
```

Returns the total number of uncompressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes output so far

- getBytesWritten

```java
public long getBytesWritten()
```

Returns the total number of uncompressed bytes output so far.

**Returns:** the total (non-negative) number of uncompressed bytes output so far
**Since:** 1.5

- reset

```java
public void reset()
```

Resets inflater so that a new set of input data can be processed.

- end

```java
public void end()
```

Closes the decompressor and discards any unprocessed input.

This method should be called when the decompressor is no longer
being used. Once this method is called, the behavior of the
Inflater object is undefined.

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to use
alternative cleanup mechanisms and remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable,

Closes the decompressor when garbage is collected.

**Overrides:** finalize

in class

Object
**Implementation Requirements:** If this

Inflater

has been subclassed and the

end

method
has been overridden, the

end

method will be called when the
inflater is unreachable.
**See Also:** WeakReference

,

PhantomReference

---

#### Method Detail

setInput

```java
public void setInput​(byte[] input,
int off,
int len)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the input data
**Parameters:** len

- the length of the input data
**See Also:** needsInput()

---

#### setInput

public void setInput​(byte[] input,
int off,
int len)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

setInput

```java
public void setInput​(byte[] input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**See Also:** needsInput()

---

#### setInput

public void setInput​(byte[] input)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

setInput

```java
public void setInput​(
ByteBuffer
input)
```

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

**Parameters:** input

- the input data bytes
**Since:** 11
**See Also:** needsInput()

---

#### setInput

public void setInput​(

ByteBuffer

input)

Sets input data for decompression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

The given buffer's position will be advanced as inflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between inflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

Modifying the input buffer's contents, position, or limit
concurrently with an inflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

setDictionary

```java
public void setDictionary​(byte[] dictionary,
int off,
int len)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsDictionary()

,

getAdler()

---

#### setDictionary

public void setDictionary​(byte[] dictionary,
int off,
int len)

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** needsDictionary()

,

getAdler()

---

#### setDictionary

public void setDictionary​(byte[] dictionary)

Sets the preset dictionary to the given array of bytes. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets the preset dictionary to the bytes in the given buffer. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**Since:** 11
**See Also:** needsDictionary()

,

getAdler()

---

#### setDictionary

public void setDictionary​(

ByteBuffer

dictionary)

Sets the preset dictionary to the bytes in the given buffer. Should be
called when inflate() returns 0 and needsDictionary() returns true
indicating that a preset dictionary is required. The method getAdler()
can be used to get the Adler-32 value of the dictionary needed.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

getRemaining

```java
public int getRemaining()
```

Returns the total number of bytes remaining in the input buffer.
This can be used to find out what bytes still remain in the input
buffer after decompression has finished.

**Returns:** the total number of bytes remaining in the input buffer

---

#### getRemaining

public int getRemaining()

Returns the total number of bytes remaining in the input buffer.
This can be used to find out what bytes still remain in the input
buffer after decompression has finished.

needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if no data remains in the input buffer

---

#### needsInput

public boolean needsInput()

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

needsDictionary

```java
public boolean needsDictionary()
```

Returns true if a preset dictionary is needed for decompression.

**Returns:** true if a preset dictionary is needed for decompression
**See Also:** setDictionary(byte[], int, int)

---

#### needsDictionary

public boolean needsDictionary()

Returns true if a preset dictionary is needed for decompression.

finished

```java
public boolean finished()
```

Returns true if the end of the compressed data stream has been
reached.

**Returns:** true if the end of the compressed data stream has been
reached

---

#### finished

public boolean finished()

Returns true if the end of the compressed data stream has been
reached.

inflate

```java
public int inflate​(byte[] output,
int off,
int len)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of uncompressed bytes
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

---

#### inflate

public int inflate​(byte[] output,
int off,
int len)
throws

DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation, even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

inflate

```java
public int inflate​(byte[] output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**See Also:** needsInput()

,

needsDictionary()

---

#### inflate

public int inflate​(byte[] output)
throws

DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

inflate

```java
public int inflate​(
ByteBuffer
output)
throws
DataFormatException
```

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

**Parameters:** output

- the buffer for the uncompressed data
**Returns:** the actual number of uncompressed bytes
**Throws:** DataFormatException

- if the compressed data format is invalid
**Throws:** ReadOnlyBufferException

- if the given output buffer is read-only
**Since:** 11
**See Also:** needsInput()

,

needsDictionary()

---

#### inflate

public int inflate​(

ByteBuffer

output)
throws

DataFormatException

Uncompresses bytes into specified buffer. Returns actual number
of bytes uncompressed. A return value of 0 indicates that
needsInput() or needsDictionary() should be called in order to
determine if more input data or a preset dictionary is required.
In the latter case, getAdler() can be used to get the Adler-32
value of the dictionary required.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method. Note that the position of the

output

buffer will be advanced even in the event that a

DataFormatException

is thrown.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

The

remaining byte count

will be reduced by
the number of consumed input bytes. If the

setInput(ByteBuffer)

method was called to provide a buffer for input, the input buffer's position
will be advanced the number of consumed bytes.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

These byte totals, as well as
the

total bytes read

and the

total bytes written

values, will be updated even in the event that a

DataFormatException

is thrown to reflect the amount of data consumed and produced before the
exception occurred.

getAdler

```java
public int getAdler()
```

Returns the ADLER-32 value of the uncompressed data.

**Returns:** the ADLER-32 value of the uncompressed data

---

#### getAdler

public int getAdler()

Returns the ADLER-32 value of the uncompressed data.

getTotalIn

```java
public int getTotalIn()
```

Returns the total number of compressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes input so far

---

#### getTotalIn

public int getTotalIn()

Returns the total number of compressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

getBytesRead

```java
public long getBytesRead()
```

Returns the total number of compressed bytes input so far.

**Returns:** the total (non-negative) number of compressed bytes input so far
**Since:** 1.5

---

#### getBytesRead

public long getBytesRead()

Returns the total number of compressed bytes input so far.

getTotalOut

```java
public int getTotalOut()
```

Returns the total number of uncompressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes output so far

---

#### getTotalOut

public int getTotalOut()

Returns the total number of uncompressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

getBytesWritten

```java
public long getBytesWritten()
```

Returns the total number of uncompressed bytes output so far.

**Returns:** the total (non-negative) number of uncompressed bytes output so far
**Since:** 1.5

---

#### getBytesWritten

public long getBytesWritten()

Returns the total number of uncompressed bytes output so far.

reset

```java
public void reset()
```

Resets inflater so that a new set of input data can be processed.

---

#### reset

public void reset()

Resets inflater so that a new set of input data can be processed.

end

```java
public void end()
```

Closes the decompressor and discards any unprocessed input.

This method should be called when the decompressor is no longer
being used. Once this method is called, the behavior of the
Inflater object is undefined.

---

#### end

public void end()

Closes the decompressor and discards any unprocessed input.

This method should be called when the decompressor is no longer
being used. Once this method is called, the behavior of the
Inflater object is undefined.

finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to use
alternative cleanup mechanisms and remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable,

Closes the decompressor when garbage is collected.

**Overrides:** finalize

in class

Object
**Implementation Requirements:** If this

Inflater

has been subclassed and the

end

method
has been overridden, the

end

method will be called when the
inflater is unreachable.
**See Also:** WeakReference

,

PhantomReference

---

#### finalize

@Deprecated

(

since

="9",

forRemoval

=true)
protected void finalize()

Closes the decompressor when garbage is collected.

---

