# Class ImageIO

**Source:** `java.desktop\javax\imageio\ImageIO.html`

### Class Description

```java
public final class
ImageIO

extends
Object
```

A class containing static convenience methods for locating

ImageReader

s and

ImageWriter

s, and
performing simple encoding and decoding.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static void scanForPlugins()

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

**See Also:**
- ClassLoader.getResources(java.lang.String)

---

#### public static void setUseCache​(boolean useCache)

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

**Parameters:**
- useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.

**See Also:**
- getUseCache()

---

#### public static boolean getUseCache()

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

**Returns:**
- true if a disk-based cache may be used for

ImageInputStream

s and

ImageOutputStream

s.

**See Also:**
- setUseCache(boolean)

---

#### public static void setCacheDirectory​(
File
cacheDirectory)

Sets the directory where cache files are to be created. A
value of

null

indicates that the system-dependent
default temporary-file directory is to be used. If

getUseCache

returns false, this value is ignored.

**Parameters:**
- cacheDirectory

- a

File

specifying a directory.

**Throws:**
- SecurityException

- if the security manager denies
access to the directory.
- IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.

**See Also:**
- File.createTempFile(String, String, File)

,

getCacheDirectory()

---

#### public static
File
getCacheDirectory()

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

**Returns:**
- a

File

indicating the directory where
cache files will be created, or

null

to indicate
the system-dependent default temporary-file directory.

**See Also:**
- setCacheDirectory(java.io.File)

---

#### public static
ImageInputStream
createImageInputStream​(
Object
input)
throws
IOException

Returns an

ImageInputStream

that will take its
input from the given

Object

. The set of

ImageInputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to take input from the supplied object is used to
create the returned

ImageInputStream

. If no
suitable

ImageInputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:**
- input

- an

Object

to be used as an input
source, such as a

File

, readable

RandomAccessFile

, or

InputStream

.

**Returns:**
- an

ImageInputStream

, or

null

.

**Throws:**
- IllegalArgumentException

- if

input

is

null

.
- IOException

- if a cache file is needed but cannot be
created.

**See Also:**
- ImageInputStreamSpi

---

#### public static
ImageOutputStream
createImageOutputStream​(
Object
output)
throws
IOException

Returns an

ImageOutputStream

that will send its
output to the given

Object

. The set of

ImageOutputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to send output from the supplied object is used to
create the returned

ImageOutputStream

. If no
suitable

ImageOutputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:**
- output

- an

Object

to be used as an output
destination, such as a

File

, writable

RandomAccessFile

, or

OutputStream

.

**Returns:**
- an

ImageOutputStream

, or

null

.

**Throws:**
- IllegalArgumentException

- if

output

is

null

.
- IOException

- if a cache file is needed but cannot be
created.

**See Also:**
- ImageOutputStreamSpi

---

#### public static
String
[] getReaderFormatNames()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

**Returns:**
- an array of

String

s.

---

#### public static
String
[] getReaderMIMETypes()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

**Returns:**
- an array of

String

s.

---

#### public static
String
[] getReaderFileSuffixes()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

**Returns:**
- an array of

String

s.

**Since:**
- 1.6

---

#### public static
Iterator
<
ImageReader
> getImageReaders​(
Object
input)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

The stream position is left at its prior position upon
exit from this method.

**Parameters:**
- input

- an

ImageInputStream

or other

Object

containing encoded image data.

**Returns:**
- an

Iterator

containing

ImageReader

s.

**Throws:**
- IllegalArgumentException

- if

input

is

null

.

**See Also:**
- ImageReaderSpi.canDecodeInput(java.lang.Object)

---

#### public static
Iterator
<
ImageReader
> getImageReadersByFormatName​(
String
formatName)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

**Parameters:**
- formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".

**Returns:**
- an

Iterator

containing

ImageReader

s.

**Throws:**
- IllegalArgumentException

- if

formatName

is

null

.

**See Also:**
- ImageReaderWriterSpi.getFormatNames()

---

