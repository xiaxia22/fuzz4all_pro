# Class BaseMultiResolutionImage

**Source:** `java.desktop\java\awt\image\BaseMultiResolutionImage.html`

### Class Description

```java
public class
BaseMultiResolutionImage

extends
AbstractMultiResolutionImage
```

This class is an array-based implementation of
the

AbstractMultiResolutionImage

class.

This class will implement the

getResolutionVariant(double destImageWidth, double destImageHeight)

method using a simple algorithm which will return the first image variant
in the array that is large enough to satisfy the rendering request. The
last image in the array will be returned if no suitable image is found
that is as large as the rendering request.

For best effect the array of images should be sorted with each image being
both wider and taller than the previous image. The base image need not be
the first image in the array. No exception will be thrown if the images
are not sorted as suggested.

**All Implemented Interfaces:** MultiResolutionImage

---

### Field Details

*No entries found.*

### Constructor Details

#### public BaseMultiResolutionImage​(
Image
... resolutionVariants)

Creates a multi-resolution image with the given resolution variants.
The first resolution variant is used as the base image.

**Parameters:**
- resolutionVariants

- array of resolution variants sorted by image size

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
- NullPointerException

- if the specified

resolutionVariants

contains one or more null elements

**Since:**
- 9

---

#### public BaseMultiResolutionImage​(int baseImageIndex,

Image
... resolutionVariants)

Creates a multi-resolution image with the given base image index and
resolution variants.

**Parameters:**
- baseImageIndex

- the index of base image in the resolution variants
array
- resolutionVariants

- array of resolution variants sorted by image size

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
- NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
- IndexOutOfBoundsException

- if

baseImageIndex

is
negative or greater than or equal to

resolutionVariants

length.

**Since:**
- 9

---

### Method Details

*No entries found.*

### Additional Sections

#### Class BaseMultiResolutionImage

java.lang.Object

- java.awt.Image
- - java.awt.image.AbstractMultiResolutionImage
- - java.awt.image.BaseMultiResolutionImage

java.awt.Image

- java.awt.image.AbstractMultiResolutionImage
- - java.awt.image.BaseMultiResolutionImage

java.awt.image.AbstractMultiResolutionImage

- java.awt.image.BaseMultiResolutionImage

java.awt.image.BaseMultiResolutionImage

**All Implemented Interfaces:** MultiResolutionImage

```java
public class
BaseMultiResolutionImage

extends
AbstractMultiResolutionImage
```

This class is an array-based implementation of
the

AbstractMultiResolutionImage

class.

This class will implement the

getResolutionVariant(double destImageWidth, double destImageHeight)

method using a simple algorithm which will return the first image variant
in the array that is large enough to satisfy the rendering request. The
last image in the array will be returned if no suitable image is found
that is as large as the rendering request.

For best effect the array of images should be sorted with each image being
both wider and taller than the previous image. The base image need not be
the first image in the array. No exception will be thrown if the images
are not sorted as suggested.

**Since:** 9
**See Also:** Image

,

MultiResolutionImage

,

AbstractMultiResolutionImage

public class

BaseMultiResolutionImage

extends

AbstractMultiResolutionImage

This class is an array-based implementation of
the

AbstractMultiResolutionImage

class.

This class will implement the

getResolutionVariant(double destImageWidth, double destImageHeight)

method using a simple algorithm which will return the first image variant
in the array that is large enough to satisfy the rendering request. The
last image in the array will be returned if no suitable image is found
that is as large as the rendering request.

For best effect the array of images should be sorted with each image being
both wider and taller than the previous image. The base image need not be
the first image in the array. No exception will be thrown if the images
are not sorted as suggested.

For best effect the array of images should be sorted with each image being
both wider and taller than the previous image. The base image need not be
the first image in the array. No exception will be thrown if the images
are not sorted as suggested.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BaseMultiResolutionImage

​(int baseImageIndex,

Image

... resolutionVariants)

