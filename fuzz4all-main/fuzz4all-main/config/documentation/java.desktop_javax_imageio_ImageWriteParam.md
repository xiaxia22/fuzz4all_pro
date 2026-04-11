# Class ImageWriteParam

**Source:** `java.desktop\javax\imageio\ImageWriteParam.html`

### Class Description

```java
public class
ImageWriteParam

extends
IIOParam
```

A class describing how a stream is to be encoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageWriter

.

A plug-in for a specific image format may define a subclass of
this class, and return objects of that class from the

getDefaultWriteParam

method of its

ImageWriter

implementation. For example, the built-in
JPEG writer plug-in will return instances of

javax.imageio.plugins.jpeg.JPEGImageWriteParam

.

The region of the image to be written is determined by first
intersecting the actual bounds of the image with the rectangle
specified by

IIOParam.setSourceRegion

, if any. If the
resulting rectangle has a width or height of zero, the writer will
throw an

IIOException

. If the intersection is
non-empty, writing will commence with the first subsampled pixel
and include additional pixels within the intersected bounds
according to the horizontal and vertical subsampling factors
specified by

IIOParam.setSourceSubsampling

.

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

**Direct Known Subclasses:** BMPImageWriteParam

,

JPEGImageWriteParam

---

### Field Details

#### public static final int MODE_DISABLED

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes. That is, when this mode is set the stream will

not

be tiled, progressive, or compressed, and the
relevant accessor methods will throw an

IllegalStateException

.

**See Also:**
- MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### public static final int MODE_DEFAULT

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed according to a
sensible default chosen internally by the writer in a plug-in
dependent way, and the relevant accessor methods will
throw an

IllegalStateException

.

**See Also:**
- MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### public static final int MODE_EXPLICIT

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes. That is, when this mode
is set the stream will be tiled or compressed according to
additional information supplied to the corresponding

set

methods in this class and retrievable from the
corresponding

get

methods. Note that this mode is
not supported for progressive output.

**See Also:**
- MODE_DISABLED

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### public static final int MODE_COPY_FROM_METADATA

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed based on the contents
of stream and/or image metadata passed into the write
operation, and any relevant accessor methods will throw an

IllegalStateException

.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

**See Also:**
- MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### protected boolean canWriteTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

---

#### protected int tilingMode

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values. The default
is

MODE_COPY_FROM_METADATA

.

Subclasses that do not writing tiles may ignore this value.

**See Also:**
- MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setTilingMode(int)

,

getTilingMode()

---

#### protected
Dimension
[] preferredTileSizes

An array of preferred tile size range pairs. The default value
is

null

, which indicates that there are no
preferred sizes. If the value is non-

null

, it
must have an even length of at least two.

Subclasses that do not support writing tiles may ignore
this value.

**See Also:**
- getPreferredTileSizes()

---

#### protected boolean tilingSet

A

boolean

that is

true

if tiling
parameters have been specified.

Subclasses that do not support writing tiles may ignore
this value.

---

#### protected int tileWidth

The width of each tile if tiling has been set, or 0 otherwise.

Subclasses that do not support tiling may ignore this
value.

---

#### protected int tileHeight

The height of each tile if tiling has been set, or 0 otherwise.
The initial value is

0

.

Subclasses that do not support tiling may ignore this
value.

---

#### protected boolean canOffsetTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

---

#### protected int tileGridXOffset

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

---

#### protected int tileGridYOffset

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

---

#### protected boolean canWriteProgressive

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes. By default,
the value is

false

. Subclasses must set the value
manually.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

---

#### protected int progressiveMode

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support progressive encoding may
ignore this value.

**See Also:**
- MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

---

#### protected boolean canWriteCompressed

A

boolean

that is

true

if this writer
can write images using compression. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support compression must ensure that
this value is set to

false

.

---

#### protected int compressionMode

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support compression may ignore this
value.

**See Also:**
- MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setCompressionMode(int)

,

getCompressionMode()

---

#### protected
String
[] compressionTypes

An array of

String

s containing the names of the
available compression types. Subclasses must set the value
manually.

Subclasses that do not support compression may ignore this
value.

---

#### protected
String
compressionType

A

String

containing the name of the current
compression type, or

null

if none is set.

Subclasses that do not support compression may ignore this
value.

---

#### protected float compressionQuality

A

float

containing the current compression quality
setting. The initial value is

1.0F

.

Subclasses that do not support compression may ignore this
value.

---

#### protected
Locale
locale

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

. Subclasses must set the value
manually.

---

### Constructor Details

#### protected ImageWriteParam()

Constructs an empty

ImageWriteParam

. It is up to
the subclass to set up the instance variables properly.

---

#### public ImageWriteParam​(
Locale
locale)

Constructs an

ImageWriteParam

set to use a
given

Locale

.

**Parameters:**
- locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

---

### Method Details

#### public
Locale
getLocale()

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

**Returns:**
- the current

Locale

, or

null

.

---

#### public boolean canWriteTiles()

Returns

true

if the writer can perform tiling
while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

.

**Returns:**
- true

if the writer supports tiling.

**See Also:**
- canOffsetTiles()

,

setTiling(int, int, int, int)

---

#### public boolean canOffsetTiles()

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

if the grid offset
arguments are not both zero. If

canWriteTiles

returns

false

, this method will return

false

as well.

**Returns:**
- true

if the writer supports non-zero tile
offsets.

**See Also:**
- canWriteTiles()

,

setTiling(int, int, int, int)

---

#### public void setTilingMode​(int mode)

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined. The modes are interpreted as follows:

- MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

**Parameters:**
- mode

- The mode to use for tiling.

**Throws:**
- UnsupportedOperationException

- if

canWriteTiles

returns

false

.
- IllegalArgumentException

- if

mode

is not
one of the modes listed above.

**See Also:**
- setTiling(int, int, int, int)

,

getTilingMode()

---

#### public int getTilingMode()

Returns the current tiling mode, if tiling is supported.
Otherwise throws an

UnsupportedOperationException

.

**Returns:**
- the current tiling mode.

**Throws:**
- UnsupportedOperationException

- if

canWriteTiles

returns

false

.

**See Also:**
- setTilingMode(int)

---

#### public
Dimension
[] getPreferredTileSizes()

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream. The returned array is a copy.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

**Returns:**
- an array of

Dimension

s with an even length
of at least two, or

null

.

**Throws:**
- UnsupportedOperationException

- if the plug-in does
not support tiling.

---

#### public void setTiling​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)

Specifies that the image should be tiled in the output stream.
The

tileWidth

and

tileHeight

parameters specify the width and height of the tiles in the
file. If the tile width or height is greater than the width or
height of the image, the image is not tiled in that dimension.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

**Parameters:**
- tileWidth

- the width of each tile.
- tileHeight

- the height of each tile.
- tileGridXOffset

- the horizontal offset of the tile grid.
- tileGridYOffset

- the vertical offset of the tile grid.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
- UnsupportedOperationException

- if the plug-in does not
support grid offsets, and the grid offsets are not both zero.
- IllegalArgumentException

- if the tile size is not
within one of the allowable ranges returned by

getPreferredTileSizes

.
- IllegalArgumentException

- if

tileWidth

or

tileHeight

is less than or equal to 0.

**See Also:**
- canWriteTiles

,

canOffsetTiles

,

getTileWidth()

,

getTileHeight()

,

getTileGridXOffset()

,

getTileGridYOffset()

---

#### public void unsetTiling()

Removes any previous tile grid parameters specified by calls to

setTiling

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.

**See Also:**
- setTiling(int, int, int, int)

---

#### public int getTileWidth()

Returns the width of each tile in an image as it will be
written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:**
- the tile width to be used for encoding.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the tiling parameters have
not been set.

**See Also:**
- setTiling(int, int, int, int)

,

getTileHeight()

---

#### public int getTileHeight()

Returns the height of each tile in an image as it will be written to
the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:**
- the tile height to be used for encoding.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the tiling parameters have
not been set.

**See Also:**
- setTiling(int, int, int, int)

,

getTileWidth()

---

#### public int getTileGridXOffset()

Returns the horizontal tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:**
- the tile grid X offset to be used for encoding.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the tiling parameters have
not been set.

**See Also:**
- setTiling(int, int, int, int)

,

getTileGridYOffset()

---

#### public int getTileGridYOffset()

Returns the vertical tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:**
- the tile grid Y offset to be used for encoding.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support tiling.
- IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the tiling parameters have
not been set.

**See Also:**
- setTiling(int, int, int, int)

,

getTileGridXOffset()

---

#### public boolean canWriteProgressive()

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

**Returns:**
- true

if the writer supports progressive
encoding.

**See Also:**
- setProgressiveMode(int)

,

getProgressiveMode()

---

#### public void setProgressiveMode​(int mode)

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality. If progressive encoding is not
supported, an

UnsupportedOperationException

will
be thrown.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:**
- mode

- The mode for setting progression in the output
stream.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support progressive encoding.
- IllegalArgumentException

- if

mode

is not
one of the modes listed above.

**See Also:**
- getProgressiveMode()

---

#### public int getProgressiveMode()

Returns the current mode for writing the stream in a
progressive manner.

**Returns:**
- the current mode for progressive encoding.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support progressive encoding.

**See Also:**
- setProgressiveMode(int)

---

#### public boolean canWriteCompressed()

Returns

true

if this writer supports compression.

**Returns:**
- true

if the writer supports compression.

---

#### public void setCompressionMode​(int mode)

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined. The

mode

argument must be one of the four modes, interpreted as follows:

- MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:**
- mode

- The mode for setting compression in the output
stream.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression, or does not support the requested mode.
- IllegalArgumentException

- if

mode

is not
one of the modes listed above.

**See Also:**
- getCompressionMode()

---

#### public int getCompressionMode()

Returns the current compression mode, if compression is
supported.

**Returns:**
- the current compression mode.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.

**See Also:**
- setCompressionMode(int)

---

#### public
String
[] getCompressionTypes()

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces. The array
returned is a copy.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

