# Class RGBImageFilter

**Source:** `java.desktop\java\awt\image\RGBImageFilter.html`

### Class Description

```java
public abstract class
RGBImageFilter

extends
ImageFilter
```

This class provides an easy way to create an ImageFilter which modifies
the pixels of an image in the default RGB ColorModel. It is meant to
be used in conjunction with a FilteredImageSource object to produce
filtered versions of existing images. It is an abstract class that
provides the calls needed to channel all of the pixel data through a
single method which converts pixels one at a time in the default RGB
ColorModel regardless of the ColorModel being used by the ImageProducer.
The only method which needs to be defined to create a useable image
filter is the filterRGB method. Here is an example of a definition
of a filter which swaps the red and blue components of an image:

```java
class RedBlueSwapFilter extends RGBImageFilter {
public RedBlueSwapFilter() {
// The filter's operation does not depend on the
// pixel's location, so IndexColorModels can be
// filtered directly.
canFilterIndexColorModel = true;
}

public int filterRGB(int x, int y, int rgb) {
return ((rgb & 0xff00ff00)
| ((rgb & 0xff0000) >> 16)
| ((rgb & 0xff) << 16));
}
}
```

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

---

### Field Details

#### protected
ColorModel
origmodel

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

---

#### protected
ColorModel
newmodel

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

---

#### protected boolean canFilterIndexColorModel

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering. Subclasses should set this variable to true in their
constructor if their filterRGB method does not depend on the
coordinate of the pixel being filtered.

**See Also:**
- substituteColorModel(java.awt.image.ColorModel, java.awt.image.ColorModel)

,

filterRGB(int, int, int)

,

IndexColorModel

---

### Constructor Details

#### public RGBImageFilter()

*No description found.*

---

### Method Details

#### public void setColorModel​(
ColorModel
model)

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.
If the ColorModel is not an IndexColorModel or is null, this method
overrides the default ColorModel used by the ImageProducer and
specifies the default RGB ColorModel instead.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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

- the specified

ColorModel

**See Also:**
- ImageConsumer

,

ColorModel.getRGBdefault()

---

#### public void substituteColorModel​(
ColorModel
oldcm,

ColorModel
newcm)

Registers two ColorModel objects for substitution. If the oldcm
is encountered during any of the setPixels methods, the newcm
is substituted and the pixels passed through
untouched (but with the new ColorModel object).

**Parameters:**
- oldcm

- the ColorModel object to be replaced on the fly
- newcm

- the ColorModel object to replace oldcm on the fly

---

#### public
IndexColorModel
filterIndexColorModel​(
IndexColorModel
icm)

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide. Uses coordinates of -1 to indicate that
a color table entry is being filtered rather than an actual
pixel value.

**Parameters:**
- icm

- the IndexColorModel object to be filtered

**Returns:**
- a new IndexColorModel representing the filtered colors

**Throws:**
- NullPointerException

- if

icm

is null

---

#### public void filterRGBPixels​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

**Parameters:**
- x

- the X coordinate of the upper-left corner of the region
of pixels
- y

- the Y coordinate of the upper-left corner of the region
of pixels
- w

- the width of the region of pixels
- h

- the height of the region of pixels
- pixels

- the array of pixels
- off

- the offset into the

pixels

array
- scansize

- the distance from one row of pixels to the next
in the array

**See Also:**
- ColorModel.getRGBdefault()

,

filterRGB(int, int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel. Otherwise converts the buffer of byte
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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

**See Also:**
- ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.
Converts a buffer of integer pixels to the default RGB ColorModel
and passes the converted buffer to the filterRGBPixels method.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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

**See Also:**
- ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

---

#### public abstract int filterRGB​(int x,
int y,
int rgb)

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

**Parameters:**
- x

- the X coordinate of the pixel
- y

- the Y coordinate of the pixel
- rgb

- the integer pixel representation in the default RGB
color model

**Returns:**
- a filtered pixel in the default RGB color model.

**See Also:**
- ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

---

### Additional Sections

#### Class RGBImageFilter

java.lang.Object

- java.awt.image.ImageFilter
- - java.awt.image.RGBImageFilter

java.awt.image.ImageFilter

- java.awt.image.RGBImageFilter

java.awt.image.RGBImageFilter

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

**Direct Known Subclasses:** GrayFilter

```java
public abstract class
RGBImageFilter

extends
ImageFilter
```

This class provides an easy way to create an ImageFilter which modifies
the pixels of an image in the default RGB ColorModel. It is meant to
be used in conjunction with a FilteredImageSource object to produce
filtered versions of existing images. It is an abstract class that
provides the calls needed to channel all of the pixel data through a
single method which converts pixels one at a time in the default RGB
ColorModel regardless of the ColorModel being used by the ImageProducer.
The only method which needs to be defined to create a useable image
filter is the filterRGB method. Here is an example of a definition
of a filter which swaps the red and blue components of an image:

