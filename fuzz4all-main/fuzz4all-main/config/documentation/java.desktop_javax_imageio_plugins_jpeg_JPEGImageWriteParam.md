# Class JPEGImageWriteParam

**Source:** `java.desktop\javax\imageio\plugins\jpeg\JPEGImageWriteParam.html`

### Class Description

```java
public class
JPEGImageWriteParam

extends
ImageWriteParam
```

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG writer plug-in, and to request that
optimized Huffman tables be computed for an image. An instance of
this class will be returned from the

getDefaultImageWriteParam

methods of the built-in JPEG

ImageWriter

.

The principal purpose of these additions is to allow the
specification of tables to use in encoding abbreviated streams.
The built-in JPEG writer will also accept an ordinary

ImageWriteParam

, in which case the writer will
construct the necessary tables internally.

In either case, the quality setting in an

ImageWriteParam

has the same meaning as for the underlying library: 1.00 means a
quantization table of all 1's, 0.75 means the "standard", visually
lossless quantization table, and 0.00 means aquantization table of
all 255's.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public JPEGImageWriteParam​(
Locale
locale)

Constructs a

JPEGImageWriteParam

. Tiling is not
supported. Progressive encoding is supported. The default
progressive mode is MODE_DISABLED. A single form of compression,
named "JPEG", is supported. The default compression quality is
0.75.

**Parameters:**
- locale

- a

Locale

to be used by the
superclass to localize compression type names and quality
descriptions, or

null

.

---

### Method Details

#### public void unsetCompression()

Removes any previous compression quality setting.

The default implementation resets the compression quality
to

0.75F

.

**Overrides:**
- unsetCompression

in class

ImageWriteParam

**Throws:**
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

**See Also:**
- ImageWriteParam.setCompressionType(java.lang.String)

,

ImageWriteParam.setCompressionQuality(float)

---

#### public boolean isCompressionLossless()

Returns

false

since the JPEG plug-in only supports
lossy compression.

**Overrides:**
- isCompressionLossless

in class

ImageWriteParam

**Returns:**
- false

.

**Throws:**
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

---

#### public boolean areTablesSet()

Returns

true

if tables are currently set.

**Returns:**
- true

if tables are present.

---

#### public void setEncodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in encoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored if tables are specified in
the metadata. All arguments must be non-

null

.
The two arrays of Huffman tables must have the same number of
elements. The table specifiers in the frame and scan headers
in the metadata are assumed to be equivalent to indices into
these arrays. The argument arrays are copied by this method.

**Parameters:**
- qTables

- An array of quantization table objects.
- DCHuffmanTables

- An array of Huffman table objects.
- ACHuffmanTables

- An array of Huffman table objects.

**Throws:**
- IllegalArgumentException

- if any of the arguments
is

null

or has more than 4 elements, or if the
numbers of DC and AC tables differ.

**See Also:**
- unsetEncodeTables()

---

#### public void unsetEncodeTables()

Removes any quantization and Huffman tables that are currently
set.

**See Also:**
- setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGQTable
[] getQTables()

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

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
- setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGHuffmanTable
[] getDCHuffmanTables()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

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
- setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public
JPEGHuffmanTable
[] getACHuffmanTables()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setEncodeTables

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
- setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### public void setOptimizeHuffmanTables​(boolean optimize)

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process. The
default is

false

. If this flag is set
to

true

, it overrides any tables specified
in the metadata. Note that this means that any image
written with this flag set to

true

will
always contain Huffman tables.

**Parameters:**
- optimize

- A boolean indicating whether to generate
optimized Huffman tables when writing.

**See Also:**
- getOptimizeHuffmanTables()

---

#### public boolean getOptimizeHuffmanTables()

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

**Returns:**
- true

if the writer will generate optimized
Huffman tables.

**See Also:**
- setOptimizeHuffmanTables(boolean)

---

### Additional Sections

#### Class JPEGImageWriteParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageWriteParam
- - javax.imageio.plugins.jpeg.JPEGImageWriteParam

