# Class BMPImageWriteParam

**Source:** `java.desktop\javax\imageio\plugins\bmp\BMPImageWriteParam.html`

### Class Description

```java
public class
BMPImageWriteParam

extends
ImageWriteParam
```

A subclass of

ImageWriteParam

for encoding images in
the BMP format.

This class allows for the specification of various parameters
while writing a BMP format image file. By default, the data layout
is bottom-up, such that the pixels are stored in bottom-up order,
the first scanline being stored last.

The particular compression scheme to be used can be specified by using
the

setCompressionType()

method with the appropriate type
string. The compression scheme specified will be honored if and only if it
is compatible with the type of image being written. If the specified
compression scheme is not compatible with the type of image being written
then the

IOException

will be thrown by the BMP image writer.
If the compression type is not set explicitly then

getCompressionType()

will return

null

. In this case the BMP image writer will select
a compression type that supports encoding of the given image without loss
of the color resolution.

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

---

### Field Details

*No entries found.*

### Constructor Details

#### public BMPImageWriteParam​(
Locale
locale)

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

**Parameters:**
- locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

---

#### public BMPImageWriteParam()

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

---

### Method Details

#### public void setTopDown​(boolean topDown)

If set, the data will be written out in a top-down manner, the first
scanline being written first.

**Parameters:**
- topDown

- whether the data are written in top-down order.

---

#### public boolean isTopDown()

Returns the value of the

topDown

parameter.
The default is

false

.

**Returns:**
- whether the data are written in top-down order.

---

### Additional Sections

#### Class BMPImageWriteParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageWriteParam
- - javax.imageio.plugins.bmp.BMPImageWriteParam

javax.imageio.IIOParam

- javax.imageio.ImageWriteParam
- - javax.imageio.plugins.bmp.BMPImageWriteParam

javax.imageio.ImageWriteParam

- javax.imageio.plugins.bmp.BMPImageWriteParam

javax.imageio.plugins.bmp.BMPImageWriteParam

```java
public class
BMPImageWriteParam

extends
ImageWriteParam
```

A subclass of

ImageWriteParam

for encoding images in
the BMP format.

This class allows for the specification of various parameters
while writing a BMP format image file. By default, the data layout
is bottom-up, such that the pixels are stored in bottom-up order,
the first scanline being stored last.

The particular compression scheme to be used can be specified by using
the

setCompressionType()

method with the appropriate type
string. The compression scheme specified will be honored if and only if it
is compatible with the type of image being written. If the specified
compression scheme is not compatible with the type of image being written
then the

IOException

will be thrown by the BMP image writer.
If the compression type is not set explicitly then

getCompressionType()

will return

null

. In this case the BMP image writer will select
a compression type that supports encoding of the given image without loss
of the color resolution.

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

public class

BMPImageWriteParam

extends

ImageWriteParam

A subclass of

ImageWriteParam

for encoding images in
the BMP format.

This class allows for the specification of various parameters
while writing a BMP format image file. By default, the data layout
is bottom-up, such that the pixels are stored in bottom-up order,
the first scanline being stored last.

The particular compression scheme to be used can be specified by using
the

setCompressionType()

method with the appropriate type
string. The compression scheme specified will be honored if and only if it
is compatible with the type of image being written. If the specified
compression scheme is not compatible with the type of image being written
then the

IOException

will be thrown by the BMP image writer.
If the compression type is not set explicitly then

getCompressionType()

will return

null

. In this case the BMP image writer will select
a compression type that supports encoding of the given image without loss
of the color resolution.

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

This class allows for the specification of various parameters
while writing a BMP format image file. By default, the data layout
is bottom-up, such that the pixels are stored in bottom-up order,
the first scanline being stored last.

The particular compression scheme to be used can be specified by using
the

setCompressionType()

method with the appropriate type
string. The compression scheme specified will be honored if and only if it
is compatible with the type of image being written. If the specified
compression scheme is not compatible with the type of image being written
then the

IOException

will be thrown by the BMP image writer.
If the compression type is not set explicitly then

getCompressionType()

will return

null

. In this case the BMP image writer will select
a compression type that supports encoding of the given image without loss
of the color resolution.

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

The particular compression scheme to be used can be specified by using
the