**Returns:**
- an array of

String

s containing the
(non-localized) names of available compression types, or

null

.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.

---

#### public void setCompressionType​(
String
compressionType)

Sets the compression type to one of the values indicated by

getCompressionTypes

. If a value of

null

is passed in, any previous setting is
removed.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

**Parameters:**
- compressionType

- one of the

String

s returned
by

getCompressionTypes

, or

null

to
remove any previous setting.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- UnsupportedOperationException

- if there are no
settable compression types.
- IllegalArgumentException

- if

compressionType

is non-

null

but is not
one of the values returned by

getCompressionTypes

.

**See Also:**
- getCompressionTypes()

,

getCompressionType()

,

unsetCompression()

---

#### public
String
getCompressionType()

Returns the currently set compression type, or

null

if none has been set. The type is returned
as a

String

from among those returned by

getCompressionTypes

.
If no compression type has been set,

null

is
returned.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

**Returns:**
- the current compression type as a

String

,
or

null

if no type is set.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

**See Also:**
- setCompressionType(java.lang.String)

---

#### public void unsetCompression()

Removes any previous compression type and quality settings.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

**Throws:**
- UnsupportedOperationException

- if the plug-in does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.

**See Also:**
- setCompressionType(java.lang.String)

,

setCompressionQuality(float)

---

#### public
String
getLocalizedCompressionTypeName()

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

**Returns:**
- a

String

containing a localized version of
the name of the current compression type.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if no compression type is set.

---

#### public boolean isCompressionLossless()

Returns

true

if the current compression type
provides lossless compression. If a plug-in provides only
one mandatory compression type, then this method may be
called without calling

setCompressionType

first.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

**Returns:**
- true

if the current compression type is
lossless.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

---

#### public void setCompressionQuality​(float quality)

Sets the compression quality to a value between

0

and

1

. Only a single compression quality setting
is supported by default; writers can provide extended versions
of

ImageWriteParam

that offer more control. For
lossy compression schemes, the compression quality should
control the tradeoff between file size and image quality (for
example, by choosing quantization tables when writing JPEG
images). For lossless schemes, the compression quality may be
used to control the tradeoff between file size and time taken
to perform the compression (for example, by optimizing row
filters and setting the ZLIB compression level when writing
PNG images).

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

**Parameters:**
- quality

- a

float

between

0

and

1

indicating the desired quality level.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
- IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.

**See Also:**
- getCompressionQuality()

---

#### public float getCompressionQuality()

Returns the current compression quality setting.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

**Returns:**
- the current compression quality setting.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

**See Also:**
- setCompressionQuality(float)

---

#### public float getBitRate​(float quality)

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level. The value will typically lie
between

0

and

1

, with smaller values
indicating more compression. A special value of

-1.0F

is used to indicate that no estimate is
available.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

**Parameters:**
- quality

- the quality setting whose bit rate is to be
queried.

**Returns:**
- an estimate of the compressed bit rate, or

-1.0F

if no estimate is available.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
- IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.

---

#### public
String
[] getCompressionQualityDescriptions()

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level. The

String

with index

i

provides a description of the range of quality levels between

getCompressionQualityValues[i]

and

getCompressionQualityValues[i + 1]

. Note that the
length of the array returned from

getCompressionQualityValues

will always be one
greater than that returned from

getCompressionQualityDescriptions

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:**
- an array of

String

s containing localized
descriptions of the compression quality levels.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

**See Also:**
- getCompressionQualityValues()

---

#### public float[] getCompressionQualityValues()

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level. See

getCompressionQualityDescriptions

for more information.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:**
- an array of

float

s indicating the
boundaries between the compression quality levels as described
by the

String

s from

getCompressionQualityDescriptions

.

**Throws:**
- UnsupportedOperationException

- if the writer does not
support compression.
- IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
- IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

**See Also:**
- getCompressionQualityDescriptions()

---

### Additional Sections

#### Class ImageWriteParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageWriteParam

javax.imageio.IIOParam

- javax.imageio.ImageWriteParam

javax.imageio.ImageWriteParam

**Direct Known Subclasses:** BMPImageWriteParam

,

JPEGImageWriteParam

```java
public class
ImageWriteParam

extends
IIOParam
```

A class describing how a stream is to be encoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageWriter

.

A plug-in for a specific image format may define a subclass of
this class, and return objects of that class from the

getDefaultWriteParam

method of its

ImageWriter

implementation. For example, the built-in
JPEG writer plug-in will return instances of

javax.imageio.plugins.jpeg.JPEGImageWriteParam

.

The region of the image to be written is determined by first
intersecting the actual bounds of the image with the rectangle
specified by

IIOParam.setSourceRegion

, if any. If the
resulting rectangle has a width or height of zero, the writer will
throw an

IIOException

. If the intersection is
non-empty, writing will commence with the first subsampled pixel
and include additional pixels within the intersected bounds
according to the horizontal and vertical subsampling factors
specified by

IIOParam.setSourceSubsampling

.

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

**See Also:** ImageReadParam

public class

ImageWriteParam

extends

IIOParam

A class describing how a stream is to be encoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageWriter

.

A plug-in for a specific image format may define a subclass of
this class, and return objects of that class from the

getDefaultWriteParam

method of its

ImageWriter

implementation. For example, the built-in
JPEG writer plug-in will return instances of

javax.imageio.plugins.jpeg.JPEGImageWriteParam

.

The region of the image to be written is determined by first
intersecting the actual bounds of the image with the rectangle
specified by

IIOParam.setSourceRegion

, if any. If the
resulting rectangle has a width or height of zero, the writer will
throw an

IIOException

. If the intersection is
non-empty, writing will commence with the first subsampled pixel
and include additional pixels within the intersected bounds
according to the horizontal and vertical subsampling factors
specified by

IIOParam.setSourceSubsampling

.

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

A plug-in for a specific image format may define a subclass of
this class, and return objects of that class from the

getDefaultWriteParam

method of its

ImageWriter

implementation. For example, the built-in
JPEG writer plug-in will return instances of

javax.imageio.plugins.jpeg.JPEGImageWriteParam

.

The region of the image to be written is determined by first
intersecting the actual bounds of the image with the rectangle
specified by

IIOParam.setSourceRegion

, if any. If the
resulting rectangle has a width or height of zero, the writer will
throw an

IIOException

. If the intersection is
non-empty, writing will commence with the first subsampled pixel
and include additional pixels within the intersected bounds
according to the horizontal and vertical subsampling factors
specified by

IIOParam.setSourceSubsampling

.

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

The region of the image to be written is determined by first
intersecting the actual bounds of the image with the rectangle
specified by

IIOParam.setSourceRegion

, if any. If the
resulting rectangle has a width or height of zero, the writer will
throw an

IIOException

. If the intersection is
non-empty, writing will commence with the first subsampled pixel
and include additional pixels within the intersected bounds
according to the horizontal and vertical subsampling factors
specified by

IIOParam.setSourceSubsampling

.

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

Individual features such as tiling, progressive encoding, and
compression may be set in one of four modes.

MODE_DISABLED

disables the features;

MODE_DEFAULT

enables the feature with
writer-controlled parameter values;

MODE_EXPLICIT

enables the feature and allows the use of a

set

method
to provide additional parameters; and

MODE_COPY_FROM_METADATA

copies relevant parameter
values from the stream and image metadata objects passed to the
writer. The default for all features is

MODE_COPY_FROM_METADATA

. Non-standard features
supplied in subclasses are encouraged, but not required to use a
similar scheme.

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

Plug-in writers may extend the functionality of

ImageWriteParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Writers will silently ignore any extended features of an

ImageWriteParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageWriteParam

instances via

getDefaultWriteParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

Note that unless a query method exists for a capability, it must
be supported by all

ImageWriter

implementations
(

e.g.

progressive encoding is optional, but subsampling must be
supported).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

canOffsetTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set.

protected boolean

canWriteCompressed

A

boolean

that is

true

if this writer
can write images using compression.

protected boolean

canWriteProgressive

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes.

protected boolean

canWriteTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set.

protected int

compressionMode

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values.

protected float

compressionQuality

A

float

containing the current compression quality
setting.

protected

String

compressionType

A

String

containing the name of the current
compression type, or

null

if none is set.

protected

String

[]

compressionTypes

An array of

String

s containing the names of the
available compression types.

protected

Locale

locale

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

.

static int

MODE_COPY_FROM_METADATA

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes.

static int

MODE_DEFAULT

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes.

static int

MODE_DISABLED

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes.

static int

MODE_EXPLICIT

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes.

protected

Dimension

[]

preferredTileSizes

An array of preferred tile size range pairs.

protected int

progressiveMode

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

.

protected int

tileGridXOffset

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise.

protected int

tileGridYOffset

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise.

protected int

tileHeight

The height of each tile if tiling has been set, or 0 otherwise.

protected int

tileWidth

The width of each tile if tiling has been set, or 0 otherwise.

protected int

tilingMode

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values.

protected boolean

tilingSet

A

boolean

that is

true

if tiling
parameters have been specified.

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

Modifier

Constructor

Description

protected

ImageWriteParam

()

Constructs an empty

ImageWriteParam

.

ImageWriteParam

​(

Locale

locale)

Constructs an

ImageWriteParam

set to use a
given

Locale

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

canOffsetTiles

()

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing.

boolean

canWriteCompressed

()

Returns

true

if this writer supports compression.

boolean

canWriteProgressive

()

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

boolean

canWriteTiles

()

Returns

true

if the writer can perform tiling
while writing.

float

getBitRate

​(float quality)

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level.

int

getCompressionMode

()

Returns the current compression mode, if compression is
supported.

float

getCompressionQuality

()

Returns the current compression quality setting.

String

[]

getCompressionQualityDescriptions

()

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level.

float[]

getCompressionQualityValues

()

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level.

String

getCompressionType

()

Returns the currently set compression type, or

null

if none has been set.

String

[]

getCompressionTypes

()

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces.

Locale

getLocale

()

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

String

getLocalizedCompressionTypeName

()

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

