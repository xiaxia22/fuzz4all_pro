# Class Deflater

**Source:** `java.base\java\util\zip\Deflater.html`

### Class Description

```java
public class
Deflater

extends
Object
```

This class provides support for general purpose compression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class deflates sequences of bytes into ZLIB compressed data format.
The input byte sequence is provided in either byte array or byte buffer,
via one of the

setInput()

methods. The output byte sequence is
written to the output byte array or byte buffer passed to the

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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

Deflater

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

Deflater

has been subclassed and the

end

method has been
overridden, the

end

method will be called by the finalization when the
deflater is unreachable. But the subclasses should not depend on this specific
implementation; the finalization is not reliable and the

finalize

method
is deprecated to be removed.
**Since:** 1.1
**See Also:** Inflater

---

### Field Details

#### public static final int DEFLATED

Compression method for the deflate algorithm (the only one currently
supported).

**See Also:**
- Constant Field Values

---

#### public static final int NO_COMPRESSION

Compression level for no compression.

**See Also:**
- Constant Field Values

---

#### public static final int BEST_SPEED

Compression level for fastest compression.

**See Also:**
- Constant Field Values

---

#### public static final int BEST_COMPRESSION

Compression level for best compression.

**See Also:**
- Constant Field Values

---

#### public static final int DEFAULT_COMPRESSION

Default compression level.

**See Also:**
- Constant Field Values

---

#### public static final int FILTERED

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution. Forces more Huffman coding
and less string matching.

**See Also:**
- Constant Field Values

---

#### public static final int HUFFMAN_ONLY

Compression strategy for Huffman coding only.

**See Also:**
- Constant Field Values

---

#### public static final int DEFAULT_STRATEGY

Default compression strategy.

**See Also:**
- Constant Field Values

---

#### public static final int NO_FLUSH

Compression flush mode used to achieve best compression result.

**See Also:**
- deflate(byte[], int, int, int)

,

Constant Field Values

**Since:**
- 1.7

---

#### public static final int SYNC_FLUSH

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

**See Also:**
- deflate(byte[], int, int, int)

,

Constant Field Values

**Since:**
- 1.7

---

#### public static final int FULL_FLUSH

Compression flush mode used to flush out all pending output and
reset the deflater. Using this mode too often can seriously degrade
compression.

**See Also:**
- deflate(byte[], int, int, int)

,

Constant Field Values

**Since:**
- 1.7

---

### Constructor Details

#### public Deflater​(int level,
boolean nowrap)

Creates a new compressor using the specified compression level.
If 'nowrap' is true then the ZLIB header and checksum fields will
not be used in order to support the compression format used in
both GZIP and PKZIP.

**Parameters:**
- level

- the compression level (0-9)
- nowrap

- if true then use GZIP compatible compression

---

#### public Deflater​(int level)

Creates a new compressor using the specified compression level.
Compressed data will be generated in ZLIB format.

**Parameters:**
- level

- the compression level (0-9)

---

#### public Deflater()

Creates a new compressor with the default compression level.
Compressed data will be generated in ZLIB format.

---

### Method Details

#### public void setInput​(byte[] input,
int off,
int len)

Sets input data for compression.

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

- the start offset of the data
- len

- the length of the data

**See Also:**
- needsInput()

---

#### public void setInput​(byte[] input)

Sets input data for compression.

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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
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

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:**
- dictionary

- the dictionary data bytes
- off

- the start offset of the data
- len

- the length of the data

**See Also:**
- Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### public void setDictionary​(byte[] dictionary)

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:**
- dictionary

- the dictionary data bytes

**See Also:**
- Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### public void setDictionary​(
ByteBuffer
dictionary)

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:**
- dictionary

- the dictionary data bytes

**See Also:**
- Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### public void setStrategy​(int strategy)

Sets the compression strategy to the specified value.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

**Parameters:**
- strategy

- the new compression strategy

**Throws:**
- IllegalArgumentException

- if the compression strategy is
invalid

---

#### public void setLevel​(int level)

Sets the compression level to the specified value.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

**Parameters:**
- level

- the new compression level (0-9)

**Throws:**
- IllegalArgumentException

- if the compression level is invalid

---

#### public boolean needsInput()

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:**
- true if the input data buffer is empty and setInput()
should be called in order to provide more input

---

#### public void finish()

When called, indicates that compression should end with the current
contents of the input buffer.

---

#### public boolean finished()

Returns true if the end of the compressed data output stream has
been reached.

**Returns:**
- true if the end of the compressed data output stream has
been reached

---

#### public int deflate​(byte[] output,
int off,
int len)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

**Parameters:**
- output

- the buffer for the compressed data
- off

- the start offset of the data
- len

- the maximum number of bytes of compressed data

**Returns:**
- the actual number of bytes of compressed data written to the
output buffer