#### public static
Iterator
<
ImageReader
> getImageReadersBySuffix​(
String
fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

**Parameters:**
- fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").

**Returns:**
- an

Iterator

containing

ImageReader

s.

**Throws:**
- IllegalArgumentException

- if

fileSuffix

is

null

.

**See Also:**
- ImageReaderWriterSpi.getFileSuffixes()

---

#### public static
Iterator
<
ImageReader
> getImageReadersByMIMEType​(
String
MIMEType)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

**Parameters:**
- MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").

**Returns:**
- an

Iterator

containing

ImageReader

s.

**Throws:**
- IllegalArgumentException

- if

MIMEType

is

null

.

**See Also:**
- ImageReaderWriterSpi.getMIMETypes()

---

#### public static
String
[] getWriterFormatNames()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

**Returns:**
- an array of

String

s.

---

#### public static
String
[] getWriterMIMETypes()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

**Returns:**
- an array of

String

s.

---

#### public static
String
[] getWriterFileSuffixes()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

**Returns:**
- an array of

String

s.

**Since:**
- 1.6

---

#### public static
Iterator
<
ImageWriter
> getImageWritersByFormatName​(
String
formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

**Parameters:**
- formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".

**Returns:**
- an

Iterator

containing

ImageWriter

s.

**Throws:**
- IllegalArgumentException

- if

formatName

is

null

.

**See Also:**
- ImageReaderWriterSpi.getFormatNames()

---

#### public static
Iterator
<
ImageWriter
> getImageWritersBySuffix​(
String
fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

**Parameters:**
- fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").

**Returns:**
- an

Iterator

containing

ImageWriter

s.

**Throws:**
- IllegalArgumentException

- if

fileSuffix

is

null

.

**See Also:**
- ImageReaderWriterSpi.getFileSuffixes()

---

#### public static
Iterator
<
ImageWriter
> getImageWritersByMIMEType​(
String
MIMEType)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

**Parameters:**
- MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").

**Returns:**
- an

Iterator

containing

ImageWriter

s.

**Throws:**
- IllegalArgumentException

- if

MIMEType

is

null

.

**See Also:**
- ImageReaderWriterSpi.getMIMETypes()

---

#### public static
ImageWriter
getImageWriter​(
ImageReader
reader)

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered. This
mechanism may be used to obtain an

ImageWriter

that will understand the internal structure of non-pixel
metadata (as encoded by

IIOMetadata

objects)
generated by the

ImageReader

. By obtaining this
data from the

ImageReader

and passing it on to the

ImageWriter

obtained with this method, a client
program can read an image, modify it in some way, and write it
back out preserving all metadata, without having to understand
anything about the structure of the metadata, or even about
the image format. Note that this method returns the
"preferred" writer, which is the first in the list returned by

javax.imageio.spi.ImageReaderSpi.getImageWriterSpiNames()

.

**Parameters:**
- reader

- an instance of a registered

ImageReader

.

**Returns:**
- an

ImageWriter

, or null.

**Throws:**
- IllegalArgumentException

- if

reader

is

null

.

**See Also:**
- getImageReader(ImageWriter)

,

ImageReaderSpi.getImageWriterSpiNames()

---

#### public static
ImageReader
getImageReader​(
ImageWriter
writer)

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered. This method
is provided principally for symmetry with

getImageWriter(ImageReader)

. Note that this
method returns the "preferred" reader, which is the first in
the list returned by
javax.imageio.spi.ImageWriterSpi.

getImageReaderSpiNames()

.

**Parameters:**
- writer

- an instance of a registered

ImageWriter

.

**Returns:**
- an

ImageReader

, or null.

**Throws:**
- IllegalArgumentException

- if

writer

is

null

.

**See Also:**
- getImageWriter(ImageReader)

,

ImageWriterSpi.getImageReaderSpiNames()

---

#### public static
Iterator
<
ImageWriter
> getImageWriters​(
ImageTypeSpecifier
type,

String
formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

**Parameters:**
- type

- an

ImageTypeSpecifier

indicating the
layout of the image to be written.
- formatName

- the informal name of the

format

.

**Returns:**
- an

Iterator

containing

ImageWriter

s.

**Throws:**
- IllegalArgumentException

- if any parameter is

null

.

**See Also:**
- ImageWriterSpi.canEncodeImage(ImageTypeSpecifier)

---

#### public static
Iterator
<
ImageTranscoder
> getImageTranscoders​(
ImageReader
reader,

ImageWriter
writer)

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

**Parameters:**
- reader

- an

ImageReader

.
- writer

- an

ImageWriter

.

**Returns:**
- an

Iterator

containing

ImageTranscoder

s.

**Throws:**
- IllegalArgumentException

- if

reader

or

writer

is

null

.

---

#### public static
BufferedImage
read​(
File
input)
throws
IOException

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.
The

File

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:**
- input

- a

File

to read from.

**Returns:**
- a

BufferedImage

containing the decoded
contents of the input, or

null

.

**Throws:**
- IllegalArgumentException

- if

input

is

null

.
- IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### public static
BufferedImage
read​(
InputStream
input)
throws
IOException

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.
The

InputStream

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:**
- input

- an

InputStream

to read from.

**Returns:**
- a

BufferedImage

containing the decoded
contents of the input, or

null

.

**Throws:**
- IllegalArgumentException

- if

input

is

null

.
- IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### public static
BufferedImage
read​(
URL
input)
throws
IOException

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered. An

InputStream

is obtained from the

URL

,
which is wrapped in an

ImageInputStream

. If no
registered

ImageReader

claims to be able to read
the resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:**
- input

- a

URL

to read from.

**Returns:**
- a

BufferedImage

containing the decoded
contents of the input, or

null

.

**Throws:**
- IllegalArgumentException

- if

input

is

null

.
- IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### public static
BufferedImage
read​(
ImageInputStream
stream)
throws
IOException

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered. If no registered

ImageReader

claims to be able to read the stream,

null

is returned.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

**Parameters:**
- stream

- an

ImageInputStream

to read from.

**Returns:**
- a

BufferedImage

containing the decoded
contents of the input, or

null

.

**Throws:**
- IllegalArgumentException

- if

stream

is

null

.
- IOException

- if an error occurs during reading.

---

#### public static boolean write​(
RenderedImage
im,

String
formatName,

ImageOutputStream
output)
throws
IOException

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

. The image is written to the

ImageOutputStream

starting at the current stream
pointer, overwriting existing stream data from that point
forward, if present.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:**
- im

- a

RenderedImage

to be written.
- formatName

- a

String

containing the informal
name of the format.
- output

- an

ImageOutputStream

to be written to.

**Returns:**
- false

if no appropriate writer is found.

**Throws:**
- IllegalArgumentException

- if any parameter is

null

.
- IOException

- if an error occurs during writing.

---

#### public static boolean write​(
RenderedImage
im,

String
formatName,

File
output)
throws
IOException

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

. If
there is already a

File

present, its contents are
discarded.

**Parameters:**
- im

- a

RenderedImage

to be written.
- formatName

- a

String

containing the informal
name of the format.
- output

- a

File

to be written to.

**Returns:**
- false

if no appropriate writer is found.

**Throws:**
- IllegalArgumentException

- if any parameter is

null

.
- IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

---

#### public static boolean write​(
RenderedImage
im,

String
formatName,

OutputStream
output)
throws
IOException

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:**
- im

- a

RenderedImage

to be written.
- formatName

- a

String

containing the informal
name of the format.
- output

- an

OutputStream

to be written to.

**Returns:**
- false

if no appropriate writer is found.

**Throws:**
- IllegalArgumentException

- if any parameter is

null

.
- IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

---

### Additional Sections

#### Class ImageIO

java.lang.Object

- javax.imageio.ImageIO

javax.imageio.ImageIO

```java
public final class
ImageIO

extends
Object
```

A class containing static convenience methods for locating

ImageReader

s and

ImageWriter

s, and
performing simple encoding and decoding.

public final class

ImageIO

extends

Object

A class containing static convenience methods for locating

ImageReader

s and

ImageWriter

s, and
performing simple encoding and decoding.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ImageInputStream

createImageInputStream

​(

Object

input)

Returns an

ImageInputStream

that will take its
input from the given

Object

.

static

ImageOutputStream

createImageOutputStream

​(

Object

output)

Returns an

ImageOutputStream

that will send its
output to the given

Object

.

static

File

getCacheDirectory

()

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

static

ImageReader

getImageReader

​(

ImageWriter

writer)

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered.

static

Iterator

<

ImageReader

>

getImageReaders

​(

Object

input)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

static

Iterator

<

ImageReader

>

getImageReadersByFormatName

​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

static

Iterator

<

ImageReader

>

getImageReadersByMIMEType

​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

static

Iterator

<

ImageReader

>

getImageReadersBySuffix

​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

static

Iterator

<

ImageTranscoder

>

getImageTranscoders

​(

ImageReader

reader,

ImageWriter

writer)

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

static

ImageWriter

getImageWriter

​(

ImageReader

reader)

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered.

static

Iterator

<

ImageWriter

>

getImageWriters

​(

ImageTypeSpecifier

type,

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

static

Iterator

<

ImageWriter

>

getImageWritersByFormatName

​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

static

Iterator

<

ImageWriter

>

getImageWritersByMIMEType

​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

static

Iterator

<

ImageWriter

>

getImageWritersBySuffix

​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

static

String

[]

getReaderFileSuffixes

()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

static

String

[]

getReaderFormatNames

()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

static

String

[]

getReaderMIMETypes

()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

static boolean

getUseCache

()

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

static

String

[]

getWriterFileSuffixes

()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

static

String

[]

getWriterFormatNames

()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

static

String

[]

getWriterMIMETypes

()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

static

BufferedImage

read

​(

File

input)

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

InputStream

input)

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

URL

input)

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

