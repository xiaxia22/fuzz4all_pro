# Class BufferedImageFilter

**Source:** `java.desktop\java\awt\image\BufferedImageFilter.html`

### Class Description

```java
public class
BufferedImageFilter

extends
ImageFilter

implements
Cloneable
```

The

BufferedImageFilter

class subclasses an

ImageFilter

to provide a simple means of
using a single-source/single-destination image operator
(

BufferedImageOp

) to filter a

BufferedImage

in the Image Producer/Consumer/Observer
paradigm. Examples of these image operators are:

ConvolveOp

,

AffineTransformOp

and

LookupOp

.

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public BufferedImageFilter​(
BufferedImageOp
op)

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

**Parameters:**
- op

- the specified

BufferedImageOp

to
use to filter a

BufferedImage

**Throws:**
- NullPointerException

- if op is null

---

### Method Details

#### public
BufferedImageOp
getBufferedImageOp()

Returns the

BufferedImageOp

.

**Returns:**
- the operator of this

BufferedImageFilter

.

---

#### public void setDimensions​(int width,
int height)

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

**Specified by:**
- setDimensions

in interface

ImageConsumer

**Overrides:**
- setDimensions

in class

ImageFilter

**Parameters:**
- width

- the width to which to set the width of this

BufferedImageFilter
- height

- the height to which to set the height of this

BufferedImageFilter

**See Also:**
- ImageConsumer.setDimensions(int, int)

---

#### public void setColorModel​(
ColorModel
model)

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

**Specified by:**
- setColorModel

in interface

ImageConsumer

**Overrides:**
- setColorModel

in class

ImageFilter

**Parameters:**
- model

- the

ColorModel

to which to set the

ColorModel

of this

BufferedImageFilter

**See Also:**
- ImageConsumer.setColorModel(java.awt.image.ColorModel)

---

#### public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Overrides:**
- setPixels

in class

ImageFilter

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
area of pixels to be set
- y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
- w

- the width of the area of pixels
- h

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- off

- the offset into the

pixels

array
- scansize

- the distance from one row of pixels to the next in
the

pixels

array

**Throws:**
- IllegalArgumentException

- if width or height are less than
zero.

**See Also:**
- ImageConsumer.setPixels(int, int, int, int, ColorModel, byte[],
int, int)

---

#### public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Overrides:**
- setPixels

in class

ImageFilter

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
area of pixels to be set
- y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
- w

- the width of the area of pixels
- h

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- off

- the offset into the

pixels

array
- scansize

- the distance from one row of pixels to the next in
the

pixels

array

**Throws:**
- IllegalArgumentException

- if width or height are less than
zero.

**See Also:**
- ImageConsumer.setPixels(int, int, int, int, ColorModel, int[],
int, int)

---

#### public void imageComplete​(int status)

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- imageComplete

in interface

ImageConsumer

**Overrides:**
- imageComplete

in class

ImageFilter

**Parameters:**
- status

- the status of image loading

**Throws:**
- ImagingOpException

- if there was a problem calling the filter
method of the

BufferedImageOp

associated with this
instance.

**See Also:**
- ImageConsumer.imageComplete(int)

---

### Additional Sections

#### Class BufferedImageFilter

java.lang.Object

- java.awt.image.ImageFilter
- - java.awt.image.BufferedImageFilter

java.awt.image.ImageFilter

- java.awt.image.BufferedImageFilter

java.awt.image.BufferedImageFilter

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

```java
public class
BufferedImageFilter

extends
ImageFilter

implements
Cloneable
```

The

BufferedImageFilter

class subclasses an

ImageFilter

to provide a simple means of
using a single-source/single-destination image operator
(

BufferedImageOp

) to filter a

BufferedImage

in the Image Producer/Consumer/Observer
paradigm. Examples of these image operators are:

ConvolveOp

,

AffineTransformOp

and

LookupOp

.

**See Also:** ImageFilter

,

BufferedImage

,

BufferedImageOp

public class

BufferedImageFilter

extends

ImageFilter

implements

Cloneable

The

BufferedImageFilter

class subclasses an

ImageFilter

to provide a simple means of
using a single-source/single-destination image operator
(

BufferedImageOp

) to filter a

BufferedImage

in the Image Producer/Consumer/Observer
paradigm. Examples of these image operators are:

ConvolveOp

,

AffineTransformOp

and

LookupOp

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

ImageFilter

consumer

- Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BufferedImageFilter

​(

BufferedImageOp

op)

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BufferedImageOp

getBufferedImageOp

()

Returns the

BufferedImageOp

.

void

imageComplete

​(int status)

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

void

setColorModel

​(

ColorModel

model)

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

void

setDimensions

​(int width,
int height)

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

resendTopDownLeftRight

,

setHints

,

setProperties

- Methods declared in class java.lang.

Object

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

- Fields declared in class java.awt.image.

ImageFilter

consumer

- Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

---

#### Field Summary

Fields declared in class java.awt.image.

ImageFilter

consumer

---

#### Fields declared in class java.awt.image. ImageFilter

Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

---

#### Fields declared in interface java.awt.image. ImageConsumer

Constructor Summary

Constructors

Constructor

Description

BufferedImageFilter

​(

BufferedImageOp

op)

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

---

#### Constructor Summary

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BufferedImageOp

getBufferedImageOp

()

Returns the

BufferedImageOp

.

void

imageComplete

​(int status)

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

void

setColorModel

​(

ColorModel

model)

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

void

setDimensions