---

#### public int deflate​(byte[] output)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

**Parameters:**
- output

- the buffer for the compressed data

**Returns:**
- the actual number of bytes of compressed data written to the
output buffer

---

#### public int deflate​(
ByteBuffer
output)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

**Parameters:**
- output

- the buffer for the compressed data

**Returns:**
- the actual number of bytes of compressed data written to the
output buffer

**Since:**
- 11

---

#### public int deflate​(byte[] output,
int off,
int len,
int flush)

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:**
- output

- the buffer for the compressed data
- off

- the start offset of the data
- len

- the maximum number of bytes of compressed data
- flush

- the compression flush mode

**Returns:**
- the actual number of bytes of compressed data written to
the output buffer

**Throws:**
- IllegalArgumentException

- if the flush mode is invalid

**Since:**
- 1.7

---

#### public int deflate​(
ByteBuffer
output,
int flush)

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:**
- output

- the buffer for the compressed data
- flush

- the compression flush mode

**Returns:**
- the actual number of bytes of compressed data written to
the output buffer

**Throws:**
- IllegalArgumentException

- if the flush mode is invalid

**Since:**
- 11

---

#### public int getAdler()

Returns the ADLER-32 value of the uncompressed data.

**Returns:**
- the ADLER-32 value of the uncompressed data

---

#### public int getTotalIn()

Returns the total number of uncompressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:**
- the total number of uncompressed bytes input so far

---

#### public long getBytesRead()

Returns the total number of uncompressed bytes input so far.

**Returns:**
- the total (non-negative) number of uncompressed bytes input so far

**Since:**
- 1.5

---

#### public int getTotalOut()

Returns the total number of compressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:**
- the total number of compressed bytes output so far

---

#### public long getBytesWritten()

Returns the total number of compressed bytes output so far.

**Returns:**
- the total (non-negative) number of compressed bytes output so far

**Since:**
- 1.5

---

#### public void reset()

Resets deflater so that a new set of input data can be processed.
Keeps current compression level and strategy settings.

---

#### public void end()

Closes the compressor and discards any unprocessed input.

This method should be called when the compressor is no longer
being used. Once this method is called, the behavior of the
Deflater object is undefined.

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()

Closes the compressor when garbage is collected.

**Overrides:**
- finalize

in class

Object

**See Also:**
- WeakReference

,

PhantomReference

---

### Additional Sections

#### Class Deflater

java.lang.Object

- java.util.zip.Deflater

java.util.zip.Deflater

```java
public class
Deflater

extends
Object
```

This class provides support for general purpose compression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class deflates sequences of bytes into ZLIB compressed data format.
The input byte sequence is provided in either byte array or byte buffer,
via one of the

setInput()

methods. The output byte sequence is
written to the output byte array or byte buffer passed to the

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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

Deflater

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

Deflater

has been subclassed and the

end

method has been
overridden, the

end

method will be called by the finalization when the
deflater is unreachable. But the subclasses should not depend on this specific
implementation; the finalization is not reliable and the

finalize

method
is deprecated to be removed.
**Since:** 1.1
**See Also:** Inflater

public class

Deflater

extends

Object

This class provides support for general purpose compression using the
popular ZLIB compression library. The ZLIB compression library was
initially developed as part of the PNG graphics standard and is not
protected by patents. It is fully described in the specifications at
the

java.util.zip
package description

.

This class deflates sequences of bytes into ZLIB compressed data format.
The input byte sequence is provided in either byte array or byte buffer,
via one of the

setInput()

methods. The output byte sequence is
written to the output byte array or byte buffer passed to the

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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

This class deflates sequences of bytes into ZLIB compressed data format.
The input byte sequence is provided in either byte array or byte buffer,
via one of the

setInput()

methods. The output byte sequence is
written to the output byte array or byte buffer passed to the

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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
String inputString = "blahblahblah";
byte[] input = inputString.getBytes("UTF-8");

// Compress the bytes
byte[] output = new byte[100];
Deflater compresser = new Deflater();
compresser.setInput(input);
compresser.finish();
int compressedDataLength = compresser.deflate(output);
compresser.end();

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BEST_COMPRESSION

Compression level for best compression.

static int

BEST_SPEED

Compression level for fastest compression.

static int

DEFAULT_COMPRESSION

Default compression level.

static int

DEFAULT_STRATEGY

Default compression strategy.

static int

DEFLATED

Compression method for the deflate algorithm (the only one currently
supported).

static int

FILTERED

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution.

static int

FULL_FLUSH

Compression flush mode used to flush out all pending output and
reset the deflater.

static int

HUFFMAN_ONLY

Compression strategy for Huffman coding only.

static int

NO_COMPRESSION

Compression level for no compression.

static int

