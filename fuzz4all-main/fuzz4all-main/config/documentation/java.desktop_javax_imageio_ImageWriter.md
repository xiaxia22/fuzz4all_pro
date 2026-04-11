# Class ImageWriter

**Source:** `java.desktop\javax\imageio\ImageWriter.html`

### Class Description

```java
public abstract class
ImageWriter

extends
Object

implements
ImageTranscoder
```

An abstract superclass for encoding and writing images. This class
must be subclassed by classes that write out images in the context
of the Java Image I/O framework.

ImageWriter

objects are normally instantiated by
the service provider class for the specific format. Service
provider classes are registered with the

IIORegistry

,
which uses them for format recognition and presentation of
available format readers and writers.

**All Implemented Interfaces:** ImageTranscoder

---

### Field Details

#### protected
ImageWriterSpi
originatingProvider

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists. By default it is initialized to

null

.

---

#### protected
Object
output

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

. By default it is initialized to

null

.

---

#### protected
Locale
[] availableLocales

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported. By default
it is initialized to

null

.

---

#### protected
Locale
locale

The current

Locale

to be used for localization, or

null

if none has been set. By default it is
initialized to

null

.

---

#### protected
List
<
IIOWriteWarningListener
> warningListeners

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

---

#### protected
List
<
Locale
> warningLocales

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

---

#### protected
List
<
IIOWriteProgressListener
> progressListeners

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

---

### Constructor Details

#### protected ImageWriter​(
ImageWriterSpi
originatingProvider)

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

**Parameters:**
- originatingProvider

- the

ImageWriterSpi

that
is constructing this object, or

null

.

---

### Method Details

#### public
ImageWriterSpi
getOriginatingProvider()

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

The default implementation returns the value of the

originatingProvider

instance variable.

**Returns:**
- an

ImageWriterSpi

, or

null

.

**See Also:**
- ImageWriterSpi

---

#### public void setOutput​(
Object
output)

Sets the destination to the given

ImageOutputStream

or other

Object

.
The destination is assumed to be ready to accept data, and will
not be closed at the end of each write. This allows distributed
imaging applications to transmit a series of images over a
single network connection. If

output

is

null

, any currently set output will be removed.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

**Parameters:**
- output

- the

ImageOutputStream

or other

Object

to use for future writing.

**Throws:**
- IllegalArgumentException

- if

output

is
not an instance of one of the classes returned by the
originating service provider's

getOutputTypes

method.

**See Also:**
- getOutput()

---

#### public
Object
getOutput()

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method. If no destination has been
set,

null

is returned.

The default implementation returns the value of the

output

instance variable.

**Returns:**
- the

Object

that was specified using

setOutput

, or

null

.

**See Also:**
- setOutput(java.lang.Object)

---

#### public
Locale
[] getAvailableLocales()

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings. A return
value of

null

indicates that localization is not
supported.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

**Returns:**
- an array of

Locale

s that may be used as
arguments to

setLocale

, or

null

.

---

#### public void setLocale​(
Locale
locale)

Sets the current

Locale

of this

ImageWriter

to the given value. A value of

null

removes any previous setting, and indicates
that the writer should localize as it sees fit.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

**Parameters:**
- locale

- the desired

Locale

, or

null

.

**Throws:**
- IllegalArgumentException

- if

locale

is
non-

null

but is not one of the values returned by

getAvailableLocales

.

**See Also:**
- getLocale()

---

#### public
Locale
getLocale()

Returns the currently set

Locale

, or

null

if none has been set.

The default implementation returns the value of the

locale

instance variable.

**Returns:**
- the current

Locale

, or

null

.

**See Also:**
- setLocale(java.util.Locale)

---

#### public
ImageWriteParam
getDefaultWriteParam()

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified. This
is useful as a starting point for tweaking just a few parameters
and otherwise leaving the default settings alone.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

**Returns:**
- a new

ImageWriteParam

object containing
default values.

---

#### public abstract
IIOMetadata
getDefaultStreamMetadata​(
ImageWriteParam
param)

Returns an

IIOMetadata

object containing default
values for encoding a stream of images. The contents of the
object may be manipulated using either the XML tree structure
returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via plug-in
specific interfaces, and the resulting data supplied to one of
the

write

methods that take a stream metadata
parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

**Parameters:**
- param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.

**Returns:**
- an

IIOMetadata

object.

---

#### public abstract
IIOMetadata
getDefaultImageMetadata​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param)

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type. The contents
of the object may be manipulated using either the XML tree
structure returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via
plug-in specific interfaces, and the resulting data supplied to
one of the

write

methods that take a stream
metadata parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:**
- imageType

- an

ImageTypeSpecifier

indicating the
format of the image to be written later.
- param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.

**Returns:**
- an

IIOMetadata

object.

---

#### public int getNumThumbnailsSupported​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding. A return value of

-1

indicates that
insufficient information is available.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

**Parameters:**
- imageType

- an

ImageTypeSpecifier

indicating
the type of image to be written, or

null

.
- param

- the

ImageWriteParam

that will be used for
writing, or

null

.
- streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
- imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.

**Returns:**
- the number of thumbnails that may be written given the
supplied parameters, or

-1

if insufficient
information is available.

---

#### public
Dimension
[] getPreferredThumbnailSizes​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream. This information is merely
advisory; the writer will resize any supplied thumbnails as
necessary.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

**Parameters:**
- imageType

- an

ImageTypeSpecifier

indicating the
type of image to be written, or

null

.
- param

- the

ImageWriteParam

that will be used for
writing, or

null

.
- streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
- imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.

**Returns:**
- an array of

Dimension

s with an even length
of at least two, or

null

.

---

#### public boolean canWriteRasters()

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image. If this method returns

false

, then
those methods will throw an

UnsupportedOperationException

if supplied with an

IIOImage

containing a

Raster

.

The default implementation returns

false

.

**Returns:**
- true

if

Raster

sources are
supported.

---

#### public abstract void write​(
IIOMetadata
streamMetadata,

IIOImage
image,

ImageWriteParam
param)
throws
IOException

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output. Any necessary header information is included. If the
output is an

ImageOutputStream

, its existing
contents prior to the current seek position are not affected,
and need not be readable or writable.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:**
- streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
- image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
- IllegalArgumentException

- if

image

is

null

.
- IOException

- if an error occurs during writing.

---

#### public void write​(
IIOImage
image)
throws
IOException

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output. This method is
a shorthand for

write(null, image, null)

.

**Parameters:**
- image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IllegalArgumentException

- if

image

is

null

.
- UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
- IOException

- if an error occurs during writing.

---

#### public void write​(
RenderedImage
image)
throws
IOException

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output. This
method is a shorthand for

write(null, new IIOImage(image, null, null), null)

.

**Parameters:**
- image

- a

RenderedImage

to be written.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IllegalArgumentException

- if

image

is

null

.
- IOException

- if an error occurs during writing.

---

#### public boolean canWriteSequence()

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

**Returns:**
- true

if images may be appended sequentially.

---

#### public void prepareWriteSequence​(
IIOMetadata
streamMetadata)
throws
IOException

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object. The metadata will be written to the stream if
it should precede the image data. If the argument is

null

,
default stream metadata is used.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- streamMetadata

- A stream metadata object, or

null

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canWriteSequence

returns

false

.
- IOException

- if an error occurs writing the stream
metadata.

---

#### public void writeToSequence​(
IIOImage
image,

ImageWriteParam
param)
throws
IOException

Appends a single image and possibly associated metadata and
thumbnails, to the output. If the output is an

ImageOutputStream

, the existing contents of the
output prior to the current seek position may be flushed, and
need not be readable or writable, unless the plug-in needs to
be able to patch up the header information when

endWriteSequence

is called (

e.g.

TIFF).

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
- UnsupportedOperationException

- if

canWriteSequence

returns

false

.
- IllegalArgumentException

- if

image

is

null

.
- UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
- IOException

- if an error occurs during writing.

---

#### public void endWriteSequence()
throws
IOException

Completes the writing of a sequence of images begun with

prepareWriteSequence

. Any stream metadata that
should come at the end of the sequence of images is written out,
and any header information at the beginning of the sequence is
patched up if necessary. If the output is an

ImageOutputStream

, data through the stream metadata
at the end of the sequence are flushed and need not be readable
or writable.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:**
- IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
- UnsupportedOperationException

- if

canWriteSequence

returns

false

.
- IOException

- if an error occurs during writing.

---

#### public boolean canReplaceStreamMetadata()
throws
IOException

Returns

true

if it is possible to replace the
stream metadata already present in the output.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:**
- true

if replacement of stream metadata is
allowed.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IOException

- if an I/O error occurs during the query.

---

#### public void replaceStreamMetadata​(
IIOMetadata
streamMetadata)
throws
IOException

Replaces the stream metadata in the output with new
information. If the output is an

ImageOutputStream

, the prior contents of the
stream are examined and possibly edited to make room for the
new data. All of the prior contents of the output must be
available for reading and writing.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if the

canReplaceStreamMetadata

returns

false

. modes do not include
- IOException

- if an error occurs during writing.

---

#### public boolean canReplaceImageMetadata​(int imageIndex)
throws
IOException

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

. If this method returns

false

, a call to

replaceImageMetadata(imageIndex)

will throw an

UnsupportedOperationException

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:**
- imageIndex

- the index of the image whose metadata is to
be replaced.

**Returns:**
- true

if the image metadata of the given
image can be replaced.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IndexOutOfBoundsException

- if the writer supports
image metadata replacement in general, but

imageIndex

is less than 0 or greater than the
largest available index.
- IOException

- if an I/O error occurs during the query.

---

#### public void replaceImageMetadata​(int imageIndex,

IIOMetadata
imageMetadata)
throws
IOException

Replaces the image metadata associated with an existing image.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- imageIndex

- the index of the image whose metadata is to
be replaced.
- imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.

**Throws:**
- IllegalStateException

- if the output has not been
set.
- UnsupportedOperationException

- if

canReplaceImageMetadata

returns

false

.
- IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
- IOException

- if an error occurs during writing.

---

#### public boolean canInsertImage​(int imageIndex)
throws
IOException

Returns

true

if the writer supports the insertion
of a new image at the given index. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:**
- imageIndex

- the index at which the image is to be
inserted.

**Returns:**
- true

if an image may be inserted at the
given index.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IndexOutOfBoundsException

- if the writer supports
image insertion in general, but

imageIndex

is less
than -1 or greater than the largest available index.
- IOException

- if an I/O error occurs during the query.

---

#### public void writeInsert​(int imageIndex,

IIOImage
image,

ImageWriteParam
param)
throws
IOException

Inserts a new image into an existing image stream. Existing
images with an index greater than

imageIndex

are
preserved, and their indices are each increased by 1. A value
for

imageIndex

of -1 may be used to signify an
index one larger than the previous largest index; that is, it
will cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- imageIndex

- the index at which to write the image.
- image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canInsertImage(imageIndex)

returns

false

.
- IllegalArgumentException

- if

image

is

null

.
- IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
- UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
- IOException

- if an error occurs during writing.

---

#### public boolean canRemoveImage​(int imageIndex)
throws
IOException

Returns

true

if the writer supports the removal
of an existing image at the given index. Existing images with
indices greater than the insertion index will have
their indices decreased by 1.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:**
- imageIndex

- the index of the image to be removed.

**Returns:**
- true

if it is possible to remove the given
image.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- IndexOutOfBoundsException

- if the writer supports
image removal in general, but

imageIndex

is less
than 0 or greater than the largest available index.
- IOException

- if an I/O error occurs during the
query.

---

#### public void removeImage​(int imageIndex)
throws
IOException

Removes an image from the stream.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- imageIndex

- the index of the image to be removed.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canRemoveImage(imageIndex)

returns

false

.
- IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
- IOException

- if an I/O error occurs during the
removal.

---

#### public boolean canWriteEmpty()
throws
IOException

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output. The pixel values may be defined by future
calls to the

replacePixels

methods. If the output
is an

ImageOutputStream

, its existing contents
prior to the current seek position are not affected, and need
not be readable or writable.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:**
- true

if the writing of complete image
stream with contents to be defined later is supported.

**Throws:**
- IllegalStateException

- if the output has not been
set.
- IOException

- if an I/O error occurs during the
query.

---

#### public void prepareWriteEmpty​(
IIOMetadata
streamMetadata,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output. The pixel values will
be defined by future calls to the

replacePixels

methods. If the output is an

ImageOutputStream

,
its existing contents prior to the current seek position are
not affected, and need not be readable or writable.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
- imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
- width

- the width of the image.
- height

- the height of the image.
- imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
- thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canWriteEmpty

returns

false

.
- IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
- IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
- IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
- IllegalArgumentException

- if width or height are less
than 1.
- IOException

- if an I/O error occurs during writing.

---

#### public void endWriteEmpty()
throws
IOException

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canWriteEmpty(imageIndex)

returns

false

.
- IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has not been made.
- IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has been made.
- IllegalStateException

- if a call to

prepareReiplacePixels

has been made without a
matching call to

endReplacePixels

.
- IOException

- if an I/O error occurs during writing.

---

#### public boolean canInsertEmpty​(int imageIndex)
throws
IOException

Returns

true

if the writer supports the insertion
of a new, empty image at the given index. The pixel values of
the image are undefined, and may be specified in pieces using
the

replacePixels

methods. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:**
- imageIndex

- the index at which the image is to be
inserted.

**Returns:**
- true

if an empty image may be inserted at
the given index.

**Throws:**
- IllegalStateException

- if the output has not been
set.
- IndexOutOfBoundsException