javax.imageio.IIOParam

- javax.imageio.ImageWriteParam
- - javax.imageio.plugins.jpeg.JPEGImageWriteParam

javax.imageio.ImageWriteParam

- javax.imageio.plugins.jpeg.JPEGImageWriteParam

javax.imageio.plugins.jpeg.JPEGImageWriteParam

```java
public class
JPEGImageWriteParam

extends
ImageWriteParam
```

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG writer plug-in, and to request that
optimized Huffman tables be computed for an image. An instance of
this class will be returned from the

getDefaultImageWriteParam

methods of the built-in JPEG

ImageWriter

.

The principal purpose of these additions is to allow the
specification of tables to use in encoding abbreviated streams.
The built-in JPEG writer will also accept an ordinary

ImageWriteParam

, in which case the writer will
construct the necessary tables internally.

In either case, the quality setting in an

ImageWriteParam

has the same meaning as for the underlying library: 1.00 means a
quantization table of all 1's, 0.75 means the "standard", visually
lossless quantization table, and 0.00 means aquantization table of
all 255's.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

public class

JPEGImageWriteParam

extends

ImageWriteParam

This class adds the ability to set JPEG quantization and Huffman
tables when using the built-in JPEG writer plug-in, and to request that
optimized Huffman tables be computed for an image. An instance of
this class will be returned from the

getDefaultImageWriteParam

methods of the built-in JPEG

ImageWriter

.

The principal purpose of these additions is to allow the
specification of tables to use in encoding abbreviated streams.
The built-in JPEG writer will also accept an ordinary

ImageWriteParam

, in which case the writer will
construct the necessary tables internally.

In either case, the quality setting in an

ImageWriteParam

has the same meaning as for the underlying library: 1.00 means a
quantization table of all 1's, 0.75 means the "standard", visually
lossless quantization table, and 0.00 means aquantization table of
all 255's.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

The principal purpose of these additions is to allow the
specification of tables to use in encoding abbreviated streams.
The built-in JPEG writer will also accept an ordinary

ImageWriteParam

, in which case the writer will
construct the necessary tables internally.

In either case, the quality setting in an

ImageWriteParam

has the same meaning as for the underlying library: 1.00 means a
quantization table of all 1's, 0.75 means the "standard", visually
lossless quantization table, and 0.00 means aquantization table of
all 255's.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

In either case, the quality setting in an

ImageWriteParam

has the same meaning as for the underlying library: 1.00 means a
quantization table of all 1's, 0.75 means the "standard", visually
lossless quantization table, and 0.00 means aquantization table of
all 255's.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

While tables for abbreviated streams are often specified by
first writing an abbreviated stream containing only the tables, in
some applications the tables are fixed ahead of time. This class
allows the tables to be specified directly from client code.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

Normally, the tables are specified in the

IIOMetadata

objects passed in to the writer, and any
tables included in these objects are written to the stream.
If no tables are specified in the metadata, then an abbreviated
stream is written. If no tables are included in the metadata and
no tables are specified in a

JPEGImageWriteParam

, then
an abbreviated stream is encoded using the "standard" visually
lossless tables. This class is necessary for specifying tables
when an abbreviated stream must be written without writing any tables
to a stream first. In order to use this class, the metadata object
passed into the writer must contain no tables, and no stream metadata
must be provided. See

JPEGQTable

and

JPEGHuffmanTable

for more
information on the default tables.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

The default

JPEGImageWriteParam

returned by the

getDefaultWriteParam

method of the writer contains no
tables. Default tables are included in the default

IIOMetadata

objects returned by the writer.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

For more information about the operation of the built-in JPEG plug-ins,
see the

JPEG
metadata format specification and usage notes

.

If the metadata does contain tables, the tables given in a

JPEGImageWriteParam

are ignored. Furthermore, once a
set of tables has been written, only tables in the metadata can
override them for subsequent writes, whether to the same stream or
a different one. In order to specify new tables using this class,
the