ImageInputStream

stream)

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered.

static void

scanForPlugins

()

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

static void

setCacheDirectory

​(

File

cacheDirectory)

Sets the directory where cache files are to be created.

static void

setUseCache

​(boolean useCache)

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

static boolean

write

​(

RenderedImage

im,

String

formatName,

File

output)

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

.

static boolean

write

​(

RenderedImage

im,

String

formatName,

OutputStream

output)

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

static boolean

write

​(

RenderedImage

im,

String

formatName,

ImageOutputStream

output)

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ImageInputStream

createImageInputStream

​(

Object

input)

Returns an

ImageInputStream

that will take its
input from the given

Object

.

static

ImageOutputStream

createImageOutputStream

​(

Object

output)

Returns an

ImageOutputStream

that will send its
output to the given

Object

.

static

File

getCacheDirectory

()

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

static

ImageReader

getImageReader

​(

ImageWriter

writer)

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered.

static

Iterator

<

ImageReader

>

getImageReaders

​(

Object

input)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

static

Iterator

<

ImageReader

>

getImageReadersByFormatName

​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

static

Iterator

<

ImageReader

>

getImageReadersByMIMEType

​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

static

Iterator

<

ImageReader

>

getImageReadersBySuffix

​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

static

Iterator

<

ImageTranscoder

>

getImageTranscoders

​(

ImageReader

reader,

ImageWriter

writer)

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

static

ImageWriter

getImageWriter

​(

ImageReader

reader)

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered.

static

Iterator

<

ImageWriter

>

getImageWriters

​(

ImageTypeSpecifier

type,

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

static

Iterator

<

ImageWriter

>

getImageWritersByFormatName

​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

static

Iterator

<

ImageWriter

>

getImageWritersByMIMEType

​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

static

Iterator

<

ImageWriter

>

getImageWritersBySuffix

​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

static

String

[]

getReaderFileSuffixes

()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

static

String

[]

getReaderFormatNames

()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

static

String

[]

getReaderMIMETypes

()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

static boolean

getUseCache

()

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

static

String

[]

getWriterFileSuffixes

()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

static

String

[]

getWriterFormatNames

()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

static

String

[]

getWriterMIMETypes

()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

static

BufferedImage

read

​(

File

input)

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

InputStream

input)

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

URL

input)

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered.

static

BufferedImage

read

​(

ImageInputStream

stream)

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered.

static void

scanForPlugins

()

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

static void

setCacheDirectory

​(

File

cacheDirectory)

Sets the directory where cache files are to be created.

static void

setUseCache

​(boolean useCache)

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

static boolean

write

​(

RenderedImage

im,

String

formatName,

File

output)

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

.

static boolean

write

​(

RenderedImage

im,

String

formatName,

OutputStream

output)

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

static boolean

write

​(

RenderedImage

im,

String

formatName,

ImageOutputStream

output)

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

.

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

Returns an

ImageInputStream

that will take its
input from the given

Object

.

Returns an

ImageOutputStream

that will send its
output to the given

Object

.

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered.

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered.

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered.

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered.

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

Sets the directory where cache files are to be created.

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

.

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

.

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

============ METHOD DETAIL ==========

- Method Detail

- scanForPlugins

```java
public static void scanForPlugins()
```

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

**See Also:** ClassLoader.getResources(java.lang.String)

- setUseCache

```java
public static void setUseCache​(boolean useCache)
```

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**See Also:** getUseCache()

- getUseCache

```java
public static boolean getUseCache()
```

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

**Returns:** true if a disk-based cache may be used for

ImageInputStream

s and

ImageOutputStream

s.
**See Also:** setUseCache(boolean)

- setCacheDirectory

```java
public static void setCacheDirectory​(
File
cacheDirectory)
```

Sets the directory where cache files are to be created. A
value of

null

indicates that the system-dependent
default temporary-file directory is to be used. If

getUseCache

returns false, this value is ignored.

**Parameters:** cacheDirectory

- a

File

specifying a directory.
**Throws:** SecurityException

- if the security manager denies
access to the directory.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**See Also:** File.createTempFile(String, String, File)

,

getCacheDirectory()

- getCacheDirectory

```java
public static
File
getCacheDirectory()
```

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

**Returns:** a

File

indicating the directory where
cache files will be created, or

null

to indicate
the system-dependent default temporary-file directory.
**See Also:** setCacheDirectory(java.io.File)

- createImageInputStream

```java
public static
ImageInputStream
createImageInputStream​(
Object
input)
throws
IOException
```

Returns an

ImageInputStream

that will take its
input from the given

Object

. The set of

ImageInputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to take input from the supplied object is used to
create the returned

ImageInputStream

. If no
suitable

ImageInputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** input

- an

Object

to be used as an input
source, such as a

File

, readable

RandomAccessFile

, or

InputStream

.
**Returns:** an

ImageInputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageInputStreamSpi

- createImageOutputStream

```java
public static
ImageOutputStream
createImageOutputStream​(
Object
output)
throws
IOException
```

Returns an

ImageOutputStream

that will send its
output to the given

Object

. The set of

ImageOutputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to send output from the supplied object is used to
create the returned

ImageOutputStream

. If no
suitable

ImageOutputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** output

- an

Object

to be used as an output
destination, such as a

File

, writable

RandomAccessFile

, or

OutputStream