- if the writer supports
empty image insertion in general, but

imageIndex

is less than -1 or greater than the largest available index.
- IOException

- if an I/O error occurs during the
query.

---

#### public void prepareInsertEmpty​(int imageIndex,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException

Begins the insertion of a new image with undefined pixel values
into an existing image stream. Existing images with an index
greater than

imageIndex

are preserved, and their
indices are each increased by 1. A value for

imageIndex

of -1 may be used to signify an index
one larger than the previous largest index; that is, it will
cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- imageIndex

- the index at which to write the image.
- imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
- width

- the width of the image.
- height

- the height of the image.
- imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
- thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
- IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
- IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
- IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
- IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
- IllegalArgumentException

- if width or height are less
than 1.
- IOException

- if an I/O error occurs during writing.

---

#### public void endInsertEmpty()
throws
IOException

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
- IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has not been made.
- IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has been made.
- IllegalStateException

- if a call to

prepareReplacePixels

has been made without a
matching call to

endReplacePixels

.
- IOException

- if an I/O error occurs during writing.

---

#### public boolean canReplacePixels​(int imageIndex)
throws
IOException

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:**
- imageIndex

- the index of the image whose pixels are to be
replaced.

**Returns:**
- true

if the pixels of the given
image can be replaced.

**Throws:**
- IllegalStateException

- if the output has not been
set.
- IndexOutOfBoundsException

- if the writer supports
pixel replacement in general, but

imageIndex

is
less than 0 or greater than the largest available index.
- IOException

- if an I/O error occurs during the query.

---

#### public void prepareReplacePixels​(int imageIndex,

Rectangle
region)
throws
IOException

Prepares the writer to handle a series of calls to the

replacePixels

methods. The affected pixel area
will be clipped against the supplied

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- imageIndex

- the index of the image whose pixels are to be
replaced.
- region

- a

Rectangle

that will be used to clip
future pixel regions.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
- IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
- IllegalStateException

- if there is a previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

(

i.e.

, nesting is not
allowed).
- IllegalArgumentException

- if

region

is

null

or has a width or height less than 1.
- IOException

- if an I/O error occurs during the
preparation.

---

#### public void replacePixels​(
RenderedImage
image,

ImageWriteParam
param)
throws
IOException

Replaces a portion of an image already present in the output
with a portion of the given image. The image data must match,
or be convertible to, the image layout of the existing image.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- image

- a

RenderedImage

containing source
pixels.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
- IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
- IllegalArgumentException

- if any of the following are true:

- image

is

null

.

the intersected region does not contain at least one pixel.

the layout of

image

does not match, or this
writer cannot convert it to, the existing image layout.
- IOException

- if an I/O error occurs during writing.

---

#### public void replacePixels​(
Raster
raster,

ImageWriteParam
param)
throws
IOException

Replaces a portion of an image already present in the output
with a portion of the given

Raster

. The image
data must match, or be convertible to, the image layout of the
existing image.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:**
- raster

- a

Raster

containing source
pixels.
- param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
- IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
- UnsupportedOperationException

- if

canWriteRasters

returns

false

.
- IllegalArgumentException

- if any of the following are true:

- raster

is

null

.

the intersected region does not contain at least one pixel.

the layout of

raster

does not match, or this
writer cannot convert it to, the existing image layout.
- IOException

- if an I/O error occurs during writing.

---

#### public void endReplacePixels()
throws
IOException

Terminates a sequence of calls to

replacePixels

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:**
- IllegalStateException

- if the output has not
been set.
- UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
- IllegalStateException

- if there is no previous call
to

prepareReplacePixels

without a matching call to

endReplacePixels

.
- IOException

- if an I/O error occurs during writing.

---

#### public void abort()

Requests that any current write operation be aborted. The
contents of the output following the abort will be undefined.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

---

#### protected boolean abortRequested()

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

**Returns:**
- true

if the current write operation should
be aborted.

**See Also:**
- abort()

,

clearAbortRequest()

---

#### protected void clearAbortRequest()

Clears any previous abort request. After this method has been
called,

abortRequested

will return

false

.

**See Also:**
- abort()

,

abortRequested()

---

#### public void addIIOWriteWarningListener​(
IIOWriteWarningListener
listener)

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken. Messages sent to the given listener will be
localized, if possible, to match the current

Locale

. If no

Locale

has been set,
warning messages may be localized as the writer sees fit.

**Parameters:**
- listener

- an

IIOWriteWarningListener

to be
registered.

**See Also:**
- removeIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

---

#### public void removeIIOWriteWarningListener​(
IIOWriteWarningListener
listener)

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:**
- listener

- an

IIOWriteWarningListener

to be
deregistered.

**See Also:**
- addIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

---

#### public void removeAllIIOWriteWarningListeners()

Removes all currently registered

IIOWriteWarningListener

objects.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

---

#### public void addIIOWriteProgressListener​(
IIOWriteProgressListener
listener)

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:**
- listener

- an

IIOWriteProgressListener

to be
registered.

**See Also:**
- removeIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

---

#### public void removeIIOWriteProgressListener​(
IIOWriteProgressListener
listener)

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:**
- listener

- an

IIOWriteProgressListener

to be
deregistered.

**See Also:**
- addIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

---

#### public void removeAllIIOWriteProgressListeners()

Removes all currently registered

IIOWriteProgressListener

objects.

The default implementation sets the

progressListeners

instance variable to

null

.

---

#### protected void processImageStarted​(int imageIndex)

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method. Subclasses may use this
method as a convenience.

**Parameters:**
- imageIndex

- the index of the image about to be written.

---

#### protected void processImageProgress​(float percentageDone)

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method. Subclasses may use
this method as a convenience.

**Parameters:**
- percentageDone

- the current percentage of completion,
as a

float

.

---

#### protected void processImageComplete()

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method. Subclasses may use this
method as a convenience.

---

#### protected void processThumbnailStarted​(int imageIndex,
int thumbnailIndex)

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method. Subclasses may use this
method as a convenience.

**Parameters:**
- imageIndex

- the index of the image associated with the
thumbnail.
- thumbnailIndex

- the index of the thumbnail.

---

#### protected void processThumbnailProgress​(float percentageDone)

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method. Subclasses may
use this method as a convenience.

**Parameters:**
- percentageDone

- the current percentage of completion,
as a

float

.

---

#### protected void processThumbnailComplete()

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method. Subclasses may use this
method as a convenience.

---

#### protected void processWriteAborted()

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method. Subclasses may use this
method as a convenience.

---

#### protected void processWarningOccurred​(int imageIndex,

String
warning)

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method. Subclasses may use this
method as a convenience.

**Parameters:**
- imageIndex

- the index of the image on which the warning
occurred.
- warning

- the warning message.

**Throws:**
- IllegalArgumentException

- if

warning

is

null

.

---

#### protected void processWarningOccurred​(int imageIndex,

String
baseName,

String
keyword)

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

. Subclasses may use this
method as a convenience.

**Parameters:**
- imageIndex

- the index of the image on which the warning
occurred.
- baseName

- the base name of a set of

ResourceBundle

s containing localized warning
messages.
- keyword

- the keyword used to index the warning message
within the set of

ResourceBundle

s.

**Throws:**
- IllegalArgumentException

- if

baseName

is

null

.
- IllegalArgumentException

- if

keyword

is

null

.
- IllegalArgumentException

- if no appropriate

ResourceBundle

may be located.
- IllegalArgumentException

- if the named resource is
not found in the located

ResourceBundle

.
- IllegalArgumentException

- if the object retrieved
from the

ResourceBundle

is not a

String

.

---

#### public void reset()

Restores the

ImageWriter

to its initial state.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

---

#### public void dispose()

Allows any resources held by this object to be released. The
result of calling any other method (other than

finalize

) subsequent to a call to this method
is undefined.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

---

### Additional Sections

#### Class ImageWriter

java.lang.Object

- javax.imageio.ImageWriter

javax.imageio.ImageWriter

**All Implemented Interfaces:** ImageTranscoder

```java
public abstract class
ImageWriter

extends
Object

implements
ImageTranscoder
```

An abstract superclass for encoding and writing images. This class
must be subclassed by classes that write out images in the context
of the Java Image I/O framework.

ImageWriter

objects are normally instantiated by
the service provider class for the specific format. Service
provider classes are registered with the

IIORegistry

,
which uses them for format recognition and presentation of
available format readers and writers.

**See Also:** ImageReader

,

ImageWriteParam

,

IIORegistry

,

ImageWriterSpi

public abstract class

ImageWriter

extends

Object

implements

ImageTranscoder

An abstract superclass for encoding and writing images. This class
must be subclassed by classes that write out images in the context
of the Java Image I/O framework.

ImageWriter

objects are normally instantiated by
the service provider class for the specific format. Service
provider classes are registered with the

IIORegistry

,
which uses them for format recognition and presentation of
available format readers and writers.

ImageWriter

objects are normally instantiated by
the service provider class for the specific format. Service
provider classes are registered with the

IIORegistry

,
which uses them for format recognition and presentation of
available format readers and writers.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Locale

[]

availableLocales

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported.

protected

Locale

locale

The current

Locale

to be used for localization, or

null

if none has been set.

protected

ImageWriterSpi

originatingProvider

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists.

protected

Object

output

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

.

protected

List

<

IIOWriteProgressListener

>

progressListeners

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

protected

List

<

IIOWriteWarningListener

>

warningListeners

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

protected

List

<

Locale

>

warningLocales

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ImageWriter

​(

ImageWriterSpi

originatingProvider)

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

abort

()

Requests that any current write operation be aborted.

protected boolean

abortRequested

()

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

void

addIIOWriteProgressListener

​(

IIOWriteProgressListener

listener)

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners.

void

addIIOWriteWarningListener

​(

IIOWriteWarningListener

listener)

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners.

boolean

canInsertEmpty

​(int imageIndex)

Returns

true

if the writer supports the insertion
of a new, empty image at the given index.

boolean

canInsertImage

​(int imageIndex)

Returns

true

if the writer supports the insertion
of a new image at the given index.

boolean

canRemoveImage

​(int imageIndex)

Returns

true

if the writer supports the removal
of an existing image at the given index.

boolean

canReplaceImageMetadata

​(int imageIndex)

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

.

boolean

canReplacePixels

​(int imageIndex)

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

boolean

canReplaceStreamMetadata

()

Returns

true

if it is possible to replace the
stream metadata already present in the output.

boolean

canWriteEmpty

()

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output.

boolean

canWriteRasters

()

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image.

boolean

canWriteSequence

()

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

protected void

clearAbortRequest

()

Clears any previous abort request.

void

dispose

()

Allows any resources held by this object to be released.

void

endInsertEmpty

()

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

void

endReplacePixels

()

Terminates a sequence of calls to

replacePixels

.

void

endWriteEmpty

()

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

void

endWriteSequence

()

Completes the writing of a sequence of images begun with

prepareWriteSequence

.

Locale

[]

getAvailableLocales

()

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings.

abstract

IIOMetadata

getDefaultImageMetadata

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type.

abstract

IIOMetadata

getDefaultStreamMetadata

