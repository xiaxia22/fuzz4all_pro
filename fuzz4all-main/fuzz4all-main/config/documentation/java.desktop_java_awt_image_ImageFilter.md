# Class ImageFilter

**Source:** `java.desktop\java\awt\image\ImageFilter.html`

### Class Description

```java
public class
ImageFilter

extends
Object

implements
ImageConsumer
,
Cloneable
```

This class implements a filter for the set of interface methods that
are used to deliver data from an ImageProducer to an ImageConsumer.
It is meant to be used in conjunction with a FilteredImageSource
object to produce filtered versions of existing images. It is a
base class that provides the calls needed to implement a "Null filter"
which has no effect on the data being passed through. Filters should
subclass this class and override the methods which deal with the
data that needs to be filtered and modify it as necessary.

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

---

### Field Details

#### protected
ImageConsumer
consumer

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data. It is not
initialized during the constructor, but rather during the
getFilterInstance() method call when the FilteredImageSource
is creating a unique instance of this object for a particular
image data stream.

**See Also:**
- getFilterInstance(java.awt.image.ImageConsumer)

,

ImageConsumer

---

### Constructor Details

#### public ImageFilter()

*No description found.*

---

### Method Details

#### public
ImageFilter
getFilterInstance​(
ImageConsumer
ic)

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.
The default implementation just clones this object.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Parameters:**
- ic

- the specified

ImageConsumer

**Returns:**
- an

ImageFilter

used to perform the
filtering for the specified

ImageConsumer

.

---

#### public void setDimensions​(int width,
int height)

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setDimensions

in interface

ImageConsumer

**Parameters:**
- width

- the width of the source image
- height

- the height of the source image

**See Also:**
- ImageConsumer.setDimensions(int, int)

---

#### public void setProperties​(
Hashtable
<?,​?> props)

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setProperties

in interface

ImageConsumer

**Parameters:**
- props

- the properties from the source object

**Throws:**
- NullPointerException

- if

props

is null

---

#### public void setColorModel​(
ColorModel
model)

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setColorModel

in interface

ImageConsumer

**Parameters:**
- model

- the specified

ColorModel

**See Also:**
- ImageConsumer.setColorModel(java.awt.image.ColorModel)

---

#### public void setHints​(int hints)

Filters the information provided in the setHints method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setHints

in interface

ImageConsumer

**Parameters:**
- hints

- a set of hints that the ImageConsumer uses to
process the pixels

**See Also:**
- ImageConsumer.setHints(int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setPixels

in interface

ImageConsumer

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

**See Also:**
- ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setPixels

in interface

ImageConsumer

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

**See Also:**
- ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

---

#### public void imageComplete​(int status)

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- imageComplete

in interface

ImageConsumer

**Parameters:**
- status

- the status of image loading

**See Also:**
- ImageConsumer.imageComplete(int)

---

#### public void resendTopDownLeftRight​(
ImageProducer
ip)

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.
When an

ImageConsumer

being fed
by an instance of this

ImageFilter

requests a resend of the data in TDLR order,
the

FilteredImageSource

invokes this method of the

ImageFilter

.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

**Parameters:**
- ip

- the ImageProducer that is feeding this instance of
the filter - also the ImageProducer that the request should be
forwarded to if necessary

**Throws:**
- NullPointerException

- if

ip

is null

**See Also:**
- ImageProducer.requestTopDownLeftRightResend(java.awt.image.ImageConsumer)

---

#### public
Object
clone()

Clones this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class ImageFilter

java.lang.Object

- java.awt.image.ImageFilter

java.awt.image.ImageFilter

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

**Direct Known Subclasses:** BufferedImageFilter

,

CropImageFilter

,

ReplicateScaleFilter

,

RGBImageFilter

```java
public class
ImageFilter

extends
Object

implements
ImageConsumer
,
Cloneable
```

This class implements a filter for the set of interface methods that
are used to deliver data from an ImageProducer to an ImageConsumer.
It is meant to be used in conjunction with a FilteredImageSource
object to produce filtered versions of existing images. It is a
base class that provides the calls needed to implement a "Null filter"
which has no effect on the data being passed through. Filters should
subclass this class and override the methods which deal with the
data that needs to be filtered and modify it as necessary.

**See Also:** FilteredImageSource

,

ImageConsumer

public class

ImageFilter

extends

Object

implements

ImageConsumer

,

Cloneable

This class implements a filter for the set of interface methods that
are used to deliver data from an ImageProducer to an ImageConsumer.
It is meant to be used in conjunction with a FilteredImageSource
object to produce filtered versions of existing images. It is a
base class that provides the calls needed to implement a "Null filter"
which has no effect on the data being passed through. Filters should
subclass this class and override the methods which deal with the
data that needs to be filtered and modify it as necessary.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ImageConsumer