Creates a multi-resolution image with the given base image index and
resolution variants.

BaseMultiResolutionImage

​(

Image

... resolutionVariants)

Creates a multi-resolution image with the given resolution variants.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.awt.image.

AbstractMultiResolutionImage

getBaseImage

,

getGraphics

,

getHeight

,

getProperty

,

getSource

,

getWidth

- Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

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

- Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

Field Summary

- Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

---

#### Field Summary

Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

---

#### Fields declared in class java.awt. Image

Constructor Summary

Constructors

Constructor

Description

BaseMultiResolutionImage

​(int baseImageIndex,

Image

... resolutionVariants)

Creates a multi-resolution image with the given base image index and
resolution variants.

BaseMultiResolutionImage

​(

Image

... resolutionVariants)

Creates a multi-resolution image with the given resolution variants.

---

#### Constructor Summary

Creates a multi-resolution image with the given base image index and
resolution variants.

Creates a multi-resolution image with the given resolution variants.

Method Summary

- Methods declared in class java.awt.image.

AbstractMultiResolutionImage

getBaseImage

,

getGraphics

,

getHeight

,

getProperty

,

getSource

,

getWidth

- Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

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

- Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

---

#### Method Summary

Methods declared in class java.awt.image.

AbstractMultiResolutionImage

getBaseImage

,

getGraphics

,

getHeight

,

getProperty

,

getSource

,

getWidth

---

#### Methods declared in class java.awt.image. AbstractMultiResolutionImage

Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

---

#### Methods declared in class java.awt. Image

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

Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

---

#### Methods declared in interface java.awt.image. MultiResolutionImage

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(
Image
... resolutionVariants)
```

Creates a multi-resolution image with the given resolution variants.
The first resolution variant is used as the base image.

**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Since:** 9

- BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(int baseImageIndex,

Image
... resolutionVariants)
```

Creates a multi-resolution image with the given base image index and
resolution variants.

**Parameters:** baseImageIndex

- the index of base image in the resolution variants
array
**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Throws:** IndexOutOfBoundsException

- if

baseImageIndex

is
negative or greater than or equal to

resolutionVariants

length.
**Since:** 9

Constructor Detail

- BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(
Image
... resolutionVariants)
```

Creates a multi-resolution image with the given resolution variants.
The first resolution variant is used as the base image.

**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Since:** 9

- BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(int baseImageIndex,

Image
... resolutionVariants)
```

Creates a multi-resolution image with the given base image index and
resolution variants.

**Parameters:** baseImageIndex

- the index of base image in the resolution variants
array
**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Throws:** IndexOutOfBoundsException

- if

baseImageIndex

is
negative or greater than or equal to

resolutionVariants

length.
**Since:** 9

---

#### Constructor Detail

BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(
Image
... resolutionVariants)
```

Creates a multi-resolution image with the given resolution variants.
The first resolution variant is used as the base image.

**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Since:** 9

---

#### BaseMultiResolutionImage

public BaseMultiResolutionImage​(

Image

... resolutionVariants)

Creates a multi-resolution image with the given resolution variants.
The first resolution variant is used as the base image.

BaseMultiResolutionImage

```java
public BaseMultiResolutionImage​(int baseImageIndex,

Image
... resolutionVariants)
```

Creates a multi-resolution image with the given base image index and
resolution variants.

**Parameters:** baseImageIndex

- the index of base image in the resolution variants
array
**Parameters:** resolutionVariants

- array of resolution variants sorted by image size
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
**Throws:** NullPointerException

- if the specified

resolutionVariants

contains one or more null elements
**Throws:** IndexOutOfBoundsException

- if

baseImageIndex

is
negative or greater than or equal to

resolutionVariants

length.
**Since:** 9

---

#### BaseMultiResolutionImage

public BaseMultiResolutionImage​(int baseImageIndex,

Image

... resolutionVariants)

Creates a multi-resolution image with the given base image index and
resolution variants.

---