reset

method of the writer must be called.

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

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

compressionMode

,

compressionQuality

,

compressionType

,

compressionTypes

,

locale

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

MODE_DISABLED

,

MODE_EXPLICIT

,

preferredTileSizes

,

progressiveMode

,

tileGridXOffset

,

tileGridYOffset

,

tileHeight

,

tileWidth

,

tilingMode

,

tilingSet

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

JPEGImageWriteParam

​(

Locale

locale)

Constructs a

JPEGImageWriteParam

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

setEncodeTables

, or

null

if tables are not currently set.

JPEGHuffmanTable

[]

getDCHuffmanTables

()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

boolean

getOptimizeHuffmanTables

()

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

JPEGQTable

[]

getQTables

()

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

boolean

isCompressionLossless

()

Returns

false

since the JPEG plug-in only supports
lossy compression.

void

setEncodeTables

​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in encoding
abbreviated streams.

void

setOptimizeHuffmanTables

​(boolean optimize)

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process.

void

unsetCompression

()

Removes any previous compression quality setting.

void

unsetEncodeTables

()

Removes any quantization and Huffman tables that are currently
set.

- Methods declared in class javax.imageio.

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

getBitRate

,

getCompressionMode

,

getCompressionQuality

,

getCompressionQualityDescriptions

,

getCompressionQualityValues

,

getCompressionType

,

getCompressionTypes

,

getLocale

,

getLocalizedCompressionTypeName

,

getPreferredTileSizes

,

getProgressiveMode

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getTilingMode

,

setCompressionMode

,

setCompressionQuality

,

setCompressionType

,

setProgressiveMode

,

setTiling

,

setTilingMode

,

unsetTiling

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

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

compressionMode

,

compressionQuality

,

compressionType

,

compressionTypes

,

locale

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

MODE_DISABLED

,

MODE_EXPLICIT

,

preferredTileSizes

,

progressiveMode

,

tileGridXOffset

,

tileGridYOffset

,

tileHeight

,

tileWidth

,

tilingMode

,

tilingSet

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

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

compressionMode

,

compressionQuality

,

compressionType

,

compressionTypes

,

locale

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

MODE_DISABLED

,

MODE_EXPLICIT

,

preferredTileSizes

,

progressiveMode

,

tileGridXOffset

,

tileGridYOffset

,

tileHeight

,

tileWidth

,

tilingMode

,

tilingSet

---

#### Fields declared in class javax.imageio. ImageWriteParam

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

JPEGImageWriteParam

​(

Locale

locale)

Constructs a

JPEGImageWriteParam

.

---

#### Constructor Summary

Constructs a

JPEGImageWriteParam

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

setEncodeTables

, or

null

if tables are not currently set.

JPEGHuffmanTable

[]

getDCHuffmanTables

()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

boolean

getOptimizeHuffmanTables

()

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

JPEGQTable

[]

getQTables

()

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

boolean

isCompressionLossless

()

Returns

false

since the JPEG plug-in only supports
lossy compression.

void

setEncodeTables

​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in encoding
abbreviated streams.

void

setOptimizeHuffmanTables

​(boolean optimize)

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process.

void

unsetCompression

()

Removes any previous compression quality setting.

void

unsetEncodeTables

()

Removes any quantization and Huffman tables that are currently
set.

- Methods declared in class javax.imageio.

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

getBitRate

,

getCompressionMode

,

getCompressionQuality

,

getCompressionQualityDescriptions

,

getCompressionQualityValues

,

getCompressionType

,

getCompressionTypes

,

getLocale

,

getLocalizedCompressionTypeName

,

getPreferredTileSizes

,

getProgressiveMode

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getTilingMode

,

setCompressionMode

,

setCompressionQuality

,

setCompressionType

,

setProgressiveMode

,

setTiling

,

setTilingMode

,

unsetTiling

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

setEncodeTables

, or

null

if tables are not currently set.

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