NO_FLUSH

Compression flush mode used to achieve best compression result.

static int

SYNC_FLUSH

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Deflater

()

Creates a new compressor with the default compression level.

Deflater

​(int level)

Creates a new compressor using the specified compression level.

Deflater

​(int level,
boolean nowrap)

Creates a new compressor using the specified compression level.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

deflate

​(byte[] output)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(byte[] output,
int off,
int len)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(byte[] output,
int off,
int len,
int flush)

Compresses the input data and fills the specified buffer with compressed
data.

int

deflate

​(

ByteBuffer

output)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(

ByteBuffer

output,
int flush)

Compresses the input data and fills the specified buffer with compressed
data.

void

end

()

Closes the compressor and discards any unprocessed input.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

void

finish

()

When called, indicates that compression should end with the current
contents of the input buffer.

boolean

finished

()

Returns true if the end of the compressed data output stream has
been reached.

int

getAdler

()

Returns the ADLER-32 value of the uncompressed data.

long

getBytesRead

()

Returns the total number of uncompressed bytes input so far.

long

getBytesWritten

()

Returns the total number of compressed bytes output so far.

int

getTotalIn

()

Returns the total number of uncompressed bytes input so far.

int

getTotalOut

()

Returns the total number of compressed bytes output so far.

boolean

needsInput

()

Returns true if no data remains in the input buffer.

void

reset

()

Resets deflater so that a new set of input data can be processed.

void

setDictionary

​(byte[] dictionary)

Sets preset dictionary for compression.

void

setDictionary

​(byte[] dictionary,
int off,
int len)

Sets preset dictionary for compression.

void

setDictionary

​(

ByteBuffer

dictionary)

Sets preset dictionary for compression.

void

setInput

​(byte[] input)

Sets input data for compression.

void

setInput

​(byte[] input,
int off,
int len)

Sets input data for compression.

void

setInput

​(

ByteBuffer

input)

Sets input data for compression.

void

setLevel

​(int level)

Sets the compression level to the specified value.

void

setStrategy

​(int strategy)

Sets the compression strategy to the specified value.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

BEST_COMPRESSION

Compression level for best compression.

static int

BEST_SPEED

Compression level for fastest compression.

static int

DEFAULT_COMPRESSION

Default compression level.

static int

DEFAULT_STRATEGY

Default compression strategy.

static int

DEFLATED

Compression method for the deflate algorithm (the only one currently
supported).

static int

FILTERED

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution.

static int

FULL_FLUSH

Compression flush mode used to flush out all pending output and
reset the deflater.

static int

HUFFMAN_ONLY

Compression strategy for Huffman coding only.

static int

NO_COMPRESSION

Compression level for no compression.

static int

NO_FLUSH

Compression flush mode used to achieve best compression result.

static int

SYNC_FLUSH

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

---

#### Field Summary

Compression level for best compression.

Compression level for fastest compression.

Default compression level.

Default compression strategy.

Compression method for the deflate algorithm (the only one currently
supported).

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution.

Compression flush mode used to flush out all pending output and
reset the deflater.

Compression strategy for Huffman coding only.

Compression level for no compression.

Compression flush mode used to achieve best compression result.

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

Constructor Summary

Constructors

Constructor

Description

Deflater

()

Creates a new compressor with the default compression level.

Deflater

​(int level)

Creates a new compressor using the specified compression level.

Deflater

​(int level,
boolean nowrap)

Creates a new compressor using the specified compression level.

---

#### Constructor Summary

Creates a new compressor with the default compression level.

Creates a new compressor using the specified compression level.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

deflate

​(byte[] output)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(byte[] output,
int off,
int len)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(byte[] output,
int off,
int len,
int flush)

Compresses the input data and fills the specified buffer with compressed
data.

int

deflate

​(

ByteBuffer

output)

Compresses the input data and fills specified buffer with compressed
data.

int

deflate

​(

ByteBuffer

output,
int flush)

Compresses the input data and fills the specified buffer with compressed
data.

void

end

()

Closes the compressor and discards any unprocessed input.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

void

finish

()

When called, indicates that compression should end with the current
contents of the input buffer.

boolean

finished

()

Returns true if the end of the compressed data output stream has
been reached.

int

getAdler

()

Returns the ADLER-32 value of the uncompressed data.

long

getBytesRead

()

Returns the total number of uncompressed bytes input so far.

long

getBytesWritten

()

Returns the total number of compressed bytes output so far.

int

getTotalIn

()

Returns the total number of uncompressed bytes input so far.

int

getTotalOut

()

Returns the total number of compressed bytes output so far.

boolean

needsInput

()

Returns true if no data remains in the input buffer.

void

reset

()

Resets deflater so that a new set of input data can be processed.

void

setDictionary

​(byte[] dictionary)

