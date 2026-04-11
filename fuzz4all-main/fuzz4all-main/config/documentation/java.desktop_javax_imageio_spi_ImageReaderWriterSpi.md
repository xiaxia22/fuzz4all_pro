# Class ImageReaderWriterSpi

**Source:** `java.desktop\javax\imageio\spi\ImageReaderWriterSpi.html`

### Class Description

```java
public abstract class
ImageReaderWriterSpi

extends
IIOServiceProvider
```

A superclass containing instance variables and methods common to

ImageReaderSpi

and

ImageWriterSpi

.

**All Implemented Interfaces:** RegisterableService

---

### Field Details

#### protected
String
[] names

An array of strings to be returned from

getFormatNames

, initially

null

.
Constructors should set this to a non-

null

value.

---

#### protected
String
[] suffixes

An array of strings to be returned from

getFileSuffixes

, initially

null

.

---

#### protected
String
[] MIMETypes

An array of strings to be returned from

getMIMETypes

, initially

null

.

---

#### protected
String
pluginClassName

A

String

containing the name of the associated
plug-in class, initially

null

.

---

#### protected boolean supportsStandardStreamMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

---

#### protected
String
nativeStreamMetadataFormatName

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

---

#### protected
String
nativeStreamMetadataFormatClassName

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

---

#### protected
String
[] extraStreamMetadataFormatNames

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

---

#### protected
String
[] extraStreamMetadataFormatClassNames

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

---

#### protected boolean supportsStandardImageMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

---

#### protected
String
nativeImageMetadataFormatName

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

---

#### protected
String
nativeImageMetadataFormatClassName

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

---

#### protected
String
[] extraImageMetadataFormatNames

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

---

#### protected
String
[] extraImageMetadataFormatClassNames

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

---

### Constructor Details

#### public ImageReaderWriterSpi​(
String
vendorName,

String
version,

String
[] names,

String
[] suffixes,

String
[] MIMETypes,

String
pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String
nativeStreamMetadataFormatName,

String
nativeStreamMetadataFormatClassName,

String
[] extraStreamMetadataFormatNames,

String
[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String
nativeImageMetadataFormatName,

String
nativeImageMetadataFormatClassName,

String
[] extraImageMetadataFormatNames,

String
[] extraImageMetadataFormatClassNames)

Constructs an

ImageReaderWriterSpi

with a given
set of values.

**Parameters:**
- vendorName

- the vendor name, as a non-

null

String

.
- version

- a version identifier, as a non-

null

String

.
- names

- a non-

null

array of

String

s indicating the format names. At least one
entry must be present.
- suffixes

- an array of

String

s indicating the
common file suffixes. If no suffixes are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
- MIMETypes

- an array of

String

s indicating
the format's MIME types. If no MIME types are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
- pluginClassName

- the fully-qualified name of the
associated

ImageReader

or

ImageWriter

class, as a non-

null String

.
- supportsStandardStreamMetadataFormat

- a

boolean

that indicates whether a stream metadata
object can use trees described by the standard metadata format.
- nativeStreamMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeStreamMetadataFormatName

.
- nativeStreamMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeStreamMetadataFormat

.
- extraStreamMetadataFormatNames

- an array of

String

s, or

null

, to be returned from

getExtraStreamMetadataFormatNames

. An array of length
0 is normalized to

null

.
- extraStreamMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getStreamMetadataFormat

. An array of length
0 is normalized to

null

.
- supportsStandardImageMetadataFormat

- a

boolean

that indicates whether an image metadata
object can use trees described by the standard metadata format.
- nativeImageMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeImageMetadataFormatName

.
- nativeImageMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeImageMetadataFormat

.
- extraImageMetadataFormatNames

- an array of

String

s to be returned from

getExtraImageMetadataFormatNames

. An array of length 0
is normalized to

null

.
- extraImageMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getImageMetadataFormat

. An array of length
0 is normalized to

null

.

**Throws:**
- IllegalArgumentException

- if

vendorName

is

null

.
- IllegalArgumentException

- if

version

is

null

.
- IllegalArgumentException

- if

names

is

null

or has length 0.
- IllegalArgumentException

- if

pluginClassName

is

null

.

---

#### public ImageReaderWriterSpi()

Constructs a blank

ImageReaderWriterSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

### Method Details

#### public
String
[] getFormatNames()

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider. For
example, a single

ImageReader

might be able to
process both PBM and PNM files.

**Returns:**
- a non-

null

array of

String

s
or length at least 1 containing informal format names
associated with this reader or writer.

---

#### public
String
[] getFileSuffixes()

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider. For example, a single

ImageReader

might be able to process files with
'.pbm' and '.pnm' suffixes, or both '.jpg' and '.jpeg'
suffixes. If there are no known file suffixes,

null

will be returned.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

**Returns:**
- an array of

String

s or length at least 1
containing common file suffixes associated with this reader or
writer, or

null

.

---

#### public
String
[] getMIMETypes()

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

**Returns:**
- an array of

String

s or length at least 1
containing MIME types associated with this reader or writer, or

null

.

---

#### public
String
getPluginClassName()

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

**Returns:**
- the class name, as a non-

null

String

.

---