Dimension

[]

getPreferredTileSizes

()

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream.

int

getProgressiveMode

()

Returns the current mode for writing the stream in a
progressive manner.

int

getTileGridXOffset

()

Returns the horizontal tile grid offset of an image as it will
be written to the output stream.

int

getTileGridYOffset

()

Returns the vertical tile grid offset of an image as it will
be written to the output stream.

int

getTileHeight

()

Returns the height of each tile in an image as it will be written to
the output stream.

int

getTileWidth

()

Returns the width of each tile in an image as it will be
written to the output stream.

int

getTilingMode

()

Returns the current tiling mode, if tiling is supported.

boolean

isCompressionLossless

()

Returns

true

if the current compression type
provides lossless compression.

void

setCompressionMode

​(int mode)

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined.

void

setCompressionQuality

​(float quality)

Sets the compression quality to a value between

0

and

1

.

void

setCompressionType

​(

String

compressionType)

Sets the compression type to one of the values indicated by

getCompressionTypes

.

void

setProgressiveMode

​(int mode)

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality.

void

setTiling

​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)

Specifies that the image should be tiled in the output stream.

void

setTilingMode

​(int mode)

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined.

void

unsetCompression

()

Removes any previous compression type and quality settings.

void

unsetTiling

()

Removes any previous tile grid parameters specified by calls to

setTiling

.

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

Fields

Modifier and Type

Field

Description

protected boolean

canOffsetTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set.

protected boolean

canWriteCompressed

A

boolean

that is

true

if this writer
can write images using compression.

protected boolean

canWriteProgressive

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes.

protected boolean

canWriteTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set.

protected int

compressionMode

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values.

protected float

compressionQuality

A

float

containing the current compression quality
setting.

protected

String

compressionType

A

String

containing the name of the current
compression type, or

null

if none is set.

protected

String

[]

compressionTypes

An array of

String

s containing the names of the
available compression types.

protected

Locale

locale

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

.

static int

MODE_COPY_FROM_METADATA

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes.

static int

MODE_DEFAULT

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes.

static int

MODE_DISABLED

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes.

static int

MODE_EXPLICIT

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes.

protected

Dimension

[]

preferredTileSizes

An array of preferred tile size range pairs.

protected int

progressiveMode

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

.

protected int

tileGridXOffset

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise.

protected int

tileGridYOffset

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise.

protected int

tileHeight

The height of each tile if tiling has been set, or 0 otherwise.

protected int

tileWidth

The width of each tile if tiling has been set, or 0 otherwise.

protected int

tilingMode

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values.

protected boolean

tilingSet

A

boolean

that is

true

if tiling
parameters have been specified.

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

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set.

A

boolean

that is

true

if this writer
can write images using compression.

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes.

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set.

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values.

A

float

containing the current compression quality
setting.

A

String

containing the name of the current
compression type, or

null

if none is set.

An array of

String

s containing the names of the
available compression types.

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

.

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes.

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes.

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes.

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes.

An array of preferred tile size range pairs.

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

.

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise.

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise.

The height of each tile if tiling has been set, or 0 otherwise.

The width of each tile if tiling has been set, or 0 otherwise.

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values.

A

boolean

that is

true

if tiling
parameters have been specified.

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

Modifier

Constructor

Description

protected

ImageWriteParam

()

Constructs an empty

ImageWriteParam

.

ImageWriteParam

​(

Locale

locale)

Constructs an

ImageWriteParam

set to use a
given

Locale

.

---

#### Constructor Summary

Constructs an empty

ImageWriteParam

.

Constructs an

ImageWriteParam

set to use a
given

Locale

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canOffsetTiles

()

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing.

boolean

canWriteCompressed

()

Returns

true

if this writer supports compression.

boolean

canWriteProgressive

()

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

boolean

canWriteTiles

()

Returns

true

if the writer can perform tiling
while writing.

float

getBitRate

​(float quality)

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level.

int

getCompressionMode

()

Returns the current compression mode, if compression is
supported.

float

getCompressionQuality

()

Returns the current compression quality setting.

String

[]

getCompressionQualityDescriptions

()

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level.

float[]

getCompressionQualityValues

()

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level.

String

getCompressionType

()

Returns the currently set compression type, or

null

if none has been set.

String

[]

getCompressionTypes

()

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces.

Locale

getLocale

()

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

String

getLocalizedCompressionTypeName

()

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

Dimension

[]

getPreferredTileSizes

()

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream.

int

getProgressiveMode

()

Returns the current mode for writing the stream in a
progressive manner.

int

getTileGridXOffset

()

Returns the horizontal tile grid offset of an image as it will
be written to the output stream.

int

getTileGridYOffset

()

Returns the vertical tile grid offset of an image as it will
be written to the output stream.

int

getTileHeight

()

Returns the height of each tile in an image as it will be written to
the output stream.

int

getTileWidth

()

Returns the width of each tile in an image as it will be
written to the output stream.

int

getTilingMode

()

Returns the current tiling mode, if tiling is supported.

boolean

isCompressionLossless

()

Returns

true

if the current compression type
provides lossless compression.

void

setCompressionMode

​(int mode)

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined.

void

setCompressionQuality

​(float quality)

Sets the compression quality to a value between

0

and

1

.

void

setCompressionType

​(

String

compressionType)

Sets the compression type to one of the values indicated by

getCompressionTypes

.

void

setProgressiveMode

​(int mode)

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality.

void

setTiling

​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)

Specifies that the image should be tiled in the output stream.

void

setTilingMode

​(int mode)

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined.

void

unsetCompression

()

Removes any previous compression type and quality settings.

void

unsetTiling

()

Removes any previous tile grid parameters specified by calls to

setTiling

.

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

if the writer can perform tiling with
non-zero grid offsets while writing.

Returns

true

if this writer supports compression.

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

Returns

true

if the writer can perform tiling
while writing.

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level.

Returns the current compression mode, if compression is
supported.

Returns the current compression quality setting.

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level.

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level.

Returns the currently set compression type, or

null

if none has been set.

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces.

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream.

Returns the current mode for writing the stream in a
progressive manner.

Returns the horizontal tile grid offset of an image as it will
be written to the output stream.

Returns the vertical tile grid offset of an image as it will
be written to the output stream.

Returns the height of each tile in an image as it will be written to
the output stream.

Returns the width of each tile in an image as it will be
written to the output stream.

Returns the current tiling mode, if tiling is supported.

Returns

true

if the current compression type
provides lossless compression.

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined.

Sets the compression quality to a value between

0

and

1

.

Sets the compression type to one of the values indicated by

getCompressionTypes

.

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality.

Specifies that the image should be tiled in the output stream.

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined.

Removes any previous compression type and quality settings.

Removes any previous tile grid parameters specified by calls to

setTiling

.

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

============ FIELD DETAIL ===========

- Field Detail

- MODE_DISABLED

```java
public static final int MODE_DISABLED
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes. That is, when this mode is set the stream will

not

be tiled, progressive, or compressed, and the
relevant accessor methods will throw an

IllegalStateException

.

**See Also:** MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_DEFAULT

```java
public static final int MODE_DEFAULT
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed according to a
sensible default chosen internally by the writer in a plug-in
dependent way, and the relevant accessor methods will
throw an

IllegalStateException

.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_EXPLICIT

```java
public static final int MODE_EXPLICIT
```

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes. That is, when this mode
is set the stream will be tiled or compressed according to
additional information supplied to the corresponding

set

methods in this class and retrievable from the
corresponding

get

methods. Note that this mode is
not supported for progressive output.

**See Also:** MODE_DISABLED

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_COPY_FROM_METADATA

```java
public static final int MODE_COPY_FROM_METADATA
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed based on the contents
of stream and/or image metadata passed into the write
operation, and any relevant accessor methods will throw an

IllegalStateException

.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- canWriteTiles

```java
protected boolean canWriteTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

- tilingMode

```java
protected int tilingMode
```

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values. The default
is

MODE_COPY_FROM_METADATA

.

Subclasses that do not writing tiles may ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setTilingMode(int)

,

getTilingMode()

- preferredTileSizes

```java
protected
Dimension
[] preferredTileSizes
```

An array of preferred tile size range pairs. The default value
is

null

, which indicates that there are no
preferred sizes. If the value is non-

null

, it
must have an even length of at least two.

Subclasses that do not support writing tiles may ignore
this value.

**See Also:** getPreferredTileSizes()

- tilingSet

```java
protected boolean tilingSet
```

A

boolean

that is

true

if tiling
parameters have been specified.

Subclasses that do not support writing tiles may ignore
this value.

- tileWidth

```java
protected int tileWidth
```

The width of each tile if tiling has been set, or 0 otherwise.

Subclasses that do not support tiling may ignore this
value.

- tileHeight

```java
protected int tileHeight
```

The height of each tile if tiling has been set, or 0 otherwise.
The initial value is

0

.

Subclasses that do not support tiling may ignore this
value.

- canOffsetTiles