```java
class RedBlueSwapFilter extends RGBImageFilter {
public RedBlueSwapFilter() {
// The filter's operation does not depend on the
// pixel's location, so IndexColorModels can be
// filtered directly.
canFilterIndexColorModel = true;
}

public int filterRGB(int x, int y, int rgb) {
return ((rgb & 0xff00ff00)
| ((rgb & 0xff0000) >> 16)
| ((rgb & 0xff) << 16));
}
}
```

**See Also:** FilteredImageSource

,

ImageFilter

,

ColorModel.getRGBdefault()

public abstract class

RGBImageFilter

extends

ImageFilter

This class provides an easy way to create an ImageFilter which modifies
the pixels of an image in the default RGB ColorModel. It is meant to
be used in conjunction with a FilteredImageSource object to produce
filtered versions of existing images. It is an abstract class that
provides the calls needed to channel all of the pixel data through a
single method which converts pixels one at a time in the default RGB
ColorModel regardless of the ColorModel being used by the ImageProducer.
The only method which needs to be defined to create a useable image
filter is the filterRGB method. Here is an example of a definition
of a filter which swaps the red and blue components of an image:

```java
class RedBlueSwapFilter extends RGBImageFilter {
public RedBlueSwapFilter() {
// The filter's operation does not depend on the
// pixel's location, so IndexColorModels can be
// filtered directly.
canFilterIndexColorModel = true;
}

public int filterRGB(int x, int y, int rgb) {
return ((rgb & 0xff00ff00)
| ((rgb & 0xff0000) >> 16)
| ((rgb & 0xff) << 16));
}
}
```

