# Class GrayFilter

**Source:** `java.desktop\javax\swing\GrayFilter.html`

### Class Description

```java
public class
GrayFilter

extends
RGBImageFilter
```

An image filter that "disables" an image by turning
it into a grayscale image, and brightening the pixels
in the image. Used by buttons to create an image for
a disabled button.

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public GrayFilter​(boolean b,
int p)

Constructs a GrayFilter object that filters a color image to a
grayscale image. Used by buttons to create disabled ("grayed out")
button images.

**Parameters:**
- b

- a boolean -- true if the pixels should be brightened
- p

- an int in the range 0..100 that determines the percentage
of gray, where 100 is the darkest gray, and 0 is the lightest

---

### Method Details

#### public static
Image
createDisabledImage​(
Image
i)

Creates a disabled image

**Parameters:**
- i

- an

Image

to be created as disabled

**Returns:**
- the new grayscale image created from

i

---

#### public int filterRGB​(int x,
int y,
int rgb)

Overrides

RGBImageFilter.filterRGB

.

**Specified by:**
- filterRGB

in class

RGBImageFilter

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

RGBImageFilter.filterRGBPixels(int, int, int, int, int[], int, int)

---

### Additional Sections

#### Class GrayFilter

java.lang.Object

- java.awt.image.ImageFilter
- - java.awt.image.RGBImageFilter
- - javax.swing.GrayFilter

java.awt.image.ImageFilter

- java.awt.image.RGBImageFilter
- - javax.swing.GrayFilter

java.awt.image.RGBImageFilter

- javax.swing.GrayFilter

javax.swing.GrayFilter

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

```java
public class
GrayFilter

extends
RGBImageFilter
```

An image filter that "disables" an image by turning
it into a grayscale image, and brightening the pixels
in the image. Used by buttons to create an image for
a disabled button.

**Since:** 1.2

public class

GrayFilter

extends

RGBImageFilter

An image filter that "disables" an image by turning
it into a grayscale image, and brightening the pixels
in the image. Used by buttons to create an image for
a disabled button.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

RGBImageFilter

canFilterIndexColorModel

,

newmodel

,

origmodel

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

GrayFilter

​(boolean b,
int p)

Constructs a GrayFilter object that filters a color image to a
grayscale image.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Image

createDisabledImage

​(

Image

i)

Creates a disabled image

int

filterRGB

​(int x,
int y,
int rgb)

Overrides

RGBImageFilter.filterRGB

.

- Methods declared in class java.awt.image.

RGBImageFilter

filterIndexColorModel

,

filterRGBPixels

,

setColorModel

,

setPixels

,

setPixels

,

substituteColorModel

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

- Fields declared in class java.awt.image.

RGBImageFilter

canFilterIndexColorModel

,

newmodel

,

origmodel

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

RGBImageFilter

canFilterIndexColorModel

,

newmodel

,

origmodel

---

#### Fields declared in class java.awt.image. RGBImageFilter

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

GrayFilter

​(boolean b,
int p)

Constructs a GrayFilter object that filters a color image to a
grayscale image.

---

#### Constructor Summary

Constructs a GrayFilter object that filters a color image to a
grayscale image.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Image

createDisabledImage

​(

Image

i)

Creates a disabled image

int

filterRGB

​(int x,
int y,
int rgb)

Overrides

RGBImageFilter.filterRGB

.

- Methods declared in class java.awt.image.

RGBImageFilter

filterIndexColorModel

,

filterRGBPixels

,

setColorModel

,

setPixels

,

setPixels

,

substituteColorModel

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

Creates a disabled image

Overrides

RGBImageFilter.filterRGB

.

Methods declared in class java.awt.image.

RGBImageFilter

filterIndexColorModel

,

filterRGBPixels

,

setColorModel

,

setPixels

,

setPixels

,

substituteColorModel

---

#### Methods declared in class java.awt.image. RGBImageFilter

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GrayFilter

```java
public GrayFilter​(boolean b,
int p)
```

Constructs a GrayFilter object that filters a color image to a
grayscale image. Used by buttons to create disabled ("grayed out")
button images.

**Parameters:** b

- a boolean -- true if the pixels should be brightened
**Parameters:** p

- an int in the range 0..100 that determines the percentage
of gray, where 100 is the darkest gray, and 0 is the lightest

============ METHOD DETAIL ==========

- Method Detail

- createDisabledImage

```java
public static
Image
createDisabledImage​(
Image
i)
```

Creates a disabled image

**Parameters:** i

- an

Image

to be created as disabled
**Returns:** the new grayscale image created from

i

- filterRGB

```java
public int filterRGB​(int x,
int y,
int rgb)
```

Overrides

RGBImageFilter.filterRGB

.

**Specified by:** filterRGB

in class

RGBImageFilter
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

RGBImageFilter.filterRGBPixels(int, int, int, int, int[], int, int)

Constructor Detail

- GrayFilter

```java
public GrayFilter​(boolean b,
int p)
```

Constructs a GrayFilter object that filters a color image to a
grayscale image. Used by buttons to create disabled ("grayed out")
button images.

**Parameters:** b

- a boolean -- true if the pixels should be brightened
**Parameters:** p

- an int in the range 0..100 that determines the percentage
of gray, where 100 is the darkest gray, and 0 is the lightest

---

#### Constructor Detail

GrayFilter

```java
public GrayFilter​(boolean b,
int p)
```

Constructs a GrayFilter object that filters a color image to a
grayscale image. Used by buttons to create disabled ("grayed out")
button images.

**Parameters:** b

- a boolean -- true if the pixels should be brightened
**Parameters:** p

- an int in the range 0..100 that determines the percentage
of gray, where 100 is the darkest gray, and 0 is the lightest

---

#### GrayFilter

public GrayFilter​(boolean b,
int p)

Constructs a GrayFilter object that filters a color image to a
grayscale image. Used by buttons to create disabled ("grayed out")
button images.

Method Detail

- createDisabledImage

```java
public static
Image
createDisabledImage​(
Image
i)
```

Creates a disabled image

**Parameters:** i

- an

Image

to be created as disabled
**Returns:** the new grayscale image created from

i

- filterRGB

```java
public int filterRGB​(int x,
int y,
int rgb)
```

Overrides

RGBImageFilter.filterRGB

.

**Specified by:** filterRGB

in class

RGBImageFilter
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

RGBImageFilter.filterRGBPixels(int, int, int, int, int[], int, int)

---

#### Method Detail

createDisabledImage

```java
public static
Image
createDisabledImage​(
Image
i)
```

Creates a disabled image

**Parameters:** i

- an

Image

to be created as disabled
**Returns:** the new grayscale image created from

i

---

#### createDisabledImage

public static

Image

createDisabledImage​(

Image

i)

Creates a disabled image

filterRGB

```java
public int filterRGB​(int x,
int y,
int rgb)
```

Overrides

RGBImageFilter.filterRGB

.

**Specified by:** filterRGB

in class

RGBImageFilter
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

RGBImageFilter.filterRGBPixels(int, int, int, int, int[], int, int)

---

#### filterRGB

public int filterRGB​(int x,
int y,
int rgb)

Overrides

RGBImageFilter.filterRGB

.

---