#### public boolean isStandardStreamMetadataFormatSupported()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

**Returns:**
- true

if the standard format is supported
for stream metadata.

---

#### public
String
getNativeStreamMetadataFormatName()

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:**
- the name of the native stream metadata format, or

null

.

---

#### public
String
[] getExtraStreamMetadataFormatNames()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:**
- an array of

String

s, or null.

**See Also:**
- IIOMetadata.getMetadataFormatNames()

,

getExtraImageMetadataFormatNames()

,

getNativeStreamMetadataFormatName()

---

#### public boolean isStandardImageMetadataFormatSupported()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

**Returns:**
- true

if the standard format is supported
for image metadata.

---

#### public
String
getNativeImageMetadataFormatName()

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:**
- the name of the native image metadata format, or

null

.

**See Also:**
- getExtraImageMetadataFormatNames()

---

#### public
String
[] getExtraImageMetadataFormatNames()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:**
- an array of

String

s, or null.

**See Also:**
- IIOMetadata.getMetadataFormatNames()

,

getExtraStreamMetadataFormatNames()

,

getNativeImageMetadataFormatName()

---

#### public
IIOMetadataFormat
getStreamMetadataFormat​(
String
formatName)

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available. The supplied name must be the native
stream metadata format name, the standard metadata format name,
or one of those returned by

getExtraStreamMetadataFormatNames

.

**Parameters:**
- formatName

- the desired stream metadata format.

**Returns:**
- an

IIOMetadataFormat

object.

**Throws:**
- IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

---

#### public
IIOMetadataFormat
getImageMetadataFormat​(
String
formatName)

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available. The supplied name must be the native
image metadata format name, the standard metadata format name,
or one of those returned by

getExtraImageMetadataFormatNames

.

**Parameters:**
- formatName

- the desired image metadata format.

**Returns:**
- an

IIOMetadataFormat

object.

**Throws:**
- IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

---

### Additional Sections

#### Class ImageReaderWriterSpi

java.lang.Object

- javax.imageio.spi.IIOServiceProvider
- - javax.imageio.spi.ImageReaderWriterSpi

javax.imageio.spi.IIOServiceProvider

- javax.imageio.spi.ImageReaderWriterSpi

javax.imageio.spi.ImageReaderWriterSpi

**All Implemented Interfaces:** RegisterableService

**Direct Known Subclasses:** ImageReaderSpi

,

ImageWriterSpi

```java
public abstract class
ImageReaderWriterSpi

extends
IIOServiceProvider
```

A superclass containing instance variables and methods common to

ImageReaderSpi

and

ImageWriterSpi

.

**See Also:** IIORegistry

,

ImageReaderSpi

,

ImageWriterSpi

public abstract class

ImageReaderWriterSpi

extends

IIOServiceProvider

A superclass containing instance variables and methods common to

ImageReaderSpi

and

ImageWriterSpi

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

[]

extraImageMetadataFormatClassNames

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

protected

String

[]

extraImageMetadataFormatNames

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

extraStreamMetadataFormatClassNames

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

extraStreamMetadataFormatNames

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

MIMETypes

An array of strings to be returned from

getMIMETypes

, initially

null

.

protected

String

[]

names

An array of strings to be returned from

getFormatNames

, initially

null

.

protected

String

nativeImageMetadataFormatClassName

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

protected

String

nativeImageMetadataFormatName

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

protected

String

nativeStreamMetadataFormatClassName

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

protected

String

nativeStreamMetadataFormatName

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

protected

String

pluginClassName

A

String

containing the name of the associated
plug-in class, initially

null

.

protected

String

[]

suffixes

An array of strings to be returned from

getFileSuffixes

, initially

null

.

protected boolean

supportsStandardImageMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

protected boolean

supportsStandardStreamMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

- Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageReaderWriterSpi

()

Constructs a blank

ImageReaderWriterSpi

.

ImageReaderWriterSpi