setCompressionType()

method with the appropriate type
string. The compression scheme specified will be honored if and only if it
is compatible with the type of image being written. If the specified
compression scheme is not compatible with the type of image being written
then the

IOException

will be thrown by the BMP image writer.
If the compression type is not set explicitly then

getCompressionType()

will return

null

. In this case the BMP image writer will select
a compression type that supports encoding of the given image without loss
of the color resolution.

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

The compression type strings and the image type(s) each supports are
listed in the following
table:

Compression Types

Type String

Description

Image Types

BI_RGB

Uncompressed RLE

<= 8-bits/sample

BI_RLE8

8-bit Run Length Encoding

<= 8-bits/sample

BI_RLE4

4-bit Run Length Encoding

<= 4-bits/sample

BI_BITFIELDS

Packed data

16 or 32 bits/sample

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

BMPImageWriteParam

()

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

BMPImageWriteParam

​(

Locale

locale)

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isTopDown

()

Returns the value of the

topDown

parameter.

void

setTopDown

​(boolean topDown)

If set, the data will be written out in a top-down manner, the first
scanline being written first.

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

isCompressionLossless

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

unsetCompression

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

BMPImageWriteParam

()

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

BMPImageWriteParam

​(

Locale

locale)

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

---

#### Constructor Summary

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isTopDown

()

Returns the value of the

topDown

parameter.

void

setTopDown

​(boolean topDown)

If set, the data will be written out in a top-down manner, the first
scanline being written first.

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

isCompressionLossless

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

unsetCompression

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

Returns the value of the

topDown

parameter.

If set, the data will be written out in a top-down manner, the first
scanline being written first.

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

isCompressionLossless

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

unsetCompression

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

- BMPImageWriteParam

```java
public BMPImageWriteParam​(
Locale
locale)
```

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

- BMPImageWriteParam

```java
public BMPImageWriteParam()
```

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

============ METHOD DETAIL ==========

- Method Detail

- setTopDown

```java
public void setTopDown​(boolean topDown)
```

If set, the data will be written out in a top-down manner, the first
scanline being written first.

**Parameters:** topDown

- whether the data are written in top-down order.

- isTopDown

```java
public boolean isTopDown()
```

Returns the value of the

topDown

parameter.
The default is

false

.

**Returns:** whether the data are written in top-down order.

Constructor Detail

- BMPImageWriteParam

```java
public BMPImageWriteParam​(
Locale
locale)
```

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

- BMPImageWriteParam

```java
public BMPImageWriteParam()
```

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

---

#### Constructor Detail

BMPImageWriteParam

```java
public BMPImageWriteParam​(
Locale
locale)
```

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

**Parameters:** locale

- a

Locale

to be used to localize
compression type names and quality descriptions, or

null

.

---

#### BMPImageWriteParam

public BMPImageWriteParam​(

Locale

locale)

Constructs a

BMPImageWriteParam

set to use a given

Locale

and with default values for all parameters.

BMPImageWriteParam

```java
public BMPImageWriteParam()
```

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

---

#### BMPImageWriteParam

public BMPImageWriteParam()

Constructs an

BMPImageWriteParam

object with default
values for all parameters and a

null Locale

.

Method Detail

- setTopDown

```java
public void setTopDown​(boolean topDown)
```

If set, the data will be written out in a top-down manner, the first
scanline being written first.

**Parameters:** topDown

- whether the data are written in top-down order.

- isTopDown

```java
public boolean isTopDown()
```

Returns the value of the

topDown

parameter.
The default is

false

.

**Returns:** whether the data are written in top-down order.

---

#### Method Detail

setTopDown

```java
public void setTopDown​(boolean topDown)
```

If set, the data will be written out in a top-down manner, the first
scanline being written first.

**Parameters:** topDown

- whether the data are written in top-down order.

---

#### setTopDown

public void setTopDown​(boolean topDown)

If set, the data will be written out in a top-down manner, the first
scanline being written first.

isTopDown

```java
public boolean isTopDown()
```

Returns the value of the

topDown

parameter.
The default is

false

.

**Returns:** whether the data are written in top-down order.

---

#### isTopDown

public boolean isTopDown()

Returns the value of the

topDown

parameter.
The default is

false

.

---

