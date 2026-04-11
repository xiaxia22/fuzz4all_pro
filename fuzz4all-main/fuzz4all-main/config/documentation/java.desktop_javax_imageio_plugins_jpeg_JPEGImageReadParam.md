# Class JPEGImageReadParam

**Source:** `java.desktop\javax\imageio\plugins\jpeg\JPEGImageReadParam.html`

### Class Description

```java
public class
JPEGImageReadParam

extends
ImageReadParam
```

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG reader plug-in. An instance of
this class will be returned from the

getDefaultImageReadParam

methods of the built-in JPEG

ImageReader

.

The sole purpose of these additions is to allow the
specification of tables for use in decoding abbreviated streams.
The built-in JPEG reader will also accept an ordinary

ImageReadParam

, which is sufficient for decoding
non-abbreviated streams.

While tables for abbreviated streams are often obtained by
first reading another abbreviated stream containing only the
tables, in some applications the tables are fixed ahead of time.
This class allows the tables to be specified directly from client
code. If no tables are specified either in the stream or in a

JPEGImageReadParam

, then the stream is presumed to use
the "standard" visually lossless tables. See

JPEGQTable

and

JPEGHuffmanTable

for more information
on the default tables.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public JPEGImageReadParam()

Constructs a

JPEGImageReadParam

.

---

### Method Details

#### public boolean areTablesSet()

Returns

true

if tables are currently set.

**Returns:**
- true

if tables are present.

---

#### public void setDecodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in decoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored once tables are
encountered in the stream. All arguments must be
non-

null

. The two arrays of Huffman tables must
have the same number of elements. The table specifiers in the
frame and scan headers in the stream are assumed to be
equivalent to indices into these arrays. The argument arrays
are copied by this method.

**Parameters:**
- qTables

- an array of quantization table objects.
- DCHuffmanTables

- an array of Huffman table objects.
- ACHuffmanTables

- an array of Huffman table objects.

**Throws:**
- IllegalArgumentException

- if any of the arguments
is

null

, has more than 4 elements, or if the
numbers of DC and AC tables differ.

**See Also:**
- unsetDecodeTables()

---

#### public void unsetDecodeTables()

Removes any quantization and Huffman tables that are currently
set.

**See Also:**
- setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGQTable
[] getQTables()

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:**
- an array of

JPEGQTable

objects, or

null

.

**See Also:**
- setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGHuffmanTable
[] getDCHuffmanTables()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:**
- an array of

JPEGHuffmanTable

objects, or

null

.

**See Also:**
- setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGHuffmanTable
[] getACHuffmanTables()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:**
- an array of

JPEGHuffmanTable

objects, or

null

.

**See Also:**
- setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

### Additional Sections

#### Class JPEGImageReadParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageReadParam
- - javax.imageio.plugins.jpeg.JPEGImageReadParam

javax.imageio.IIOParam

- javax.imageio.ImageReadParam
- - javax.imageio.plugins.jpeg.JPEGImageReadParam

javax.imageio.ImageReadParam

- javax.imageio.plugins.jpeg.JPEGImageReadParam

javax.imageio.plugins.jpeg.JPEGImageReadParam

```java
public class
JPEGImageReadParam

extends
ImageReadParam
```

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG reader plug-in. An instance of
this class will be returned from the

getDefaultImageReadParam

methods of the built-in JPEG

ImageReader

.

The sole purpose of these additions is to allow the
specification of tables for use in decoding abbreviated streams.
The built-in JPEG reader will also accept an ordinary

ImageReadParam

, which is sufficient for decoding
non-abbreviated streams.

While tables for abbreviated streams are often obtained by
first reading another abbreviated stream containing only the
tables, in some applications the tables are fixed ahead of time.
This class allows the tables to be specified directly from client
code. If no tables are specified either in the stream or in a

JPEGImageReadParam

, then the stream is presumed to use
the "standard" visually lossless tables. See

JPEGQTable

and

JPEGHuffmanTable

for more information
on the default tables.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

public class

JPEGImageReadParam

extends

ImageReadParam

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG reader plug-in. An instance of
this class will be returned from the

getDefaultImageReadParam

methods of the built-in JPEG

ImageReader

.

The sole purpose of these additions is to allow the
specification of tables for use in decoding abbreviated streams.
The built-in JPEG reader will also accept an ordinary