​(

String

vendorName,

String

version,

String

[] names,

String

[] suffixes,

String

[] MIMETypes,

String

pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String

nativeStreamMetadataFormatName,

String

nativeStreamMetadataFormatClassName,

String

[] extraStreamMetadataFormatNames,

String

[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String

nativeImageMetadataFormatName,

String

nativeImageMetadataFormatClassName,

String

[] extraImageMetadataFormatNames,

String

[] extraImageMetadataFormatClassNames)

Constructs an

ImageReaderWriterSpi

with a given
set of values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

[]

getExtraImageMetadataFormatNames

()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

String

[]

getExtraStreamMetadataFormatNames

()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

String

[]

getFileSuffixes

()

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

String

[]

getFormatNames

()

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider.

IIOMetadataFormat

getImageMetadataFormat

​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available.

String

[]

getMIMETypes

()

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

String

getNativeImageMetadataFormatName

()

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in.

String

getNativeStreamMetadataFormatName

()

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in.

String

getPluginClassName

()

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

IIOMetadataFormat

getStreamMetadataFormat

​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available.

boolean

isStandardImageMetadataFormatSupported

()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

boolean

isStandardStreamMetadataFormatSupported

()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

- Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

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

protected

String

[]

extraImageMetadataFormatClassNames

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

protected

String

[]

extraImageMetadataFormatNames

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

extraStreamMetadataFormatClassNames

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

extraStreamMetadataFormatNames

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

protected

String

[]

MIMETypes

An array of strings to be returned from

getMIMETypes

, initially

null

.

protected

String

[]

names

An array of strings to be returned from

getFormatNames

, initially

null

.

protected

String

nativeImageMetadataFormatClassName

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

protected

String

nativeImageMetadataFormatName

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

protected

String

nativeStreamMetadataFormatClassName

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

protected

String

nativeStreamMetadataFormatName

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

protected

String

pluginClassName

A

String

containing the name of the associated
plug-in class, initially

null

.

protected

String

[]

suffixes

An array of strings to be returned from

getFileSuffixes

, initially

null

.

protected boolean

supportsStandardImageMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

protected boolean

supportsStandardStreamMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

- Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

---

#### Field Summary

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

An array of strings to be returned from

getMIMETypes

, initially

null

.

An array of strings to be returned from

getFormatNames

, initially

null

.

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

A

String

containing the name of the associated
plug-in class, initially

null

.

An array of strings to be returned from

getFileSuffixes

, initially

null

.

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

---

#### Fields declared in class javax.imageio.spi. IIOServiceProvider

Constructor Summary

Constructors

Constructor

Description

ImageReaderWriterSpi

()

Constructs a blank

ImageReaderWriterSpi

.

ImageReaderWriterSpi

​(

String

vendorName,

String

version,

String

[] names,

String

[] suffixes,

String

[] MIMETypes,

String

pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String

nativeStreamMetadataFormatName,

String

nativeStreamMetadataFormatClassName,

String

[] extraStreamMetadataFormatNames,

String

[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String

nativeImageMetadataFormatName,

String

nativeImageMetadataFormatClassName,

String

[] extraImageMetadataFormatNames,

String

[] extraImageMetadataFormatClassNames)

Constructs an

ImageReaderWriterSpi

with a given
set of values.

---

#### Constructor Summary

Constructs a blank

ImageReaderWriterSpi

.

Constructs an

ImageReaderWriterSpi

with a given
set of values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

[]

getExtraImageMetadataFormatNames

()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

String

[]

getExtraStreamMetadataFormatNames

()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

String

[]

getFileSuffixes

()

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

String

[]

getFormatNames

()

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider.

IIOMetadataFormat

getImageMetadataFormat

​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available.

String

[]

getMIMETypes

()

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

String

getNativeImageMetadataFormatName

()

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in.

String

getNativeStreamMetadataFormatName

()

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in.

String

getPluginClassName

()

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

IIOMetadataFormat

getStreamMetadataFormat

​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available.

boolean

isStandardImageMetadataFormatSupported

()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

boolean

isStandardStreamMetadataFormatSupported

()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

- Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

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

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider.

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available.

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in.

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in.

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available.

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

---

#### Methods declared in class javax.imageio.spi. IIOServiceProvider

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

- names

```java
protected
String
[] names
```

An array of strings to be returned from

getFormatNames

, initially

null

.
Constructors should set this to a non-

null

value.

- suffixes

```java
protected
String
[] suffixes
```

An array of strings to be returned from

getFileSuffixes

, initially

null

.

- MIMETypes

```java
protected
String
[] MIMETypes
```

An array of strings to be returned from

getMIMETypes

, initially

null

.

- pluginClassName

```java
protected
String
pluginClassName
```

A

String

containing the name of the associated
plug-in class, initially

null

.

- supportsStandardStreamMetadataFormat

```java
protected boolean supportsStandardStreamMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

- nativeStreamMetadataFormatName

```java
protected
String
nativeStreamMetadataFormatName
```

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

- nativeStreamMetadataFormatClassName

```java
protected
String
nativeStreamMetadataFormatClassName
```

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

- extraStreamMetadataFormatNames

```java
protected
String
[] extraStreamMetadataFormatNames
```

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

- extraStreamMetadataFormatClassNames

```java
protected
String
[] extraStreamMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

- supportsStandardImageMetadataFormat

```java
protected boolean supportsStandardImageMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

- nativeImageMetadataFormatName

```java
protected
String
nativeImageMetadataFormatName
```

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

- nativeImageMetadataFormatClassName

```java
protected
String
nativeImageMetadataFormatClassName
```

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

- extraImageMetadataFormatNames

```java
protected
String
[] extraImageMetadataFormatNames
```

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

- extraImageMetadataFormatClassNames

```java
protected
String
[] extraImageMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageReaderWriterSpi

```java
public ImageReaderWriterSpi​(
String
vendorName,

String
version,

String
[] names,

String
[] suffixes,

String
[] MIMETypes,

String
pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String
nativeStreamMetadataFormatName,

String
nativeStreamMetadataFormatClassName,

String
[] extraStreamMetadataFormatNames,

String
[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String
nativeImageMetadataFormatName,

String
nativeImageMetadataFormatClassName,

String
[] extraImageMetadataFormatNames,

String
[] extraImageMetadataFormatClassNames)
```

Constructs an

ImageReaderWriterSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name, as a non-

null

String

.
**Parameters:** version

- a version identifier, as a non-

null

String

.
**Parameters:** names

- a non-

null

array of

String

s indicating the format names. At least one
entry must be present.
**Parameters:** suffixes

- an array of

String

s indicating the
common file suffixes. If no suffixes are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** MIMETypes

- an array of

String

s indicating
the format's MIME types. If no MIME types are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** pluginClassName

- the fully-qualified name of the
associated

ImageReader

or

ImageWriter

class, as a non-

null String

.
**Parameters:** supportsStandardStreamMetadataFormat

- a

boolean

that indicates whether a stream metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeStreamMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeStreamMetadataFormatName

.
**Parameters:** nativeStreamMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeStreamMetadataFormat

.
**Parameters:** extraStreamMetadataFormatNames

- an array of

String

s, or

null

, to be returned from

getExtraStreamMetadataFormatNames

. An array of length
0 is normalized to

null

.
**Parameters:** extraStreamMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getStreamMetadataFormat

. An array of length
0 is normalized to

null

.
**Parameters:** supportsStandardImageMetadataFormat

- a

boolean

that indicates whether an image metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeImageMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeImageMetadataFormatName

.
**Parameters:** nativeImageMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeImageMetadataFormat

.
**Parameters:** extraImageMetadataFormatNames

- an array of

String

s to be returned from

getExtraImageMetadataFormatNames

. An array of length 0
is normalized to

null

.
**Parameters:** extraImageMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getImageMetadataFormat

. An array of length
0 is normalized to

null

.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.
**Throws:** IllegalArgumentException

- if

names

is

null

or has length 0.
**Throws:** IllegalArgumentException

- if

pluginClassName

is

null

.

- ImageReaderWriterSpi

```java
public ImageReaderWriterSpi()
```

Constructs a blank

ImageReaderWriterSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

============ METHOD DETAIL ==========

- Method Detail

- getFormatNames

```java
public
String
[] getFormatNames()
```

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider. For
example, a single

ImageReader

might be able to
process both PBM and PNM files.

**Returns:** a non-

null

array of

String

s
or length at least 1 containing informal format names
associated with this reader or writer.

- getFileSuffixes

```java
public
String
[] getFileSuffixes()
```

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider. For example, a single

ImageReader

might be able to process files with
'.pbm' and '.pnm' suffixes, or both '.jpg' and '.jpeg'
suffixes. If there are no known file suffixes,

null

will be returned.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

**Returns:** an array of

String

s or length at least 1
containing common file suffixes associated with this reader or
writer, or

null

.

- getMIMETypes

```java
public
String
[] getMIMETypes()
```

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

**Returns:** an array of

String

s or length at least 1
containing MIME types associated with this reader or writer, or

null

.

- getPluginClassName

```java
public
String
getPluginClassName()
```

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

**Returns:** the class name, as a non-

null

String

.

- isStandardStreamMetadataFormatSupported

```java
public boolean isStandardStreamMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for stream metadata.

- getNativeStreamMetadataFormatName

```java
public
String
getNativeStreamMetadataFormatName()
```

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native stream metadata format, or

null

.

- getExtraStreamMetadataFormatNames

```java
public
String
[] getExtraStreamMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraImageMetadataFormatNames()

,

getNativeStreamMetadataFormatName()

- isStandardImageMetadataFormatSupported

```java
public boolean isStandardImageMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for image metadata.

- getNativeImageMetadataFormatName

```java
public
String
getNativeImageMetadataFormatName()
```

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native image metadata format, or

null

.
**See Also:** getExtraImageMetadataFormatNames()

- getExtraImageMetadataFormatNames

```java
public
String
[] getExtraImageMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraStreamMetadataFormatNames()

,

getNativeImageMetadataFormatName()

- getStreamMetadataFormat

```java
public
IIOMetadataFormat
getStreamMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available. The supplied name must be the native
stream metadata format name, the standard metadata format name,
or one of those returned by

getExtraStreamMetadataFormatNames

.

**Parameters:** formatName

- the desired stream metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

- getImageMetadataFormat

```java
public
IIOMetadataFormat
getImageMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available. The supplied name must be the native
image metadata format name, the standard metadata format name,
or one of those returned by

getExtraImageMetadataFormatNames

.

**Parameters:** formatName

- the desired image metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

Field Detail

- names

```java
protected
String
[] names
```

An array of strings to be returned from

getFormatNames

, initially

null

.
Constructors should set this to a non-

null

value.

- suffixes

```java
protected
String
[] suffixes
```

An array of strings to be returned from

getFileSuffixes

, initially

null

.

- MIMETypes

```java
protected
String
[] MIMETypes
```

An array of strings to be returned from

getMIMETypes

, initially

null

.

- pluginClassName

```java
protected
String
pluginClassName
```

A

String

containing the name of the associated
plug-in class, initially

null

.

- supportsStandardStreamMetadataFormat

```java
protected boolean supportsStandardStreamMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

- nativeStreamMetadataFormatName

```java
protected
String
nativeStreamMetadataFormatName
```

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

- nativeStreamMetadataFormatClassName

```java
protected
String
nativeStreamMetadataFormatClassName
```

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

- extraStreamMetadataFormatNames

```java
protected
String
[] extraStreamMetadataFormatNames
```

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

- extraStreamMetadataFormatClassNames

```java
protected
String
[] extraStreamMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

- supportsStandardImageMetadataFormat

```java
protected boolean supportsStandardImageMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

- nativeImageMetadataFormatName

```java
protected
String
nativeImageMetadataFormatName
```

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

- nativeImageMetadataFormatClassName

```java
protected
String
nativeImageMetadataFormatClassName
```

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

- extraImageMetadataFormatNames

```java
protected
String
[] extraImageMetadataFormatNames
```

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

- extraImageMetadataFormatClassNames

```java
protected
String
[] extraImageMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

---

#### Field Detail

names

```java
protected
String
[] names
```

An array of strings to be returned from

getFormatNames

, initially

null

.
Constructors should set this to a non-

null

value.

---

#### names

protected

String

[] names

An array of strings to be returned from

getFormatNames

, initially

null

.
Constructors should set this to a non-

null

value.

suffixes

```java
protected
String
[] suffixes
```

An array of strings to be returned from

getFileSuffixes

, initially

null

.

---

#### suffixes

protected

String

[] suffixes

An array of strings to be returned from

getFileSuffixes

, initially

null

.

MIMETypes

```java
protected
String
[] MIMETypes
```

An array of strings to be returned from

getMIMETypes

, initially

null

.

---

#### MIMETypes

protected

String

[] MIMETypes

An array of strings to be returned from

getMIMETypes

, initially

null

.

pluginClassName

```java
protected
String
pluginClassName
```

A

String

containing the name of the associated
plug-in class, initially

null

.

---

#### pluginClassName

protected

String

pluginClassName

A

String

containing the name of the associated
plug-in class, initially

null

.

supportsStandardStreamMetadataFormat

```java
protected boolean supportsStandardStreamMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

---

#### supportsStandardStreamMetadataFormat

protected boolean supportsStandardStreamMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for stream metadata, initially

false

.

nativeStreamMetadataFormatName

```java
protected
String
nativeStreamMetadataFormatName
```

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

---

#### nativeStreamMetadataFormatName

protected

String

nativeStreamMetadataFormatName

A

String

containing the name of the native stream
metadata format supported by this plug-in, initially

null

.

nativeStreamMetadataFormatClassName

```java
protected
String
nativeStreamMetadataFormatClassName
```

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

---

#### nativeStreamMetadataFormatClassName

protected

String

nativeStreamMetadataFormatClassName

A

String

containing the class name of the native
stream metadata format supported by this plug-in, initially

null

.

extraStreamMetadataFormatNames

```java
protected
String
[] extraStreamMetadataFormatNames
```

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

---

#### extraStreamMetadataFormatNames

protected

String

[] extraStreamMetadataFormatNames

An array of

String

s containing the names of any
additional stream metadata formats supported by this plug-in,
initially

null

.

extraStreamMetadataFormatClassNames

```java
protected
String
[] extraStreamMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

---

#### extraStreamMetadataFormatClassNames

protected

String

[] extraStreamMetadataFormatClassNames

An array of

String

s containing the class names of
any additional stream metadata formats supported by this plug-in,
initially

null

.

supportsStandardImageMetadataFormat

```java
protected boolean supportsStandardImageMetadataFormat
```

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

---

#### supportsStandardImageMetadataFormat

protected boolean supportsStandardImageMetadataFormat

A boolean indicating whether this plug-in supports the
standard metadata format for image metadata, initially

false

.

nativeImageMetadataFormatName

```java
protected
String
nativeImageMetadataFormatName
```

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

---

#### nativeImageMetadataFormatName

protected

String

nativeImageMetadataFormatName

A

String

containing the name of the
native stream metadata format supported by this plug-in,
initially

null

.

nativeImageMetadataFormatClassName

```java
protected
String
nativeImageMetadataFormatClassName
```

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

---

#### nativeImageMetadataFormatClassName

protected

String

nativeImageMetadataFormatClassName

A

String

containing the class name of the
native stream metadata format supported by this plug-in,
initially

null

.

extraImageMetadataFormatNames

```java
protected
String
[] extraImageMetadataFormatNames
```

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

---

#### extraImageMetadataFormatNames

protected

String

[] extraImageMetadataFormatNames

An array of

String

s containing the names of any
additional image metadata formats supported by this plug-in,
initially

null

.

extraImageMetadataFormatClassNames

```java
protected
String
[] extraImageMetadataFormatClassNames
```

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

---

#### extraImageMetadataFormatClassNames

protected

String

[] extraImageMetadataFormatClassNames

An array of

String

s containing the class names of
any additional image metadata formats supported by this
plug-in, initially

null

.

Constructor Detail

- ImageReaderWriterSpi

```java
public ImageReaderWriterSpi​(
String
vendorName,

String
version,

String
[] names,

String
[] suffixes,

String
[] MIMETypes,

String
pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String
nativeStreamMetadataFormatName,

String
nativeStreamMetadataFormatClassName,

String
[] extraStreamMetadataFormatNames,

String
[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String
nativeImageMetadataFormatName,

String
nativeImageMetadataFormatClassName,

String
[] extraImageMetadataFormatNames,

String
[] extraImageMetadataFormatClassNames)
```

Constructs an

ImageReaderWriterSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name, as a non-

null

String

.
**Parameters:** version

- a version identifier, as a non-

null

String

.
**Parameters:** names

- a non-

null

array of

String

s indicating the format names. At least one
entry must be present.
**Parameters:** suffixes

- an array of

String

s indicating the
common file suffixes. If no suffixes are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** MIMETypes

- an array of

String

s indicating
the format's MIME types. If no MIME types are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** pluginClassName

- the fully-qualified name of the
associated

ImageReader

or

ImageWriter

class, as a non-

null String

.
**Parameters:** supportsStandardStreamMetadataFormat

- a

boolean

that indicates whether a stream metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeStreamMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeStreamMetadataFormatName

.
**Parameters:** nativeStreamMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeStreamMetadataFormat

.
**Parameters:** extraStreamMetadataFormatNames

- an array of

String

s, or

null

, to be returned from

getExtraStreamMetadataFormatNames

. An array of length
0 is normalized to

null

.
**Parameters:** extraStreamMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getStreamMetadataFormat

. An array of length
0 is normalized to

null

.
**Parameters:** supportsStandardImageMetadataFormat

- a

boolean

that indicates whether an image metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeImageMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeImageMetadataFormatName

.
**Parameters:** nativeImageMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeImageMetadataFormat

.
**Parameters:** extraImageMetadataFormatNames

- an array of

String

s to be returned from

getExtraImageMetadataFormatNames

. An array of length 0
is normalized to

null

.
**Parameters:** extraImageMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getImageMetadataFormat

. An array of length
0 is normalized to

null

.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.
**Throws:** IllegalArgumentException

- if

names

is

null

or has length 0.
**Throws:** IllegalArgumentException

- if

pluginClassName

is

null

.

- ImageReaderWriterSpi

```java
public ImageReaderWriterSpi()
```

Constructs a blank

ImageReaderWriterSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### Constructor Detail

ImageReaderWriterSpi

```java
public ImageReaderWriterSpi​(
String
vendorName,

String
version,

String
[] names,

String
[] suffixes,

String
[] MIMETypes,

String
pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String
nativeStreamMetadataFormatName,

String
nativeStreamMetadataFormatClassName,

String
[] extraStreamMetadataFormatNames,

String
[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String
nativeImageMetadataFormatName,

String
nativeImageMetadataFormatClassName,

String
[] extraImageMetadataFormatNames,

String
[] extraImageMetadataFormatClassNames)
```

Constructs an

ImageReaderWriterSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name, as a non-

null

String

.
**Parameters:** version

- a version identifier, as a non-

null

String

.
**Parameters:** names

- a non-

null

array of

String

s indicating the format names. At least one
entry must be present.
**Parameters:** suffixes

- an array of

String

s indicating the
common file suffixes. If no suffixes are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** MIMETypes

- an array of

String

s indicating
the format's MIME types. If no MIME types are defined,

null

should be supplied. An array of length 0
will be normalized to

null

.
**Parameters:** pluginClassName

- the fully-qualified name of the
associated

ImageReader

or

ImageWriter

class, as a non-

null String

.
**Parameters:** supportsStandardStreamMetadataFormat

- a

boolean

that indicates whether a stream metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeStreamMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeStreamMetadataFormatName

.
**Parameters:** nativeStreamMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeStreamMetadataFormat

.
**Parameters:** extraStreamMetadataFormatNames

- an array of

String

s, or

null

, to be returned from

getExtraStreamMetadataFormatNames

. An array of length
0 is normalized to

null

.
**Parameters:** extraStreamMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getStreamMetadataFormat

. An array of length
0 is normalized to

null

.
**Parameters:** supportsStandardImageMetadataFormat

- a

boolean

that indicates whether an image metadata
object can use trees described by the standard metadata format.
**Parameters:** nativeImageMetadataFormatName

- a

String

, or

null

, to be returned from

getNativeImageMetadataFormatName

.
**Parameters:** nativeImageMetadataFormatClassName

- a

String

, or

null

, to be used to instantiate
a metadata format object to be returned from

getNativeImageMetadataFormat

.
**Parameters:** extraImageMetadataFormatNames

- an array of

String

s to be returned from

getExtraImageMetadataFormatNames

. An array of length 0
is normalized to

null

.
**Parameters:** extraImageMetadataFormatClassNames

- an array of

String

s, or

null

, to be used to instantiate
a metadata format object to be returned from

getImageMetadataFormat

. An array of length
0 is normalized to

null

.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.
**Throws:** IllegalArgumentException

- if

names

is

null

or has length 0.
**Throws:** IllegalArgumentException

- if

pluginClassName

is

null

.

---

#### ImageReaderWriterSpi

public ImageReaderWriterSpi​(

String

vendorName,

String

version,

String

[] names,

String

[] suffixes,

String

[] MIMETypes,

String

pluginClassName,
boolean supportsStandardStreamMetadataFormat,

String

nativeStreamMetadataFormatName,

String

nativeStreamMetadataFormatClassName,

String

[] extraStreamMetadataFormatNames,

String

[] extraStreamMetadataFormatClassNames,
boolean supportsStandardImageMetadataFormat,

String

nativeImageMetadataFormatName,

String

nativeImageMetadataFormatClassName,

String

[] extraImageMetadataFormatNames,

String

[] extraImageMetadataFormatClassNames)

Constructs an

ImageReaderWriterSpi

with a given
set of values.

ImageReaderWriterSpi

```java
public ImageReaderWriterSpi()
```

Constructs a blank

ImageReaderWriterSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### ImageReaderWriterSpi

public ImageReaderWriterSpi()

Constructs a blank

ImageReaderWriterSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

Method Detail

- getFormatNames

```java
public
String
[] getFormatNames()
```

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider. For
example, a single

ImageReader

might be able to
process both PBM and PNM files.

**Returns:** a non-

null

array of

String

s
or length at least 1 containing informal format names
associated with this reader or writer.

- getFileSuffixes

```java
public
String
[] getFileSuffixes()
```

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider. For example, a single

ImageReader

might be able to process files with
'.pbm' and '.pnm' suffixes, or both '.jpg' and '.jpeg'
suffixes. If there are no known file suffixes,

null

will be returned.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

**Returns:** an array of

String

s or length at least 1
containing common file suffixes associated with this reader or
writer, or

null

.

- getMIMETypes

```java
public
String
[] getMIMETypes()
```

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

**Returns:** an array of

String

s or length at least 1
containing MIME types associated with this reader or writer, or

null

.

- getPluginClassName

```java
public
String
getPluginClassName()
```

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

**Returns:** the class name, as a non-

null

String

.

- isStandardStreamMetadataFormatSupported

```java
public boolean isStandardStreamMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for stream metadata.

- getNativeStreamMetadataFormatName

```java
public
String
getNativeStreamMetadataFormatName()
```

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native stream metadata format, or

null

.

- getExtraStreamMetadataFormatNames

```java
public
String
[] getExtraStreamMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraImageMetadataFormatNames()

,

getNativeStreamMetadataFormatName()

- isStandardImageMetadataFormatSupported

```java
public boolean isStandardImageMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for image metadata.

- getNativeImageMetadataFormatName

```java
public
String
getNativeImageMetadataFormatName()
```

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native image metadata format, or

null

.
**See Also:** getExtraImageMetadataFormatNames()

- getExtraImageMetadataFormatNames

```java
public
String
[] getExtraImageMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraStreamMetadataFormatNames()

,

getNativeImageMetadataFormatName()

- getStreamMetadataFormat

```java
public
IIOMetadataFormat
getStreamMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available. The supplied name must be the native
stream metadata format name, the standard metadata format name,
or one of those returned by

getExtraStreamMetadataFormatNames

.

**Parameters:** formatName

- the desired stream metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

- getImageMetadataFormat

```java
public
IIOMetadataFormat
getImageMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available. The supplied name must be the native
image metadata format name, the standard metadata format name,
or one of those returned by

getExtraImageMetadataFormatNames

.

**Parameters:** formatName

- the desired image metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

---

#### Method Detail

getFormatNames

```java
public
String
[] getFormatNames()
```

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider. For
example, a single

ImageReader

might be able to
process both PBM and PNM files.

**Returns:** a non-

null

array of

String

s
or length at least 1 containing informal format names
associated with this reader or writer.

---

#### getFormatNames

public

String

[] getFormatNames()

Returns an array of

String

s containing
human-readable names for the formats that are generally usable
by the

ImageReader

or

ImageWriter

implementation associated with this service provider. For
example, a single

ImageReader

might be able to
process both PBM and PNM files.

getFileSuffixes

```java
public
String
[] getFileSuffixes()
```

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider. For example, a single

ImageReader

might be able to process files with
'.pbm' and '.pnm' suffixes, or both '.jpg' and '.jpeg'
suffixes. If there are no known file suffixes,

null

will be returned.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

**Returns:** an array of

String

s or length at least 1
containing common file suffixes associated with this reader or
writer, or

null

.

---

#### getFileSuffixes

public

String

[] getFileSuffixes()

Returns an array of

String

s containing a list of
file suffixes associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider. For example, a single

ImageReader

might be able to process files with
'.pbm' and '.pnm' suffixes, or both '.jpg' and '.jpeg'
suffixes. If there are no known file suffixes,

null

will be returned.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

Returning a particular suffix does not guarantee that files
with that suffix can be processed; it merely indicates that it
may be worthwhile attempting to decode or encode such files
using this service provider.

getMIMETypes

```java
public
String
[] getMIMETypes()
```

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

**Returns:** an array of

String

s or length at least 1
containing MIME types associated with this reader or writer, or

null

.

---

#### getMIMETypes

public

String

[] getMIMETypes()

Returns an array of

String

s containing a list of
MIME types associated with the formats that are generally
usable by the

ImageReader

or

ImageWriter

implementation associated with this
service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

Ideally, only a single MIME type would be required in order
to describe a particular format. However, for several reasons
it is necessary to associate a list of types with each service
provider. First, many common image file formats do not have
standard MIME types, so a list of commonly used unofficial
names will be required, such as

image/x-pbm

and

image/x-portable-bitmap

. Some file formats have
official MIME types but may sometimes be referred to using
their previous unofficial designations, such as

image/x-png

instead of the official

image/png

. Finally, a single service provider may
be capable of parsing multiple distinct types from the MIME
point of view, for example

image/x-xbitmap

and

image/x-xpixmap

.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

Returning a particular MIME type does not guarantee that
files claiming to be of that type can be processed; it merely
indicates that it may be worthwhile attempting to decode or
encode such files using this service provider.

getPluginClassName

```java
public
String
getPluginClassName()
```

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

**Returns:** the class name, as a non-

null

String

.

---

#### getPluginClassName

public

String

getPluginClassName()

Returns the fully-qualified class name of the

ImageReader

or

ImageWriter

plug-in
associated with this service provider.

isStandardStreamMetadataFormatSupported

```java
public boolean isStandardStreamMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for stream metadata.

---

#### isStandardStreamMetadataFormatSupported

public boolean isStandardStreamMetadataFormatSupported()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

getNativeStreamMetadataFormatName

```java
public
String
getNativeStreamMetadataFormatName()
```

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native stream metadata format, or

null

.

---

#### getNativeStreamMetadataFormatName

public

String

getNativeStreamMetadataFormatName()

Returns the name of the "native" stream metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the stream metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

The default implementation returns the

nativeStreamMetadataFormatName

instance variable,
which is typically set by the constructor.

getExtraStreamMetadataFormatNames

```java
public
String
[] getExtraStreamMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraImageMetadataFormatNames()

,

getNativeStreamMetadataFormatName()

---

#### getExtraStreamMetadataFormatNames

public

String

[] getExtraStreamMetadataFormatNames()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the stream metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

If the plug-in does not handle metadata, null should be
returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any
circumstances.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

The default implementation returns a clone of the

extraStreamMetadataFormatNames

instance variable,
which is typically set by the constructor.

isStandardImageMetadataFormatSupported

```java
public boolean isStandardImageMetadataFormatSupported()
```

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

**Returns:** true

if the standard format is supported
for image metadata.

---

#### isStandardImageMetadataFormatSupported

public boolean isStandardImageMetadataFormatSupported()

Returns

true

if the standard metadata format is
among the document formats recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

getNativeImageMetadataFormatName

```java
public
String
getNativeImageMetadataFormatName()
```

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

**Returns:** the name of the native image metadata format, or

null

.
**See Also:** getExtraImageMetadataFormatNames()

---

#### getNativeImageMetadataFormatName

public

String

getNativeImageMetadataFormatName()

Returns the name of the "native" image metadata format for
this plug-in, which typically allows for lossless encoding and
transmission of the image metadata stored in the format handled by
this plug-in. If no such format is supported,

null

will be returned.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

The default implementation returns the

nativeImageMetadataFormatName

instance variable,
which is typically set by the constructor.

getExtraImageMetadataFormatNames

```java
public
String
[] getExtraImageMetadataFormatNames()
```

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

**Returns:** an array of

String

s, or null.
**See Also:** IIOMetadata.getMetadataFormatNames()

,

getExtraStreamMetadataFormatNames()

,

getNativeImageMetadataFormatName()

---

#### getExtraImageMetadataFormatNames

public

String

[] getExtraImageMetadataFormatNames()

Returns an array of

String

s containing the names
of additional document formats, other than the native and
standard formats, recognized by the

getAsTree

and

setFromTree

methods on
the image metadata objects produced or consumed by this
plug-in.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

If the plug-in does not handle image metadata, null should
be returned.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

The set of formats may differ according to the particular
images being read or written; this method should indicate all
the additional formats supported by the plug-in under any circumstances.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

The default implementation returns a clone of the

extraImageMetadataFormatNames

instance variable,
which is typically set by the constructor.

getStreamMetadataFormat

```java
public
IIOMetadataFormat
getStreamMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available. The supplied name must be the native
stream metadata format name, the standard metadata format name,
or one of those returned by

getExtraStreamMetadataFormatNames

.

**Parameters:** formatName

- the desired stream metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

---

#### getStreamMetadataFormat

public

IIOMetadataFormat

getStreamMetadataFormat​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given stream metadata format, or

null

if no
description is available. The supplied name must be the native
stream metadata format name, the standard metadata format name,
or one of those returned by

getExtraStreamMetadataFormatNames

.

getImageMetadataFormat

```java
public
IIOMetadataFormat
getImageMetadataFormat​(
String
formatName)
```

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available. The supplied name must be the native
image metadata format name, the standard metadata format name,
or one of those returned by

getExtraImageMetadataFormatNames

.

**Parameters:** formatName

- the desired image metadata format.
**Returns:** an

IIOMetadataFormat

object.
**Throws:** IllegalArgumentException

- if

formatName

is

null

or is not a supported name.

---

#### getImageMetadataFormat

public

IIOMetadataFormat

getImageMetadataFormat​(

String

formatName)

Returns an

IIOMetadataFormat

object describing the
given image metadata format, or

null

if no
description is available. The supplied name must be the native
image metadata format name, the standard metadata format name,
or one of those returned by

getExtraImageMetadataFormatNames

.

---