.
**Returns:** an

ImageOutputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

output

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageOutputStreamSpi

- getReaderFormatNames

```java
public static
String
[] getReaderFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

**Returns:** an array of

String

s.

- getReaderMIMETypes

```java
public static
String
[] getReaderMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

**Returns:** an array of

String

s.

- getReaderFileSuffixes

```java
public static
String
[] getReaderFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

**Returns:** an array of

String

s.
**Since:** 1.6

- getImageReaders

```java
public static
Iterator
<
ImageReader
> getImageReaders​(
Object
input)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

The stream position is left at its prior position upon
exit from this method.

**Parameters:** input

- an

ImageInputStream

or other

Object

containing encoded image data.
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**See Also:** ImageReaderSpi.canDecodeInput(java.lang.Object)

- getImageReadersByFormatName

```java
public static
Iterator
<
ImageReader
> getImageReadersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

- getImageReadersBySuffix

```java
public static
Iterator
<
ImageReader
> getImageReadersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

- getImageReadersByMIMEType

```java
public static
Iterator
<
ImageReader
> getImageReadersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

- getWriterFormatNames

```java
public static
String
[] getWriterFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

**Returns:** an array of

String

s.

- getWriterMIMETypes

```java
public static
String
[] getWriterMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

**Returns:** an array of

String

s.

- getWriterFileSuffixes

```java
public static
String
[] getWriterFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

**Returns:** an array of

String

s.
**Since:** 1.6

- getImageWritersByFormatName

```java
public static
Iterator
<
ImageWriter
> getImageWritersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

- getImageWritersBySuffix

```java
public static
Iterator
<
ImageWriter
> getImageWritersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

- getImageWritersByMIMEType