​(

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding a stream of images.

ImageWriteParam

getDefaultWriteParam

()

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified.

Locale

getLocale

()

Returns the currently set

Locale

, or

null

if none has been set.

int

getNumThumbnailsSupported

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding.

ImageWriterSpi

getOriginatingProvider

()

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

Object

getOutput

()

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method.

Dimension

[]

getPreferredThumbnailSizes

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream.

void

prepareInsertEmpty

​(int imageIndex,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)

Begins the insertion of a new image with undefined pixel values
into an existing image stream.

void

prepareReplacePixels

​(int imageIndex,

Rectangle

region)

Prepares the writer to handle a series of calls to the

replacePixels

methods.

void

prepareWriteEmpty

​(

IIOMetadata

streamMetadata,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output.

void

prepareWriteSequence

​(

IIOMetadata

streamMetadata)

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object.

protected void

processImageComplete

()

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method.

protected void

processImageProgress

​(float percentageDone)

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method.

protected void

processImageStarted

​(int imageIndex)

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method.

protected void

processThumbnailComplete

()

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method.

protected void

processThumbnailProgress

​(float percentageDone)

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method.

protected void

processThumbnailStarted

​(int imageIndex,
int thumbnailIndex)

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method.

protected void

processWarningOccurred

​(int imageIndex,

String

warning)

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method.

protected void

processWarningOccurred

​(int imageIndex,

String

baseName,

String

keyword)

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

.

protected void

processWriteAborted

()

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method.

void

removeAllIIOWriteProgressListeners

()

Removes all currently registered

IIOWriteProgressListener

objects.

void

removeAllIIOWriteWarningListeners

()

Removes all currently registered

IIOWriteWarningListener

objects.

void

removeIIOWriteProgressListener

​(

IIOWriteProgressListener

listener)

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners.

void

removeIIOWriteWarningListener

​(

IIOWriteWarningListener

listener)

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners.

void

removeImage

​(int imageIndex)

Removes an image from the stream.

void

replaceImageMetadata

​(int imageIndex,

IIOMetadata

imageMetadata)

Replaces the image metadata associated with an existing image.

void

replacePixels

​(

Raster

raster,

ImageWriteParam

param)

Replaces a portion of an image already present in the output
with a portion of the given

Raster

.

void

replacePixels

​(

RenderedImage

image,

ImageWriteParam

param)

Replaces a portion of an image already present in the output
with a portion of the given image.

void

replaceStreamMetadata

​(

IIOMetadata

streamMetadata)

Replaces the stream metadata in the output with new
information.

void

reset

()

Restores the

ImageWriter

to its initial state.

void

setLocale

​(

Locale

locale)

Sets the current

Locale

of this

ImageWriter

to the given value.

void

setOutput

​(

Object

output)

Sets the destination to the given

ImageOutputStream

or other

Object

.

void

write

​(

RenderedImage

image)

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output.

void

write

​(

IIOImage

image)

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output.

abstract void

write

​(

IIOMetadata

streamMetadata,

IIOImage

image,

ImageWriteParam

param)

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output.

void

writeInsert

​(int imageIndex,

IIOImage

image,

ImageWriteParam

param)

Inserts a new image into an existing image stream.

void

writeToSequence

​(

IIOImage

image,

ImageWriteParam

param)

Appends a single image and possibly associated metadata and
thumbnails, to the output.

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

- Methods declared in interface javax.imageio.

ImageTranscoder

convertImageMetadata

,

convertStreamMetadata

Field Summary

Fields

Modifier and Type

Field

Description

protected

Locale

[]

availableLocales

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported.

protected

Locale

locale

The current

Locale

to be used for localization, or

null

if none has been set.

protected

ImageWriterSpi

originatingProvider

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists.

protected

Object

output

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

.

protected

List

<

IIOWriteProgressListener

>

progressListeners

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

protected

List

<

IIOWriteWarningListener

>

warningListeners

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

protected

List

<

Locale

>

warningLocales

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

---

#### Field Summary

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported.

The current

Locale

to be used for localization, or

null

if none has been set.

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists.

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

.

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ImageWriter

​(

ImageWriterSpi

originatingProvider)

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

---

#### Constructor Summary

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

abort

()

Requests that any current write operation be aborted.

protected boolean

abortRequested

()

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

void

addIIOWriteProgressListener

​(

IIOWriteProgressListener

listener)

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners.

void

addIIOWriteWarningListener

​(

IIOWriteWarningListener

listener)

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners.

boolean

canInsertEmpty

​(int imageIndex)

Returns

true

if the writer supports the insertion
of a new, empty image at the given index.

boolean

canInsertImage

​(int imageIndex)

Returns

true

if the writer supports the insertion
of a new image at the given index.

boolean

canRemoveImage

​(int imageIndex)

Returns

true

if the writer supports the removal
of an existing image at the given index.

boolean

canReplaceImageMetadata

​(int imageIndex)

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

.

boolean

canReplacePixels

​(int imageIndex)

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

boolean

canReplaceStreamMetadata

()

Returns

true

if it is possible to replace the
stream metadata already present in the output.

boolean

canWriteEmpty

()

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output.

boolean

canWriteRasters

()

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image.

boolean

canWriteSequence

()

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

protected void

clearAbortRequest

()

Clears any previous abort request.

void

dispose

()

Allows any resources held by this object to be released.

void

endInsertEmpty

()

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

void

endReplacePixels

()

Terminates a sequence of calls to

replacePixels

.

void

endWriteEmpty

()

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

void

endWriteSequence

()

Completes the writing of a sequence of images begun with

prepareWriteSequence

.

Locale

[]

getAvailableLocales

()

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings.

abstract

IIOMetadata

getDefaultImageMetadata

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type.

abstract

IIOMetadata

getDefaultStreamMetadata

​(

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding a stream of images.

ImageWriteParam

getDefaultWriteParam

()

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified.

Locale

getLocale

()

Returns the currently set

Locale

, or

null

if none has been set.

int

getNumThumbnailsSupported

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding.

ImageWriterSpi

getOriginatingProvider

()

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

Object

getOutput

()

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method.

Dimension

[]

getPreferredThumbnailSizes

​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream.

void

prepareInsertEmpty

​(int imageIndex,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)

Begins the insertion of a new image with undefined pixel values
into an existing image stream.

void

prepareReplacePixels

​(int imageIndex,

Rectangle

region)

Prepares the writer to handle a series of calls to the

replacePixels

methods.

void

prepareWriteEmpty

​(

IIOMetadata

streamMetadata,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output.

void

prepareWriteSequence

​(

IIOMetadata

streamMetadata)

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object.

protected void

processImageComplete

()

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method.

protected void

processImageProgress

​(float percentageDone)

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method.

protected void

processImageStarted

​(int imageIndex)

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method.

protected void

processThumbnailComplete

()

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method.

protected void

processThumbnailProgress

​(float percentageDone)

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method.

protected void

processThumbnailStarted

​(int imageIndex,
int thumbnailIndex)

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method.

protected void

processWarningOccurred

​(int imageIndex,

String

warning)

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method.

protected void

processWarningOccurred

​(int imageIndex,

String

baseName,

String

keyword)

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

.

protected void

processWriteAborted

()

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method.

void

removeAllIIOWriteProgressListeners

()

Removes all currently registered

IIOWriteProgressListener

objects.

void

removeAllIIOWriteWarningListeners

()

Removes all currently registered

IIOWriteWarningListener

objects.

void

removeIIOWriteProgressListener

​(

IIOWriteProgressListener

listener)

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners.

void

removeIIOWriteWarningListener

​(

IIOWriteWarningListener

listener)

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners.

void

removeImage

​(int imageIndex)

Removes an image from the stream.

void

replaceImageMetadata

​(int imageIndex,

IIOMetadata

imageMetadata)

Replaces the image metadata associated with an existing image.

void

replacePixels

​(

Raster

raster,

ImageWriteParam

param)

Replaces a portion of an image already present in the output
with a portion of the given

Raster

.

void

replacePixels

​(

RenderedImage

image,

ImageWriteParam

param)

Replaces a portion of an image already present in the output
with a portion of the given image.

void

replaceStreamMetadata

​(

IIOMetadata

streamMetadata)

Replaces the stream metadata in the output with new
information.

void

reset

()

Restores the

ImageWriter

to its initial state.

void

setLocale

​(

Locale

locale)

Sets the current

Locale

of this

ImageWriter

to the given value.

void

setOutput

​(

Object

output)

Sets the destination to the given

ImageOutputStream

or other

Object

.

void

write

​(

RenderedImage

image)

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output.

void

write

​(

IIOImage

image)

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output.

abstract void

write

​(

IIOMetadata

streamMetadata,

IIOImage

image,

ImageWriteParam

param)

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output.

void

writeInsert

​(int imageIndex,

IIOImage

image,

ImageWriteParam

param)

Inserts a new image into an existing image stream.

void

writeToSequence

​(

IIOImage

image,

ImageWriteParam

param)

Appends a single image and possibly associated metadata and
thumbnails, to the output.

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

- Methods declared in interface javax.imageio.

ImageTranscoder

convertImageMetadata

,

convertStreamMetadata

---

#### Method Summary

Requests that any current write operation be aborted.

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners.

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners.

Returns

true

if the writer supports the insertion
of a new, empty image at the given index.

Returns

true

if the writer supports the insertion
of a new image at the given index.

Returns

true

if the writer supports the removal
of an existing image at the given index.

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

.

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

Returns

true

if it is possible to replace the
stream metadata already present in the output.

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output.

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image.

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

Clears any previous abort request.

Allows any resources held by this object to be released.

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

Terminates a sequence of calls to

replacePixels

.

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

Completes the writing of a sequence of images begun with

prepareWriteSequence

.

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings.

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type.

Returns an

IIOMetadata

object containing default
values for encoding a stream of images.

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified.

Returns the currently set

Locale

, or

null

if none has been set.

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding.

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method.

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream.

Begins the insertion of a new image with undefined pixel values
into an existing image stream.

Prepares the writer to handle a series of calls to the

replacePixels

methods.

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output.

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object.

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method.

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method.

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method.

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method.

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method.

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method.

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method.

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

.

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method.

Removes all currently registered

IIOWriteProgressListener

objects.

Removes all currently registered

IIOWriteWarningListener

objects.

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners.

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners.

Removes an image from the stream.

Replaces the image metadata associated with an existing image.

Replaces a portion of an image already present in the output
with a portion of the given

Raster

.

Replaces a portion of an image already present in the output
with a portion of the given image.

Replaces the stream metadata in the output with new
information.

Restores the

ImageWriter

to its initial state.

Sets the current

Locale

of this

ImageWriter

to the given value.

Sets the destination to the given

ImageOutputStream

or other

Object

.

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output.

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output.

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output.

Inserts a new image into an existing image stream.

Appends a single image and possibly associated metadata and
thumbnails, to the output.

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

Methods declared in interface javax.imageio.

ImageTranscoder

convertImageMetadata

,

convertStreamMetadata

---

#### Methods declared in interface javax.imageio. ImageTranscoder

============ FIELD DETAIL ===========

- Field Detail

- originatingProvider

```java
protected
ImageWriterSpi
originatingProvider
```

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists. By default it is initialized to

null

.

- output

```java
protected
Object
output
```

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

. By default it is initialized to

null

.

- availableLocales

```java
protected
Locale
[] availableLocales
```

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported. By default
it is initialized to

null

.

- locale

```java
protected
Locale
locale
```

The current

Locale

to be used for localization, or

null

if none has been set. By default it is
initialized to

null

.

- warningListeners

```java
protected
List
<
IIOWriteWarningListener
> warningListeners
```

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

- warningLocales

```java
protected
List
<
Locale
> warningLocales
```

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

- progressListeners

```java
protected
List
<
IIOWriteProgressListener
> progressListeners
```

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageWriter

```java
protected ImageWriter​(
ImageWriterSpi
originatingProvider)
```

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

**Parameters:** originatingProvider

- the

ImageWriterSpi

that
is constructing this object, or

null

.

============ METHOD DETAIL ==========

- Method Detail

- getOriginatingProvider

```java
public
ImageWriterSpi
getOriginatingProvider()
```

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

The default implementation returns the value of the

originatingProvider

instance variable.

**Returns:** an

ImageWriterSpi

, or

null

.
**See Also:** ImageWriterSpi

- setOutput

```java
public void setOutput​(
Object
output)
```

Sets the destination to the given

ImageOutputStream

or other

Object

.
The destination is assumed to be ready to accept data, and will
not be closed at the end of each write. This allows distributed
imaging applications to transmit a series of images over a
single network connection. If

output

is

null

, any currently set output will be removed.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

**Parameters:** output

- the

ImageOutputStream

or other

Object

to use for future writing.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of one of the classes returned by the
originating service provider's

getOutputTypes

method.
**See Also:** getOutput()

- getOutput

```java
public
Object
getOutput()
```

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method. If no destination has been
set,

null

is returned.

The default implementation returns the value of the

output

instance variable.

**Returns:** the

Object

that was specified using

setOutput

, or

null

.
**See Also:** setOutput(java.lang.Object)

- getAvailableLocales

```java
public
Locale
[] getAvailableLocales()
```

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings. A return
value of

null

indicates that localization is not
supported.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

**Returns:** an array of

Locale

s that may be used as
arguments to

setLocale

, or

null

.

- setLocale

```java
public void setLocale​(
Locale
locale)
```

Sets the current

Locale

of this

ImageWriter

to the given value. A value of

null

removes any previous setting, and indicates
that the writer should localize as it sees fit.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

**Parameters:** locale

- the desired

Locale

, or

null

.
**Throws:** IllegalArgumentException

- if

locale

is
non-

null

but is not one of the values returned by

getAvailableLocales

.
**See Also:** getLocale()

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

if none has been set.

The default implementation returns the value of the

locale

instance variable.

**Returns:** the current

Locale

, or

null

.
**See Also:** setLocale(java.util.Locale)

- getDefaultWriteParam

```java
public
ImageWriteParam
getDefaultWriteParam()
```

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified. This
is useful as a starting point for tweaking just a few parameters
and otherwise leaving the default settings alone.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

**Returns:** a new

ImageWriteParam

object containing
default values.

- getDefaultStreamMetadata

```java
public abstract
IIOMetadata
getDefaultStreamMetadata​(
ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding a stream of images. The contents of the
object may be manipulated using either the XML tree structure
returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via plug-in
specific interfaces, and the resulting data supplied to one of
the

write

methods that take a stream metadata
parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

- getDefaultImageMetadata

```java
public abstract
IIOMetadata
getDefaultImageMetadata​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type. The contents
of the object may be manipulated using either the XML tree
structure returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via
plug-in specific interfaces, and the resulting data supplied to
one of the

write

methods that take a stream
metadata parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
format of the image to be written later.
**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

- getNumThumbnailsSupported

```java
public int getNumThumbnailsSupported​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding. A return value of

-1

indicates that
insufficient information is available.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** the number of thumbnails that may be written given the
supplied parameters, or

-1

if insufficient
information is available.

- getPreferredThumbnailSizes

```java
public
Dimension
[] getPreferredThumbnailSizes​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream. This information is merely
advisory; the writer will resize any supplied thumbnails as
necessary.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.

- canWriteRasters

```java
public boolean canWriteRasters()
```

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image. If this method returns

false

, then
those methods will throw an

UnsupportedOperationException

if supplied with an

IIOImage

containing a

Raster

.

The default implementation returns

false

.

**Returns:** true

if

Raster

sources are
supported.

- write

```java
public abstract void write​(
IIOMetadata
streamMetadata,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output. Any necessary header information is included. If the
output is an

ImageOutputStream

, its existing
contents prior to the current seek position are not affected,
and need not be readable or writable.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public void write​(
IIOImage
image)
throws
IOException
```

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output. This method is
a shorthand for

write(null, image, null)

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public void write​(
RenderedImage
image)
throws
IOException
```

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output. This
method is a shorthand for

write(null, new IIOImage(image, null, null), null)

.

**Parameters:** image

- a

RenderedImage

to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

- canWriteSequence

```java
public boolean canWriteSequence()
```

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

**Returns:** true

if images may be appended sequentially.

- prepareWriteSequence

```java
public void prepareWriteSequence​(
IIOMetadata
streamMetadata)
throws
IOException
```

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object. The metadata will be written to the stream if
it should precede the image data. If the argument is

null

,
default stream metadata is used.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- A stream metadata object, or

null

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs writing the stream
metadata.

- writeToSequence

```java
public void writeToSequence​(
IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a single image and possibly associated metadata and
thumbnails, to the output. If the output is an

ImageOutputStream

, the existing contents of the
output prior to the current seek position may be flushed, and
need not be readable or writable, unless the plug-in needs to
be able to patch up the header information when

endWriteSequence

is called (

e.g.

TIFF).

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- endWriteSequence

```java
public void endWriteSequence()
throws
IOException
```

Completes the writing of a sequence of images begun with

prepareWriteSequence

. Any stream metadata that
should come at the end of the sequence of images is written out,
and any header information at the beginning of the sequence is
patched up if necessary. If the output is an

ImageOutputStream

, data through the stream metadata
at the end of the sequence are flushed and need not be readable
or writable.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- canReplaceStreamMetadata

```java
public boolean canReplaceStreamMetadata()
throws
IOException
```

Returns

true

if it is possible to replace the
stream metadata already present in the output.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if replacement of stream metadata is
allowed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IOException

- if an I/O error occurs during the query.

- replaceStreamMetadata

```java
public void replaceStreamMetadata​(
IIOMetadata
streamMetadata)
throws
IOException
```

Replaces the stream metadata in the output with new
information. If the output is an

ImageOutputStream

, the prior contents of the
stream are examined and possibly edited to make room for the
new data. All of the prior contents of the output must be
available for reading and writing.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if the

canReplaceStreamMetadata

returns

false

. modes do not include
**Throws:** IOException

- if an error occurs during writing.

- canReplaceImageMetadata

```java
public boolean canReplaceImageMetadata​(int imageIndex)
throws
IOException
```

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

. If this method returns

false

, a call to

replaceImageMetadata(imageIndex)

will throw an

UnsupportedOperationException

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Returns:** true

if the image metadata of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image metadata replacement in general, but

imageIndex

is less than 0 or greater than the
largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- replaceImageMetadata

```java
public void replaceImageMetadata​(int imageIndex,

IIOMetadata
imageMetadata)
throws
IOException
```

Replaces the image metadata associated with an existing image.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** UnsupportedOperationException

- if

canReplaceImageMetadata

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an error occurs during writing.

- canInsertImage

```java
public boolean canInsertImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new image at the given index. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an image may be inserted at the
given index.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image insertion in general, but

imageIndex

is less
than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- writeInsert

```java
public void writeInsert​(int imageIndex,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Inserts a new image into an existing image stream. Existing
images with an index greater than

imageIndex

are
preserved, and their indices are each increased by 1. A value
for

imageIndex

of -1 may be used to signify an
index one larger than the previous largest index; that is, it
will cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertImage(imageIndex)

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- canRemoveImage

```java
public boolean canRemoveImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the removal
of an existing image at the given index. Existing images with
indices greater than the insertion index will have
their indices decreased by 1.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Returns:** true

if it is possible to remove the given
image.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image removal in general, but

imageIndex

is less
than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

- removeImage

```java
public void removeImage​(int imageIndex)
throws
IOException
```

Removes an image from the stream.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canRemoveImage(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
removal.

- canWriteEmpty

```java
public boolean canWriteEmpty()
throws
IOException
```

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output. The pixel values may be defined by future
calls to the

replacePixels

methods. If the output
is an

ImageOutputStream

, its existing contents
prior to the current seek position are not affected, and need
not be readable or writable.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if the writing of complete image
stream with contents to be defined later is supported.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IOException

- if an I/O error occurs during the
query.

- prepareWriteEmpty

```java
public void prepareWriteEmpty​(
IIOMetadata
streamMetadata,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output. The pixel values will
be defined by future calls to the

replacePixels

methods. If the output is an

ImageOutputStream

,
its existing contents prior to the current seek position are
not affected, and need not be readable or writable.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

- endWriteEmpty

```java
public void endWriteEmpty()
throws
IOException
```

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReiplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- canInsertEmpty

```java
public boolean canInsertEmpty​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new, empty image at the given index. The pixel values of
the image are undefined, and may be specified in pieces using
the

replacePixels

methods. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an empty image may be inserted at
the given index.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
empty image insertion in general, but

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

- prepareInsertEmpty

```java
public void prepareInsertEmpty​(int imageIndex,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the insertion of a new image with undefined pixel values
into an existing image stream. Existing images with an index
greater than

imageIndex

are preserved, and their
indices are each increased by 1. A value for

imageIndex

of -1 may be used to signify an index
one larger than the previous largest index; that is, it will
cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

- endInsertEmpty

```java
public void endInsertEmpty()
throws
IOException
```

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- canReplacePixels

```java
public boolean canReplacePixels​(int imageIndex)
throws
IOException
```

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Returns:** true

if the pixels of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
pixel replacement in general, but

imageIndex

is
less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- prepareReplacePixels

```java
public void prepareReplacePixels​(int imageIndex,

Rectangle
region)
throws
IOException
```

Prepares the writer to handle a series of calls to the

replacePixels

methods. The affected pixel area
will be clipped against the supplied

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Parameters:** region

- a

Rectangle

that will be used to clip
future pixel regions.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IllegalStateException

- if there is a previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

(

i.e.

, nesting is not
allowed).
**Throws:** IllegalArgumentException

- if

region

is

null

or has a width or height less than 1.
**Throws:** IOException

- if an I/O error occurs during the
preparation.

- replacePixels

```java
public void replacePixels​(
RenderedImage
image,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given image. The image data must match,
or be convertible to, the image layout of the existing image.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- a

RenderedImage

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- image

is

null

.

the intersected region does not contain at least one pixel.

the layout of

image

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

- replacePixels

```java
public void replacePixels​(
Raster
raster,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given

Raster

. The image
data must match, or be convertible to, the image layout of the
existing image.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** raster

- a

Raster

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** UnsupportedOperationException

- if

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- raster

is

null

.

the intersected region does not contain at least one pixel.

the layout of

raster

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

- endReplacePixels

```java
public void endReplacePixels()
throws
IOException
```

Terminates a sequence of calls to

replacePixels

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call
to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- abort

```java
public void abort()
```

Requests that any current write operation be aborted. The
contents of the output following the abort will be undefined.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

- abortRequested

```java
protected boolean abortRequested()
```

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

**Returns:** true

if the current write operation should
be aborted.
**See Also:** abort()

,

clearAbortRequest()

- clearAbortRequest

```java
protected void clearAbortRequest()
```

Clears any previous abort request. After this method has been
called,

abortRequested

will return

false

.

**See Also:** abort()

,

abortRequested()

- addIIOWriteWarningListener

```java
public void addIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken. Messages sent to the given listener will be
localized, if possible, to match the current

Locale

. If no

Locale

has been set,
warning messages may be localized as the writer sees fit.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
registered.
**See Also:** removeIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

- removeIIOWriteWarningListener

```java
public void removeIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
deregistered.
**See Also:** addIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

- removeAllIIOWriteWarningListeners

```java
public void removeAllIIOWriteWarningListeners()
```

Removes all currently registered

IIOWriteWarningListener

objects.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

- addIIOWriteProgressListener

```java
public void addIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
registered.
**See Also:** removeIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

- removeIIOWriteProgressListener

```java
public void removeIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
deregistered.
**See Also:** addIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

- removeAllIIOWriteProgressListeners

```java
public void removeAllIIOWriteProgressListeners()
```

Removes all currently registered

IIOWriteProgressListener

objects.

The default implementation sets the

progressListeners

instance variable to

null

.

- processImageStarted

```java
protected void processImageStarted​(int imageIndex)
```

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image about to be written.

- processImageProgress

```java
protected void processImageProgress​(float percentageDone)
```

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method. Subclasses may use
this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

- processImageComplete

```java
protected void processImageComplete()
```

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method. Subclasses may use this
method as a convenience.

- processThumbnailStarted

```java
protected void processThumbnailStarted​(int imageIndex,
int thumbnailIndex)
```

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image associated with the
thumbnail.
**Parameters:** thumbnailIndex

- the index of the thumbnail.

- processThumbnailProgress

```java
protected void processThumbnailProgress​(float percentageDone)
```

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method. Subclasses may
use this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

- processThumbnailComplete

```java
protected void processThumbnailComplete()
```

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method. Subclasses may use this
method as a convenience.

- processWriteAborted

```java
protected void processWriteAborted()
```

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method. Subclasses may use this
method as a convenience.

- processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
warning)
```

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** warning

- the warning message.
**Throws:** IllegalArgumentException

- if

warning

is

null

.

- processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
baseName,

String
keyword)
```

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** baseName

- the base name of a set of

ResourceBundle

s containing localized warning
messages.
**Parameters:** keyword

- the keyword used to index the warning message
within the set of

ResourceBundle

s.
**Throws:** IllegalArgumentException

- if

baseName

is

null

.
**Throws:** IllegalArgumentException

- if

keyword

is

null

.
**Throws:** IllegalArgumentException

- if no appropriate

ResourceBundle

may be located.
**Throws:** IllegalArgumentException

- if the named resource is
not found in the located

ResourceBundle

.
**Throws:** IllegalArgumentException

- if the object retrieved
from the

ResourceBundle

is not a

String

.

- reset

```java
public void reset()
```

Restores the

ImageWriter

to its initial state.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

- dispose

```java
public void dispose()
```

Allows any resources held by this object to be released. The
result of calling any other method (other than

finalize

) subsequent to a call to this method
is undefined.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

Field Detail

- originatingProvider

```java
protected
ImageWriterSpi
originatingProvider
```

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists. By default it is initialized to

null

.

- output

```java
protected
Object
output
```

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

. By default it is initialized to

null

.

- availableLocales

```java
protected
Locale
[] availableLocales
```

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported. By default
it is initialized to

null

.

- locale

```java
protected
Locale
locale
```

The current

Locale

to be used for localization, or

null

if none has been set. By default it is
initialized to

null

.

- warningListeners

```java
protected
List
<
IIOWriteWarningListener
> warningListeners
```

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

- warningLocales

```java
protected
List
<
Locale
> warningLocales
```

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

- progressListeners

```java
protected
List
<
IIOWriteProgressListener
> progressListeners
```

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

---

#### Field Detail

originatingProvider

```java
protected
ImageWriterSpi
originatingProvider
```

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists. By default it is initialized to

null

.

---

#### originatingProvider

protected

ImageWriterSpi

originatingProvider

The

ImageWriterSpi

that instantiated this object,
or

null

if its identity is not known or none
exists. By default it is initialized to

null

.

output

```java
protected
Object
output
```

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

. By default it is initialized to

null

.

---

#### output

protected

Object

output

The

ImageOutputStream

or other

Object

set by

setOutput

and retrieved by

getOutput

. By default it is initialized to

null

.

availableLocales

```java
protected
Locale
[] availableLocales
```

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported. By default
it is initialized to

null

.

---

#### availableLocales

protected

Locale

[] availableLocales

An array of

Locale

s that may be used to localize
warning messages and compression setting values, or

null

if localization is not supported. By default
it is initialized to

null

.

locale

```java
protected
Locale
locale
```

The current

Locale

to be used for localization, or

null

if none has been set. By default it is
initialized to

null

.

---

#### locale

protected

Locale

locale

The current

Locale

to be used for localization, or

null

if none has been set. By default it is
initialized to

null

.

warningListeners

```java
protected
List
<
IIOWriteWarningListener
> warningListeners
```

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

---

#### warningListeners

protected

List

<

IIOWriteWarningListener

> warningListeners

A

List

of currently registered

IIOWriteWarningListener

s, initialized by default to

null

, which is synonymous with an empty

List

.

warningLocales

```java
protected
List
<
Locale
> warningLocales
```

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

---

#### warningLocales

protected

List

<

Locale

> warningLocales

A

List

of

Locale

s, one for each
element of

warningListeners

, initialized by default

null

, which is synonymous with an empty

List

.

progressListeners

```java
protected
List
<
IIOWriteProgressListener
> progressListeners
```

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

---

#### progressListeners

protected

List

<

IIOWriteProgressListener

> progressListeners

A

List

of currently registered

IIOWriteProgressListener

s, initialized by default

null

, which is synonymous with an empty

List

.

Constructor Detail

- ImageWriter

```java
protected ImageWriter​(
ImageWriterSpi
originatingProvider)
```

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

**Parameters:** originatingProvider

- the

ImageWriterSpi

that
is constructing this object, or

null

.

---

#### Constructor Detail

ImageWriter

```java
protected ImageWriter​(
ImageWriterSpi
originatingProvider)
```

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

**Parameters:** originatingProvider

- the

ImageWriterSpi

that
is constructing this object, or

null

.

---

#### ImageWriter

protected ImageWriter​(

ImageWriterSpi

originatingProvider)

Constructs an

ImageWriter

and sets its

originatingProvider

instance variable to the
supplied value.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

Subclasses that make use of extensions should provide a
constructor with signature

(ImageWriterSpi, Object)

in order to retrieve the extension object. If
the extension object is unsuitable, an

IllegalArgumentException

should be thrown.

Method Detail

- getOriginatingProvider

```java
public
ImageWriterSpi
getOriginatingProvider()
```

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

The default implementation returns the value of the

originatingProvider

instance variable.

**Returns:** an

ImageWriterSpi

, or

null

.
**See Also:** ImageWriterSpi

- setOutput

```java
public void setOutput​(
Object
output)
```

Sets the destination to the given

ImageOutputStream

or other

Object

.
The destination is assumed to be ready to accept data, and will
not be closed at the end of each write. This allows distributed
imaging applications to transmit a series of images over a
single network connection. If

output

is

null

, any currently set output will be removed.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

**Parameters:** output

- the

ImageOutputStream

or other

Object

to use for future writing.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of one of the classes returned by the
originating service provider's

getOutputTypes

method.
**See Also:** getOutput()

- getOutput

```java
public
Object
getOutput()
```

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method. If no destination has been
set,

null

is returned.

The default implementation returns the value of the

output

instance variable.

**Returns:** the

Object

that was specified using

setOutput

, or

null

.
**See Also:** setOutput(java.lang.Object)

- getAvailableLocales

```java
public
Locale
[] getAvailableLocales()
```

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings. A return
value of

null

indicates that localization is not
supported.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

**Returns:** an array of

Locale

s that may be used as
arguments to

setLocale

, or

null

.

- setLocale

```java
public void setLocale​(
Locale
locale)
```

Sets the current

Locale

of this

ImageWriter

to the given value. A value of

null

removes any previous setting, and indicates
that the writer should localize as it sees fit.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

**Parameters:** locale

- the desired

Locale

, or

null

.
**Throws:** IllegalArgumentException

- if

locale

is
non-

null

but is not one of the values returned by

getAvailableLocales

.
**See Also:** getLocale()

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

if none has been set.

The default implementation returns the value of the

locale

instance variable.

**Returns:** the current

Locale

, or

null

.
**See Also:** setLocale(java.util.Locale)

- getDefaultWriteParam

```java
public
ImageWriteParam
getDefaultWriteParam()
```

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified. This
is useful as a starting point for tweaking just a few parameters
and otherwise leaving the default settings alone.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

**Returns:** a new

ImageWriteParam

object containing
default values.

- getDefaultStreamMetadata

```java
public abstract
IIOMetadata
getDefaultStreamMetadata​(
ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding a stream of images. The contents of the
object may be manipulated using either the XML tree structure
returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via plug-in
specific interfaces, and the resulting data supplied to one of
the

write

methods that take a stream metadata
parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

- getDefaultImageMetadata

```java
public abstract
IIOMetadata
getDefaultImageMetadata​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type. The contents
of the object may be manipulated using either the XML tree
structure returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via
plug-in specific interfaces, and the resulting data supplied to
one of the

write

methods that take a stream
metadata parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
format of the image to be written later.
**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

- getNumThumbnailsSupported

```java
public int getNumThumbnailsSupported​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding. A return value of

-1

indicates that
insufficient information is available.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** the number of thumbnails that may be written given the
supplied parameters, or

-1

if insufficient
information is available.

- getPreferredThumbnailSizes

```java
public
Dimension
[] getPreferredThumbnailSizes​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream. This information is merely
advisory; the writer will resize any supplied thumbnails as
necessary.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.

- canWriteRasters

```java
public boolean canWriteRasters()
```

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image. If this method returns

false

, then
those methods will throw an

UnsupportedOperationException

if supplied with an

IIOImage

containing a

Raster

.

The default implementation returns

false

.

**Returns:** true

if

Raster

sources are
supported.

- write

```java
public abstract void write​(
IIOMetadata
streamMetadata,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output. Any necessary header information is included. If the
output is an

ImageOutputStream

, its existing
contents prior to the current seek position are not affected,
and need not be readable or writable.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public void write​(
IIOImage
image)
throws
IOException
```

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output. This method is
a shorthand for

write(null, image, null)

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public void write​(
RenderedImage
image)
throws
IOException
```

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output. This
method is a shorthand for

write(null, new IIOImage(image, null, null), null)

.

**Parameters:** image

- a

RenderedImage

to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

- canWriteSequence

```java
public boolean canWriteSequence()
```

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

**Returns:** true

if images may be appended sequentially.

- prepareWriteSequence

```java
public void prepareWriteSequence​(
IIOMetadata
streamMetadata)
throws
IOException
```

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object. The metadata will be written to the stream if
it should precede the image data. If the argument is

null

,
default stream metadata is used.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- A stream metadata object, or

null

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs writing the stream
metadata.

- writeToSequence

```java
public void writeToSequence​(
IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a single image and possibly associated metadata and
thumbnails, to the output. If the output is an

ImageOutputStream

, the existing contents of the
output prior to the current seek position may be flushed, and
need not be readable or writable, unless the plug-in needs to
be able to patch up the header information when

endWriteSequence

is called (

e.g.

TIFF).

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- endWriteSequence

```java
public void endWriteSequence()
throws
IOException
```

Completes the writing of a sequence of images begun with

prepareWriteSequence

. Any stream metadata that
should come at the end of the sequence of images is written out,
and any header information at the beginning of the sequence is
patched up if necessary. If the output is an

ImageOutputStream

, data through the stream metadata
at the end of the sequence are flushed and need not be readable
or writable.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- canReplaceStreamMetadata

```java
public boolean canReplaceStreamMetadata()
throws
IOException
```

Returns

true

if it is possible to replace the
stream metadata already present in the output.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if replacement of stream metadata is
allowed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IOException

- if an I/O error occurs during the query.

- replaceStreamMetadata

```java
public void replaceStreamMetadata​(
IIOMetadata
streamMetadata)
throws
IOException
```

Replaces the stream metadata in the output with new
information. If the output is an

ImageOutputStream

, the prior contents of the
stream are examined and possibly edited to make room for the
new data. All of the prior contents of the output must be
available for reading and writing.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if the

canReplaceStreamMetadata

returns

false

. modes do not include
**Throws:** IOException

- if an error occurs during writing.

- canReplaceImageMetadata

```java
public boolean canReplaceImageMetadata​(int imageIndex)
throws
IOException
```

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

. If this method returns

false

, a call to

replaceImageMetadata(imageIndex)

will throw an

UnsupportedOperationException

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Returns:** true

if the image metadata of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image metadata replacement in general, but

imageIndex

is less than 0 or greater than the
largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- replaceImageMetadata

```java
public void replaceImageMetadata​(int imageIndex,

IIOMetadata
imageMetadata)
throws
IOException
```

Replaces the image metadata associated with an existing image.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** UnsupportedOperationException

- if

canReplaceImageMetadata

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an error occurs during writing.

- canInsertImage

```java
public boolean canInsertImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new image at the given index. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an image may be inserted at the
given index.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image insertion in general, but

imageIndex

is less
than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- writeInsert

```java
public void writeInsert​(int imageIndex,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Inserts a new image into an existing image stream. Existing
images with an index greater than

imageIndex

are
preserved, and their indices are each increased by 1. A value
for

imageIndex

of -1 may be used to signify an
index one larger than the previous largest index; that is, it
will cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertImage(imageIndex)

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

- canRemoveImage

```java
public boolean canRemoveImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the removal
of an existing image at the given index. Existing images with
indices greater than the insertion index will have
their indices decreased by 1.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Returns:** true

if it is possible to remove the given
image.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image removal in general, but

imageIndex

is less
than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

- removeImage

```java
public void removeImage​(int imageIndex)
throws
IOException
```

Removes an image from the stream.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canRemoveImage(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
removal.

- canWriteEmpty

```java
public boolean canWriteEmpty()
throws
IOException
```

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output. The pixel values may be defined by future
calls to the

replacePixels

methods. If the output
is an

ImageOutputStream

, its existing contents
prior to the current seek position are not affected, and need
not be readable or writable.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if the writing of complete image
stream with contents to be defined later is supported.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IOException

- if an I/O error occurs during the
query.

- prepareWriteEmpty

```java
public void prepareWriteEmpty​(
IIOMetadata
streamMetadata,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output. The pixel values will
be defined by future calls to the

replacePixels

methods. If the output is an

ImageOutputStream

,
its existing contents prior to the current seek position are
not affected, and need not be readable or writable.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

- endWriteEmpty

```java
public void endWriteEmpty()
throws
IOException
```

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReiplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- canInsertEmpty

```java
public boolean canInsertEmpty​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new, empty image at the given index. The pixel values of
the image are undefined, and may be specified in pieces using
the

replacePixels

methods. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an empty image may be inserted at
the given index.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
empty image insertion in general, but

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

- prepareInsertEmpty

```java
public void prepareInsertEmpty​(int imageIndex,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the insertion of a new image with undefined pixel values
into an existing image stream. Existing images with an index
greater than

imageIndex

are preserved, and their
indices are each increased by 1. A value for

imageIndex

of -1 may be used to signify an index
one larger than the previous largest index; that is, it will
cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

- endInsertEmpty

```java
public void endInsertEmpty()
throws
IOException
```

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- canReplacePixels

```java
public boolean canReplacePixels​(int imageIndex)
throws
IOException
```

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Returns:** true

if the pixels of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
pixel replacement in general, but

imageIndex

is
less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

- prepareReplacePixels

```java
public void prepareReplacePixels​(int imageIndex,

Rectangle
region)
throws
IOException
```

Prepares the writer to handle a series of calls to the

replacePixels

methods. The affected pixel area
will be clipped against the supplied

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Parameters:** region

- a

Rectangle

that will be used to clip
future pixel regions.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IllegalStateException

- if there is a previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

(

i.e.

, nesting is not
allowed).
**Throws:** IllegalArgumentException

- if

region

is

null

or has a width or height less than 1.
**Throws:** IOException

- if an I/O error occurs during the
preparation.

- replacePixels

```java
public void replacePixels​(
RenderedImage
image,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given image. The image data must match,
or be convertible to, the image layout of the existing image.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- a

RenderedImage

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- image

is

null

.

the intersected region does not contain at least one pixel.

the layout of

image

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

- replacePixels

```java
public void replacePixels​(
Raster
raster,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given

Raster

. The image
data must match, or be convertible to, the image layout of the
existing image.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** raster

- a

Raster

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** UnsupportedOperationException

- if

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- raster

is

null

.

the intersected region does not contain at least one pixel.

the layout of

raster

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

- endReplacePixels

```java
public void endReplacePixels()
throws
IOException
```

Terminates a sequence of calls to

replacePixels

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call
to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

- abort

```java
public void abort()
```

Requests that any current write operation be aborted. The
contents of the output following the abort will be undefined.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

- abortRequested

```java
protected boolean abortRequested()
```

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

**Returns:** true

if the current write operation should
be aborted.
**See Also:** abort()

,

clearAbortRequest()

- clearAbortRequest

```java
protected void clearAbortRequest()
```

Clears any previous abort request. After this method has been
called,

abortRequested

will return

false

.

**See Also:** abort()

,

abortRequested()

- addIIOWriteWarningListener

```java
public void addIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken. Messages sent to the given listener will be
localized, if possible, to match the current

Locale

. If no

Locale

has been set,
warning messages may be localized as the writer sees fit.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
registered.
**See Also:** removeIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

- removeIIOWriteWarningListener

```java
public void removeIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
deregistered.
**See Also:** addIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

- removeAllIIOWriteWarningListeners

```java
public void removeAllIIOWriteWarningListeners()
```

Removes all currently registered

IIOWriteWarningListener

objects.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

- addIIOWriteProgressListener

```java
public void addIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
registered.
**See Also:** removeIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

- removeIIOWriteProgressListener

```java
public void removeIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
deregistered.
**See Also:** addIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

- removeAllIIOWriteProgressListeners

```java
public void removeAllIIOWriteProgressListeners()
```

Removes all currently registered

IIOWriteProgressListener

objects.

The default implementation sets the

progressListeners

instance variable to

null

.

- processImageStarted

```java
protected void processImageStarted​(int imageIndex)
```

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image about to be written.

- processImageProgress

```java
protected void processImageProgress​(float percentageDone)
```

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method. Subclasses may use
this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

- processImageComplete

```java
protected void processImageComplete()
```

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method. Subclasses may use this
method as a convenience.

- processThumbnailStarted

```java
protected void processThumbnailStarted​(int imageIndex,
int thumbnailIndex)
```

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image associated with the
thumbnail.
**Parameters:** thumbnailIndex

- the index of the thumbnail.

- processThumbnailProgress

```java
protected void processThumbnailProgress​(float percentageDone)
```

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method. Subclasses may
use this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

- processThumbnailComplete

```java
protected void processThumbnailComplete()
```

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method. Subclasses may use this
method as a convenience.

- processWriteAborted

```java
protected void processWriteAborted()
```

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method. Subclasses may use this
method as a convenience.

- processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
warning)
```

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** warning

- the warning message.
**Throws:** IllegalArgumentException

- if

warning

is

null

.

- processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
baseName,

String
keyword)
```

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** baseName

- the base name of a set of

ResourceBundle

s containing localized warning
messages.
**Parameters:** keyword

- the keyword used to index the warning message
within the set of

ResourceBundle

s.
**Throws:** IllegalArgumentException

- if

baseName

is

null

.
**Throws:** IllegalArgumentException

- if

keyword

is

null

.
**Throws:** IllegalArgumentException

- if no appropriate

ResourceBundle

may be located.
**Throws:** IllegalArgumentException

- if the named resource is
not found in the located

ResourceBundle

.
**Throws:** IllegalArgumentException

- if the object retrieved
from the

ResourceBundle

is not a

String

.

- reset

```java
public void reset()
```

Restores the

ImageWriter

to its initial state.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

- dispose

```java
public void dispose()
```

Allows any resources held by this object to be released. The
result of calling any other method (other than

finalize

) subsequent to a call to this method
is undefined.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

---

#### Method Detail

getOriginatingProvider

```java
public
ImageWriterSpi
getOriginatingProvider()
```

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

The default implementation returns the value of the

originatingProvider

instance variable.

**Returns:** an

ImageWriterSpi

, or

null

.
**See Also:** ImageWriterSpi

---

#### getOriginatingProvider

public

ImageWriterSpi

getOriginatingProvider()

Returns the

ImageWriterSpi

object that created
this

ImageWriter

, or

null

if this
object was not created through the

IIORegistry

.

The default implementation returns the value of the

originatingProvider

instance variable.

The default implementation returns the value of the

originatingProvider

instance variable.

setOutput

```java
public void setOutput​(
Object
output)
```

Sets the destination to the given

ImageOutputStream

or other

Object

.
The destination is assumed to be ready to accept data, and will
not be closed at the end of each write. This allows distributed
imaging applications to transmit a series of images over a
single network connection. If

output

is

null

, any currently set output will be removed.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

**Parameters:** output

- the

ImageOutputStream

or other

Object

to use for future writing.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of one of the classes returned by the
originating service provider's

getOutputTypes

method.
**See Also:** getOutput()

---

#### setOutput

public void setOutput​(

Object

output)

Sets the destination to the given

ImageOutputStream

or other

Object

.
The destination is assumed to be ready to accept data, and will
not be closed at the end of each write. This allows distributed
imaging applications to transmit a series of images over a
single network connection. If

output

is

null

, any currently set output will be removed.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

If

output

is an

ImageOutputStream

, calls to the

write

,

writeToSequence

, and

prepareWriteEmpty

/

endWriteEmpty

methods will preserve the existing contents of the stream.
Other write methods, such as

writeInsert

,

replaceStreamMetadata

,

replaceImageMetadata

,

replacePixels

,

prepareInsertEmpty

/

endInsertEmpty

,
and

endWriteSequence

, require the full contents
of the stream to be readable and writable, and may alter any
portion of the stream.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

Use of a general

Object

other than an

ImageOutputStream

is intended for writers that
interact directly with an output device or imaging protocol.
The set of legal classes is advertised by the writer's service
provider's

getOutputTypes

method; most writers
will return a single-element array containing only

ImageOutputStream.class

to indicate that they
accept only an

ImageOutputStream

.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

The default implementation sets the

output

instance variable to the value of

output

after
checking

output

against the set of classes
advertised by the originating provider, if there is one.

getOutput

```java
public
Object
getOutput()
```

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method. If no destination has been
set,

null

is returned.

The default implementation returns the value of the

output

instance variable.

**Returns:** the

Object

that was specified using

setOutput

, or

null

.
**See Also:** setOutput(java.lang.Object)

---

#### getOutput

public

Object

getOutput()

Returns the

ImageOutputStream

or other

Object

set by the most recent call to the

setOutput

method. If no destination has been
set,

null

is returned.

The default implementation returns the value of the

output

instance variable.

The default implementation returns the value of the

output

instance variable.

getAvailableLocales

```java
public
Locale
[] getAvailableLocales()
```

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings. A return
value of

null

indicates that localization is not
supported.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

**Returns:** an array of

Locale

s that may be used as
arguments to

setLocale

, or

null

.

---

#### getAvailableLocales

public

Locale

[] getAvailableLocales()

Returns an array of

Locale

s that may be used to
localize warning listeners and compression settings. A return
value of

null

indicates that localization is not
supported.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

The default implementation returns a clone of the

availableLocales

instance variable if it is
non-

null

, or else returns

null

.

setLocale

```java
public void setLocale​(
Locale
locale)
```

Sets the current

Locale

of this

ImageWriter

to the given value. A value of

null

removes any previous setting, and indicates
that the writer should localize as it sees fit.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

**Parameters:** locale

- the desired

Locale

, or

null

.
**Throws:** IllegalArgumentException

- if

locale

is
non-

null

but is not one of the values returned by

getAvailableLocales

.
**See Also:** getLocale()

---

#### setLocale

public void setLocale​(

Locale

locale)

Sets the current

Locale

of this

ImageWriter

to the given value. A value of

null

removes any previous setting, and indicates
that the writer should localize as it sees fit.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

The default implementation checks

locale

against the values returned by

getAvailableLocales

, and sets the

locale

instance variable if it is found. If

locale

is

null

, the instance variable
is set to

null

without any checking.

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

if none has been set.

The default implementation returns the value of the

locale

instance variable.

**Returns:** the current

Locale

, or

null

.
**See Also:** setLocale(java.util.Locale)

---

#### getLocale

public

Locale

getLocale()

Returns the currently set

Locale

, or

null

if none has been set.

The default implementation returns the value of the

locale

instance variable.

The default implementation returns the value of the

locale

instance variable.

getDefaultWriteParam

```java
public
ImageWriteParam
getDefaultWriteParam()
```

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified. This
is useful as a starting point for tweaking just a few parameters
and otherwise leaving the default settings alone.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

**Returns:** a new

ImageWriteParam

object containing
default values.

---

#### getDefaultWriteParam

public

ImageWriteParam

getDefaultWriteParam()

Returns a new

ImageWriteParam

object of the
appropriate type for this file format containing default
values, that is, those values that would be used
if no

ImageWriteParam

object were specified. This
is useful as a starting point for tweaking just a few parameters
and otherwise leaving the default settings alone.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

The default implementation constructs and returns a new

ImageWriteParam

object that does not allow tiling,
progressive encoding, or compression, and that will be
localized for the current

Locale

(

i.e.

,
what you would get by calling

new ImageWriteParam(getLocale())

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

Individual plug-ins may return an instance of

ImageWriteParam

with additional optional features
enabled, or they may return an instance of a plug-in specific
subclass of

ImageWriteParam

.

getDefaultStreamMetadata

```java
public abstract
IIOMetadata
getDefaultStreamMetadata​(
ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding a stream of images. The contents of the
object may be manipulated using either the XML tree structure
returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via plug-in
specific interfaces, and the resulting data supplied to one of
the

write

methods that take a stream metadata
parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

---

#### getDefaultStreamMetadata

public abstract

IIOMetadata

getDefaultStreamMetadata​(

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding a stream of images. The contents of the
object may be manipulated using either the XML tree structure
returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via plug-in
specific interfaces, and the resulting data supplied to one of
the

write

methods that take a stream metadata
parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the stream
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

Writers that do not make use of stream metadata
(

e.g.

, writers for single-image formats) should return

null

.

getDefaultImageMetadata

```java
public abstract
IIOMetadata
getDefaultImageMetadata​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param)
```

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type. The contents
of the object may be manipulated using either the XML tree
structure returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via
plug-in specific interfaces, and the resulting data supplied to
one of the

write

methods that take a stream
metadata parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
format of the image to be written later.
**Parameters:** param

- an

ImageWriteParam

that will be used to
encode the image, or

null

.
**Returns:** an

IIOMetadata

object.

---

#### getDefaultImageMetadata

public abstract

IIOMetadata

getDefaultImageMetadata​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param)

Returns an

IIOMetadata

object containing default
values for encoding an image of the given type. The contents
of the object may be manipulated using either the XML tree
structure returned by the

IIOMetadata.getAsTree

method, an

IIOMetadataController

object, or via
plug-in specific interfaces, and the resulting data supplied to
one of the

write

methods that take a stream
metadata parameter.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

An optional

ImageWriteParam

may be supplied
for cases where it may affect the structure of the image
metadata.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

getNumThumbnailsSupported

```java
public int getNumThumbnailsSupported​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding. A return value of

-1

indicates that
insufficient information is available.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** the number of thumbnails that may be written given the
supplied parameters, or

-1

if insufficient
information is available.

---

#### getNumThumbnailsSupported

public int getNumThumbnailsSupported​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns the number of thumbnails supported by the format being
written, given the image type and any additional write
parameters and metadata objects that will be used during
encoding. A return value of

-1

indicates that
insufficient information is available.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns 0.

The default implementation returns 0.

getPreferredThumbnailSizes

```java
public
Dimension
[] getPreferredThumbnailSizes​(
ImageTypeSpecifier
imageType,

ImageWriteParam
param,

IIOMetadata
streamMetadata,

IIOMetadata
imageMetadata)
```

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream. This information is merely
advisory; the writer will resize any supplied thumbnails as
necessary.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

**Parameters:** imageType

- an

ImageTypeSpecifier

indicating the
type of image to be written, or

null

.
**Parameters:** param

- the

ImageWriteParam

that will be used for
writing, or

null

.
**Parameters:** streamMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Parameters:** imageMetadata

- an

IIOMetadata

object that will
be used for writing, or

null

.
**Returns:** an array of

Dimension

s with an even length
of at least two, or

null

.

---

#### getPreferredThumbnailSizes

public

Dimension

[] getPreferredThumbnailSizes​(

ImageTypeSpecifier

imageType,

ImageWriteParam

param,

IIOMetadata

streamMetadata,

IIOMetadata

imageMetadata)

Returns an array of

Dimension

s indicating the
legal size ranges for thumbnail images as they will be encoded
in the output file or stream. This information is merely
advisory; the writer will resize any supplied thumbnails as
necessary.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

The information is returned as a set of pairs; the first
element of a pair contains an (inclusive) minimum width and
height, and the second element contains an (inclusive) maximum
width and height. Together, each pair defines a valid range of
sizes. To specify a fixed size, the same width and height will
appear for both elements. A return value of

null

indicates that the size is arbitrary or unknown.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

An

ImageWriteParam

may optionally be supplied
for cases where it may affect thumbnail handling.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation returns

null

.

The default implementation returns

null

.

canWriteRasters

```java
public boolean canWriteRasters()
```

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image. If this method returns

false

, then
those methods will throw an

UnsupportedOperationException

if supplied with an

IIOImage

containing a

Raster

.

The default implementation returns

false

.

**Returns:** true

if

Raster

sources are
supported.

---

#### canWriteRasters

public boolean canWriteRasters()

Returns

true

if the methods that take an

IIOImage

parameter are capable of dealing with a

Raster

(as opposed to

RenderedImage

)
source image. If this method returns

false

, then
those methods will throw an

UnsupportedOperationException

if supplied with an

IIOImage

containing a

Raster

.

The default implementation returns

false

.

The default implementation returns

false

.

write

```java
public abstract void write​(
IIOMetadata
streamMetadata,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output. Any necessary header information is included. If the
output is an

ImageOutputStream

, its existing
contents prior to the current seek position are not affected,
and need not be readable or writable.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

---

#### write

public abstract void write​(

IIOMetadata

streamMetadata,

IIOImage

image,

ImageWriteParam

param)
throws

IOException

Appends a complete image stream containing a single image and
associated stream and image metadata and thumbnails to the
output. Any necessary header information is included. If the
output is an

ImageOutputStream

, its existing
contents prior to the current seek position are not affected,
and need not be readable or writable.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The output must have been set beforehand using the

setOutput

method.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

Stream metadata may optionally be supplied; if it is

null

, default stream metadata will be used.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer should generate them internally.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

An

ImageWriteParam

may
optionally be supplied to control the writing process. If

param

is

null

, a default write param
will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

write

```java
public void write​(
IIOImage
image)
throws
IOException
```

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output. This method is
a shorthand for

write(null, image, null)

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

---

#### write

public void write​(

IIOImage

image)
throws

IOException

Appends a complete image stream containing a single image with
default metadata and thumbnails to the output. This method is
a shorthand for

write(null, image, null)

.

write

```java
public void write​(
RenderedImage
image)
throws
IOException
```

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output. This
method is a shorthand for

write(null, new IIOImage(image, null, null), null)

.

**Parameters:** image

- a

RenderedImage

to be written.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IOException

- if an error occurs during writing.

---

#### write

public void write​(

RenderedImage

image)
throws

IOException

Appends a complete image stream consisting of a single image
with default metadata and thumbnails to the output. This
method is a shorthand for

write(null, new IIOImage(image, null, null), null)

.

canWriteSequence

```java
public boolean canWriteSequence()
```

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

**Returns:** true

if images may be appended sequentially.

---

#### canWriteSequence

public boolean canWriteSequence()

Returns

true

if the writer is able to append an
image to an image stream that already contains header
information and possibly prior images.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

If

canWriteSequence

returns

false

,

writeToSequence

and

endWriteSequence

will throw an

UnsupportedOperationException

.

The default implementation returns

false

.

The default implementation returns

false

.

prepareWriteSequence

```java
public void prepareWriteSequence​(
IIOMetadata
streamMetadata)
throws
IOException
```

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object. The metadata will be written to the stream if
it should precede the image data. If the argument is

null

,
default stream metadata is used.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- A stream metadata object, or

null

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs writing the stream
metadata.

---

#### prepareWriteSequence

public void prepareWriteSequence​(

IIOMetadata

streamMetadata)
throws

IOException

Prepares a stream to accept a series of subsequent

writeToSequence

calls, using the provided stream
metadata object. The metadata will be written to the stream if
it should precede the image data. If the argument is

null

,
default stream metadata is used.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the output is an

ImageOutputStream

, the existing
contents of the output prior to the current seek position are
flushed, and need not be readable or writable. If the format
requires that

endWriteSequence

be able to rewind to
patch up the header information, such as for a sequence of images
in a single TIFF file, then the metadata written by this method
must remain in a writable portion of the stream. Other formats
may flush the stream after this method and after each image.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The output must have been set beforehand using either
the

setOutput

method.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

writeToSequence

```java
public void writeToSequence​(
IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Appends a single image and possibly associated metadata and
thumbnails, to the output. If the output is an

ImageOutputStream

, the existing contents of the
output prior to the current seek position may be flushed, and
need not be readable or writable, unless the plug-in needs to
be able to patch up the header information when

endWriteSequence

is called (

e.g.

TIFF).

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

---

#### writeToSequence

public void writeToSequence​(

IIOImage

image,

ImageWriteParam

param)
throws

IOException

Appends a single image and possibly associated metadata and
thumbnails, to the output. If the output is an

ImageOutputStream

, the existing contents of the
output prior to the current seek position may be flushed, and
need not be readable or writable, unless the plug-in needs to
be able to patch up the header information when

endWriteSequence

is called (

e.g.

TIFF).

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The output must have been set beforehand using
the

setOutput

method.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

prepareWriteSequence

must have been called
beforehand, or an

IllegalStateException

is thrown.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteRasters

returns

true

,
the

IIOImage

may contain a

Raster

source. Otherwise, it must contain a

RenderedImage

source.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The supplied thumbnails will be resized if needed, and any
thumbnails in excess of the supported number will be ignored.
If the format requires additional thumbnails that are not
provided, the writer will generate them internally.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

endWriteSequence

```java
public void endWriteSequence()
throws
IOException
```

Completes the writing of a sequence of images begun with

prepareWriteSequence

. Any stream metadata that
should come at the end of the sequence of images is written out,
and any header information at the beginning of the sequence is
patched up if necessary. If the output is an

ImageOutputStream

, data through the stream metadata
at the end of the sequence are flushed and need not be readable
or writable.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set, or

prepareWriteSequence

has not been called.
**Throws:** UnsupportedOperationException

- if

canWriteSequence

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

---

#### endWriteSequence

public void endWriteSequence()
throws

IOException

Completes the writing of a sequence of images begun with

prepareWriteSequence

. Any stream metadata that
should come at the end of the sequence of images is written out,
and any header information at the beginning of the sequence is
patched up if necessary. If the output is an

ImageOutputStream

, data through the stream metadata
at the end of the sequence are flushed and need not be readable
or writable.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteSequence

returns

false

,
this method will throw an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canReplaceStreamMetadata

```java
public boolean canReplaceStreamMetadata()
throws
IOException
```

Returns

true

if it is possible to replace the
stream metadata already present in the output.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if replacement of stream metadata is
allowed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IOException

- if an I/O error occurs during the query.

---

#### canReplaceStreamMetadata

public boolean canReplaceStreamMetadata()
throws

IOException

Returns

true

if it is possible to replace the
stream metadata already present in the output.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

replaceStreamMetadata

```java
public void replaceStreamMetadata​(
IIOMetadata
streamMetadata)
throws
IOException
```

Replaces the stream metadata in the output with new
information. If the output is an

ImageOutputStream

, the prior contents of the
stream are examined and possibly edited to make room for the
new data. All of the prior contents of the output must be
available for reading and writing.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if the

canReplaceStreamMetadata

returns

false

. modes do not include
**Throws:** IOException

- if an error occurs during writing.

---

#### replaceStreamMetadata

public void replaceStreamMetadata​(

IIOMetadata

streamMetadata)
throws

IOException

Replaces the stream metadata in the output with new
information. If the output is an

ImageOutputStream

, the prior contents of the
stream are examined and possibly edited to make room for the
new data. All of the prior contents of the output must be
available for reading and writing.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canReplaceStreamMetadata

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canReplaceImageMetadata

```java
public boolean canReplaceImageMetadata​(int imageIndex)
throws
IOException
```

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

. If this method returns

false

, a call to

replaceImageMetadata(imageIndex)

will throw an

UnsupportedOperationException

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Returns:** true

if the image metadata of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image metadata replacement in general, but

imageIndex

is less than 0 or greater than the
largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

---

#### canReplaceImageMetadata

public boolean canReplaceImageMetadata​(int imageIndex)
throws

IOException

Returns

true

if it is possible to replace the
image metadata associated with an existing image with index

imageIndex

. If this method returns

false

, a call to

replaceImageMetadata(imageIndex)

will throw an

UnsupportedOperationException

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

A writer that does not support any image metadata
replacement may return

false

without performing
bounds checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

replaceImageMetadata

```java
public void replaceImageMetadata​(int imageIndex,

IIOMetadata
imageMetadata)
throws
IOException
```

Replaces the image metadata associated with an existing image.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose metadata is to
be replaced.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** UnsupportedOperationException

- if

canReplaceImageMetadata

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an error occurs during writing.

---

#### replaceImageMetadata

public void replaceImageMetadata​(int imageIndex,

IIOMetadata

imageMetadata)
throws

IOException

Replaces the image metadata associated with an existing image.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canReplaceImageMetadata(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canInsertImage

```java
public boolean canInsertImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new image at the given index. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an image may be inserted at the
given index.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image insertion in general, but

imageIndex

is less
than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

---

#### canInsertImage

public boolean canInsertImage​(int imageIndex)
throws

IOException

Returns

true

if the writer supports the insertion
of a new image at the given index. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

A writer that does not support any image insertion may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

writeInsert

```java
public void writeInsert​(int imageIndex,

IIOImage
image,

ImageWriteParam
param)
throws
IOException
```

Inserts a new image into an existing image stream. Existing
images with an index greater than

imageIndex

are
preserved, and their indices are each increased by 1. A value
for

imageIndex

of -1 may be used to signify an
index one larger than the previous largest index; that is, it
will cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** image

- an

IIOImage

object containing an
image, thumbnails, and metadata to be written.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertImage(imageIndex)

returns

false

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** UnsupportedOperationException

- if

image

contains a

Raster

and

canWriteRasters

returns

false

.
**Throws:** IOException

- if an error occurs during writing.

---

#### writeInsert

public void writeInsert​(int imageIndex,

IIOImage

image,

ImageWriteParam

param)
throws

IOException

Inserts a new image into an existing image stream. Existing
images with an index greater than

imageIndex

are
preserved, and their indices are each increased by 1. A value
for

imageIndex

of -1 may be used to signify an
index one larger than the previous largest index; that is, it
will cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canInsertImage(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canRemoveImage

```java
public boolean canRemoveImage​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the removal
of an existing image at the given index. Existing images with
indices greater than the insertion index will have
their indices decreased by 1.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Returns:** true

if it is possible to remove the given
image.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
image removal in general, but

imageIndex

is less
than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

---

#### canRemoveImage

public boolean canRemoveImage​(int imageIndex)
throws

IOException

Returns

true

if the writer supports the removal
of an existing image at the given index. Existing images with
indices greater than the insertion index will have
their indices decreased by 1.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

A writer that does not support any image removal may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

removeImage

```java
public void removeImage​(int imageIndex)
throws
IOException
```

Removes an image from the stream.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image to be removed.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canRemoveImage(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
removal.

---

#### removeImage

public void removeImage​(int imageIndex)
throws

IOException

Removes an image from the stream.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canRemoveImage(imageIndex)

returns false,
an

UnsupportedOperationException

will be thrown.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The removal may or may not cause a reduction in the actual
file size.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canWriteEmpty

```java
public boolean canWriteEmpty()
throws
IOException
```

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output. The pixel values may be defined by future
calls to the

replacePixels

methods. If the output
is an

ImageOutputStream

, its existing contents
prior to the current seek position are not affected, and need
not be readable or writable.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

**Returns:** true

if the writing of complete image
stream with contents to be defined later is supported.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IOException

- if an I/O error occurs during the
query.

---

#### canWriteEmpty

public boolean canWriteEmpty()
throws

IOException

Returns

true

if the writer supports the writing of
a complete image stream consisting of a single image with
undefined pixel values and associated metadata and thumbnails
to the output. The pixel values may be defined by future
calls to the

replacePixels

methods. If the output
is an

ImageOutputStream

, its existing contents
prior to the current seek position are not affected, and need
not be readable or writable.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

.

prepareWriteEmpty

```java
public void prepareWriteEmpty​(
IIOMetadata
streamMetadata,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output. The pixel values will
be defined by future calls to the

replacePixels

methods. If the output is an

ImageOutputStream

,
its existing contents prior to the current seek position are
not affected, and need not be readable or writable.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** streamMetadata

- an

IIOMetadata

object representing
stream metadata, or

null

to use default values.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### prepareWriteEmpty

public void prepareWriteEmpty​(

IIOMetadata

streamMetadata,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)
throws

IOException

Begins the writing of a complete image stream, consisting of a
single image with undefined pixel values and associated
metadata and thumbnails, to the output. The pixel values will
be defined by future calls to the

replacePixels

methods. If the output is an

ImageOutputStream

,
its existing contents prior to the current seek position are
not affected, and need not be readable or writable.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The writing is not complete until a call to

endWriteEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareWriteEmpty

and

endWriteEmpty

.
However, calls to

prepareWriteEmpty

cannot be
nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteEmpty

returns

false

,
an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

endWriteEmpty

```java
public void endWriteEmpty()
throws
IOException
```

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canWriteEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReiplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### endWriteEmpty

public void endWriteEmpty()
throws

IOException

Completes the writing of a new image that was begun with a
prior call to

prepareWriteEmpty

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canWriteEmpty()

returns

false

,
an

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canInsertEmpty

```java
public boolean canInsertEmpty​(int imageIndex)
throws
IOException
```

Returns

true

if the writer supports the insertion
of a new, empty image at the given index. The pixel values of
the image are undefined, and may be specified in pieces using
the

replacePixels

methods. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index at which the image is to be
inserted.
**Returns:** true

if an empty image may be inserted at
the given index.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
empty image insertion in general, but

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the
query.

---

#### canInsertEmpty

public boolean canInsertEmpty​(int imageIndex)
throws

IOException

Returns

true

if the writer supports the insertion
of a new, empty image at the given index. The pixel values of
the image are undefined, and may be specified in pieces using
the

replacePixels

methods. Existing images with
indices greater than or equal to the insertion index will have
their indices increased by 1. A value for

imageIndex

of

-1

may be used to
signify an index one larger than the current largest index.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

A writer that does not support insertion of empty images
may return

false

without performing bounds
checking on the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

prepareInsertEmpty

```java
public void prepareInsertEmpty​(int imageIndex,

ImageTypeSpecifier
imageType,
int width,
int height,

IIOMetadata
imageMetadata,

List
<? extends
BufferedImage
> thumbnails,

ImageWriteParam
param)
throws
IOException
```

Begins the insertion of a new image with undefined pixel values
into an existing image stream. Existing images with an index
greater than

imageIndex

are preserved, and their
indices are each increased by 1. A value for

imageIndex

of -1 may be used to signify an index
one larger than the previous largest index; that is, it will
cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index at which to write the image.
**Parameters:** imageType

- an

ImageTypeSpecifier

describing
the layout of the image.
**Parameters:** width

- the width of the image.
**Parameters:** height

- the height of the image.
**Parameters:** imageMetadata

- an

IIOMetadata

object
representing image metadata, or

null

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails for this image, or

null

.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than -1 or greater than the largest available index.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

has been made without a
corresponding call to

endInsertEmpty

.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

has been made without a
corresponding call to

endWriteEmpty

.
**Throws:** IllegalArgumentException

- if

imageType

is

null

or

thumbnails

contains

null

references or objects other than

BufferedImage

s.
**Throws:** IllegalArgumentException

- if width or height are less
than 1.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### prepareInsertEmpty

public void prepareInsertEmpty​(int imageIndex,

ImageTypeSpecifier

imageType,
int width,
int height,

IIOMetadata

imageMetadata,

List

<? extends

BufferedImage

> thumbnails,

ImageWriteParam

param)
throws

IOException

Begins the insertion of a new image with undefined pixel values
into an existing image stream. Existing images with an index
greater than

imageIndex

are preserved, and their
indices are each increased by 1. A value for

imageIndex

of -1 may be used to signify an index
one larger than the previous largest index; that is, it will
cause the image to be logically appended to the end of the
sequence. If the output is an

ImageOutputStream

,
the entirety of the stream must be both readable and writeable.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The image contents may be
supplied later using the

replacePixels

method.
The insertion is not complete until a call to

endInsertEmpty

occurs. Calls to

prepareReplacePixels

,

replacePixels

,
and

endReplacePixels

may occur between calls to

prepareInsertEmpty

and

endInsertEmpty

. However, calls to

prepareInsertEmpty

cannot be nested, and calls to

prepareWriteEmpty

and

prepareInsertEmpty

may not be interspersed.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canInsertEmpty(imageIndex)

returns

false

, an

UnsupportedOperationException

will be thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

endInsertEmpty

```java
public void endInsertEmpty()
throws
IOException
```

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canInsertEmpty(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if a previous call to

prepareInsertEmpty

without a corresponding call to

endInsertEmpty

has not been made.
**Throws:** IllegalStateException

- if a previous call to

prepareWriteEmpty

without a corresponding call to

endWriteEmpty

has been made.
**Throws:** IllegalStateException

- if a call to

prepareReplacePixels

has been made without a
matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### endInsertEmpty

public void endInsertEmpty()
throws

IOException

Completes the insertion of a new image that was begun with a
prior call to

prepareInsertEmpty

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

canReplacePixels

```java
public boolean canReplacePixels​(int imageIndex)
throws
IOException
```

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Returns:** true

if the pixels of the given
image can be replaced.
**Throws:** IllegalStateException

- if the output has not been
set.
**Throws:** IndexOutOfBoundsException

- if the writer supports
pixel replacement in general, but

imageIndex

is
less than 0 or greater than the largest available index.
**Throws:** IOException

- if an I/O error occurs during the query.

---

#### canReplacePixels

public boolean canReplacePixels​(int imageIndex)
throws

IOException

Returns

true

if the writer allows pixels of the
given image to be replaced using the

replacePixels

methods.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

A writer that does not support any pixel replacement may
return

false

without performing bounds checking on
the index.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise returns

false

without checking the value of

imageIndex

.

prepareReplacePixels

```java
public void prepareReplacePixels​(int imageIndex,

Rectangle
region)
throws
IOException
```

Prepares the writer to handle a series of calls to the

replacePixels

methods. The affected pixel area
will be clipped against the supplied

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** imageIndex

- the index of the image whose pixels are to be
replaced.
**Parameters:** region

- a

Rectangle

that will be used to clip
future pixel regions.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IndexOutOfBoundsException

- if

imageIndex

is less than 0 or greater than the largest available index.
**Throws:** IllegalStateException

- if there is a previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

(

i.e.

, nesting is not
allowed).
**Throws:** IllegalArgumentException

- if

region

is

null

or has a width or height less than 1.
**Throws:** IOException

- if an I/O error occurs during the
preparation.

---

#### prepareReplacePixels

public void prepareReplacePixels​(int imageIndex,

Rectangle

region)
throws

IOException

Prepares the writer to handle a series of calls to the

replacePixels

methods. The affected pixel area
will be clipped against the supplied

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

replacePixels

```java
public void replacePixels​(
RenderedImage
image,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given image. The image data must match,
or be convertible to, the image layout of the existing image.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** image

- a

RenderedImage

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- image

is

null

.

the intersected region does not contain at least one pixel.

the layout of

image

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### replacePixels

public void replacePixels​(

RenderedImage

image,

ImageWriteParam

param)
throws

IOException

Replaces a portion of an image already present in the output
with a portion of the given image. The image data must match,
or be convertible to, the image layout of the existing image.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

image

is

null

.

the intersected region does not contain at least one pixel.

the layout of

image

does not match, or this
writer cannot convert it to, the existing image layout.

replacePixels

```java
public void replacePixels​(
Raster
raster,

ImageWriteParam
param)
throws
IOException
```

Replaces a portion of an image already present in the output
with a portion of the given

Raster

. The image
data must match, or be convertible to, the image layout of the
existing image.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Parameters:** raster

- a

Raster

containing source
pixels.
**Parameters:** param

- an

ImageWriteParam

, or

null

to use a default

ImageWriteParam

.
**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** UnsupportedOperationException

- if

canWriteRasters

returns

false

.
**Throws:** IllegalArgumentException

- if any of the following are true:

- raster

is

null

.

the intersected region does not contain at least one pixel.

the layout of

raster

does not match, or this
writer cannot convert it to, the existing image layout.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### replacePixels

public void replacePixels​(

Raster

raster,

ImageWriteParam

param)
throws

IOException

Replaces a portion of an image already present in the output
with a portion of the given

Raster

. The image
data must match, or be convertible to, the image layout of the
existing image.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

An

ImageWriteParam

may optionally be supplied
to control the writing process. If

param

is

null

, a default write param will be used.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The destination region is specified in the

param

argument, and will be clipped to the image
boundaries and the region supplied to

prepareReplacePixels

. At least one pixel of the
source must not be clipped, or an exception is thrown.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If the supplied

ImageWriteParam

contains
optional setting values not supported by this writer (

e.g.

progressive encoding or any format-specific settings), they
will be ignored.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

This method may only be called after a call to

prepareReplacePixels

, or else an

IllegalStateException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

raster

is

null

.

the intersected region does not contain at least one pixel.

the layout of

raster

does not match, or this
writer cannot convert it to, the existing image layout.

endReplacePixels

```java
public void endReplacePixels()
throws
IOException
```

Terminates a sequence of calls to

replacePixels

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

**Throws:** IllegalStateException

- if the output has not
been set.
**Throws:** UnsupportedOperationException

- if

canReplacePixels(imageIndex)

returns

false

.
**Throws:** IllegalStateException

- if there is no previous call
to

prepareReplacePixels

without a matching call to

endReplacePixels

.
**Throws:** IOException

- if an I/O error occurs during writing.

---

#### endReplacePixels

public void endReplacePixels()
throws

IOException

Terminates a sequence of calls to

replacePixels

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

If

canReplacePixels

returns

false

, and

UnsupportedOperationException

will be thrown.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

The default implementation throws an

IllegalStateException

if the output is

null

, and otherwise throws an

UnsupportedOperationException

.

abort

```java
public void abort()
```

Requests that any current write operation be aborted. The
contents of the output following the abort will be undefined.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

---

#### abort

public void abort()

Requests that any current write operation be aborted. The
contents of the output following the abort will be undefined.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

Writers should call

clearAbortRequest

at the
beginning of each write operation, and poll the value of

abortRequested

regularly during the write.

abortRequested

```java
protected boolean abortRequested()
```

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

**Returns:** true

if the current write operation should
be aborted.
**See Also:** abort()

,

clearAbortRequest()

---

#### abortRequested

protected boolean abortRequested()

Returns

true

if a request to abort the current
write operation has been made since the writer was instantiated or

clearAbortRequest

was called.

clearAbortRequest

```java
protected void clearAbortRequest()
```

Clears any previous abort request. After this method has been
called,

abortRequested

will return

false

.

**See Also:** abort()

,

abortRequested()

---

#### clearAbortRequest

protected void clearAbortRequest()

Clears any previous abort request. After this method has been
called,

abortRequested

will return

false

.

addIIOWriteWarningListener

```java
public void addIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken. Messages sent to the given listener will be
localized, if possible, to match the current

Locale

. If no

Locale

has been set,
warning messages may be localized as the writer sees fit.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
registered.
**See Also:** removeIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

---

#### addIIOWriteWarningListener

public void addIIOWriteWarningListener​(

IIOWriteWarningListener

listener)

Adds an

IIOWriteWarningListener

to the list of
registered warning listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken. Messages sent to the given listener will be
localized, if possible, to match the current

Locale

. If no

Locale

has been set,
warning messages may be localized as the writer sees fit.

removeIIOWriteWarningListener

```java
public void removeIIOWriteWarningListener​(
IIOWriteWarningListener
listener)
```

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteWarningListener

to be
deregistered.
**See Also:** addIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

---

#### removeIIOWriteWarningListener

public void removeIIOWriteWarningListener​(

IIOWriteWarningListener

listener)

Removes an

IIOWriteWarningListener

from the list
of registered warning listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

removeAllIIOWriteWarningListeners

```java
public void removeAllIIOWriteWarningListeners()
```

Removes all currently registered

IIOWriteWarningListener

objects.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

---

#### removeAllIIOWriteWarningListeners

public void removeAllIIOWriteWarningListeners()

Removes all currently registered

IIOWriteWarningListener

objects.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

The default implementation sets the

warningListeners

and

warningLocales

instance variables to

null

.

addIIOWriteProgressListener

```java
public void addIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
registered.
**See Also:** removeIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

---

#### addIIOWriteProgressListener

public void addIIOWriteProgressListener​(

IIOWriteProgressListener

listener)

Adds an

IIOWriteProgressListener

to the list of
registered progress listeners. If

listener

is

null

, no exception will be thrown and no action
will be taken.

removeIIOWriteProgressListener

```java
public void removeIIOWriteProgressListener​(
IIOWriteProgressListener
listener)
```

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

**Parameters:** listener

- an

IIOWriteProgressListener

to be
deregistered.
**See Also:** addIIOWriteProgressListener(javax.imageio.event.IIOWriteProgressListener)

---

#### removeIIOWriteProgressListener

public void removeIIOWriteProgressListener​(

IIOWriteProgressListener

listener)

Removes an

IIOWriteProgressListener

from the list
of registered progress listeners. If the listener was not
previously registered, or if

listener

is

null

, no exception will be thrown and no action
will be taken.

removeAllIIOWriteProgressListeners

```java
public void removeAllIIOWriteProgressListeners()
```

Removes all currently registered

IIOWriteProgressListener

objects.

The default implementation sets the

progressListeners

instance variable to

null

.

---

#### removeAllIIOWriteProgressListeners

public void removeAllIIOWriteProgressListeners()

Removes all currently registered

IIOWriteProgressListener

objects.

The default implementation sets the

progressListeners

instance variable to

null

.

The default implementation sets the

progressListeners

instance variable to

null

.

processImageStarted

```java
protected void processImageStarted​(int imageIndex)
```

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image about to be written.

---

#### processImageStarted

protected void processImageStarted​(int imageIndex)

Broadcasts the start of an image write to all registered

IIOWriteProgressListener

s by calling their

imageStarted

method. Subclasses may use this
method as a convenience.

processImageProgress

```java
protected void processImageProgress​(float percentageDone)
```

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method. Subclasses may use
this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

---

#### processImageProgress

protected void processImageProgress​(float percentageDone)

Broadcasts the current percentage of image completion to all
registered

IIOWriteProgressListener

s by calling
their

imageProgress

method. Subclasses may use
this method as a convenience.

processImageComplete

```java
protected void processImageComplete()
```

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method. Subclasses may use this
method as a convenience.

---

#### processImageComplete

protected void processImageComplete()

Broadcasts the completion of an image write to all registered

IIOWriteProgressListener

s by calling their

imageComplete

method. Subclasses may use this
method as a convenience.

processThumbnailStarted

```java
protected void processThumbnailStarted​(int imageIndex,
int thumbnailIndex)
```

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image associated with the
thumbnail.
**Parameters:** thumbnailIndex

- the index of the thumbnail.

---

#### processThumbnailStarted

protected void processThumbnailStarted​(int imageIndex,
int thumbnailIndex)

Broadcasts the start of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailStarted

method. Subclasses may use this
method as a convenience.

processThumbnailProgress

```java
protected void processThumbnailProgress​(float percentageDone)
```

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method. Subclasses may
use this method as a convenience.

**Parameters:** percentageDone

- the current percentage of completion,
as a

float

.

---

#### processThumbnailProgress

protected void processThumbnailProgress​(float percentageDone)

Broadcasts the current percentage of thumbnail completion to
all registered

IIOWriteProgressListener

s by calling
their

thumbnailProgress

method. Subclasses may
use this method as a convenience.

processThumbnailComplete

```java
protected void processThumbnailComplete()
```

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method. Subclasses may use this
method as a convenience.

---

#### processThumbnailComplete

protected void processThumbnailComplete()

Broadcasts the completion of a thumbnail write to all registered

IIOWriteProgressListener

s by calling their

thumbnailComplete

method. Subclasses may use this
method as a convenience.

processWriteAborted

```java
protected void processWriteAborted()
```

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method. Subclasses may use this
method as a convenience.

---

#### processWriteAborted

protected void processWriteAborted()

Broadcasts that the write has been aborted to all registered

IIOWriteProgressListener

s by calling their

writeAborted

method. Subclasses may use this
method as a convenience.

processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
warning)
```

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** warning

- the warning message.
**Throws:** IllegalArgumentException

- if

warning

is

null

.

---

#### processWarningOccurred

protected void processWarningOccurred​(int imageIndex,

String

warning)

Broadcasts a warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method. Subclasses may use this
method as a convenience.

processWarningOccurred

```java
protected void processWarningOccurred​(int imageIndex,

String
baseName,

String
keyword)
```

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

. Subclasses may use this
method as a convenience.

**Parameters:** imageIndex

- the index of the image on which the warning
occurred.
**Parameters:** baseName

- the base name of a set of

ResourceBundle

s containing localized warning
messages.
**Parameters:** keyword

- the keyword used to index the warning message
within the set of

ResourceBundle

s.
**Throws:** IllegalArgumentException

- if

baseName

is

null

.
**Throws:** IllegalArgumentException

- if

keyword

is

null

.
**Throws:** IllegalArgumentException

- if no appropriate

ResourceBundle

may be located.
**Throws:** IllegalArgumentException

- if the named resource is
not found in the located

ResourceBundle

.
**Throws:** IllegalArgumentException

- if the object retrieved
from the

ResourceBundle

is not a

String

.

---

#### processWarningOccurred

protected void processWarningOccurred​(int imageIndex,

String

baseName,

String

keyword)

Broadcasts a localized warning message to all registered

IIOWriteWarningListener

s by calling their

warningOccurred

method with a string taken
from a

ResourceBundle

. Subclasses may use this
method as a convenience.

reset

```java
public void reset()
```

Restores the

ImageWriter

to its initial state.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

---

#### reset

public void reset()

Restores the

ImageWriter

to its initial state.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

The default implementation calls

setOutput(null)

,

setLocale(null)

,

removeAllIIOWriteWarningListeners()

,

removeAllIIOWriteProgressListeners()

, and

clearAbortRequest

.

dispose

```java
public void dispose()
```

Allows any resources held by this object to be released. The
result of calling any other method (other than

finalize

) subsequent to a call to this method
is undefined.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

---

#### dispose

public void dispose()

Allows any resources held by this object to be released. The
result of calling any other method (other than

finalize

) subsequent to a call to this method
is undefined.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

It is important for applications to call this method when they
know they will no longer be using this

ImageWriter

.
Otherwise, the writer may continue to hold on to resources
indefinitely.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

The default implementation of this method in the superclass does
nothing. Subclass implementations should ensure that all resources,
especially native resources, are released.

---