class RedBlueSwapFilter extends RGBImageFilter {
public RedBlueSwapFilter() {
// The filter's operation does not depend on the
// pixel's location, so IndexColorModels can be
// filtered directly.
canFilterIndexColorModel = true;
}

public int filterRGB(int x, int y, int rgb) {
return ((rgb & 0xff00ff00)
| ((rgb & 0xff0000) >> 16)
| ((rgb & 0xff) << 16));
}
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

canFilterIndexColorModel

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering.

protected

ColorModel

newmodel

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

protected

ColorModel

origmodel

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

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

RGBImageFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

IndexColorModel

filterIndexColorModel

​(

IndexColorModel

icm)

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide.

abstract int

filterRGB

​(int x,
int y,
int rgb)

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

void

filterRGBPixels

​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

void

setColorModel

​(

ColorModel

model)

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel.

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

void

substituteColorModel

​(

ColorModel

oldcm,

ColorModel

newcm)

Registers two ColorModel objects for substitution.

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setDimensions

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

Fields

Modifier and Type

Field

Description

protected boolean

canFilterIndexColorModel

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering.

protected

ColorModel

newmodel

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

protected

ColorModel

origmodel

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

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

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering.

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

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

RGBImageFilter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

IndexColorModel

filterIndexColorModel

​(

IndexColorModel

icm)

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide.

abstract int

filterRGB

​(int x,
int y,
int rgb)

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

void

filterRGBPixels

​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

void

setColorModel

​(

ColorModel

model)

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel.

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

void

substituteColorModel

​(

ColorModel

oldcm,

ColorModel

newcm)

Registers two ColorModel objects for substitution.

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setDimensions

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

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide.

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel.

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Registers two ColorModel objects for substitution.

Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setDimensions

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

============ FIELD DETAIL ===========

- Field Detail

- origmodel

```java
protected
ColorModel
origmodel
```

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

- newmodel

```java
protected
ColorModel
newmodel
```

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

- canFilterIndexColorModel

```java
protected boolean canFilterIndexColorModel
```

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering. Subclasses should set this variable to true in their
constructor if their filterRGB method does not depend on the
coordinate of the pixel being filtered.

**See Also:** substituteColorModel(java.awt.image.ColorModel, java.awt.image.ColorModel)

,

filterRGB(int, int, int)

,

IndexColorModel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RGBImageFilter

```java
public RGBImageFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.
If the ColorModel is not an IndexColorModel or is null, this method
overrides the default ColorModel used by the ImageProducer and
specifies the default RGB ColorModel instead.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer

,

ColorModel.getRGBdefault()

- substituteColorModel

```java
public void substituteColorModel​(
ColorModel
oldcm,

ColorModel
newcm)
```

Registers two ColorModel objects for substitution. If the oldcm
is encountered during any of the setPixels methods, the newcm
is substituted and the pixels passed through
untouched (but with the new ColorModel object).

**Parameters:** oldcm

- the ColorModel object to be replaced on the fly
**Parameters:** newcm

- the ColorModel object to replace oldcm on the fly

- filterIndexColorModel

```java
public
IndexColorModel
filterIndexColorModel​(
IndexColorModel
icm)
```

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide. Uses coordinates of -1 to indicate that
a color table entry is being filtered rather than an actual
pixel value.

**Parameters:** icm

- the IndexColorModel object to be filtered
**Returns:** a new IndexColorModel representing the filtered colors
**Throws:** NullPointerException

- if

icm

is null

- filterRGBPixels

```java
public void filterRGBPixels​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)
```

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

**Parameters:** x

- the X coordinate of the upper-left corner of the region
of pixels
**Parameters:** y

- the Y coordinate of the upper-left corner of the region
of pixels
**Parameters:** w

- the width of the region of pixels
**Parameters:** h

- the height of the region of pixels
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next
in the array
**See Also:** ColorModel.getRGBdefault()

,

filterRGB(int, int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel. Otherwise converts the buffer of byte
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.
Converts a buffer of integer pixels to the default RGB ColorModel
and passes the converted buffer to the filterRGBPixels method.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

- filterRGB

```java
public abstract int filterRGB​(int x,
int y,
int rgb)
```

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

**Parameters:** x

- the X coordinate of the pixel
**Parameters:** y

- the Y coordinate of the pixel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Returns:** a filtered pixel in the default RGB color model.
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

Field Detail

- origmodel

```java
protected
ColorModel
origmodel
```

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

- newmodel

```java
protected
ColorModel
newmodel
```

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

- canFilterIndexColorModel

```java
protected boolean canFilterIndexColorModel
```

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering. Subclasses should set this variable to true in their
constructor if their filterRGB method does not depend on the
coordinate of the pixel being filtered.

**See Also:** substituteColorModel(java.awt.image.ColorModel, java.awt.image.ColorModel)

,

filterRGB(int, int, int)

,

IndexColorModel

---

#### Field Detail

origmodel

```java
protected
ColorModel
origmodel
```

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

---

#### origmodel

protected

ColorModel

origmodel

The

ColorModel

to be replaced by

newmodel

when the user calls

substituteColorModel

.

newmodel

```java
protected
ColorModel
newmodel
```

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

---

#### newmodel

protected

ColorModel

newmodel

The

ColorModel

with which to
replace

origmodel

when the user calls

substituteColorModel

.

canFilterIndexColorModel

```java
protected boolean canFilterIndexColorModel
```

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering. Subclasses should set this variable to true in their
constructor if their filterRGB method does not depend on the
coordinate of the pixel being filtered.

**See Also:** substituteColorModel(java.awt.image.ColorModel, java.awt.image.ColorModel)

,

filterRGB(int, int, int)

,

IndexColorModel

---

#### canFilterIndexColorModel

protected boolean canFilterIndexColorModel

This boolean indicates whether or not it is acceptable to apply
the color filtering of the filterRGB method to the color table
entries of an IndexColorModel object in lieu of pixel by pixel
filtering. Subclasses should set this variable to true in their
constructor if their filterRGB method does not depend on the
coordinate of the pixel being filtered.

Constructor Detail

- RGBImageFilter

```java
public RGBImageFilter()
```

---

#### Constructor Detail

RGBImageFilter

```java
public RGBImageFilter()
```

---

#### RGBImageFilter

public RGBImageFilter()

Method Detail

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.
If the ColorModel is not an IndexColorModel or is null, this method
overrides the default ColorModel used by the ImageProducer and
specifies the default RGB ColorModel instead.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer

,

ColorModel.getRGBdefault()

- substituteColorModel

```java
public void substituteColorModel​(
ColorModel
oldcm,

ColorModel
newcm)
```

Registers two ColorModel objects for substitution. If the oldcm
is encountered during any of the setPixels methods, the newcm
is substituted and the pixels passed through
untouched (but with the new ColorModel object).

**Parameters:** oldcm

- the ColorModel object to be replaced on the fly
**Parameters:** newcm

- the ColorModel object to replace oldcm on the fly

- filterIndexColorModel

```java
public
IndexColorModel
filterIndexColorModel​(
IndexColorModel
icm)
```

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide. Uses coordinates of -1 to indicate that
a color table entry is being filtered rather than an actual
pixel value.

**Parameters:** icm

- the IndexColorModel object to be filtered
**Returns:** a new IndexColorModel representing the filtered colors
**Throws:** NullPointerException

- if

icm

is null

- filterRGBPixels

```java
public void filterRGBPixels​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)
```

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

**Parameters:** x

- the X coordinate of the upper-left corner of the region
of pixels
**Parameters:** y

- the Y coordinate of the upper-left corner of the region
of pixels
**Parameters:** w

- the width of the region of pixels
**Parameters:** h

- the height of the region of pixels
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next
in the array
**See Also:** ColorModel.getRGBdefault()

,

filterRGB(int, int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel. Otherwise converts the buffer of byte
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.
Converts a buffer of integer pixels to the default RGB ColorModel
and passes the converted buffer to the filterRGBPixels method.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

- filterRGB

```java
public abstract int filterRGB​(int x,
int y,
int rgb)
```

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

**Parameters:** x

- the X coordinate of the pixel
**Parameters:** y

- the Y coordinate of the pixel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Returns:** a filtered pixel in the default RGB color model.
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

---

#### Method Detail

setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.
If the ColorModel is not an IndexColorModel or is null, this method
overrides the default ColorModel used by the ImageProducer and
specifies the default RGB ColorModel instead.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setColorModel

in interface

ImageConsumer
**Overrides:** setColorModel

in class

ImageFilter
**Parameters:** model

- the specified

ColorModel
**See Also:** ImageConsumer

,

ColorModel.getRGBdefault()

---

#### setColorModel

public void setColorModel​(

ColorModel

model)

If the ColorModel is an IndexColorModel and the subclass has
set the canFilterIndexColorModel flag to true, we substitute
a filtered version of the color model here and wherever
that original ColorModel object appears in the setPixels methods.
If the ColorModel is not an IndexColorModel or is null, this method
overrides the default ColorModel used by the ImageProducer and
specifies the default RGB ColorModel instead.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

substituteColorModel

```java
public void substituteColorModel​(
ColorModel
oldcm,

ColorModel
newcm)
```

Registers two ColorModel objects for substitution. If the oldcm
is encountered during any of the setPixels methods, the newcm
is substituted and the pixels passed through
untouched (but with the new ColorModel object).

**Parameters:** oldcm

- the ColorModel object to be replaced on the fly
**Parameters:** newcm

- the ColorModel object to replace oldcm on the fly

---

#### substituteColorModel

public void substituteColorModel​(

ColorModel

oldcm,

ColorModel

newcm)

Registers two ColorModel objects for substitution. If the oldcm
is encountered during any of the setPixels methods, the newcm
is substituted and the pixels passed through
untouched (but with the new ColorModel object).

filterIndexColorModel

```java
public
IndexColorModel
filterIndexColorModel​(
IndexColorModel
icm)
```

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide. Uses coordinates of -1 to indicate that
a color table entry is being filtered rather than an actual
pixel value.

**Parameters:** icm

- the IndexColorModel object to be filtered
**Returns:** a new IndexColorModel representing the filtered colors
**Throws:** NullPointerException

- if

icm

is null

---

#### filterIndexColorModel

public

IndexColorModel

filterIndexColorModel​(

IndexColorModel

icm)

Filters an IndexColorModel object by running each entry in its
color tables through the filterRGB function that RGBImageFilter
subclasses must provide. Uses coordinates of -1 to indicate that
a color table entry is being filtered rather than an actual
pixel value.

filterRGBPixels

```java
public void filterRGBPixels​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)
```

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

**Parameters:** x

- the X coordinate of the upper-left corner of the region
of pixels
**Parameters:** y

- the Y coordinate of the upper-left corner of the region
of pixels
**Parameters:** w

- the width of the region of pixels
**Parameters:** h

- the height of the region of pixels
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next
in the array
**See Also:** ColorModel.getRGBdefault()

,

filterRGB(int, int, int)

---

#### filterRGBPixels

public void filterRGBPixels​(int x,
int y,
int w,
int h,
int[] pixels,
int off,
int scansize)

Filters a buffer of pixels in the default RGB ColorModel by passing
them one by one through the filterRGB method.

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel. Otherwise converts the buffer of byte
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel. Otherwise converts the buffer of byte
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.
Converts a buffer of integer pixels to the default RGB ColorModel
and passes the converted buffer to the filterRGBPixels method.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

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
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

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

If the ColorModel object is the same one that has already
been converted, then simply passes the pixels through with the
converted ColorModel, otherwise converts the buffer of integer
pixels to the default RGB ColorModel and passes the converted
buffer to the filterRGBPixels method to be converted one by one.
Converts a buffer of integer pixels to the default RGB ColorModel
and passes the converted buffer to the filterRGBPixels method.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels
are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

filterRGB

```java
public abstract int filterRGB​(int x,
int y,
int rgb)
```

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

**Parameters:** x

- the X coordinate of the pixel
**Parameters:** y

- the Y coordinate of the pixel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Returns:** a filtered pixel in the default RGB color model.
**See Also:** ColorModel.getRGBdefault()

,

filterRGBPixels(int, int, int, int, int[], int, int)

---

#### filterRGB

public abstract int filterRGB​(int x,
int y,
int rgb)

Subclasses must specify a method to convert a single input pixel
in the default RGB ColorModel to a single output pixel.

---

