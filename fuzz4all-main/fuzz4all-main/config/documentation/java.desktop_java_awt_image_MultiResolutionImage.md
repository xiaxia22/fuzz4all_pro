# Interface MultiResolutionImage

**Source:** `java.desktop\java\awt\image\MultiResolutionImage.html`

### Class Description

```java
public interface
MultiResolutionImage
```

This interface is designed to be an optional additional API supported by
some implementations of

Image

to allow them to provide
alternate images for various rendering resolutions. The various

Graphics.drawImage(...)

variant methods will consult the methods
of this interface if it is implemented on the argument

Image

object
in order to choose the best representation to use for each rendering operation.

The

MultiResolutionImage

interface should be implemented by any
subclass of

java.awt.Image

whose instances are intended to provide
image resolution variants according to the given image width and height.
For convenience, toolkit images obtained from

Toolkit.getImage(String name)

and

Toolkit.getImage(URL url)

will implement this interface on platforms that support naming conventions
for resolution variants of stored image media and the

AbstractMultiResolutionImage

and

BaseMultiResolutionImage

classes are provided to facilitate easy construction of custom multi-resolution
images from a list of related images.

**All Known Implementing Classes:** AbstractMultiResolutionImage

,

BaseMultiResolutionImage

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Image
getResolutionVariant​(double destImageWidth,
double destImageHeight)

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

**Parameters:**
- destImageWidth

- the width of the destination image, in pixels.
- destImageHeight

- the height of the destination image, in pixels.

**Returns:**
- image resolution variant.

**Throws:**
- IllegalArgumentException

- if

destImageWidth

or

destImageHeight

is less than or equal to zero, infinity,
or NaN.

**Since:**
- 9

---

#### List
<
Image
> getResolutionVariants()

Gets a readable list of all resolution variants.
The list must be nonempty and contain at least one resolution variant.

Note that many implementations might return an unmodifiable list.

**Returns:**
- list of resolution variants.

**Since:**
- 9

---

### Additional Sections

#### Interface MultiResolutionImage

**All Known Implementing Classes:** AbstractMultiResolutionImage

,

BaseMultiResolutionImage

```java
public interface
MultiResolutionImage
```

This interface is designed to be an optional additional API supported by
some implementations of

Image

to allow them to provide
alternate images for various rendering resolutions. The various

Graphics.drawImage(...)

variant methods will consult the methods
of this interface if it is implemented on the argument

Image

object
in order to choose the best representation to use for each rendering operation.

The

MultiResolutionImage

interface should be implemented by any
subclass of

java.awt.Image

whose instances are intended to provide
image resolution variants according to the given image width and height.
For convenience, toolkit images obtained from

Toolkit.getImage(String name)

and

Toolkit.getImage(URL url)

will implement this interface on platforms that support naming conventions
for resolution variants of stored image media and the

AbstractMultiResolutionImage

and

BaseMultiResolutionImage

classes are provided to facilitate easy construction of custom multi-resolution
images from a list of related images.

**Since:** 9
**See Also:** Image

,

AbstractMultiResolutionImage

,

BaseMultiResolutionImage

,

Toolkit.getImage(java.lang.String filename)

,

Toolkit.getImage(java.net.URL url)

public interface

MultiResolutionImage

This interface is designed to be an optional additional API supported by
some implementations of

Image

to allow them to provide
alternate images for various rendering resolutions. The various

Graphics.drawImage(...)

variant methods will consult the methods
of this interface if it is implemented on the argument

Image

object
in order to choose the best representation to use for each rendering operation.

The

MultiResolutionImage

interface should be implemented by any
subclass of

java.awt.Image

whose instances are intended to provide
image resolution variants according to the given image width and height.
For convenience, toolkit images obtained from

Toolkit.getImage(String name)

and

Toolkit.getImage(URL url)

will implement this interface on platforms that support naming conventions
for resolution variants of stored image media and the