```java
protected boolean canOffsetTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

- tileGridXOffset

```java
protected int tileGridXOffset
```

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

- tileGridYOffset

```java
protected int tileGridYOffset
```

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

- canWriteProgressive

```java
protected boolean canWriteProgressive
```

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes. By default,
the value is

false

. Subclasses must set the value
manually.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

- progressiveMode

```java
protected int progressiveMode
```

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support progressive encoding may
ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

- canWriteCompressed

```java
protected boolean canWriteCompressed
```

A

boolean

that is

true

if this writer
can write images using compression. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support compression must ensure that
this value is set to

false

.

- compressionMode

```java
protected int compressionMode
```

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support compression may ignore this
value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setCompressionMode(int)

,

getCompressionMode()

- compressionTypes

```java
protected
String
[] compressionTypes
```

An array of

String

s containing the names of the
available compression types. Subclasses must set the value
manually.

Subclasses that do not support compression may ignore this
value.

- compressionType

```java
protected
String
compressionType
```

A

String

containing the name of the current
compression type, or

null

if none is set.

Subclasses that do not support compression may ignore this
value.

- compressionQuality

```java
protected float compressionQuality
```

A

float

containing the current compression quality
setting. The initial value is

1.0F

.

Subclasses that do not support compression may ignore this
value.

- locale

```java
protected
Locale
locale
```

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

. Subclasses must set the value
manually.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageWriteParam

```java
protected ImageWriteParam()
```

Constructs an empty

ImageWriteParam

. It is up to
the subclass to set up the instance variables properly.

- ImageWriteParam

```java
public ImageWriteParam​(
Locale
locale)
```

Constructs an

ImageWriteParam

set to use a
given

Locale

.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

============ METHOD DETAIL ==========

- Method Detail

- getLocale

```java
public
Locale
getLocale()
```

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

**Returns:** the current

Locale

, or

null

.

- canWriteTiles

```java
public boolean canWriteTiles()
```

Returns

true

if the writer can perform tiling
while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

.

**Returns:** true

if the writer supports tiling.
**See Also:** canOffsetTiles()

,

setTiling(int, int, int, int)

- canOffsetTiles

```java
public boolean canOffsetTiles()
```

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

if the grid offset
arguments are not both zero. If

canWriteTiles

returns

false

, this method will return

false

as well.

**Returns:** true

if the writer supports non-zero tile
offsets.
**See Also:** canWriteTiles()

,

setTiling(int, int, int, int)

- setTilingMode

```java
public void setTilingMode​(int mode)
```

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined. The modes are interpreted as follows:

- MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

**Parameters:** mode

- The mode to use for tiling.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** setTiling(int, int, int, int)

,

getTilingMode()

- getTilingMode

```java
public int getTilingMode()
```

Returns the current tiling mode, if tiling is supported.
Otherwise throws an

UnsupportedOperationException

.

**Returns:** the current tiling mode.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**See Also:** setTilingMode(int)

- getPreferredTileSizes

```java
public
Dimension
[] getPreferredTileSizes()
```

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream. The returned array is a copy.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.
**Throws:** UnsupportedOperationException

- if the plug-in does
not support tiling.

- setTiling

```java
public void setTiling​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)
```

Specifies that the image should be tiled in the output stream.
The

tileWidth

and

tileHeight

parameters specify the width and height of the tiles in the
file. If the tile width or height is greater than the width or
height of the image, the image is not tiled in that dimension.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

**Parameters:** tileWidth

- the width of each tile.
**Parameters:** tileHeight

- the height of each tile.
**Parameters:** tileGridXOffset

- the horizontal offset of the tile grid.
**Parameters:** tileGridYOffset

- the vertical offset of the tile grid.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support grid offsets, and the grid offsets are not both zero.
**Throws:** IllegalArgumentException

- if the tile size is not
within one of the allowable ranges returned by

getPreferredTileSizes

.
**Throws:** IllegalArgumentException

- if

tileWidth

or

tileHeight

is less than or equal to 0.
**See Also:** canWriteTiles

,

canOffsetTiles

,

getTileWidth()

,

getTileHeight()

,

getTileGridXOffset()

,

getTileGridYOffset()

- unsetTiling

```java
public void unsetTiling()
```

Removes any previous tile grid parameters specified by calls to

setTiling

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**See Also:** setTiling(int, int, int, int)

- getTileWidth

```java
public int getTileWidth()
```

Returns the width of each tile in an image as it will be
written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile width to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileHeight()

- getTileHeight

```java
public int getTileHeight()
```

Returns the height of each tile in an image as it will be written to
the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile height to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileWidth()

- getTileGridXOffset

```java
public int getTileGridXOffset()
```

Returns the horizontal tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid X offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridYOffset()

- getTileGridYOffset

```java
public int getTileGridYOffset()
```

Returns the vertical tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid Y offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridXOffset()

- canWriteProgressive

```java
public boolean canWriteProgressive()
```

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

**Returns:** true

if the writer supports progressive
encoding.
**See Also:** setProgressiveMode(int)

,

getProgressiveMode()

- setProgressiveMode

```java
public void setProgressiveMode​(int mode)
```

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality. If progressive encoding is not
supported, an

UnsupportedOperationException

will
be thrown.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting progression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getProgressiveMode()

- getProgressiveMode

```java
public int getProgressiveMode()
```

Returns the current mode for writing the stream in a
progressive manner.

**Returns:** the current mode for progressive encoding.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**See Also:** setProgressiveMode(int)

- canWriteCompressed

```java
public boolean canWriteCompressed()
```

Returns

true

if this writer supports compression.

**Returns:** true

if the writer supports compression.

- setCompressionMode

```java
public void setCompressionMode​(int mode)
```

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined. The

mode

argument must be one of the four modes, interpreted as follows:

- MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting compression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression, or does not support the requested mode.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getCompressionMode()

- getCompressionMode

```java
public int getCompressionMode()
```

Returns the current compression mode, if compression is
supported.

**Returns:** the current compression mode.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**See Also:** setCompressionMode(int)

- getCompressionTypes

```java
public
String
[] getCompressionTypes()
```

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces. The array
returned is a copy.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

**Returns:** an array of

String

s containing the
(non-localized) names of available compression types, or

null

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.

- setCompressionType

```java
public void setCompressionType​(
String
compressionType)
```

Sets the compression type to one of the values indicated by

getCompressionTypes

. If a value of

null

is passed in, any previous setting is
removed.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

**Parameters:** compressionType

- one of the

String

s returned
by

getCompressionTypes

, or

null

to
remove any previous setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if there are no
settable compression types.
**Throws:** IllegalArgumentException

- if

compressionType

is non-

null

but is not
one of the values returned by

getCompressionTypes

.
**See Also:** getCompressionTypes()

,

getCompressionType()

,

unsetCompression()

- getCompressionType

```java
public
String
getCompressionType()
```

Returns the currently set compression type, or

null

if none has been set. The type is returned
as a

String

from among those returned by

getCompressionTypes

.
If no compression type has been set,

null

is
returned.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

**Returns:** the current compression type as a

String

,
or

null

if no type is set.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

- unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression type and quality settings.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

,

setCompressionQuality(float)

- getLocalizedCompressionTypeName

```java
public
String
getLocalizedCompressionTypeName()
```

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

**Returns:** a

String

containing a localized version of
the name of the current compression type.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if no compression type is set.

- isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

true

if the current compression type
provides lossless compression. If a plug-in provides only
one mandatory compression type, then this method may be
called without calling

setCompressionType

first.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

**Returns:** true

if the current compression type is
lossless.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

- setCompressionQuality

```java
public void setCompressionQuality​(float quality)
```

Sets the compression quality to a value between

0

and

1

. Only a single compression quality setting
is supported by default; writers can provide extended versions
of

ImageWriteParam

that offer more control. For
lossy compression schemes, the compression quality should
control the tradeoff between file size and image quality (for
example, by choosing quantization tables when writing JPEG
images). For lossless schemes, the compression quality may be
used to control the tradeoff between file size and time taken
to perform the compression (for example, by optimizing row
filters and setting the ZLIB compression level when writing
PNG images).

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

**Parameters:** quality

- a

float

between

0

and

1

indicating the desired quality level.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.
**See Also:** getCompressionQuality()

- getCompressionQuality

```java
public float getCompressionQuality()
```

Returns the current compression quality setting.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

**Returns:** the current compression quality setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** setCompressionQuality(float)

- getBitRate

```java
public float getBitRate​(float quality)
```

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level. The value will typically lie
between

0

and

1

, with smaller values
indicating more compression. A special value of

-1.0F

is used to indicate that no estimate is
available.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

**Parameters:** quality

- the quality setting whose bit rate is to be
queried.
**Returns:** an estimate of the compressed bit rate, or

-1.0F

if no estimate is available.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.

- getCompressionQualityDescriptions

```java
public
String
[] getCompressionQualityDescriptions()
```

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level. The

String

with index

i

provides a description of the range of quality levels between

getCompressionQualityValues[i]

and

getCompressionQualityValues[i + 1]

. Note that the
length of the array returned from

getCompressionQualityValues

will always be one
greater than that returned from

getCompressionQualityDescriptions

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

String

s containing localized
descriptions of the compression quality levels.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityValues()

- getCompressionQualityValues

```java
public float[] getCompressionQualityValues()
```

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level. See

getCompressionQualityDescriptions

for more information.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

float

s indicating the
boundaries between the compression quality levels as described
by the

String

s from

getCompressionQualityDescriptions

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityDescriptions()

Field Detail

- MODE_DISABLED

```java
public static final int MODE_DISABLED
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes. That is, when this mode is set the stream will

not

be tiled, progressive, or compressed, and the
relevant accessor methods will throw an

IllegalStateException

.

**See Also:** MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_DEFAULT

```java
public static final int MODE_DEFAULT
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed according to a
sensible default chosen internally by the writer in a plug-in
dependent way, and the relevant accessor methods will
throw an

IllegalStateException

.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_EXPLICIT

```java
public static final int MODE_EXPLICIT
```

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes. That is, when this mode
is set the stream will be tiled or compressed according to
additional information supplied to the corresponding

set

methods in this class and retrievable from the
corresponding

get

methods. Note that this mode is
not supported for progressive output.

**See Also:** MODE_DISABLED

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- MODE_COPY_FROM_METADATA

```java
public static final int MODE_COPY_FROM_METADATA
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed based on the contents
of stream and/or image metadata passed into the write
operation, and any relevant accessor methods will throw an

IllegalStateException

.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

- canWriteTiles