ImageReadParam

, which is sufficient for decoding
non-abbreviated streams.

While tables for abbreviated streams are often obtained by
first reading another abbreviated stream containing only the
tables, in some applications the tables are fixed ahead of time.
This class allows the tables to be specified directly from client
code. If no tables are specified either in the stream or in a

JPEGImageReadParam

, then the stream is presumed to use
the "standard" visually lossless tables. See

JPEGQTable

and

JPEGHuffmanTable

for more information
on the default tables.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

The sole purpose of these additions is to allow the
specification of tables for use in decoding abbreviated streams.
The built-in JPEG reader will also accept an ordinary

ImageReadParam

, which is sufficient for decoding
non-abbreviated streams.

While tables for abbreviated streams are often obtained by
first reading another abbreviated stream containing only the
tables, in some applications the tables are fixed ahead of time.
This class allows the tables to be specified directly from client
code. If no tables are specified either in the stream or in a

JPEGImageReadParam

, then the stream is presumed to use
the "standard" visually lossless tables. See

JPEGQTable

and

JPEGHuffmanTable

for more information
on the default tables.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

While tables for abbreviated streams are often obtained by
first reading another abbreviated stream containing only the
tables, in some applications the tables are fixed ahead of time.
This class allows the tables to be specified directly from client
code. If no tables are specified either in the stream or in a

JPEGImageReadParam

, then the stream is presumed to use
the "standard" visually lossless tables. See

JPEGQTable

and

JPEGHuffmanTable

for more information
on the default tables.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

The default

JPEGImageReadParam

returned by the

getDefaultReadParam

method of the builtin JPEG reader
contains no tables. Default tables may be obtained from the table
classes

JPEGQTable

and

JPEGHuffmanTable

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

If a stream does contain tables, the tables given in a

JPEGImageReadParam

are ignored. Furthermore, if the
first image in a stream does contain tables and subsequent ones do
not, then the tables given in the first image are used for all the
abbreviated images. Once tables have been read from a stream, they
can be overridden only by tables subsequently read from the same
stream. In order to specify new tables, the

setInput

method of
the reader must be called to change the stream.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

Note that this class does not provide a means for obtaining the
tables found in a stream. These may be extracted from a stream by
consulting the IIOMetadata object returned by the reader.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JPEGImageReadParam

()

Constructs a

JPEGImageReadParam

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

areTablesSet

()

Returns

true

if tables are currently set.

JPEGHuffmanTable

[]

getACHuffmanTables

()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

JPEGHuffmanTable

[]

getDCHuffmanTables

()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

JPEGQTable

[]

getQTables

()

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

void

setDecodeTables

​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in decoding
abbreviated streams.

void

unsetDecodeTables

()

Removes any quantization and Huffman tables that are currently
set.

- Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

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

- Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Field Summary

Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

---

#### Fields declared in class javax.imageio. ImageReadParam

Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Fields declared in class javax.imageio. IIOParam

Constructor Summary

Constructors

Constructor

Description

JPEGImageReadParam

()

Constructs a

JPEGImageReadParam

.

---

#### Constructor Summary

Constructs a

JPEGImageReadParam

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

areTablesSet

()

Returns

true

if tables are currently set.

JPEGHuffmanTable

[]

getACHuffmanTables

()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

JPEGHuffmanTable

[]

getDCHuffmanTables

()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

JPEGQTable

[]

getQTables

()

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

void

setDecodeTables

​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in decoding
abbreviated streams.

void

unsetDecodeTables

()

Removes any quantization and Huffman tables that are currently
set.

- Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

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

Returns

true

if tables are currently set.

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

Sets the quantization and Huffman tables to use in decoding
abbreviated streams.

Removes any quantization and Huffman tables that are currently
set.

Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

---

#### Methods declared in class javax.imageio. ImageReadParam

Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

---

#### Methods declared in class javax.imageio. IIOParam

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

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

- JPEGImageReadParam

```java
public JPEGImageReadParam()
```

Constructs a

JPEGImageReadParam

.

============ METHOD DETAIL ==========

- Method Detail

- areTablesSet

```java
public boolean areTablesSet()
```

Returns

true

if tables are currently set.

**Returns:** true

if tables are present.

- setDecodeTables