Sets preset dictionary for compression.

void

setDictionary

​(byte[] dictionary,
int off,
int len)

Sets preset dictionary for compression.

void

setDictionary

​(

ByteBuffer

dictionary)

Sets preset dictionary for compression.

void

setInput

​(byte[] input)

Sets input data for compression.

void

setInput

​(byte[] input,
int off,
int len)

Sets input data for compression.

void

setInput

​(

ByteBuffer

input)

Sets input data for compression.

void

setLevel

​(int level)

Sets the compression level to the specified value.

void

setStrategy

​(int strategy)

Sets the compression strategy to the specified value.

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

Compresses the input data and fills specified buffer with compressed
data.

Compresses the input data and fills the specified buffer with compressed
data.

Closes the compressor and discards any unprocessed input.

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

When called, indicates that compression should end with the current
contents of the input buffer.

Returns true if the end of the compressed data output stream has
been reached.

Returns the ADLER-32 value of the uncompressed data.

Returns the total number of uncompressed bytes input so far.

Returns the total number of compressed bytes output so far.

Returns true if no data remains in the input buffer.

Resets deflater so that a new set of input data can be processed.

Sets preset dictionary for compression.

Sets input data for compression.

Sets the compression level to the specified value.

Sets the compression strategy to the specified value.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for the deflate algorithm (the only one currently
supported).

**See Also:** Constant Field Values

- NO_COMPRESSION

```java
public static final int NO_COMPRESSION
```

Compression level for no compression.

**See Also:** Constant Field Values

- BEST_SPEED

```java
public static final int BEST_SPEED
```

Compression level for fastest compression.

**See Also:** Constant Field Values

- BEST_COMPRESSION

```java
public static final int BEST_COMPRESSION
```

Compression level for best compression.

**See Also:** Constant Field Values

- DEFAULT_COMPRESSION

```java
public static final int DEFAULT_COMPRESSION
```

Default compression level.

**See Also:** Constant Field Values

- FILTERED

```java
public static final int FILTERED
```

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution. Forces more Huffman coding
and less string matching.

**See Also:** Constant Field Values

- HUFFMAN_ONLY

```java
public static final int HUFFMAN_ONLY
```

Compression strategy for Huffman coding only.

**See Also:** Constant Field Values

- DEFAULT_STRATEGY

```java
public static final int DEFAULT_STRATEGY
```

Default compression strategy.

**See Also:** Constant Field Values

- NO_FLUSH

```java
public static final int NO_FLUSH
```

Compression flush mode used to achieve best compression result.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

- SYNC_FLUSH

```java
public static final int SYNC_FLUSH
```

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

- FULL_FLUSH

```java
public static final int FULL_FLUSH
```

Compression flush mode used to flush out all pending output and
reset the deflater. Using this mode too often can seriously degrade
compression.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Deflater

```java
public Deflater​(int level,
boolean nowrap)
```

Creates a new compressor using the specified compression level.
If 'nowrap' is true then the ZLIB header and checksum fields will
not be used in order to support the compression format used in
both GZIP and PKZIP.

**Parameters:** level

- the compression level (0-9)
**Parameters:** nowrap

- if true then use GZIP compatible compression

- Deflater

```java
public Deflater​(int level)
```

Creates a new compressor using the specified compression level.
Compressed data will be generated in ZLIB format.

**Parameters:** level

- the compression level (0-9)

- Deflater

```java
public Deflater()
```

Creates a new compressor with the default compression level.
Compressed data will be generated in ZLIB format.

============ METHOD DETAIL ==========

- Method Detail

- setInput

```java
public void setInput​(byte[] input,
int off,
int len)
```

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsInput()

- setInput

```java
public void setInput​(byte[] input)
```

Sets input data for compression.

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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
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

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setStrategy

```java
public void setStrategy​(int strategy)
```

Sets the compression strategy to the specified value.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

**Parameters:** strategy

- the new compression strategy
**Throws:** IllegalArgumentException

- if the compression strategy is
invalid

- setLevel

```java
public void setLevel​(int level)
```

Sets the compression level to the specified value.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

**Parameters:** level

- the new compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

- needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if the input data buffer is empty and setInput()
should be called in order to provide more input

- finish

```java
public void finish()
```

When called, indicates that compression should end with the current
contents of the input buffer.

- finished

```java
public boolean finished()
```

Returns true if the end of the compressed data output stream has
been reached.

**Returns:** true if the end of the compressed data output stream has
been reached

- deflate