consumer

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data.

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

ImageFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones this object.

ImageFilter

getFilterInstance

​(

ImageConsumer

ic)

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.

void

imageComplete

​(int status)

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

void

resendTopDownLeftRight

​(

ImageProducer

ip)

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.

void

setColorModel

​(

ColorModel

model)

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

void

setDimensions

​(int width,
int height)

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

void

setHints

​(int hints)

Filters the information provided in the setHints method
of the ImageConsumer interface.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

void

setProperties

​(

Hashtable

<?,​?> props)

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

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

Fields

Modifier and Type

Field

Description

protected

ImageConsumer

consumer

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data.

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

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data.

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

ImageFilter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones this object.

ImageFilter

getFilterInstance

​(

ImageConsumer

ic)

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.

void

imageComplete

​(int status)

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

void

resendTopDownLeftRight

​(

ImageProducer

ip)

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.

void

setColorModel

​(

ColorModel

model)

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

void

setDimensions

​(int width,
int height)

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

void

setHints

​(int hints)

Filters the information provided in the setHints method
of the ImageConsumer interface.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

void

setProperties

​(

Hashtable

<?,​?> props)

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

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

Clones this object.

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Filters the information provided in the setHints method
of the ImageConsumer interface.

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

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

============ FIELD DETAIL ===========

- Field Detail

- consumer

```java
protected
ImageConsumer
consumer
```

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data. It is not
initialized during the constructor, but rather during the
getFilterInstance() method call when the FilteredImageSource
is creating a unique instance of this object for a particular
image data stream.

**See Also:** getFilterInstance(java.awt.image.ImageConsumer)

,

ImageConsumer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageFilter

```java
public ImageFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- getFilterInstance

```java
public
ImageFilter
getFilterInstance​(
ImageConsumer
ic)
```

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.
The default implementation just clones this object.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Parameters:** ic

- the specified

ImageConsumer
**Returns:** an

ImageFilter

used to perform the
filtering for the specified

ImageConsumer

.

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image
**See Also:** ImageConsumer.setDimensions(int, int)

- setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the properties from the source object
**Throws:** NullPointerException

- if

props

is null

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

- setHints

```java
public void setHints​(int hints)
```

Filters the information provided in the setHints method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

- imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageConsumer.imageComplete(int)

- resendTopDownLeftRight

```java
public void resendTopDownLeftRight​(
ImageProducer
ip)
```

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.
When an

ImageConsumer

being fed
by an instance of this

ImageFilter

requests a resend of the data in TDLR order,
the

FilteredImageSource

invokes this method of the

ImageFilter

.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

**Parameters:** ip

- the ImageProducer that is feeding this instance of
the filter - also the ImageProducer that the request should be
forwarded to if necessary
**Throws:** NullPointerException

- if

ip

is null
**See Also:** ImageProducer.requestTopDownLeftRightResend(java.awt.image.ImageConsumer)

- clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

Field Detail

- consumer

```java
protected
ImageConsumer
consumer
```

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data. It is not
initialized during the constructor, but rather during the
getFilterInstance() method call when the FilteredImageSource
is creating a unique instance of this object for a particular
image data stream.

**See Also:** getFilterInstance(java.awt.image.ImageConsumer)

,

ImageConsumer

---

#### Field Detail

consumer

```java
protected
ImageConsumer
consumer
```

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data. It is not
initialized during the constructor, but rather during the
getFilterInstance() method call when the FilteredImageSource
is creating a unique instance of this object for a particular
image data stream.

**See Also:** getFilterInstance(java.awt.image.ImageConsumer)

,

ImageConsumer

---

#### consumer

protected

ImageConsumer

consumer

The consumer of the particular image data stream for which this
instance of the ImageFilter is filtering data. It is not
initialized during the constructor, but rather during the
getFilterInstance() method call when the FilteredImageSource
is creating a unique instance of this object for a particular
image data stream.

Constructor Detail

- ImageFilter

```java
public ImageFilter()
```

---

#### Constructor Detail

ImageFilter

```java
public ImageFilter()
```

---

#### ImageFilter

public ImageFilter()

Method Detail

- getFilterInstance

```java
public
ImageFilter
getFilterInstance​(
ImageConsumer
ic)
```

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.
The default implementation just clones this object.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Parameters:** ic

- the specified

ImageConsumer
**Returns:** an

ImageFilter

used to perform the
filtering for the specified

ImageConsumer

.

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image
**See Also:** ImageConsumer.setDimensions(int, int)

- setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the properties from the source object
**Throws:** NullPointerException

- if

props

is null

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

- setHints

```java
public void setHints​(int hints)
```

Filters the information provided in the setHints method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

- imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageConsumer.imageComplete(int)

- resendTopDownLeftRight

```java
public void resendTopDownLeftRight​(
ImageProducer
ip)
```

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.
When an

ImageConsumer

being fed
by an instance of this

ImageFilter

requests a resend of the data in TDLR order,
the

FilteredImageSource

invokes this method of the

ImageFilter

.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

**Parameters:** ip

- the ImageProducer that is feeding this instance of
the filter - also the ImageProducer that the request should be
forwarded to if necessary
**Throws:** NullPointerException

- if

ip

is null
**See Also:** ImageProducer.requestTopDownLeftRightResend(java.awt.image.ImageConsumer)

- clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### Method Detail

getFilterInstance

```java
public
ImageFilter
getFilterInstance​(
ImageConsumer
ic)
```

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.
The default implementation just clones this object.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Parameters:** ic

- the specified

ImageConsumer
**Returns:** an

ImageFilter

used to perform the
filtering for the specified

ImageConsumer

.

---

#### getFilterInstance

public

ImageFilter

getFilterInstance​(

ImageConsumer

ic)

Returns a unique instance of an ImageFilter object which will
actually perform the filtering for the specified ImageConsumer.
The default implementation just clones this object.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setDimensions

```java
public void setDimensions​(int width,
int height)
```

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image
**See Also:** ImageConsumer.setDimensions(int, int)

---

#### setDimensions

public void setDimensions​(int width,
int height)

Filters the information provided in the setDimensions method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the properties from the source object
**Throws:** NullPointerException

- if

props

is null

---

#### setProperties

public void setProperties​(

Hashtable

<?,​?> props)

Passes the properties from the source object along after adding a
property indicating the stream of filters it has been run through.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer.setColorModel(java.awt.image.ColorModel)

---

#### setColorModel

public void setColorModel​(

ColorModel

model)

Filter the information provided in the setColorModel method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setHints

```java
public void setHints​(int hints)
```

Filters the information provided in the setHints method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

---

#### setHints

public void setHints​(int hints)

Filters the information provided in the setHints method
of the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of bytes.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
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
**See Also:** ImageConsumer.setPixels(int, int, int, int, java.awt.image.ColorModel, byte[], int, int)

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

Filters the information provided in the setPixels method of the
ImageConsumer interface which takes an array of integers.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

imageComplete

```java
public void imageComplete​(int status)
```

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageConsumer.imageComplete(int)

---

#### imageComplete

public void imageComplete​(int status)

Filters the information provided in the imageComplete method of
the ImageConsumer interface.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

resendTopDownLeftRight

```java
public void resendTopDownLeftRight​(
ImageProducer
ip)
```

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.
When an

ImageConsumer

being fed
by an instance of this

ImageFilter

requests a resend of the data in TDLR order,
the

FilteredImageSource

invokes this method of the

ImageFilter

.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

**Parameters:** ip

- the ImageProducer that is feeding this instance of
the filter - also the ImageProducer that the request should be
forwarded to if necessary
**Throws:** NullPointerException

- if

ip

is null
**See Also:** ImageProducer.requestTopDownLeftRightResend(java.awt.image.ImageConsumer)

---

#### resendTopDownLeftRight

public void resendTopDownLeftRight​(

ImageProducer

ip)

Responds to a request for a TopDownLeftRight (TDLR) ordered resend
of the pixel data from an

ImageConsumer

.
When an

ImageConsumer

being fed
by an instance of this

ImageFilter

requests a resend of the data in TDLR order,
the

FilteredImageSource

invokes this method of the

ImageFilter

.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

An

ImageFilter

subclass might override this method or not,
depending on if and how it can send data in TDLR order.
Three possibilities exist:

- Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

Do not override this method.
This makes the subclass use the default implementation,
which is to
forward the request
to the indicated

ImageProducer

using this filter as the requesting

ImageConsumer

.
This behavior
is appropriate if the filter can determine
that it will forward the pixels
in TDLR order if its upstream producer object
sends them in TDLR order.

Override the method to simply send the data.
This is appropriate if the filter can handle the request itself —
for example,
if the generated pixels have been saved in some sort of buffer.

Override the method to do nothing.
This is appropriate
if the filter cannot produce filtered data in TDLR order.

clone

```java
public
Object
clone()
```

Clones this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clones this object.

---