```java
public static
Iterator
<
ImageWriter
> getImageWritersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

- getImageWriter

```java
public static
ImageWriter
getImageWriter​(
ImageReader
reader)
```

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered. This
mechanism may be used to obtain an

ImageWriter

that will understand the internal structure of non-pixel
metadata (as encoded by

IIOMetadata

objects)
generated by the

ImageReader

. By obtaining this
data from the

ImageReader

and passing it on to the

ImageWriter

obtained with this method, a client
program can read an image, modify it in some way, and write it
back out preserving all metadata, without having to understand
anything about the structure of the metadata, or even about
the image format. Note that this method returns the
"preferred" writer, which is the first in the list returned by

javax.imageio.spi.ImageReaderSpi.getImageWriterSpiNames()

.

**Parameters:** reader

- an instance of a registered

ImageReader

.
**Returns:** an

ImageWriter

, or null.
**Throws:** IllegalArgumentException

- if

reader

is

null

.
**See Also:** getImageReader(ImageWriter)

,

ImageReaderSpi.getImageWriterSpiNames()

- getImageReader

```java
public static
ImageReader
getImageReader​(
ImageWriter
writer)
```

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered. This method
is provided principally for symmetry with

getImageWriter(ImageReader)

. Note that this
method returns the "preferred" reader, which is the first in
the list returned by
javax.imageio.spi.ImageWriterSpi.

getImageReaderSpiNames()

.

**Parameters:** writer

- an instance of a registered

ImageWriter

.
**Returns:** an

ImageReader

, or null.
**Throws:** IllegalArgumentException

- if

writer

is

null

.
**See Also:** getImageWriter(ImageReader)

,

ImageWriterSpi.getImageReaderSpiNames()

- getImageWriters

```java
public static
Iterator
<
ImageWriter
> getImageWriters​(
ImageTypeSpecifier
type,

String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

**Parameters:** type

- an

ImageTypeSpecifier

indicating the
layout of the image to be written.
**Parameters:** formatName

- the informal name of the

format

.
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**See Also:** ImageWriterSpi.canEncodeImage(ImageTypeSpecifier)

- getImageTranscoders

```java
public static
Iterator
<
ImageTranscoder
> getImageTranscoders​(
ImageReader
reader,

ImageWriter
writer)
```

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

**Parameters:** reader

- an

ImageReader

.
**Parameters:** writer

- an

ImageWriter

.
**Returns:** an

Iterator

containing

ImageTranscoder

s.
**Throws:** IllegalArgumentException

- if

reader

or

writer

is

null

.

- read

```java
public static
BufferedImage
read​(
File
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.
The

File

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

File

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
InputStream
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.
The

InputStream

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** input

- an

InputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
URL
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered. An

InputStream

is obtained from the

URL

,
which is wrapped in an

ImageInputStream

. If no
registered

ImageReader

claims to be able to read
the resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

URL

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
ImageInputStream
stream)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered. If no registered

ImageReader

claims to be able to read the stream,

null

is returned.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

**Parameters:** stream

- an

ImageInputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IOException

- if an error occurs during reading.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

ImageOutputStream
output)
throws
IOException
```

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

. The image is written to the

ImageOutputStream

starting at the current stream
pointer, overwriting existing stream data from that point
forward, if present.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

ImageOutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

File
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

. If
there is already a

File

present, its contents are
discarded.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- a

File

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

OutputStream
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

OutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

Method Detail

- scanForPlugins

```java
public static void scanForPlugins()
```

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

**See Also:** ClassLoader.getResources(java.lang.String)

- setUseCache

```java
public static void setUseCache​(boolean useCache)
```

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**See Also:** getUseCache()

- getUseCache

```java
public static boolean getUseCache()
```

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

**Returns:** true if a disk-based cache may be used for

ImageInputStream

s and

ImageOutputStream

s.
**See Also:** setUseCache(boolean)

- setCacheDirectory

```java
public static void setCacheDirectory​(
File
cacheDirectory)
```

Sets the directory where cache files are to be created. A
value of

null

indicates that the system-dependent
default temporary-file directory is to be used. If

getUseCache

returns false, this value is ignored.

**Parameters:** cacheDirectory

- a

File

specifying a directory.
**Throws:** SecurityException

- if the security manager denies
access to the directory.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**See Also:** File.createTempFile(String, String, File)

,

getCacheDirectory()

- getCacheDirectory

```java
public static
File
getCacheDirectory()
```

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

**Returns:** a

File

indicating the directory where
cache files will be created, or

null

to indicate
the system-dependent default temporary-file directory.
**See Also:** setCacheDirectory(java.io.File)

- createImageInputStream

```java
public static
ImageInputStream
createImageInputStream​(
Object
input)
throws
IOException
```

Returns an

ImageInputStream

that will take its
input from the given

Object

. The set of

ImageInputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to take input from the supplied object is used to
create the returned

ImageInputStream

. If no
suitable

ImageInputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** input

- an

Object

to be used as an input
source, such as a

File

, readable

RandomAccessFile

, or

InputStream

.
**Returns:** an

ImageInputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageInputStreamSpi

- createImageOutputStream

```java
public static
ImageOutputStream
createImageOutputStream​(
Object
output)
throws
IOException
```

Returns an

ImageOutputStream

that will send its
output to the given

Object

. The set of

ImageOutputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to send output from the supplied object is used to
create the returned

ImageOutputStream

. If no
suitable

ImageOutputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** output

- an

Object

to be used as an output
destination, such as a

File

, writable

RandomAccessFile

, or

OutputStream

.
**Returns:** an

ImageOutputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

output

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageOutputStreamSpi

- getReaderFormatNames

```java
public static
String
[] getReaderFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

**Returns:** an array of

String

s.

- getReaderMIMETypes

```java
public static
String
[] getReaderMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

**Returns:** an array of

String

s.

- getReaderFileSuffixes

```java
public static
String
[] getReaderFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

**Returns:** an array of

String

s.
**Since:** 1.6

- getImageReaders

```java
public static
Iterator
<
ImageReader
> getImageReaders​(
Object
input)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

The stream position is left at its prior position upon
exit from this method.

**Parameters:** input

- an

ImageInputStream

or other

Object

containing encoded image data.
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**See Also:** ImageReaderSpi.canDecodeInput(java.lang.Object)

- getImageReadersByFormatName

```java
public static
Iterator
<
ImageReader
> getImageReadersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

- getImageReadersBySuffix

```java
public static
Iterator
<
ImageReader
> getImageReadersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

- getImageReadersByMIMEType

```java
public static
Iterator
<
ImageReader
> getImageReadersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

- getWriterFormatNames

```java
public static
String
[] getWriterFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

**Returns:** an array of

String

s.

- getWriterMIMETypes

```java
public static
String
[] getWriterMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

**Returns:** an array of

String

s.

- getWriterFileSuffixes

```java
public static
String
[] getWriterFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

**Returns:** an array of

String

s.
**Since:** 1.6

- getImageWritersByFormatName

```java
public static
Iterator
<
ImageWriter
> getImageWritersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

- getImageWritersBySuffix

```java
public static
Iterator
<
ImageWriter
> getImageWritersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

- getImageWritersByMIMEType

```java
public static
Iterator
<
ImageWriter
> getImageWritersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

- getImageWriter

```java
public static
ImageWriter
getImageWriter​(
ImageReader
reader)
```

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered. This
mechanism may be used to obtain an

ImageWriter

that will understand the internal structure of non-pixel
metadata (as encoded by

IIOMetadata

objects)
generated by the

ImageReader

. By obtaining this
data from the

ImageReader

and passing it on to the

ImageWriter

obtained with this method, a client
program can read an image, modify it in some way, and write it
back out preserving all metadata, without having to understand
anything about the structure of the metadata, or even about
the image format. Note that this method returns the
"preferred" writer, which is the first in the list returned by

javax.imageio.spi.ImageReaderSpi.getImageWriterSpiNames()

.

**Parameters:** reader

- an instance of a registered

ImageReader

.
**Returns:** an

ImageWriter

, or null.
**Throws:** IllegalArgumentException

- if

reader

is

null

.
**See Also:** getImageReader(ImageWriter)

,

ImageReaderSpi.getImageWriterSpiNames()

- getImageReader

```java
public static
ImageReader
getImageReader​(
ImageWriter
writer)
```

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered. This method
is provided principally for symmetry with

getImageWriter(ImageReader)

. Note that this
method returns the "preferred" reader, which is the first in
the list returned by
javax.imageio.spi.ImageWriterSpi.

getImageReaderSpiNames()

.

**Parameters:** writer

- an instance of a registered

ImageWriter

.
**Returns:** an

ImageReader

, or null.
**Throws:** IllegalArgumentException

- if

writer

is

null

.
**See Also:** getImageWriter(ImageReader)

,

ImageWriterSpi.getImageReaderSpiNames()

- getImageWriters

```java
public static
Iterator
<
ImageWriter
> getImageWriters​(
ImageTypeSpecifier
type,

String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

**Parameters:** type

- an

ImageTypeSpecifier

indicating the
layout of the image to be written.
**Parameters:** formatName

- the informal name of the

format

.
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**See Also:** ImageWriterSpi.canEncodeImage(ImageTypeSpecifier)

- getImageTranscoders

```java
public static
Iterator
<
ImageTranscoder
> getImageTranscoders​(
ImageReader
reader,

ImageWriter
writer)
```

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

**Parameters:** reader

- an

ImageReader

.
**Parameters:** writer

- an

ImageWriter

.
**Returns:** an

Iterator

containing

ImageTranscoder

s.
**Throws:** IllegalArgumentException

- if

reader

or

writer

is

null

.

- read

```java
public static
BufferedImage
read​(
File
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.
The

File

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

File

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
InputStream
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.
The

InputStream

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** input

- an

InputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
URL
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered. An

InputStream

is obtained from the

URL

,
which is wrapped in an

ImageInputStream

. If no
registered

ImageReader

claims to be able to read
the resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

URL

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

- read

```java
public static
BufferedImage
read​(
ImageInputStream
stream)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered. If no registered

ImageReader

claims to be able to read the stream,

null

is returned.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

**Parameters:** stream

- an

ImageInputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IOException

- if an error occurs during reading.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

ImageOutputStream
output)
throws
IOException
```

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

. The image is written to the

ImageOutputStream

starting at the current stream
pointer, overwriting existing stream data from that point
forward, if present.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

ImageOutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

File
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

. If
there is already a

File

present, its contents are
discarded.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- a

File

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

- write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

OutputStream
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

OutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

---

#### Method Detail

scanForPlugins

```java
public static void scanForPlugins()
```

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

**See Also:** ClassLoader.getResources(java.lang.String)

---

#### scanForPlugins

public static void scanForPlugins()

Scans for plug-ins on the application class path,
loads their service provider classes, and registers a service
provider instance for each one found with the

IIORegistry

.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

This method is needed because the application class path can
theoretically change, or additional plug-ins may become available.
Rather than re-scanning the classpath on every invocation of the
API, the class path is scanned automatically only on the first
invocation. Clients can call this method to prompt a re-scan.
Thus this method need only be invoked by sophisticated applications
which dynamically make new plug-ins available at runtime.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

The

getResources

method of the context

ClassLoader

is used locate JAR files containing
files named

META-INF/services/javax.imageio.spi.

classname

,
where

classname

is one of

ImageReaderSpi

,

ImageWriterSpi

,

ImageTranscoderSpi

,

ImageInputStreamSpi

, or

ImageOutputStreamSpi

, along the application class
path.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

The contents of the located files indicate the names of
actual implementation classes which implement the
aforementioned service provider interfaces; the default class
loader is then used to load each of these classes and to
instantiate an instance of each class, which is then placed
into the registry for later retrieval.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

The exact set of locations searched depends on the
implementation of the Java runtime environment.

setUseCache

```java
public static void setUseCache​(boolean useCache)
```

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**See Also:** getUseCache()

---

#### setUseCache

public static void setUseCache​(boolean useCache)

Sets a flag indicating whether a disk-based cache file should
be used when creating

ImageInputStream

s and

ImageOutputStream

s.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

When reading from a standard

InputStream

, it
may be necessary to save previously read information in a cache
since the underlying stream does not allow data to be re-read.
Similarly, when writing to a standard

OutputStream

, a cache may be used to allow a
previously written value to be changed before flushing it to
the final destination.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

The cache may reside in main memory or on disk. Setting
this flag to

false

disallows the use of disk for
future streams, which may be advantageous when working with
small images, as the overhead of creating and destroying files
is removed.

On startup, the value is set to

true

.

On startup, the value is set to

true

.

getUseCache

```java
public static boolean getUseCache()
```

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

**Returns:** true if a disk-based cache may be used for

ImageInputStream

s and

ImageOutputStream

s.
**See Also:** setUseCache(boolean)

---

#### getUseCache

public static boolean getUseCache()

Returns the current value set by

setUseCache

, or

true

if no explicit setting has been made.

setCacheDirectory

```java
public static void setCacheDirectory​(
File
cacheDirectory)
```

Sets the directory where cache files are to be created. A
value of

null

indicates that the system-dependent
default temporary-file directory is to be used. If

getUseCache

returns false, this value is ignored.

**Parameters:** cacheDirectory

- a

File

specifying a directory.
**Throws:** SecurityException

- if the security manager denies
access to the directory.
**Throws:** IllegalArgumentException

- if

cacheDir

is
non-

null

but is not a directory.
**See Also:** File.createTempFile(String, String, File)

,

getCacheDirectory()

---

#### setCacheDirectory

public static void setCacheDirectory​(

File

cacheDirectory)

Sets the directory where cache files are to be created. A
value of

null

indicates that the system-dependent
default temporary-file directory is to be used. If

getUseCache

returns false, this value is ignored.

getCacheDirectory

```java
public static
File
getCacheDirectory()
```

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

**Returns:** a

File

indicating the directory where
cache files will be created, or

null

to indicate
the system-dependent default temporary-file directory.
**See Also:** setCacheDirectory(java.io.File)

---

#### getCacheDirectory

public static

File

getCacheDirectory()

Returns the current value set by

setCacheDirectory

, or

null

if no
explicit setting has been made.

createImageInputStream

```java
public static
ImageInputStream
createImageInputStream​(
Object
input)
throws
IOException
```

Returns an

ImageInputStream

that will take its
input from the given

Object

. The set of

ImageInputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to take input from the supplied object is used to
create the returned

ImageInputStream

. If no
suitable

ImageInputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** input

- an

Object

to be used as an input
source, such as a

File

, readable

RandomAccessFile

, or

InputStream

.
**Returns:** an

ImageInputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageInputStreamSpi

---

#### createImageInputStream

public static

ImageInputStream

createImageInputStream​(

Object

input)
throws

IOException

Returns an

ImageInputStream

that will take its
input from the given

Object

. The set of

ImageInputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to take input from the supplied object is used to
create the returned

ImageInputStream

. If no
suitable

ImageInputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

createImageOutputStream

```java
public static
ImageOutputStream
createImageOutputStream​(
Object
output)
throws
IOException
```

Returns an

ImageOutputStream

that will send its
output to the given

Object

. The set of

ImageOutputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to send output from the supplied object is used to
create the returned

ImageOutputStream

. If no
suitable

ImageOutputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** output

- an

Object

to be used as an output
destination, such as a

File

, writable

RandomAccessFile

, or

OutputStream

.
**Returns:** an

ImageOutputStream

, or

null

.
**Throws:** IllegalArgumentException

- if

output

is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** ImageOutputStreamSpi

---

#### createImageOutputStream

public static

ImageOutputStream

createImageOutputStream​(

Object

output)
throws

IOException

Returns an

ImageOutputStream

that will send its
output to the given

Object

. The set of

ImageOutputStreamSpi

s registered with the

IIORegistry

class is queried and the first one
that is able to send output from the supplied object is used to
create the returned

ImageOutputStream

. If no
suitable

ImageOutputStreamSpi

exists,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

getReaderFormatNames

```java
public static
String
[] getReaderFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

**Returns:** an array of

String

s.

---

#### getReaderFormatNames

public static

String

[] getReaderFormatNames()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
readers.

getReaderMIMETypes

```java
public static
String
[] getReaderMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

**Returns:** an array of

String

s.

---

#### getReaderMIMETypes

public static

String

[] getReaderMIMETypes()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
readers.

getReaderFileSuffixes

```java
public static
String
[] getReaderFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

**Returns:** an array of

String

s.
**Since:** 1.6

---

#### getReaderFileSuffixes

public static

String

[] getReaderFileSuffixes()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered readers.

getImageReaders

```java
public static
Iterator
<
ImageReader
> getImageReaders​(
Object
input)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

The stream position is left at its prior position upon
exit from this method.

**Parameters:** input

- an

ImageInputStream

or other

Object

containing encoded image data.
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**See Also:** ImageReaderSpi.canDecodeInput(java.lang.Object)

---

#### getImageReaders

public static

Iterator

<

ImageReader

> getImageReaders​(

Object

input)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the supplied

Object

, typically an

ImageInputStream

.

The stream position is left at its prior position upon
exit from this method.

The stream position is left at its prior position upon
exit from this method.

getImageReadersByFormatName

```java
public static
Iterator
<
ImageReader
> getImageReadersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

---

#### getImageReadersByFormatName

public static

Iterator

<

ImageReader

> getImageReadersByFormatName​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode the named format.

getImageReadersBySuffix

```java
public static
Iterator
<
ImageReader
> getImageReadersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

---

#### getImageReadersBySuffix

public static

Iterator

<

ImageReader

> getImageReadersBySuffix​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given suffix.

getImageReadersByMIMEType

```java
public static
Iterator
<
ImageReader
> getImageReadersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageReader

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

---

#### getImageReadersByMIMEType

public static

Iterator

<

ImageReader

> getImageReadersByMIMEType​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageReader

s that claim to be able to
decode files with the given MIME type.

getWriterFormatNames

```java
public static
String
[] getWriterFormatNames()
```

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

**Returns:** an array of

String

s.

---

#### getWriterFormatNames

public static

String

[] getWriterFormatNames()

Returns an array of

String

s listing all of the
informal format names understood by the current set of registered
writers.

getWriterMIMETypes

```java
public static
String
[] getWriterMIMETypes()
```

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

**Returns:** an array of

String

s.

---

#### getWriterMIMETypes

public static

String

[] getWriterMIMETypes()

Returns an array of

String

s listing all of the
MIME types understood by the current set of registered
writers.

getWriterFileSuffixes

```java
public static
String
[] getWriterFileSuffixes()
```

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

**Returns:** an array of

String

s.
**Since:** 1.6

---

#### getWriterFileSuffixes

public static

String

[] getWriterFileSuffixes()

Returns an array of

String

s listing all of the
file suffixes associated with the formats understood
by the current set of registered writers.

getImageWritersByFormatName

```java
public static
Iterator
<
ImageWriter
> getImageWritersByFormatName​(
String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

**Parameters:** formatName

- a

String

containing the informal
name of a format (

e.g.

, "jpeg" or "tiff".
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

formatName

is

null

.
**See Also:** ImageReaderWriterSpi.getFormatNames()

---

#### getImageWritersByFormatName

public static

Iterator

<

ImageWriter

> getImageWritersByFormatName​(

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode the named format.

getImageWritersBySuffix

```java
public static
Iterator
<
ImageWriter
> getImageWritersBySuffix​(
String
fileSuffix)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

**Parameters:** fileSuffix

- a

String

containing a file
suffix (

e.g.

, "jpg" or "tiff").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

fileSuffix

is

null

.
**See Also:** ImageReaderWriterSpi.getFileSuffixes()

---

#### getImageWritersBySuffix

public static

Iterator

<

ImageWriter

> getImageWritersBySuffix​(

String

fileSuffix)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given suffix.

getImageWritersByMIMEType

```java
public static
Iterator
<
ImageWriter
> getImageWritersByMIMEType​(
String
MIMEType)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

**Parameters:** MIMEType

- a

String

containing a file
suffix (

e.g.

, "image/jpeg" or "image/x-bmp").
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if

MIMEType

is

null

.
**See Also:** ImageReaderWriterSpi.getMIMETypes()

---

#### getImageWritersByMIMEType

public static

Iterator

<

ImageWriter

> getImageWritersByMIMEType​(

String

MIMEType)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode files with the given MIME type.

getImageWriter

```java
public static
ImageWriter
getImageWriter​(
ImageReader
reader)
```

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered. This
mechanism may be used to obtain an

ImageWriter

that will understand the internal structure of non-pixel
metadata (as encoded by

IIOMetadata

objects)
generated by the

ImageReader

. By obtaining this
data from the

ImageReader

and passing it on to the

ImageWriter

obtained with this method, a client
program can read an image, modify it in some way, and write it
back out preserving all metadata, without having to understand
anything about the structure of the metadata, or even about
the image format. Note that this method returns the
"preferred" writer, which is the first in the list returned by

javax.imageio.spi.ImageReaderSpi.getImageWriterSpiNames()

.

**Parameters:** reader

- an instance of a registered

ImageReader

.
**Returns:** an

ImageWriter

, or null.
**Throws:** IllegalArgumentException

- if

reader

is

null

.
**See Also:** getImageReader(ImageWriter)

,

ImageReaderSpi.getImageWriterSpiNames()

---

#### getImageWriter

public static

ImageWriter

getImageWriter​(

ImageReader

reader)

Returns an

ImageWriter

corresponding to the given

ImageReader

, if there is one, or

null

if the plug-in for this

ImageReader

does not
specify a corresponding

ImageWriter

, or if the
given

ImageReader

is not registered. This
mechanism may be used to obtain an

ImageWriter

that will understand the internal structure of non-pixel
metadata (as encoded by

IIOMetadata

objects)
generated by the

ImageReader

. By obtaining this
data from the

ImageReader

and passing it on to the

ImageWriter

obtained with this method, a client
program can read an image, modify it in some way, and write it
back out preserving all metadata, without having to understand
anything about the structure of the metadata, or even about
the image format. Note that this method returns the
"preferred" writer, which is the first in the list returned by

javax.imageio.spi.ImageReaderSpi.getImageWriterSpiNames()

.

getImageReader

```java
public static
ImageReader
getImageReader​(
ImageWriter
writer)
```

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered. This method
is provided principally for symmetry with

getImageWriter(ImageReader)

. Note that this
method returns the "preferred" reader, which is the first in
the list returned by
javax.imageio.spi.ImageWriterSpi.

getImageReaderSpiNames()

.

**Parameters:** writer

- an instance of a registered

ImageWriter

.
**Returns:** an

ImageReader

, or null.
**Throws:** IllegalArgumentException

- if

writer

is

null

.
**See Also:** getImageWriter(ImageReader)

,

ImageWriterSpi.getImageReaderSpiNames()

---

#### getImageReader

public static

ImageReader

getImageReader​(

ImageWriter

writer)

Returns an

ImageReader

corresponding to the given

ImageWriter

, if there is one, or

null

if the plug-in for this

ImageWriter

does not
specify a corresponding

ImageReader

, or if the
given

ImageWriter

is not registered. This method
is provided principally for symmetry with

getImageWriter(ImageReader)

. Note that this
method returns the "preferred" reader, which is the first in
the list returned by
javax.imageio.spi.ImageWriterSpi.

getImageReaderSpiNames()

.

getImageWriters

```java
public static
Iterator
<
ImageWriter
> getImageWriters​(
ImageTypeSpecifier
type,

String
formatName)
```

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

**Parameters:** type

- an

ImageTypeSpecifier

indicating the
layout of the image to be written.
**Parameters:** formatName

- the informal name of the

format

.
**Returns:** an

Iterator

containing

ImageWriter

s.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**See Also:** ImageWriterSpi.canEncodeImage(ImageTypeSpecifier)

---

#### getImageWriters

public static

Iterator

<

ImageWriter

> getImageWriters​(

ImageTypeSpecifier

type,

String

formatName)

Returns an

Iterator

containing all currently
registered

ImageWriter

s that claim to be able to
encode images of the given layout (specified using an

ImageTypeSpecifier

) in the given format.

getImageTranscoders

```java
public static
Iterator
<
ImageTranscoder
> getImageTranscoders​(
ImageReader
reader,

ImageWriter
writer)
```

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

**Parameters:** reader

- an

ImageReader

.
**Parameters:** writer

- an

ImageWriter

.
**Returns:** an

Iterator

containing

ImageTranscoder

s.
**Throws:** IllegalArgumentException

- if

reader

or

writer

is

null

.

---

#### getImageTranscoders

public static

Iterator

<

ImageTranscoder

> getImageTranscoders​(

ImageReader

reader,

ImageWriter

writer)

Returns an

Iterator

containing all currently
registered

ImageTranscoder

s that claim to be
able to transcode between the metadata of the given

ImageReader

and

ImageWriter

.

read

```java
public static
BufferedImage
read​(
File
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.
The

File

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

File

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### read

public static

BufferedImage

read​(

File

input)
throws

IOException

Returns a

BufferedImage

as the result of decoding
a supplied

File

with an

ImageReader

chosen automatically from among those currently registered.
The

File

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

Note that there is no

read

method that takes a
filename as a

String

; use this method instead after
creating a

File

from the filename.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method does not attempt to locate

ImageReader

s that can read directly from a

File

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

read

```java
public static
BufferedImage
read​(
InputStream
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.
The

InputStream

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** input

- an

InputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### read

public static

BufferedImage

read​(

InputStream

input)
throws

IOException

Returns a

BufferedImage

as the result of decoding
a supplied

InputStream

with an

ImageReader

chosen automatically from among those currently registered.
The

InputStream

is wrapped in an

ImageInputStream

. If no registered

ImageReader

claims to be able to read the
resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

This method does not attempt to locate

ImageReader

s that can read directly from an

InputStream

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

This method

does not

close the provided

InputStream

after the read operation has completed;
it is the responsibility of the caller to close the stream, if desired.

read

```java
public static
BufferedImage
read​(
URL
input)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered. An

InputStream

is obtained from the

URL

,
which is wrapped in an

ImageInputStream

. If no
registered

ImageReader

claims to be able to read
the resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

**Parameters:** input

- a

URL

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

input

is

null

.
**Throws:** IOException

- if an error occurs during reading or when not
able to create required ImageInputStream.

---

#### read

public static

BufferedImage

read​(

URL

input)
throws

IOException

Returns a

BufferedImage

as the result of decoding
a supplied

URL

with an

ImageReader

chosen automatically from among those currently registered. An

InputStream

is obtained from the

URL

,
which is wrapped in an

ImageInputStream

. If no
registered

ImageReader

claims to be able to read
the resulting stream,

null

is returned.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching in the

ImageInputStream

that is created.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

This method does not attempt to locate

ImageReader

s that can read directly from a

URL

; that may be accomplished using

IIORegistry

and

ImageReaderSpi

.

read

```java
public static
BufferedImage
read​(
ImageInputStream
stream)
throws
IOException
```

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered. If no registered

ImageReader

claims to be able to read the stream,

null

is returned.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

**Parameters:** stream

- an

ImageInputStream

to read from.
**Returns:** a

BufferedImage

containing the decoded
contents of the input, or

null

.
**Throws:** IllegalArgumentException

- if

stream

is

null

.
**Throws:** IOException

- if an error occurs during reading.

---

#### read

public static

BufferedImage

read​(

ImageInputStream

stream)
throws

IOException

Returns a

BufferedImage

as the result of decoding
a supplied

ImageInputStream

with an

ImageReader

chosen automatically from among those
currently registered. If no registered

ImageReader

claims to be able to read the stream,

null

is returned.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

Unlike most other methods in this class, this method

does

close the provided

ImageInputStream

after the read
operation has completed, unless

null

is returned,
in which case this method

does not

close the stream.

write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

ImageOutputStream
output)
throws
IOException
```

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

. The image is written to the

ImageOutputStream

starting at the current stream
pointer, overwriting existing stream data from that point
forward, if present.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

ImageOutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing.

---

#### write

public static boolean write​(

RenderedImage

im,

String

formatName,

ImageOutputStream

output)
throws

IOException

Writes an image using the an arbitrary

ImageWriter

that supports the given format to an

ImageOutputStream

. The image is written to the

ImageOutputStream

starting at the current stream
pointer, overwriting existing stream data from that point
forward, if present.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

This method

does not

close the provided

ImageOutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

File
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

. If
there is already a

File

present, its contents are
discarded.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- a

File

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

---

#### write

public static boolean write​(

RenderedImage

im,

String

formatName,

File

output)
throws

IOException

Writes an image using an arbitrary

ImageWriter

that supports the given format to a

File

. If
there is already a

File

present, its contents are
discarded.

write

```java
public static boolean write​(
RenderedImage
im,

String
formatName,

OutputStream
output)
throws
IOException
```

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

**Parameters:** im

- a

RenderedImage

to be written.
**Parameters:** formatName

- a

String

containing the informal
name of the format.
**Parameters:** output

- an

OutputStream

to be written to.
**Returns:** false

if no appropriate writer is found.
**Throws:** IllegalArgumentException

- if any parameter is

null

.
**Throws:** IOException

- if an error occurs during writing or when not
able to create required ImageOutputStream.

---

#### write

public static boolean write​(

RenderedImage

im,

String

formatName,

OutputStream

output)
throws

IOException

Writes an image using an arbitrary

ImageWriter

that supports the given format to an

OutputStream

.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

This method

does not

close the provided

OutputStream

after the write operation has completed;
it is the responsibility of the caller to close the stream, if desired.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

The current cache settings from

getUseCache

and

getCacheDirectory

will be used to control caching.

---