```java
public int deflate​(byte[] output,
int off,
int len)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

- deflate

```java
public int deflate​(byte[] output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

- deflate

```java
public int deflate​(
ByteBuffer
output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer
**Since:** 11

- deflate

```java
public int deflate​(byte[] output,
int off,
int len,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 1.7

- deflate

```java
public int deflate​(
ByteBuffer
output,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 11

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

Returns the total number of uncompressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes input so far

- getBytesRead

```java
public long getBytesRead()
```

Returns the total number of uncompressed bytes input so far.

**Returns:** the total (non-negative) number of uncompressed bytes input so far
**Since:** 1.5

- getTotalOut

```java
public int getTotalOut()
```

Returns the total number of compressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes output so far

- getBytesWritten

```java
public long getBytesWritten()
```

Returns the total number of compressed bytes output so far.

**Returns:** the total (non-negative) number of compressed bytes output so far
**Since:** 1.5

- reset

```java
public void reset()
```

Resets deflater so that a new set of input data can be processed.
Keeps current compression level and strategy settings.

- end

```java
public void end()
```

Closes the compressor and discards any unprocessed input.

This method should be called when the compressor is no longer
being used. Once this method is called, the behavior of the
Deflater object is undefined.

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
alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable.

Closes the compressor when garbage is collected.

**Overrides:** finalize

in class

Object
**See Also:** WeakReference

,

PhantomReference

Field Detail

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for the deflate algorithm (the only one currently
supported).

**See Also:** Constant Field Values

- NO_COMPRESSION

```java
public static final int NO_COMPRESSION
```

Compression level for no compression.

**See Also:** Constant Field Values

- BEST_SPEED

```java
public static final int BEST_SPEED
```

Compression level for fastest compression.

**See Also:** Constant Field Values

- BEST_COMPRESSION

```java
public static final int BEST_COMPRESSION
```

Compression level for best compression.

**See Also:** Constant Field Values

- DEFAULT_COMPRESSION

```java
public static final int DEFAULT_COMPRESSION
```

Default compression level.

**See Also:** Constant Field Values

- FILTERED

```java
public static final int FILTERED
```

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution. Forces more Huffman coding
and less string matching.

**See Also:** Constant Field Values

- HUFFMAN_ONLY

```java
public static final int HUFFMAN_ONLY
```

Compression strategy for Huffman coding only.

**See Also:** Constant Field Values

- DEFAULT_STRATEGY

```java
public static final int DEFAULT_STRATEGY
```

Default compression strategy.

**See Also:** Constant Field Values

- NO_FLUSH

```java
public static final int NO_FLUSH
```

Compression flush mode used to achieve best compression result.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

- SYNC_FLUSH

```java
public static final int SYNC_FLUSH
```

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

- FULL_FLUSH

```java
public static final int FULL_FLUSH
```

Compression flush mode used to flush out all pending output and
reset the deflater. Using this mode too often can seriously degrade
compression.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

---

#### Field Detail

DEFLATED

```java
public static final int DEFLATED
```

Compression method for the deflate algorithm (the only one currently
supported).

**See Also:** Constant Field Values

---

#### DEFLATED

public static final int DEFLATED

Compression method for the deflate algorithm (the only one currently
supported).

NO_COMPRESSION

```java
public static final int NO_COMPRESSION
```

Compression level for no compression.

**See Also:** Constant Field Values

---

#### NO_COMPRESSION

public static final int NO_COMPRESSION

Compression level for no compression.

BEST_SPEED

```java
public static final int BEST_SPEED
```

Compression level for fastest compression.

**See Also:** Constant Field Values

---

#### BEST_SPEED

public static final int BEST_SPEED

Compression level for fastest compression.

BEST_COMPRESSION

```java
public static final int BEST_COMPRESSION
```

Compression level for best compression.

**See Also:** Constant Field Values

---

#### BEST_COMPRESSION

public static final int BEST_COMPRESSION

Compression level for best compression.

DEFAULT_COMPRESSION

```java
public static final int DEFAULT_COMPRESSION
```

Default compression level.

**See Also:** Constant Field Values

---

#### DEFAULT_COMPRESSION

public static final int DEFAULT_COMPRESSION

Default compression level.

FILTERED

```java
public static final int FILTERED
```

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution. Forces more Huffman coding
and less string matching.

**See Also:** Constant Field Values

---

#### FILTERED

public static final int FILTERED

Compression strategy best used for data consisting mostly of small
values with a somewhat random distribution. Forces more Huffman coding
and less string matching.

HUFFMAN_ONLY

```java
public static final int HUFFMAN_ONLY
```

Compression strategy for Huffman coding only.

**See Also:** Constant Field Values

---

#### HUFFMAN_ONLY

public static final int HUFFMAN_ONLY

Compression strategy for Huffman coding only.

DEFAULT_STRATEGY

```java
public static final int DEFAULT_STRATEGY
```

Default compression strategy.

**See Also:** Constant Field Values

---

#### DEFAULT_STRATEGY

public static final int DEFAULT_STRATEGY

Default compression strategy.

NO_FLUSH

```java
public static final int NO_FLUSH
```

Compression flush mode used to achieve best compression result.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

---

#### NO_FLUSH

public static final int NO_FLUSH

Compression flush mode used to achieve best compression result.

SYNC_FLUSH

```java
public static final int SYNC_FLUSH
```

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

---

#### SYNC_FLUSH

public static final int SYNC_FLUSH

Compression flush mode used to flush out all pending output; may
degrade compression for some compression algorithms.

FULL_FLUSH

```java
public static final int FULL_FLUSH
```

Compression flush mode used to flush out all pending output and
reset the deflater. Using this mode too often can seriously degrade
compression.

**Since:** 1.7
**See Also:** deflate(byte[], int, int, int)

,

Constant Field Values

---

#### FULL_FLUSH

public static final int FULL_FLUSH

Compression flush mode used to flush out all pending output and
reset the deflater. Using this mode too often can seriously degrade
compression.

Constructor Detail

- Deflater

```java
public Deflater​(int level,
boolean nowrap)
```

Creates a new compressor using the specified compression level.
If 'nowrap' is true then the ZLIB header and checksum fields will
not be used in order to support the compression format used in
both GZIP and PKZIP.

**Parameters:** level

- the compression level (0-9)
**Parameters:** nowrap

- if true then use GZIP compatible compression

- Deflater

```java
public Deflater​(int level)
```

Creates a new compressor using the specified compression level.
Compressed data will be generated in ZLIB format.

**Parameters:** level

- the compression level (0-9)

- Deflater

```java
public Deflater()
```

Creates a new compressor with the default compression level.
Compressed data will be generated in ZLIB format.

---

#### Constructor Detail

Deflater

```java
public Deflater​(int level,
boolean nowrap)
```

Creates a new compressor using the specified compression level.
If 'nowrap' is true then the ZLIB header and checksum fields will
not be used in order to support the compression format used in
both GZIP and PKZIP.

**Parameters:** level

- the compression level (0-9)
**Parameters:** nowrap

- if true then use GZIP compatible compression

---

#### Deflater

public Deflater​(int level,
boolean nowrap)

Creates a new compressor using the specified compression level.
If 'nowrap' is true then the ZLIB header and checksum fields will
not be used in order to support the compression format used in
both GZIP and PKZIP.

Deflater

```java
public Deflater​(int level)
```

Creates a new compressor using the specified compression level.
Compressed data will be generated in ZLIB format.

**Parameters:** level

- the compression level (0-9)

---

#### Deflater

public Deflater​(int level)

Creates a new compressor using the specified compression level.
Compressed data will be generated in ZLIB format.

Deflater

```java
public Deflater()
```

Creates a new compressor with the default compression level.
Compressed data will be generated in ZLIB format.

---

#### Deflater

public Deflater()

Creates a new compressor with the default compression level.
Compressed data will be generated in ZLIB format.

Method Detail

- setInput

```java
public void setInput​(byte[] input,
int off,
int len)
```

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsInput()

- setInput

```java
public void setInput​(byte[] input)
```

Sets input data for compression.

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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
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

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

- setStrategy

```java
public void setStrategy​(int strategy)
```

Sets the compression strategy to the specified value.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

**Parameters:** strategy

- the new compression strategy
**Throws:** IllegalArgumentException

- if the compression strategy is
invalid

- setLevel

```java
public void setLevel​(int level)
```

Sets the compression level to the specified value.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

**Parameters:** level

- the new compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

- needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if the input data buffer is empty and setInput()
should be called in order to provide more input

- finish

```java
public void finish()
```

When called, indicates that compression should end with the current
contents of the input buffer.

- finished

```java
public boolean finished()
```

Returns true if the end of the compressed data output stream has
been reached.

**Returns:** true if the end of the compressed data output stream has
been reached

- deflate

```java
public int deflate​(byte[] output,
int off,
int len)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

- deflate

```java
public int deflate​(byte[] output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

- deflate

```java
public int deflate​(
ByteBuffer
output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer
**Since:** 11

- deflate

```java
public int deflate​(byte[] output,
int off,
int len,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 1.7

- deflate

```java
public int deflate​(
ByteBuffer
output,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 11

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

Returns the total number of uncompressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes input so far

- getBytesRead

```java
public long getBytesRead()
```

Returns the total number of uncompressed bytes input so far.

**Returns:** the total (non-negative) number of uncompressed bytes input so far
**Since:** 1.5

- getTotalOut

```java
public int getTotalOut()
```

Returns the total number of compressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes output so far

- getBytesWritten

```java
public long getBytesWritten()
```

Returns the total number of compressed bytes output so far.

**Returns:** the total (non-negative) number of compressed bytes output so far
**Since:** 1.5

- reset

```java
public void reset()
```

Resets deflater so that a new set of input data can be processed.
Keeps current compression level and strategy settings.

- end

```java
public void end()
```

Closes the compressor and discards any unprocessed input.

This method should be called when the compressor is no longer
being used. Once this method is called, the behavior of the
Deflater object is undefined.

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
alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable.

Closes the compressor when garbage is collected.

**Overrides:** finalize

in class

Object
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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

**Parameters:** input

- the input data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** needsInput()

---

#### setInput

public void setInput​(byte[] input,
int off,
int len)

Sets input data for compression.

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

Sets input data for compression.

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

Sets input data for compression.

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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
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

Sets input data for compression.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

One of the

setInput()

methods should be called whenever

needsInput()

returns true indicating that more input data
is required.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

The given buffer's position will be advanced as deflate
operations are performed, up to the buffer's limit.
The input buffer may be modified (refilled) between deflate
operations; doing so is equivalent to creating a new buffer
and setting it with this method.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

Modifying the input buffer's contents, position, or limit
concurrently with an deflate operation will result in
undefined behavior, which may include incorrect operation
results or operation failure.

setDictionary

```java
public void setDictionary​(byte[] dictionary,
int off,
int len)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the length of the data
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### setDictionary

public void setDictionary​(byte[] dictionary,
int off,
int len)

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

setDictionary

```java
public void setDictionary​(byte[] dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### setDictionary

public void setDictionary​(byte[] dictionary)

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

setDictionary

```java
public void setDictionary​(
ByteBuffer
dictionary)
```

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

**Parameters:** dictionary

- the dictionary data bytes
**See Also:** Inflater.inflate(byte[], int, int)

,

Inflater.getAdler()

---

#### setDictionary

public void setDictionary​(

ByteBuffer

dictionary)

Sets preset dictionary for compression. A preset dictionary is used
when the history buffer can be predetermined. When the data is later
uncompressed with Inflater.inflate(), Inflater.getAdler() can be called
in order to get the Adler-32 value of the dictionary required for
decompression.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

The bytes in given byte buffer will be fully consumed by this method. On
return, its position will equal its limit.

setStrategy

```java
public void setStrategy​(int strategy)
```

Sets the compression strategy to the specified value.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

**Parameters:** strategy

- the new compression strategy
**Throws:** IllegalArgumentException

- if the compression strategy is
invalid

---

#### setStrategy

public void setStrategy​(int strategy)

Sets the compression strategy to the specified value.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

If the compression strategy is changed, the next invocation
of

deflate

will compress the input available so far with
the old strategy (and may be flushed); the new strategy will take
effect only after that invocation.

setLevel

```java
public void setLevel​(int level)
```

Sets the compression level to the specified value.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

**Parameters:** level

- the new compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

---

#### setLevel

public void setLevel​(int level)

Sets the compression level to the specified value.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

If the compression level is changed, the next invocation
of

deflate

will compress the input available so far
with the old level (and may be flushed); the new level will
take effect only after that invocation.

needsInput

```java
public boolean needsInput()
```

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

**Returns:** true if the input data buffer is empty and setInput()
should be called in order to provide more input

---

#### needsInput

public boolean needsInput()

Returns true if no data remains in the input buffer. This can
be used to determine if one of the

setInput()

methods should be
called in order to provide more input.

finish

```java
public void finish()
```

When called, indicates that compression should end with the current
contents of the input buffer.

---

#### finish

public void finish()

When called, indicates that compression should end with the current
contents of the input buffer.

finished

```java
public boolean finished()
```

Returns true if the end of the compressed data output stream has
been reached.

**Returns:** true if the end of the compressed data output stream has
been reached

---

#### finished

public boolean finished()

Returns true if the end of the compressed data output stream has
been reached.

deflate

```java
public int deflate​(byte[] output,
int off,
int len)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

---

#### deflate

public int deflate​(byte[] output,
int off,
int len)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b, off, len)

yields the same result as the invocation of

deflater.deflate(b, off, len, Deflater.NO_FLUSH)

.

deflate

```java
public int deflate​(byte[] output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer

---

#### deflate

public int deflate​(byte[] output)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(b)

yields the same result as the invocation of

deflater.deflate(b, 0, b.length, Deflater.NO_FLUSH)

.

deflate

```java
public int deflate​(
ByteBuffer
output)
```

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

**Parameters:** output

- the buffer for the compressed data
**Returns:** the actual number of bytes of compressed data written to the
output buffer
**Since:** 11

---

#### deflate

public int deflate​(

ByteBuffer

output)

Compresses the input data and fills specified buffer with compressed
data. Returns actual number of bytes of compressed data. A return value
of 0 indicates that

needsInput

should be called
in order to determine if more input data is required.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

This method uses

NO_FLUSH

as its compression flush mode.
An invocation of this method of the form

deflater.deflate(output)

yields the same result as the invocation of

deflater.deflate(output, Deflater.NO_FLUSH)

.

deflate

```java
public int deflate​(byte[] output,
int off,
int len,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the maximum number of bytes of compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 1.7

---

#### deflate

public int deflate​(byte[] output,
int off,
int len,
int flush)

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is

len

, the space available in output
buffer

b

, this method should be invoked again with the same

flush

parameter and more output space. Make sure that

len

is greater than 6 to avoid flush marker (5 bytes) being
repeatedly output to the output buffer every time this method is
invoked.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

deflate

```java
public int deflate​(
ByteBuffer
output,
int flush)
```

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

**Parameters:** output

- the buffer for the compressed data
**Parameters:** flush

- the compression flush mode
**Returns:** the actual number of bytes of compressed data written to
the output buffer
**Throws:** IllegalArgumentException

- if the flush mode is invalid
**Since:** 11

---

#### deflate

public int deflate​(

ByteBuffer

output,
int flush)

Compresses the input data and fills the specified buffer with compressed
data. Returns actual number of bytes of data compressed.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

Compression flush mode is one of the following three modes:

- NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

NO_FLUSH

: allows the deflater to decide how much data
to accumulate, before producing output, in order to achieve the best
compression (should be used in normal use scenario). A return value
of 0 in this flush mode indicates that

needsInput()

should
be called in order to determine if more input data is required.

SYNC_FLUSH

: all pending output in the deflater is flushed,
to the specified output buffer, so that an inflater that works on
compressed data can get all input data available so far (In particular
the

needsInput()

returns

true

after this invocation
if enough output space is provided). Flushing with

SYNC_FLUSH

may degrade compression for some compression algorithms and so it
should be used only when necessary.

FULL_FLUSH

: all pending output is flushed out as with

SYNC_FLUSH

. The compression state is reset so that the inflater
that works on the compressed output data can restart from this point
if previous compressed data has been damaged or if random access is
desired. Using

FULL_FLUSH

too often can seriously degrade
compression.

In the case of

FULL_FLUSH

or

SYNC_FLUSH

, if
the return value is equal to the

remaining space

of the buffer, this method should be invoked again with the same

flush

parameter and more output space. Make sure that
the buffer has at least 6 bytes of remaining space to avoid the
flush marker (5 bytes) being repeatedly output to the output buffer
every time this method is invoked.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

On success, the position of the given

output

byte buffer will be
advanced by as many bytes as were produced by the operation, which is equal
to the number returned by this method.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

If the

setInput(ByteBuffer)

method was called to provide a buffer
for input, the input buffer's position will be advanced by the number of bytes
consumed by this operation.

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

Returns the total number of uncompressed bytes input so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesRead()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of uncompressed bytes input so far

---

#### getTotalIn

public int getTotalIn()

Returns the total number of uncompressed bytes input so far.

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

Returns the total number of uncompressed bytes input so far.

**Returns:** the total (non-negative) number of uncompressed bytes input so far
**Since:** 1.5

---

#### getBytesRead

public long getBytesRead()

Returns the total number of uncompressed bytes input so far.

getTotalOut

```java
public int getTotalOut()
```

Returns the total number of compressed bytes output so far.

Since the number of bytes may be greater than
Integer.MAX_VALUE, the

getBytesWritten()

method is now
the preferred means of obtaining this information.

**Returns:** the total number of compressed bytes output so far

---

#### getTotalOut

public int getTotalOut()

Returns the total number of compressed bytes output so far.

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

Returns the total number of compressed bytes output so far.

**Returns:** the total (non-negative) number of compressed bytes output so far
**Since:** 1.5

---

#### getBytesWritten

public long getBytesWritten()

Returns the total number of compressed bytes output so far.

reset

```java
public void reset()
```

Resets deflater so that a new set of input data can be processed.
Keeps current compression level and strategy settings.

---

#### reset

public void reset()

Resets deflater so that a new set of input data can be processed.
Keeps current compression level and strategy settings.

end

```java
public void end()
```

Closes the compressor and discards any unprocessed input.

This method should be called when the compressor is no longer
being used. Once this method is called, the behavior of the
Deflater object is undefined.

---

#### end

public void end()

Closes the compressor and discards any unprocessed input.

This method should be called when the compressor is no longer
being used. Once this method is called, the behavior of the
Deflater object is undefined.

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
alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for compressor is to explicitly call

end

method when it is no longer in use. If the

end

is
not invoked explicitly the resource of the compressor will be released
when the instance becomes unreachable.

Closes the compressor when garbage is collected.

**Overrides:** finalize

in class

Object
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

Closes the compressor when garbage is collected.

---