```java
public void setDecodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in decoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored once tables are
encountered in the stream. All arguments must be
non-

null

. The two arrays of Huffman tables must
have the same number of elements. The table specifiers in the
frame and scan headers in the stream are assumed to be
equivalent to indices into these arrays. The argument arrays
are copied by this method.

**Parameters:** qTables

- an array of quantization table objects.
**Parameters:** DCHuffmanTables

- an array of Huffman table objects.
**Parameters:** ACHuffmanTables

- an array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

, has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetDecodeTables()

- unsetDecodeTables

```java
public void unsetDecodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getQTables

```java
public
JPEGQTable
[] getQTables()
```

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getDCHuffmanTables

```java
public
JPEGHuffmanTable
[] getDCHuffmanTables()
```

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getACHuffmanTables

```java
public
JPEGHuffmanTable
[] getACHuffmanTables()
```

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

Constructor Detail

- JPEGImageReadParam

```java
public JPEGImageReadParam()
```

Constructs a

JPEGImageReadParam

.

---

#### Constructor Detail

JPEGImageReadParam

```java
public JPEGImageReadParam()
```

Constructs a

JPEGImageReadParam

.

---

#### JPEGImageReadParam

public JPEGImageReadParam()

Constructs a

JPEGImageReadParam

.

Method Detail

- areTablesSet

```java
public boolean areTablesSet()
```

Returns

true

if tables are currently set.

**Returns:** true

if tables are present.

- setDecodeTables

```java
public void setDecodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in decoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored once tables are
encountered in the stream. All arguments must be
non-

null

. The two arrays of Huffman tables must
have the same number of elements. The table specifiers in the
frame and scan headers in the stream are assumed to be
equivalent to indices into these arrays. The argument arrays
are copied by this method.

**Parameters:** qTables

- an array of quantization table objects.
**Parameters:** DCHuffmanTables

- an array of Huffman table objects.
**Parameters:** ACHuffmanTables

- an array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

, has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetDecodeTables()

- unsetDecodeTables

```java
public void unsetDecodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getQTables

```java
public
JPEGQTable
[] getQTables()
```

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getDCHuffmanTables

```java
public
JPEGHuffmanTable
[] getDCHuffmanTables()
```

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getACHuffmanTables

```java
public
JPEGHuffmanTable
[] getACHuffmanTables()
```

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### Method Detail

areTablesSet

```java
public boolean areTablesSet()
```

Returns

true

if tables are currently set.

**Returns:** true

if tables are present.

---

#### areTablesSet

public boolean areTablesSet()

Returns

true

if tables are currently set.

setDecodeTables

```java
public void setDecodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in decoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored once tables are
encountered in the stream. All arguments must be
non-

null

. The two arrays of Huffman tables must
have the same number of elements. The table specifiers in the
frame and scan headers in the stream are assumed to be
equivalent to indices into these arrays. The argument arrays
are copied by this method.

**Parameters:** qTables

- an array of quantization table objects.
**Parameters:** DCHuffmanTables

- an array of Huffman table objects.
**Parameters:** ACHuffmanTables

- an array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

, has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetDecodeTables()

---

#### setDecodeTables

public void setDecodeTables​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in decoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored once tables are
encountered in the stream. All arguments must be
non-

null

. The two arrays of Huffman tables must
have the same number of elements. The table specifiers in the
frame and scan headers in the stream are assumed to be
equivalent to indices into these arrays. The argument arrays
are copied by this method.

unsetDecodeTables

```java
public void unsetDecodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### unsetDecodeTables

public void unsetDecodeTables()

Removes any quantization and Huffman tables that are currently
set.

getQTables

```java
public
JPEGQTable
[] getQTables()
```

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getQTables

public

JPEGQTable

[] getQTables()

Returns a copy of the array of quantization tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

getDCHuffmanTables

```java
public
JPEGHuffmanTable
[] getDCHuffmanTables()
```

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getDCHuffmanTables

public

JPEGHuffmanTable

[] getDCHuffmanTables()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

getACHuffmanTables

```java
public
JPEGHuffmanTable
[] getACHuffmanTables()
```

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setDecodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getACHuffmanTables

public

JPEGHuffmanTable

[] getACHuffmanTables()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setDecodeTables

, or

null

if tables are not currently set.

---