​(int width,
int height)

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

resendTopDownLeftRight

,

setHints

,

setProperties

- Methods declared in class java.lang.

Object

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

Returns the

BufferedImageOp

.

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

resendTopDownLeftRight

,

setHints

,

setProperties

---

#### Methods declared in class java.awt.image. ImageFilter

Methods declared in class java.lang.

Object

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

- BufferedImageFilter

```java
public BufferedImageFilter​(
BufferedImageOp
op)
```

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

**Parameters:** op

- the specified

BufferedImageOp

to
use to filter a

BufferedImage
**Throws:** NullPointerException

- if op is null

============ METHOD DETAIL ==========

- Method Detail

- getBufferedImageOp

```java
public
BufferedImageOp
getBufferedImageOp()
```

Returns the

BufferedImageOp

.

**Returns:** the operator of this

BufferedImageFilter

.

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Overrides:** setDimensions

in class

ImageFilter
**Parameters:** width

- the width to which to set the width of this

BufferedImageFilter
**Parameters:** height

- the height to which to set the height of this

BufferedImageFilter
**See Also:** ImageConsumer.setDimensions(int, int)

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the

ColorModel

to which to set the

ColorModel

of this

BufferedImageFilter
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, byte[],
int, int)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, int[],
int, int)

- imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Overrides:** imageComplete

in class

ImageFilter
**Parameters:** status

- the status of image loading
**Throws:** ImagingOpException

- if there was a problem calling the filter
method of the

BufferedImageOp

associated with this
instance.
**See Also:** ImageConsumer.imageComplete(int)

Constructor Detail

- BufferedImageFilter

```java
public BufferedImageFilter​(
BufferedImageOp
op)
```

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

**Parameters:** op

- the specified

BufferedImageOp

to
use to filter a

BufferedImage
**Throws:** NullPointerException

- if op is null

---

#### Constructor Detail

BufferedImageFilter

```java
public BufferedImageFilter​(
BufferedImageOp
op)
```

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

**Parameters:** op

- the specified

BufferedImageOp

to
use to filter a

BufferedImage
**Throws:** NullPointerException

- if op is null

---

#### BufferedImageFilter

public BufferedImageFilter​(

BufferedImageOp

op)

Constructs a

BufferedImageFilter

with the
specified single-source/single-destination operator.

Method Detail

- getBufferedImageOp

```java
public
BufferedImageOp
getBufferedImageOp()
```

Returns the

BufferedImageOp

.

**Returns:** the operator of this

BufferedImageFilter

.

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Overrides:** setDimensions

in class

ImageFilter
**Parameters:** width

- the width to which to set the width of this

BufferedImageFilter
**Parameters:** height

- the height to which to set the height of this

BufferedImageFilter
**See Also:** ImageConsumer.setDimensions(int, int)

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the

ColorModel

to which to set the

ColorModel

of this

BufferedImageFilter
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, byte[],
int, int)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, int[],
int, int)

- imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Overrides:** imageComplete

in class

ImageFilter
**Parameters:** status

- the status of image loading
**Throws:** ImagingOpException

- if there was a problem calling the filter
method of the

BufferedImageOp

associated with this
instance.
**See Also:** ImageConsumer.imageComplete(int)

---

#### Method Detail

getBufferedImageOp

```java
public
BufferedImageOp
getBufferedImageOp()
```

Returns the

BufferedImageOp

.

**Returns:** the operator of this

BufferedImageFilter

.

---

#### getBufferedImageOp

public

BufferedImageOp

getBufferedImageOp()

Returns the

BufferedImageOp

.

setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Overrides:** setDimensions

in class

ImageFilter
**Parameters:** width

- the width to which to set the width of this

BufferedImageFilter
**Parameters:** height

- the height to which to set the height of this

BufferedImageFilter
**See Also:** ImageConsumer.setDimensions(int, int)

---

#### setDimensions

public void setDimensions​(int width,
int height)

Filters the information provided in the

setDimensions

method
of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are
being filtered. Developers using this class to retrieve pixels from
an image should avoid calling this method directly since that
operation could result in problems with retrieving the requested
pixels.

setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the

ColorModel

to which to set the

ColorModel

of this

BufferedImageFilter
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

---

#### setColorModel

public void setColorModel​(

ColorModel

model)

Filters the information provided in the

setColorModel

method
of the

ImageConsumer

interface.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

If

model

is

null

, this
method clears the current

ColorModel

of this

BufferedImageFilter

.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using this
class to retrieve pixels from an image
should avoid calling this method directly since that
operation could result in problems with retrieving the
requested pixels.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, byte[],
int, int)

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of bytes.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ImageFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**Throws:** IllegalArgumentException

- if width or height are less than
zero.
**See Also:** ImageConsumer.setPixels(int, int, int, int, ColorModel, int[],
int, int)

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Filters the information provided in the

setPixels

method of the

ImageConsumer

interface which takes
an array of integers.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using this class to
retrieve pixels from an image should avoid calling this method
directly since that operation could result in problems
with retrieving the requested pixels.

imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Overrides:** imageComplete

in class

ImageFilter
**Parameters:** status

- the status of image loading
**Throws:** ImagingOpException

- if there was a problem calling the filter
method of the

BufferedImageOp

associated with this
instance.
**See Also:** ImageConsumer.imageComplete(int)

---

#### imageComplete

public void imageComplete​(int status)

Filters the information provided in the

imageComplete

method of the

ImageConsumer

interface.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

---