Returns

false

since the JPEG plug-in only supports
lossy compression.

Sets the quantization and Huffman tables to use in encoding
abbreviated streams.

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process.

Removes any previous compression quality setting.

Removes any quantization and Huffman tables that are currently
set.

Methods declared in class javax.imageio.

ImageWriteParam

canOffsetTiles

,

canWriteCompressed

,

canWriteProgressive

,

canWriteTiles

,

getBitRate

,

getCompressionMode

,

getCompressionQuality

,

getCompressionQualityDescriptions

,

getCompressionQualityValues

,

getCompressionType

,

getCompressionTypes

,

getLocale

,

getLocalizedCompressionTypeName

,

getPreferredTileSizes

,

getProgressiveMode

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getTilingMode

,

setCompressionMode

,

setCompressionQuality

,

setCompressionType

,

setProgressiveMode

,

setTiling

,

setTilingMode

,

unsetTiling

---

#### Methods declared in class javax.imageio. ImageWriteParam

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

- JPEGImageWriteParam

```java
public JPEGImageWriteParam​(
Locale
locale)
```

Constructs a

JPEGImageWriteParam

. Tiling is not
supported. Progressive encoding is supported. The default
progressive mode is MODE_DISABLED. A single form of compression,
named "JPEG", is supported. The default compression quality is
0.75.

**Parameters:** locale

- a

Locale

to be used by the
superclass to localize compression type names and quality
descriptions, or

null

.

============ METHOD DETAIL ==========

- Method Detail

- unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression quality setting.

The default implementation resets the compression quality
to

0.75F

.

**Overrides:** unsetCompression

in class

ImageWriteParam
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** ImageWriteParam.setCompressionType(java.lang.String)

,

ImageWriteParam.setCompressionQuality(float)

- isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

false

since the JPEG plug-in only supports
lossy compression.

**Overrides:** isCompressionLossless

in class

ImageWriteParam
**Returns:** false

.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

- areTablesSet

```java
public boolean areTablesSet()
```

Returns

true

if tables are currently set.

**Returns:** true

if tables are present.

- setEncodeTables

```java
public void setEncodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in encoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored if tables are specified in
the metadata. All arguments must be non-

null

.
The two arrays of Huffman tables must have the same number of
elements. The table specifiers in the frame and scan headers
in the metadata are assumed to be equivalent to indices into
these arrays. The argument arrays are copied by this method.

**Parameters:** qTables

- An array of quantization table objects.
**Parameters:** DCHuffmanTables

- An array of Huffman table objects.
**Parameters:** ACHuffmanTables

- An array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

or has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetEncodeTables()

- unsetEncodeTables

```java
public void unsetEncodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getQTables

```java
public
JPEGQTable
[] getQTables()
```

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getDCHuffmanTables

```java
public
JPEGHuffmanTable
[] getDCHuffmanTables()
```

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getACHuffmanTables

```java
public
JPEGHuffmanTable
[] getACHuffmanTables()
```

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- setOptimizeHuffmanTables

```java
public void setOptimizeHuffmanTables​(boolean optimize)
```

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process. The
default is

false

. If this flag is set
to

true

, it overrides any tables specified
in the metadata. Note that this means that any image
written with this flag set to

true

will
always contain Huffman tables.

**Parameters:** optimize

- A boolean indicating whether to generate
optimized Huffman tables when writing.
**See Also:** getOptimizeHuffmanTables()

- getOptimizeHuffmanTables

```java
public boolean getOptimizeHuffmanTables()
```

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

**Returns:** true

if the writer will generate optimized
Huffman tables.
**See Also:** setOptimizeHuffmanTables(boolean)

Constructor Detail

- JPEGImageWriteParam

```java
public JPEGImageWriteParam​(
Locale
locale)
```

Constructs a

JPEGImageWriteParam

. Tiling is not
supported. Progressive encoding is supported. The default
progressive mode is MODE_DISABLED. A single form of compression,
named "JPEG", is supported. The default compression quality is
0.75.