```java
protected boolean canWriteTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

- tilingMode

```java
protected int tilingMode
```

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values. The default
is

MODE_COPY_FROM_METADATA

.

Subclasses that do not writing tiles may ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setTilingMode(int)

,

getTilingMode()

- preferredTileSizes

```java
protected
Dimension
[] preferredTileSizes
```

An array of preferred tile size range pairs. The default value
is

null

, which indicates that there are no
preferred sizes. If the value is non-

null

, it
must have an even length of at least two.

Subclasses that do not support writing tiles may ignore
this value.

**See Also:** getPreferredTileSizes()

- tilingSet

```java
protected boolean tilingSet
```

A

boolean

that is

true

if tiling
parameters have been specified.

Subclasses that do not support writing tiles may ignore
this value.

- tileWidth

```java
protected int tileWidth
```

The width of each tile if tiling has been set, or 0 otherwise.

Subclasses that do not support tiling may ignore this
value.

- tileHeight

```java
protected int tileHeight
```

The height of each tile if tiling has been set, or 0 otherwise.
The initial value is

0

.

Subclasses that do not support tiling may ignore this
value.

- canOffsetTiles

```java
protected boolean canOffsetTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

- tileGridXOffset

```java
protected int tileGridXOffset
```

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

- tileGridYOffset

```java
protected int tileGridYOffset
```

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

- canWriteProgressive

```java
protected boolean canWriteProgressive
```

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes. By default,
the value is

false

. Subclasses must set the value
manually.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

- progressiveMode

```java
protected int progressiveMode
```

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support progressive encoding may
ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

- canWriteCompressed

```java
protected boolean canWriteCompressed
```

A

boolean

that is

true

if this writer
can write images using compression. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support compression must ensure that
this value is set to

false

.

- compressionMode

```java
protected int compressionMode
```

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support compression may ignore this
value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setCompressionMode(int)

,

getCompressionMode()

- compressionTypes

```java
protected
String
[] compressionTypes
```

An array of

String

s containing the names of the
available compression types. Subclasses must set the value
manually.

Subclasses that do not support compression may ignore this
value.

- compressionType

```java
protected
String
compressionType
```

A

String

containing the name of the current
compression type, or

null

if none is set.

Subclasses that do not support compression may ignore this
value.

- compressionQuality

```java
protected float compressionQuality
```

A

float

containing the current compression quality
setting. The initial value is

1.0F

.

Subclasses that do not support compression may ignore this
value.

- locale

```java
protected
Locale
locale
```

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

. Subclasses must set the value
manually.

---

#### Field Detail

MODE_DISABLED

```java
public static final int MODE_DISABLED
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes. That is, when this mode is set the stream will

not

be tiled, progressive, or compressed, and the
relevant accessor methods will throw an

IllegalStateException

.

**See Also:** MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### MODE_DISABLED

public static final int MODE_DISABLED

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

,
and

setCompressionMode

to disable a feature for
future writes. That is, when this mode is set the stream will

not

be tiled, progressive, or compressed, and the
relevant accessor methods will throw an

IllegalStateException

.

MODE_DEFAULT

```java
public static final int MODE_DEFAULT
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed according to a
sensible default chosen internally by the writer in a plug-in
dependent way, and the relevant accessor methods will
throw an

IllegalStateException

.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### MODE_DEFAULT

public static final int MODE_DEFAULT

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, and

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed according to a
sensible default chosen internally by the writer in a plug-in
dependent way, and the relevant accessor methods will
throw an

IllegalStateException

.

MODE_EXPLICIT

```java
public static final int MODE_EXPLICIT
```

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes. That is, when this mode
is set the stream will be tiled or compressed according to
additional information supplied to the corresponding

set

methods in this class and retrievable from the
corresponding

get

methods. Note that this mode is
not supported for progressive output.

**See Also:** MODE_DISABLED

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### MODE_EXPLICIT

public static final int MODE_EXPLICIT

A constant value that may be passed into methods such as

setTilingMode

or

setCompressionMode

to enable a feature for future writes. That is, when this mode
is set the stream will be tiled or compressed according to
additional information supplied to the corresponding

set

methods in this class and retrievable from the
corresponding

get

methods. Note that this mode is
not supported for progressive output.

MODE_COPY_FROM_METADATA

```java
public static final int MODE_COPY_FROM_METADATA
```

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed based on the contents
of stream and/or image metadata passed into the write
operation, and any relevant accessor methods will throw an

IllegalStateException

.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

,

setTilingMode(int)

,

getTilingMode()

,

setCompressionMode(int)

,

getCompressionMode()

,

Constant Field Values

---

#### MODE_COPY_FROM_METADATA

public static final int MODE_COPY_FROM_METADATA

A constant value that may be passed into methods such as

setTilingMode

,

setProgressiveMode

, or

setCompressionMode

to enable that feature for
future writes. That is, when this mode is enabled the stream
will be tiled, progressive, or compressed based on the contents
of stream and/or image metadata passed into the write
operation, and any relevant accessor methods will throw an

IllegalStateException

.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

This is the default mode for all features, so that a read
including metadata followed by a write including metadata will
preserve as much information as possible.

canWriteTiles