AbstractMultiResolutionImage

and

BaseMultiResolutionImage

classes are provided to facilitate easy construction of custom multi-resolution
images from a list of related images.

The

MultiResolutionImage

interface should be implemented by any
subclass of

java.awt.Image

whose instances are intended to provide
image resolution variants according to the given image width and height.
For convenience, toolkit images obtained from

Toolkit.getImage(String name)

and

Toolkit.getImage(URL url)

will implement this interface on platforms that support naming conventions
for resolution variants of stored image media and the

AbstractMultiResolutionImage

and

BaseMultiResolutionImage

classes are provided to facilitate easy construction of custom multi-resolution
images from a list of related images.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Image

getResolutionVariant

​(double destImageWidth,
double destImageHeight)

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

List

<

Image

>

getResolutionVariants

()

Gets a readable list of all resolution variants.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Image

getResolutionVariant

​(double destImageWidth,
double destImageHeight)

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

List

<

Image

>

getResolutionVariants

()

Gets a readable list of all resolution variants.

---

#### Method Summary

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

Gets a readable list of all resolution variants.

============ METHOD DETAIL ==========

- Method Detail

- getResolutionVariant

```java
Image
getResolutionVariant​(double destImageWidth,
double destImageHeight)
```

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

**Parameters:** destImageWidth

- the width of the destination image, in pixels.
**Parameters:** destImageHeight

- the height of the destination image, in pixels.
**Returns:** image resolution variant.
**Throws:** IllegalArgumentException

- if

destImageWidth

or

destImageHeight

is less than or equal to zero, infinity,
or NaN.
**Since:** 9

- getResolutionVariants

```java
List
<
Image
> getResolutionVariants()
```

Gets a readable list of all resolution variants.
The list must be nonempty and contain at least one resolution variant.

Note that many implementations might return an unmodifiable list.

**Returns:** list of resolution variants.
**Since:** 9

Method Detail

- getResolutionVariant

```java
Image
getResolutionVariant​(double destImageWidth,
double destImageHeight)
```

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

**Parameters:** destImageWidth

- the width of the destination image, in pixels.
**Parameters:** destImageHeight

- the height of the destination image, in pixels.
**Returns:** image resolution variant.
**Throws:** IllegalArgumentException

- if

destImageWidth

or

destImageHeight

is less than or equal to zero, infinity,
or NaN.
**Since:** 9

- getResolutionVariants

```java
List
<
Image
> getResolutionVariants()
```

Gets a readable list of all resolution variants.
The list must be nonempty and contain at least one resolution variant.

Note that many implementations might return an unmodifiable list.

**Returns:** list of resolution variants.
**Since:** 9

---

#### Method Detail

getResolutionVariant

```java
Image
getResolutionVariant​(double destImageWidth,
double destImageHeight)
```

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

**Parameters:** destImageWidth

- the width of the destination image, in pixels.
**Parameters:** destImageHeight

- the height of the destination image, in pixels.
**Returns:** image resolution variant.
**Throws:** IllegalArgumentException

- if

destImageWidth

or

destImageHeight

is less than or equal to zero, infinity,
or NaN.
**Since:** 9

---

#### getResolutionVariant

Image

getResolutionVariant​(double destImageWidth,
double destImageHeight)

Gets a specific image that is the best variant to represent
this logical image at the indicated size.

getResolutionVariants

```java
List
<
Image
> getResolutionVariants()
```

Gets a readable list of all resolution variants.
The list must be nonempty and contain at least one resolution variant.

Note that many implementations might return an unmodifiable list.

**Returns:** list of resolution variants.
**Since:** 9

---

#### getResolutionVariants

List

<

Image

> getResolutionVariants()

Gets a readable list of all resolution variants.
The list must be nonempty and contain at least one resolution variant.

Note that many implementations might return an unmodifiable list.

Note that many implementations might return an unmodifiable list.

---