**Parameters:** locale

- a

Locale

to be used by the
superclass to localize compression type names and quality
descriptions, or

null

.

---

#### Constructor Detail

JPEGImageWriteParam

```java
public JPEGImageWriteParam​(
Locale
locale)
```

Constructs a

JPEGImageWriteParam

. Tiling is not
supported. Progressive encoding is supported. The default
progressive mode is MODE_DISABLED. A single form of compression,
named "JPEG", is supported. The default compression quality is
0.75.

**Parameters:** locale

- a

Locale

to be used by the
superclass to localize compression type names and quality
descriptions, or

null

.

---

#### JPEGImageWriteParam

public JPEGImageWriteParam​(

Locale

locale)

Constructs a

JPEGImageWriteParam

. Tiling is not
supported. Progressive encoding is supported. The default
progressive mode is MODE_DISABLED. A single form of compression,
named "JPEG", is supported. The default compression quality is
0.75.

Method Detail

- unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression quality setting.

The default implementation resets the compression quality
to

0.75F

.

**Overrides:** unsetCompression

in class

ImageWriteParam
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** ImageWriteParam.setCompressionType(java.lang.String)

,

ImageWriteParam.setCompressionQuality(float)

- isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

false

since the JPEG plug-in only supports
lossy compression.

**Overrides:** isCompressionLossless

in class

ImageWriteParam
**Returns:** false

.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

- areTablesSet

```java
public boolean areTablesSet()
```

Returns

true

if tables are currently set.

**Returns:** true

if tables are present.

- setEncodeTables

```java
public void setEncodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in encoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored if tables are specified in
the metadata. All arguments must be non-

null

.
The two arrays of Huffman tables must have the same number of
elements. The table specifiers in the frame and scan headers
in the metadata are assumed to be equivalent to indices into
these arrays. The argument arrays are copied by this method.

**Parameters:** qTables

- An array of quantization table objects.
**Parameters:** DCHuffmanTables

- An array of Huffman table objects.
**Parameters:** ACHuffmanTables

- An array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

or has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetEncodeTables()

- unsetEncodeTables

```java
public void unsetEncodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getQTables

```java
public
JPEGQTable
[] getQTables()
```

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getDCHuffmanTables

```java
public
JPEGHuffmanTable
[] getDCHuffmanTables()
```

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- getACHuffmanTables

```java
public
JPEGHuffmanTable
[] getACHuffmanTables()
```

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

- setOptimizeHuffmanTables

```java
public void setOptimizeHuffmanTables​(boolean optimize)
```

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process. The
default is

false

. If this flag is set
to

true

, it overrides any tables specified
in the metadata. Note that this means that any image
written with this flag set to

true

will
always contain Huffman tables.

**Parameters:** optimize

- A boolean indicating whether to generate
optimized Huffman tables when writing.
**See Also:** getOptimizeHuffmanTables()

- getOptimizeHuffmanTables

```java
public boolean getOptimizeHuffmanTables()
```

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

**Returns:** true

if the writer will generate optimized
Huffman tables.
**See Also:** setOptimizeHuffmanTables(boolean)

---

#### Method Detail

unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression quality setting.

The default implementation resets the compression quality
to

0.75F

.

**Overrides:** unsetCompression

in class

ImageWriteParam
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** ImageWriteParam.setCompressionType(java.lang.String)

,

ImageWriteParam.setCompressionQuality(float)

---

#### unsetCompression

public void unsetCompression()

Removes any previous compression quality setting.

The default implementation resets the compression quality
to

0.75F

.

The default implementation resets the compression quality
to

0.75F

.

isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

false

since the JPEG plug-in only supports
lossy compression.

**Overrides:** isCompressionLossless

in class

ImageWriteParam
**Returns:** false

.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

---

#### isCompressionLossless

public boolean isCompressionLossless()

Returns

false

since the JPEG plug-in only supports
lossy compression.

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