```java
protected boolean canWriteTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

---

#### canWriteTiles

protected boolean canWriteTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tile width and tile height
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

Subclasses that do not support writing tiles should ensure
that this value is set to

false

.

tilingMode

```java
protected int tilingMode
```

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values. The default
is

MODE_COPY_FROM_METADATA

.

Subclasses that do not writing tiles may ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setTilingMode(int)

,

getTilingMode()

---

#### tilingMode

protected int tilingMode

The mode controlling tiling settings, which Must be
set to one of the four

MODE_*

values. The default
is

MODE_COPY_FROM_METADATA

.

Subclasses that do not writing tiles may ignore this value.

Subclasses that do not writing tiles may ignore this value.

preferredTileSizes

```java
protected
Dimension
[] preferredTileSizes
```

An array of preferred tile size range pairs. The default value
is

null

, which indicates that there are no
preferred sizes. If the value is non-

null

, it
must have an even length of at least two.

Subclasses that do not support writing tiles may ignore
this value.

**See Also:** getPreferredTileSizes()

---

#### preferredTileSizes

protected

Dimension

[] preferredTileSizes

An array of preferred tile size range pairs. The default value
is

null

, which indicates that there are no
preferred sizes. If the value is non-

null

, it
must have an even length of at least two.

Subclasses that do not support writing tiles may ignore
this value.

Subclasses that do not support writing tiles may ignore
this value.

tilingSet

```java
protected boolean tilingSet
```

A

boolean

that is

true

if tiling
parameters have been specified.

Subclasses that do not support writing tiles may ignore
this value.

---

#### tilingSet

protected boolean tilingSet

A

boolean

that is

true

if tiling
parameters have been specified.

Subclasses that do not support writing tiles may ignore
this value.

Subclasses that do not support writing tiles may ignore
this value.

tileWidth

```java
protected int tileWidth
```

The width of each tile if tiling has been set, or 0 otherwise.

Subclasses that do not support tiling may ignore this
value.

---

#### tileWidth

protected int tileWidth

The width of each tile if tiling has been set, or 0 otherwise.

Subclasses that do not support tiling may ignore this
value.

Subclasses that do not support tiling may ignore this
value.

tileHeight

```java
protected int tileHeight
```

The height of each tile if tiling has been set, or 0 otherwise.
The initial value is

0

.

Subclasses that do not support tiling may ignore this
value.

---

#### tileHeight

protected int tileHeight

The height of each tile if tiling has been set, or 0 otherwise.
The initial value is

0

.

Subclasses that do not support tiling may ignore this
value.

Subclasses that do not support tiling may ignore this
value.

canOffsetTiles

```java
protected boolean canOffsetTiles
```

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

---

#### canOffsetTiles

protected boolean canOffsetTiles

A

boolean

that is

true

if this

ImageWriteParam

allows tiling grid offset
parameters to be set. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

Subclasses that do not support writing tiles, or that
support writing but not offsetting tiles must ensure that this
value is set to

false

.

tileGridXOffset

```java
protected int tileGridXOffset
```

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

---

#### tileGridXOffset

protected int tileGridXOffset

The amount by which the tile grid origin should be offset
horizontally from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

Subclasses that do not support offsetting tiles may ignore
this value.

tileGridYOffset

```java
protected int tileGridYOffset
```

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

---

#### tileGridYOffset

protected int tileGridYOffset

The amount by which the tile grid origin should be offset
vertically from the image origin if tiling has been set,
or 0 otherwise. The initial value is

0

.

Subclasses that do not support offsetting tiles may ignore
this value.

Subclasses that do not support offsetting tiles may ignore
this value.

canWriteProgressive

```java
protected boolean canWriteProgressive
```

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes. By default,
the value is

false

. Subclasses must set the value
manually.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

---

#### canWriteProgressive

protected boolean canWriteProgressive

A

boolean

that is

true

if this

ImageWriteParam

allows images to be written as a
progressive sequence of increasing quality passes. By default,
the value is

false

. Subclasses must set the value
manually.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

Subclasses that do not support progressive encoding must
ensure that this value is set to

false

.

progressiveMode

```java
protected int progressiveMode
```

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support progressive encoding may
ignore this value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setProgressiveMode(int)

,

getProgressiveMode()

---

#### progressiveMode

protected int progressiveMode

The mode controlling progressive encoding, which must be set to
one of the four

MODE_*

values, except

MODE_EXPLICIT

. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support progressive encoding may
ignore this value.

Subclasses that do not support progressive encoding may
ignore this value.

canWriteCompressed

```java
protected boolean canWriteCompressed
```

A

boolean

that is

true

if this writer
can write images using compression. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support compression must ensure that
this value is set to

false

.

---

#### canWriteCompressed

protected boolean canWriteCompressed

A

boolean

that is

true

if this writer
can write images using compression. By default, the value is

false

. Subclasses must set the value manually.

Subclasses that do not support compression must ensure that
this value is set to

false

.

Subclasses that do not support compression must ensure that
this value is set to

false

.

compressionMode

```java
protected int compressionMode
```

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support compression may ignore this
value.

**See Also:** MODE_DISABLED

,

MODE_EXPLICIT

,

MODE_COPY_FROM_METADATA

,

MODE_DEFAULT

,

setCompressionMode(int)

,

getCompressionMode()

---

#### compressionMode

protected int compressionMode

The mode controlling compression settings, which must be set to
one of the four

MODE_*

values. The default is

MODE_COPY_FROM_METADATA

.

Subclasses that do not support compression may ignore this
value.

Subclasses that do not support compression may ignore this
value.

compressionTypes

```java
protected
String
[] compressionTypes
```

An array of

String

s containing the names of the
available compression types. Subclasses must set the value
manually.

Subclasses that do not support compression may ignore this
value.

---

#### compressionTypes

protected

String

[] compressionTypes

An array of

String

s containing the names of the
available compression types. Subclasses must set the value
manually.

Subclasses that do not support compression may ignore this
value.

Subclasses that do not support compression may ignore this
value.

compressionType

```java
protected
String
compressionType
```

A

String

containing the name of the current
compression type, or

null

if none is set.

Subclasses that do not support compression may ignore this
value.

---

#### compressionType

protected

String

compressionType

A

String

containing the name of the current
compression type, or

null

if none is set.

Subclasses that do not support compression may ignore this
value.

Subclasses that do not support compression may ignore this
value.

compressionQuality

```java
protected float compressionQuality
```

A

float

containing the current compression quality
setting. The initial value is

1.0F

.

Subclasses that do not support compression may ignore this
value.

---

#### compressionQuality

protected float compressionQuality

A

float

containing the current compression quality
setting. The initial value is

1.0F

.

Subclasses that do not support compression may ignore this
value.

Subclasses that do not support compression may ignore this
value.

locale

```java
protected
Locale
locale
```

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

. Subclasses must set the value
manually.

---

#### locale

protected

Locale

locale

A

Locale

to be used to localize compression type
names and quality descriptions, or

null

to use a
default

Locale

. Subclasses must set the value
manually.

Constructor Detail

- ImageWriteParam

```java
protected ImageWriteParam()
```

Constructs an empty

ImageWriteParam

. It is up to
the subclass to set up the instance variables properly.

- ImageWriteParam

```java
public ImageWriteParam​(
Locale
locale)
```

Constructs an

ImageWriteParam

set to use a
given

Locale

.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

---

#### Constructor Detail

ImageWriteParam

```java
protected ImageWriteParam()
```

Constructs an empty

ImageWriteParam

. It is up to
the subclass to set up the instance variables properly.

---

#### ImageWriteParam

protected ImageWriteParam()

Constructs an empty

ImageWriteParam

. It is up to
the subclass to set up the instance variables properly.

ImageWriteParam

```java
public ImageWriteParam​(
Locale
locale)
```

Constructs an

ImageWriteParam

set to use a
given

Locale

.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

---

#### ImageWriteParam

public ImageWriteParam​(

Locale

locale)

Constructs an

ImageWriteParam

set to use a
given

Locale

.

Method Detail

- getLocale

```java
public
Locale
getLocale()
```

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

**Returns:** the current

Locale

, or

null

.

- canWriteTiles

```java
public boolean canWriteTiles()
```

Returns

true

if the writer can perform tiling
while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

.

**Returns:** true

if the writer supports tiling.
**See Also:** canOffsetTiles()

,

setTiling(int, int, int, int)

- canOffsetTiles

```java
public boolean canOffsetTiles()
```

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

if the grid offset
arguments are not both zero. If

canWriteTiles

returns

false

, this method will return

false

as well.

**Returns:** true

if the writer supports non-zero tile
offsets.
**See Also:** canWriteTiles()

,

setTiling(int, int, int, int)

- setTilingMode

```java
public void setTilingMode​(int mode)
```

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined. The modes are interpreted as follows:

- MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

**Parameters:** mode

- The mode to use for tiling.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** setTiling(int, int, int, int)

,

getTilingMode()

- getTilingMode

```java
public int getTilingMode()
```

Returns the current tiling mode, if tiling is supported.
Otherwise throws an

UnsupportedOperationException

.

**Returns:** the current tiling mode.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**See Also:** setTilingMode(int)

- getPreferredTileSizes

```java
public
Dimension
[] getPreferredTileSizes()
```

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream. The returned array is a copy.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.
**Throws:** UnsupportedOperationException

- if the plug-in does
not support tiling.

- setTiling

```java
public void setTiling​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)
```

Specifies that the image should be tiled in the output stream.
The

tileWidth

and

tileHeight

parameters specify the width and height of the tiles in the
file. If the tile width or height is greater than the width or
height of the image, the image is not tiled in that dimension.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

**Parameters:** tileWidth

- the width of each tile.
**Parameters:** tileHeight

- the height of each tile.
**Parameters:** tileGridXOffset

- the horizontal offset of the tile grid.
**Parameters:** tileGridYOffset

- the vertical offset of the tile grid.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support grid offsets, and the grid offsets are not both zero.
**Throws:** IllegalArgumentException

- if the tile size is not
within one of the allowable ranges returned by

getPreferredTileSizes

.
**Throws:** IllegalArgumentException

- if

tileWidth

or

tileHeight

is less than or equal to 0.
**See Also:** canWriteTiles

,

canOffsetTiles

,

getTileWidth()

,

getTileHeight()

,

getTileGridXOffset()

,

getTileGridYOffset()

- unsetTiling

```java
public void unsetTiling()
```

Removes any previous tile grid parameters specified by calls to

setTiling

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**See Also:** setTiling(int, int, int, int)

- getTileWidth

```java
public int getTileWidth()
```

Returns the width of each tile in an image as it will be
written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile width to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileHeight()

- getTileHeight

```java
public int getTileHeight()
```

Returns the height of each tile in an image as it will be written to
the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile height to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileWidth()

- getTileGridXOffset

```java
public int getTileGridXOffset()
```

Returns the horizontal tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid X offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridYOffset()

- getTileGridYOffset

```java
public int getTileGridYOffset()
```

Returns the vertical tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid Y offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridXOffset()

- canWriteProgressive

```java
public boolean canWriteProgressive()
```

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

**Returns:** true

if the writer supports progressive
encoding.
**See Also:** setProgressiveMode(int)

,

getProgressiveMode()

- setProgressiveMode

```java
public void setProgressiveMode​(int mode)
```

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality. If progressive encoding is not
supported, an

UnsupportedOperationException

will
be thrown.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting progression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getProgressiveMode()

- getProgressiveMode

```java
public int getProgressiveMode()
```

Returns the current mode for writing the stream in a
progressive manner.

**Returns:** the current mode for progressive encoding.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**See Also:** setProgressiveMode(int)

- canWriteCompressed

```java
public boolean canWriteCompressed()
```

Returns

true

if this writer supports compression.

**Returns:** true

if the writer supports compression.

- setCompressionMode

```java
public void setCompressionMode​(int mode)
```

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined. The

mode

argument must be one of the four modes, interpreted as follows:

- MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting compression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression, or does not support the requested mode.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getCompressionMode()

- getCompressionMode

```java
public int getCompressionMode()
```

Returns the current compression mode, if compression is
supported.

**Returns:** the current compression mode.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**See Also:** setCompressionMode(int)

- getCompressionTypes

```java
public
String
[] getCompressionTypes()
```

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces. The array
returned is a copy.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

**Returns:** an array of

String

s containing the
(non-localized) names of available compression types, or

null

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.

- setCompressionType

```java
public void setCompressionType​(
String
compressionType)
```

Sets the compression type to one of the values indicated by

getCompressionTypes

. If a value of

null

is passed in, any previous setting is
removed.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

**Parameters:** compressionType

- one of the

String

s returned
by

getCompressionTypes

, or

null

to
remove any previous setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if there are no
settable compression types.
**Throws:** IllegalArgumentException

- if

compressionType

is non-

null

but is not
one of the values returned by

getCompressionTypes

.
**See Also:** getCompressionTypes()

,

getCompressionType()

,

unsetCompression()

- getCompressionType

```java
public
String
getCompressionType()
```

Returns the currently set compression type, or

null

if none has been set. The type is returned
as a

String

from among those returned by

getCompressionTypes

.
If no compression type has been set,

null

is
returned.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

**Returns:** the current compression type as a

String

,
or

null

if no type is set.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

- unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression type and quality settings.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

,

setCompressionQuality(float)

- getLocalizedCompressionTypeName

```java
public
String
getLocalizedCompressionTypeName()
```

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

**Returns:** a

String

containing a localized version of
the name of the current compression type.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if no compression type is set.

- isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

true

if the current compression type
provides lossless compression. If a plug-in provides only
one mandatory compression type, then this method may be
called without calling

setCompressionType

first.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

**Returns:** true

if the current compression type is
lossless.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

- setCompressionQuality

```java
public void setCompressionQuality​(float quality)
```

Sets the compression quality to a value between

0

and

1

. Only a single compression quality setting
is supported by default; writers can provide extended versions
of

ImageWriteParam

that offer more control. For
lossy compression schemes, the compression quality should
control the tradeoff between file size and image quality (for
example, by choosing quantization tables when writing JPEG
images). For lossless schemes, the compression quality may be
used to control the tradeoff between file size and time taken
to perform the compression (for example, by optimizing row
filters and setting the ZLIB compression level when writing
PNG images).

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

**Parameters:** quality

- a

float

between

0

and

1

indicating the desired quality level.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.
**See Also:** getCompressionQuality()

- getCompressionQuality

```java
public float getCompressionQuality()
```

Returns the current compression quality setting.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

**Returns:** the current compression quality setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** setCompressionQuality(float)

- getBitRate

```java
public float getBitRate​(float quality)
```

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level. The value will typically lie
between

0

and

1

, with smaller values
indicating more compression. A special value of

-1.0F

is used to indicate that no estimate is
available.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

**Parameters:** quality

- the quality setting whose bit rate is to be
queried.
**Returns:** an estimate of the compressed bit rate, or

-1.0F

if no estimate is available.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.

- getCompressionQualityDescriptions

```java
public
String
[] getCompressionQualityDescriptions()
```

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level. The

String

with index

i

provides a description of the range of quality levels between

getCompressionQualityValues[i]

and

getCompressionQualityValues[i + 1]

. Note that the
length of the array returned from

getCompressionQualityValues

will always be one
greater than that returned from

getCompressionQualityDescriptions

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

String

s containing localized
descriptions of the compression quality levels.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityValues()

- getCompressionQualityValues

```java
public float[] getCompressionQualityValues()
```

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level. See

getCompressionQualityDescriptions

for more information.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

float

s indicating the
boundaries between the compression quality levels as described
by the

String

s from

getCompressionQualityDescriptions

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityDescriptions()

---

#### Method Detail

getLocale

```java
public
Locale
getLocale()
```

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

**Returns:** the current

Locale

, or

null

.

---

#### getLocale

public

Locale

getLocale()

Returns the currently set

Locale

, or

null

if only a default

Locale

is
supported.

canWriteTiles

```java
public boolean canWriteTiles()
```

Returns

true

if the writer can perform tiling
while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

.

**Returns:** true

if the writer supports tiling.
**See Also:** canOffsetTiles()

,

setTiling(int, int, int, int)

---

#### canWriteTiles

public boolean canWriteTiles()

Returns

true

if the writer can perform tiling
while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

.

canOffsetTiles

```java
public boolean canOffsetTiles()
```

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

if the grid offset
arguments are not both zero. If

canWriteTiles

returns

false

, this method will return

false

as well.

**Returns:** true

if the writer supports non-zero tile
offsets.
**See Also:** canWriteTiles()

,

setTiling(int, int, int, int)

---

#### canOffsetTiles

public boolean canOffsetTiles()

Returns

true

if the writer can perform tiling with
non-zero grid offsets while writing. If this method returns

false

, then

setTiling

will throw an

UnsupportedOperationException

if the grid offset
arguments are not both zero. If

canWriteTiles

returns

false

, this method will return

false

as well.

setTilingMode

```java
public void setTilingMode​(int mode)
```

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined. The modes are interpreted as follows:

- MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

**Parameters:** mode

- The mode to use for tiling.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** setTiling(int, int, int, int)

,

getTilingMode()

---

#### setTilingMode

public void setTilingMode​(int mode)

Determines whether the image will be tiled in the output
stream and, if it will, how the tiling parameters will be
determined. The modes are interpreted as follows:

- MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

MODE_DISABLED

- The image will not be tiled.

setTiling

will throw an

IllegalStateException

.

MODE_DEFAULT

- The image will be tiled using
default parameters.

setTiling

will throw an

IllegalStateException

.

MODE_EXPLICIT

- The image will be tiled
according to parameters given in the

setTiling

method. Any previously set tiling parameters are discarded.

MODE_COPY_FROM_METADATA

- The image will
conform to the metadata object passed in to a write.

setTiling

will throw an

IllegalStateException

.

getTilingMode

```java
public int getTilingMode()
```

Returns the current tiling mode, if tiling is supported.
Otherwise throws an

UnsupportedOperationException

.

**Returns:** the current tiling mode.
**Throws:** UnsupportedOperationException

- if

canWriteTiles

returns

false

.
**See Also:** setTilingMode(int)

---

#### getTilingMode

public int getTilingMode()

Returns the current tiling mode, if tiling is supported.
Otherwise throws an

UnsupportedOperationException

.

getPreferredTileSizes

```java
public
Dimension
[] getPreferredTileSizes()
```

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream. The returned array is a copy.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.
**Throws:** UnsupportedOperationException

- if the plug-in does
not support tiling.

---

#### getPreferredTileSizes

public

Dimension

[] getPreferredTileSizes()

Returns an array of

Dimension

s indicating the
legal size ranges for tiles as they will be encoded in the
output file or stream. The returned array is a copy.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, use the same width and height
for both elements. To specify an arbitrary range, a value of

null

is used in place of an actual array of

Dimension

s.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

If no array is specified on the constructor, but tiling is
allowed, then this method returns

null

.

setTiling

```java
public void setTiling​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)
```

Specifies that the image should be tiled in the output stream.
The

tileWidth

and

tileHeight

parameters specify the width and height of the tiles in the
file. If the tile width or height is greater than the width or
height of the image, the image is not tiled in that dimension.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

**Parameters:** tileWidth

- the width of each tile.
**Parameters:** tileHeight

- the height of each tile.
**Parameters:** tileGridXOffset

- the horizontal offset of the tile grid.
**Parameters:** tileGridYOffset

- the vertical offset of the tile grid.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support grid offsets, and the grid offsets are not both zero.
**Throws:** IllegalArgumentException

- if the tile size is not
within one of the allowable ranges returned by

getPreferredTileSizes

.
**Throws:** IllegalArgumentException

- if

tileWidth

or

tileHeight

is less than or equal to 0.
**See Also:** canWriteTiles

,

canOffsetTiles

,

getTileWidth()

,

getTileHeight()

,

getTileGridXOffset()

,

getTileGridYOffset()

---

#### setTiling

public void setTiling​(int tileWidth,
int tileHeight,
int tileGridXOffset,
int tileGridYOffset)

Specifies that the image should be tiled in the output stream.
The

tileWidth

and

tileHeight

parameters specify the width and height of the tiles in the
file. If the tile width or height is greater than the width or
height of the image, the image is not tiled in that dimension.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

If

canOffsetTiles

returns

false

,
then the

tileGridXOffset

and

tileGridYOffset

parameters must be zero.

unsetTiling

```java
public void unsetTiling()
```

Removes any previous tile grid parameters specified by calls to

setTiling

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**See Also:** setTiling(int, int, int, int)

---

#### unsetTiling

public void unsetTiling()

Removes any previous tile grid parameters specified by calls to

setTiling

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

The default implementation sets the instance variables

tileWidth

,

tileHeight

,

tileGridXOffset

, and

tileGridYOffset

to

0

.

getTileWidth

```java
public int getTileWidth()
```

Returns the width of each tile in an image as it will be
written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile width to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileHeight()

---

#### getTileWidth

public int getTileWidth()

Returns the width of each tile in an image as it will be
written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

getTileHeight

```java
public int getTileHeight()
```

Returns the height of each tile in an image as it will be written to
the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile height to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileWidth()

---

#### getTileHeight

public int getTileHeight()

Returns the height of each tile in an image as it will be written to
the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

getTileGridXOffset

```java
public int getTileGridXOffset()
```

Returns the horizontal tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid X offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridYOffset()

---

#### getTileGridXOffset

public int getTileGridXOffset()

Returns the horizontal tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

getTileGridYOffset

```java
public int getTileGridYOffset()
```

Returns the vertical tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

**Returns:** the tile grid Y offset to be used for encoding.
**Throws:** UnsupportedOperationException

- if the plug-in does not
support tiling.
**Throws:** IllegalStateException

- if the tiling mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the tiling parameters have
not been set.
**See Also:** setTiling(int, int, int, int)

,

getTileGridXOffset()

---

#### getTileGridYOffset

public int getTileGridYOffset()

Returns the vertical tile grid offset of an image as it will
be written to the output stream. If tiling parameters have not
been set, an

IllegalStateException

is thrown.

canWriteProgressive

```java
public boolean canWriteProgressive()
```

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

**Returns:** true

if the writer supports progressive
encoding.
**See Also:** setProgressiveMode(int)

,

getProgressiveMode()

---

#### canWriteProgressive

public boolean canWriteProgressive()

Returns

true

if the writer can write out images
as a series of passes of progressively increasing quality.

setProgressiveMode

```java
public void setProgressiveMode​(int mode)
```

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality. If progressive encoding is not
supported, an

UnsupportedOperationException

will
be thrown.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting progression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getProgressiveMode()

---

#### setProgressiveMode

public void setProgressiveMode​(int mode)

Specifies that the writer is to write the image out in a
progressive mode such that the stream will contain a series of
scans of increasing quality. If progressive encoding is not
supported, an

UnsupportedOperationException

will
be thrown.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

The mode argument determines how
the progression parameters are chosen, and must be either

MODE_DISABLED

,

MODE_COPY_FROM_METADATA

, or

MODE_DEFAULT

. Otherwise an

IllegalArgumentException

is thrown.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

The modes are interpreted as follows:

- MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

MODE_DISABLED

- No progression. Use this to
turn off progression.

MODE_COPY_FROM_METADATA

- The output image
will use whatever progression parameters are found in the
metadata objects passed into the writer.

MODE_DEFAULT

- The image will be written
progressively, with parameters chosen by the writer.

The default is

MODE_COPY_FROM_METADATA

.

getProgressiveMode

```java
public int getProgressiveMode()
```

Returns the current mode for writing the stream in a
progressive manner.

**Returns:** the current mode for progressive encoding.
**Throws:** UnsupportedOperationException

- if the writer does not
support progressive encoding.
**See Also:** setProgressiveMode(int)

---

#### getProgressiveMode

public int getProgressiveMode()

Returns the current mode for writing the stream in a
progressive manner.

canWriteCompressed

```java
public boolean canWriteCompressed()
```

Returns

true

if this writer supports compression.

**Returns:** true

if the writer supports compression.

---

#### canWriteCompressed

public boolean canWriteCompressed()

Returns

true

if this writer supports compression.

setCompressionMode

```java
public void setCompressionMode​(int mode)
```

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined. The

mode

argument must be one of the four modes, interpreted as follows:

- MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

**Parameters:** mode

- The mode for setting compression in the output
stream.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression, or does not support the requested mode.
**Throws:** IllegalArgumentException

- if

mode

is not
one of the modes listed above.
**See Also:** getCompressionMode()

---

#### setCompressionMode

public void setCompressionMode​(int mode)

Specifies whether compression is to be performed, and if so how
compression parameters are to be determined. The

mode

argument must be one of the four modes, interpreted as follows:

- MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

MODE_DISABLED

- If the mode is set to

MODE_DISABLED

, methods that query or modify the
compression type or parameters will throw an

IllegalStateException

(if compression is
normally supported by the plug-in). Some writers, such as JPEG,
do not normally offer uncompressed output. In this case, attempting
to set the mode to

MODE_DISABLED

will throw an

UnsupportedOperationException

and the mode will not be
changed.

MODE_EXPLICIT

- Compress using the
compression type and quality settings specified in this

ImageWriteParam

. Any previously set compression
parameters are discarded.

MODE_COPY_FROM_METADATA

- Use whatever
compression parameters are specified in metadata objects
passed in to the writer.

MODE_DEFAULT

- Use default compression
parameters.

The default is

MODE_COPY_FROM_METADATA

.

getCompressionMode

```java
public int getCompressionMode()
```

Returns the current compression mode, if compression is
supported.

**Returns:** the current compression mode.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**See Also:** setCompressionMode(int)

---

#### getCompressionMode

public int getCompressionMode()

Returns the current compression mode, if compression is
supported.

getCompressionTypes

```java
public
String
[] getCompressionTypes()
```

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces. The array
returned is a copy.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

**Returns:** an array of

String

s containing the
(non-localized) names of available compression types, or

null

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.

---

#### getCompressionTypes

public

String

[] getCompressionTypes()

Returns a list of available compression types, as an array or

String

s, or

null

if a compression
type may not be chosen using these interfaces. The array
returned is a copy.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

If the writer only offers a single, mandatory form of
compression, it is not necessary to provide any named
compression types. Named compression types should only be
used where the user is able to make a meaningful choice
between different schemes.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

The default implementation checks if compression is
supported and throws an

UnsupportedOperationException

if not. Otherwise,
it returns a clone of the

compressionTypes

instance variable if it is non-

null

, or else
returns

null

.

setCompressionType

```java
public void setCompressionType​(
String
compressionType)
```

Sets the compression type to one of the values indicated by

getCompressionTypes

. If a value of

null

is passed in, any previous setting is
removed.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

**Parameters:** compressionType

- one of the

String

s returned
by

getCompressionTypes

, or

null

to
remove any previous setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** UnsupportedOperationException

- if there are no
settable compression types.
**Throws:** IllegalArgumentException

- if

compressionType

is non-

null

but is not
one of the values returned by

getCompressionTypes

.
**See Also:** getCompressionTypes()

,

getCompressionType()

,

unsetCompression()

---

#### setCompressionType

public void setCompressionType​(

String

compressionType)

Sets the compression type to one of the values indicated by

getCompressionTypes

. If a value of

null

is passed in, any previous setting is
removed.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it calls

getCompressionTypes

and checks if

compressionType

is one of the legal values. If it
is, the

compressionType

instance variable is set.
If

compressionType

is

null

, the
instance variable is set without performing any checking.

getCompressionType

```java
public
String
getCompressionType()
```

Returns the currently set compression type, or

null

if none has been set. The type is returned
as a

String

from among those returned by

getCompressionTypes

.
If no compression type has been set,

null

is
returned.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

**Returns:** the current compression type as a

String

,
or

null

if no type is set.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

---

#### getCompressionType

public

String

getCompressionType()

Returns the currently set compression type, or

null

if none has been set. The type is returned
as a

String

from among those returned by

getCompressionTypes

.
If no compression type has been set,

null

is
returned.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, it returns the value of the

compressionType

instance variable.

unsetCompression

```java
public void unsetCompression()
```

Removes any previous compression type and quality settings.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

**Throws:** UnsupportedOperationException

- if the plug-in does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**See Also:** setCompressionType(java.lang.String)

,

setCompressionQuality(float)

---

#### unsetCompression

public void unsetCompression()

Removes any previous compression type and quality settings.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

The default implementation sets the instance variable

compressionType

to

null

, and the
instance variable

compressionQuality

to

1.0F

.

getLocalizedCompressionTypeName

```java
public
String
getLocalizedCompressionTypeName()
```

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

**Returns:** a

String

containing a localized version of
the name of the current compression type.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if no compression type is set.

---

#### getLocalizedCompressionTypeName

public

String

getLocalizedCompressionTypeName()

Returns a localized version of the name of the current
compression type, using the

Locale

returned by

getLocale

.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

compressionType

is

non-null

the value
of

getCompressionType

is returned as a
convenience.

isCompressionLossless

```java
public boolean isCompressionLossless()
```

Returns

true

if the current compression type
provides lossless compression. If a plug-in provides only
one mandatory compression type, then this method may be
called without calling

setCompressionType

first.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

**Returns:** true

if the current compression type is
lossless.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.

---

#### isCompressionLossless

public boolean isCompressionLossless()

Returns

true

if the current compression type
provides lossless compression. If a plug-in provides only
one mandatory compression type, then this method may be
called without calling

setCompressionType

first.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

If there are multiple compression types but none has
been set, an

IllegalStateException

is thrown.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

The default implementation checks whether compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

true

is returned as a convenience.

setCompressionQuality

```java
public void setCompressionQuality​(float quality)
```

Sets the compression quality to a value between

0

and

1

. Only a single compression quality setting
is supported by default; writers can provide extended versions
of

ImageWriteParam

that offer more control. For
lossy compression schemes, the compression quality should
control the tradeoff between file size and image quality (for
example, by choosing quantization tables when writing JPEG
images). For lossless schemes, the compression quality may be
used to control the tradeoff between file size and time taken
to perform the compression (for example, by optimizing row
filters and setting the ZLIB compression level when writing
PNG images).

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

**Parameters:** quality

- a

float

between

0

and

1

indicating the desired quality level.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.
**See Also:** getCompressionQuality()

---

#### setCompressionQuality

public void setCompressionQuality​(float quality)

Sets the compression quality to a value between

0

and

1

. Only a single compression quality setting
is supported by default; writers can provide extended versions
of

ImageWriteParam

that offer more control. For
lossy compression schemes, the compression quality should
control the tradeoff between file size and image quality (for
example, by choosing quantization tables when writing JPEG
images). For lossless schemes, the compression quality may be
used to control the tradeoff between file size and time taken
to perform the compression (for example, by optimizing row
filters and setting the ZLIB compression level when writing
PNG images).

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

A compression quality setting of 0.0 is most generically
interpreted as "high compression is important," while a setting of
1.0 is most generically interpreted as "high image quality is
important."

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

The default implementation checks that compression is
supported, and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

returns

null

or

compressionType

is non-

null

it sets
the

compressionQuality

instance variable.

getCompressionQuality

```java
public float getCompressionQuality()
```

Returns the current compression quality setting.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

**Returns:** the current compression quality setting.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** setCompressionQuality(float)

---

#### getCompressionQuality

public float getCompressionQuality()

Returns the current compression quality setting.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

If there are multiple compression types but none has been
set, an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns the value of the

compressionQuality

instance variable.

getBitRate

```java
public float getBitRate​(float quality)
```

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level. The value will typically lie
between

0

and

1

, with smaller values
indicating more compression. A special value of

-1.0F

is used to indicate that no estimate is
available.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

**Parameters:** quality

- the quality setting whose bit rate is to be
queried.
**Returns:** an estimate of the compressed bit rate, or

-1.0F

if no estimate is available.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**Throws:** IllegalArgumentException

- if

quality

is
not between

0

and

1

, inclusive.

---

#### getBitRate

public float getBitRate​(float quality)

Returns a

float

indicating an estimate of the
number of bits of output data for each bit of input image data
at the given quality level. The value will typically lie
between

0

and

1

, with smaller values
indicating more compression. A special value of

-1.0F

is used to indicate that no estimate is
available.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

The default implementation checks that compression is
supported and the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, and

quality

is within bounds, it returns

-1.0

.

getCompressionQualityDescriptions

```java
public
String
[] getCompressionQualityDescriptions()
```

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level. The

String

with index

i

provides a description of the range of quality levels between

getCompressionQualityValues[i]

and

getCompressionQualityValues[i + 1]

. Note that the
length of the array returned from

getCompressionQualityValues

will always be one
greater than that returned from

getCompressionQualityDescriptions

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

String

s containing localized
descriptions of the compression quality levels.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityValues()

---

#### getCompressionQualityDescriptions

public

String

[] getCompressionQualityDescriptions()

Returns an array of

String

s that may be used along
with

getCompressionQualityValues

as part of a user
interface for setting or displaying the compression quality
level. The

String

with index

i

provides a description of the range of quality levels between

getCompressionQualityValues[i]

and

getCompressionQualityValues[i + 1]

. Note that the
length of the array returned from

getCompressionQualityValues

will always be one
greater than that returned from

getCompressionQualityDescriptions

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

As an example, the strings "Good", "Better", and "Best"
could be associated with the ranges

[0, .33)

,

[.33, .66)

, and

[.66, 1.0]

. In this
case,

getCompressionQualityDescriptions

would
return

{ "Good", "Better", "Best" }

and

getCompressionQualityValues

would return

{ 0.0F, .33F, .66F, 1.0F }

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityValues

, this method must also
return

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

The descriptions should be localized for the

Locale

returned by

getLocale

, if it
is non-

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

getCompressionQualityValues

```java
public float[] getCompressionQualityValues()
```

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level. See

getCompressionQualityDescriptions

for more information.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

**Returns:** an array of

float

s indicating the
boundaries between the compression quality levels as described
by the

String

s from

getCompressionQualityDescriptions

.
**Throws:** UnsupportedOperationException

- if the writer does not
support compression.
**Throws:** IllegalStateException

- if the compression mode is not

MODE_EXPLICIT

.
**Throws:** IllegalStateException

- if the set of legal
compression types is non-

null

and the current
compression type is

null

.
**See Also:** getCompressionQualityDescriptions()

---

#### getCompressionQualityValues

public float[] getCompressionQualityValues()

Returns an array of

float

s that may be used along
with

getCompressionQualityDescriptions

as part of a user
interface for setting or displaying the compression quality
level. See

getCompressionQualityDescriptions

for more information.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

If no descriptions are available,

null

is
returned. If

null

is returned from

getCompressionQualityDescriptions

, this method
must also return

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

If there are multiple compression types but none has been set,
an

IllegalStateException

is thrown.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

The default implementation checks that compression is
supported and that the compression mode is

MODE_EXPLICIT

. If so, if

getCompressionTypes()

is

null

or

getCompressionType()

is non-

null

, it
returns

null

.

---