setEncodeTables

```java
public void setEncodeTables​(
JPEGQTable
[] qTables,

JPEGHuffmanTable
[] DCHuffmanTables,

JPEGHuffmanTable
[] ACHuffmanTables)
```

Sets the quantization and Huffman tables to use in encoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored if tables are specified in
the metadata. All arguments must be non-

null

.
The two arrays of Huffman tables must have the same number of
elements. The table specifiers in the frame and scan headers
in the metadata are assumed to be equivalent to indices into
these arrays. The argument arrays are copied by this method.

**Parameters:** qTables

- An array of quantization table objects.
**Parameters:** DCHuffmanTables

- An array of Huffman table objects.
**Parameters:** ACHuffmanTables

- An array of Huffman table objects.
**Throws:** IllegalArgumentException

- if any of the arguments
is

null

or has more than 4 elements, or if the
numbers of DC and AC tables differ.
**See Also:** unsetEncodeTables()

---

#### setEncodeTables

public void setEncodeTables​(

JPEGQTable

[] qTables,

JPEGHuffmanTable

[] DCHuffmanTables,

JPEGHuffmanTable

[] ACHuffmanTables)

Sets the quantization and Huffman tables to use in encoding
abbreviated streams. There may be a maximum of 4 tables of
each type. These tables are ignored if tables are specified in
the metadata. All arguments must be non-

null

.
The two arrays of Huffman tables must have the same number of
elements. The table specifiers in the frame and scan headers
in the metadata are assumed to be equivalent to indices into
these arrays. The argument arrays are copied by this method.

unsetEncodeTables

```java
public void unsetEncodeTables()
```

Removes any quantization and Huffman tables that are currently
set.

**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### unsetEncodeTables

public void unsetEncodeTables()

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

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGQTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getQTables

public

JPEGQTable

[] getQTables()

Returns a copy of the array of quantization tables set on the
most recent call to

setEncodeTables

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

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getDCHuffmanTables

public

JPEGHuffmanTable

[] getDCHuffmanTables()

Returns a copy of the array of DC Huffman tables set on the
most recent call to

setEncodeTables

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

setEncodeTables

, or

null

if tables are not currently set.

**Returns:** an array of

JPEGHuffmanTable

objects, or

null

.
**See Also:** setEncodeTables(javax.imageio.plugins.jpeg.JPEGQTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[], javax.imageio.plugins.jpeg.JPEGHuffmanTable[])

---

#### getACHuffmanTables

public

JPEGHuffmanTable

[] getACHuffmanTables()

Returns a copy of the array of AC Huffman tables set on the
most recent call to

setEncodeTables

, or

null

if tables are not currently set.

setOptimizeHuffmanTables

```java
public void setOptimizeHuffmanTables​(boolean optimize)
```

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process. The
default is

false

. If this flag is set
to

true

, it overrides any tables specified
in the metadata. Note that this means that any image
written with this flag set to

true

will
always contain Huffman tables.

**Parameters:** optimize

- A boolean indicating whether to generate
optimized Huffman tables when writing.
**See Also:** getOptimizeHuffmanTables()

---

#### setOptimizeHuffmanTables

public void setOptimizeHuffmanTables​(boolean optimize)

Tells the writer to generate optimized Huffman tables
for the image as part of the writing process. The
default is

false

. If this flag is set
to

true

, it overrides any tables specified
in the metadata. Note that this means that any image
written with this flag set to

true

will
always contain Huffman tables.

getOptimizeHuffmanTables

```java
public boolean getOptimizeHuffmanTables()
```

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

**Returns:** true

if the writer will generate optimized
Huffman tables.
**See Also:** setOptimizeHuffmanTables(boolean)

---

#### getOptimizeHuffmanTables

public boolean getOptimizeHuffmanTables()

Returns the value passed into the most recent call
to

setOptimizeHuffmanTables

, or

false

if

setOptimizeHuffmanTables

has never been called.

---

