# Interface RenderableImage

**Source:** `java.desktop\java\awt\image\renderable\RenderableImage.html`

### Class Description

```java
public interface
RenderableImage
```

A RenderableImage is a common interface for rendering-independent
images (a notion which subsumes resolution independence). That is,
images which are described and have operations applied to them
independent of any specific rendering of the image. For example, a
RenderableImage can be rotated and cropped in
resolution-independent terms. Then, it can be rendered for various
specific contexts, such as a draft preview, a high-quality screen
display, or a printer, each in an optimal fashion.

A RenderedImage is returned from a RenderableImage via the
createRendering() method, which takes a RenderContext. The
RenderContext specifies how the RenderedImage should be
constructed. Note that it is not possible to extract pixels
directly from a RenderableImage.

The createDefaultRendering() and createScaledRendering() methods are
convenience methods that construct an appropriate RenderContext
internally. All of the rendering methods may return a reference to a
previously produced rendering.

**All Known Implementing Classes:** RenderableImageOp

---

### Field Details

#### static final
String
HINTS_OBSERVED

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods. If such a property exists,
the value of the property will be a RenderingHints object
specifying which hints were observed in creating the rendering.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Vector
<
RenderableImage
> getSources()

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Returns:**
- a (possibly empty) Vector of RenderableImages, or null.

---

#### Object
getProperty​(
String
name)

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Parameters:**
- name

- the name of the property to get, as a String.

**Returns:**
- a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

---

#### String
[] getPropertyNames()

Returns a list of names recognized by getProperty.

**Returns:**
- a list of property names.

---

#### boolean isDynamic()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:**
- true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

---

#### float getWidth()

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Returns:**
- the width of the image in user coordinates.

---

#### float getHeight()

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Returns:**
- the height of the image in user coordinates.

---

#### float getMinX()

Gets the minimum X coordinate of the rendering-independent image data.

**Returns:**
- the minimum X coordinate of the rendering-independent image
data.

---

#### float getMinY()

Gets the minimum Y coordinate of the rendering-independent image data.

**Returns:**
- the minimum Y coordinate of the rendering-independent image
data.

---

#### RenderedImage
createScaledRendering​(int w,
int h,

RenderingHints
hints)

Creates a RenderedImage instance of this image with width w, and
height h in pixels. The RenderContext is built automatically
with an appropriate usr2dev transform and an area of interest
of the full image. All the rendering hints come from hints
passed in.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:**
- w

- the width of rendered image in pixels, or 0.
- h

- the height of rendered image in pixels, or 0.
- hints

- a RenderingHints object containing hints.

**Returns:**
- a RenderedImage containing the rendered data.

---

#### RenderedImage
createDefaultRendering()

Returns a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. The rendering hints are
empty. createDefaultRendering may make use of a stored
rendering for speed.

**Returns:**
- a RenderedImage containing the rendered data.

---

#### RenderedImage
createRendering​(
RenderContext
renderContext)

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext. This is the most general way to obtain a
rendering of a RenderableImage.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:**
- renderContext

- the RenderContext to use to produce the rendering.

**Returns:**
- a RenderedImage containing the rendered data.

---

### Additional Sections

#### Interface RenderableImage

**All Known Implementing Classes:** RenderableImageOp

```java
public interface
RenderableImage
```

A RenderableImage is a common interface for rendering-independent
images (a notion which subsumes resolution independence). That is,
images which are described and have operations applied to them
independent of any specific rendering of the image. For example, a
RenderableImage can be rotated and cropped in
resolution-independent terms. Then, it can be rendered for various
specific contexts, such as a draft preview, a high-quality screen
display, or a printer, each in an optimal fashion.

A RenderedImage is returned from a RenderableImage via the
createRendering() method, which takes a RenderContext. The
RenderContext specifies how the RenderedImage should be
constructed. Note that it is not possible to extract pixels
directly from a RenderableImage.

The createDefaultRendering() and createScaledRendering() methods are
convenience methods that construct an appropriate RenderContext
internally. All of the rendering methods may return a reference to a
previously produced rendering.

public interface

RenderableImage

A RenderableImage is a common interface for rendering-independent
images (a notion which subsumes resolution independence). That is,
images which are described and have operations applied to them
independent of any specific rendering of the image. For example, a
RenderableImage can be rotated and cropped in
resolution-independent terms. Then, it can be rendered for various
specific contexts, such as a draft preview, a high-quality screen
display, or a printer, each in an optimal fashion.

A RenderedImage is returned from a RenderableImage via the
createRendering() method, which takes a RenderContext. The
RenderContext specifies how the RenderedImage should be
constructed. Note that it is not possible to extract pixels
directly from a RenderableImage.

The createDefaultRendering() and createScaledRendering() methods are
convenience methods that construct an appropriate RenderContext
internally. All of the rendering methods may return a reference to a
previously produced rendering.

A RenderedImage is returned from a RenderableImage via the
createRendering() method, which takes a RenderContext. The
RenderContext specifies how the RenderedImage should be
constructed. Note that it is not possible to extract pixels
directly from a RenderableImage.

The createDefaultRendering() and createScaledRendering() methods are
convenience methods that construct an appropriate RenderContext
internally. All of the rendering methods may return a reference to a
previously produced rendering.

The createDefaultRendering() and createScaledRendering() methods are
convenience methods that construct an appropriate RenderContext
internally. All of the rendering methods may return a reference to a
previously produced rendering.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

HINTS_OBSERVED

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

RenderedImage

createDefaultRendering

()

Returns a RenderedImage instance of this image with a default
width and height in pixels.

RenderedImage

createRendering

​(

RenderContext

renderContext)

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext.

RenderedImage

createScaledRendering

​(int w,
int h,

RenderingHints

hints)

Creates a RenderedImage instance of this image with width w, and
height h in pixels.

float

getHeight

()

Gets the height in user coordinate space.

float

getMinX

()

Gets the minimum X coordinate of the rendering-independent image data.

float

getMinY

()

Gets the minimum Y coordinate of the rendering-independent image data.

Object

getProperty

​(

String

name)

Gets a property from the property set of this image.

String

[]

getPropertyNames

()

Returns a list of names recognized by getProperty.

Vector

<

RenderableImage

>

getSources

()

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage.

float

getWidth

()

Gets the width in user coordinate space.

boolean

isDynamic

()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

HINTS_OBSERVED

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods.

---

#### Field Summary

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

RenderedImage

createDefaultRendering

()

Returns a RenderedImage instance of this image with a default
width and height in pixels.

RenderedImage

createRendering

​(

RenderContext

renderContext)

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext.

RenderedImage

createScaledRendering

​(int w,
int h,

RenderingHints

hints)

Creates a RenderedImage instance of this image with width w, and
height h in pixels.

float

getHeight

()

Gets the height in user coordinate space.

float

getMinX

()

Gets the minimum X coordinate of the rendering-independent image data.

float

getMinY

()

Gets the minimum Y coordinate of the rendering-independent image data.

Object

getProperty

​(

String

name)

Gets a property from the property set of this image.

String

[]

getPropertyNames

()

Returns a list of names recognized by getProperty.

Vector

<

RenderableImage

>

getSources

()

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage.

float

getWidth

()

Gets the width in user coordinate space.

boolean

isDynamic

()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results.

---

#### Method Summary

Returns a RenderedImage instance of this image with a default
width and height in pixels.

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext.

Creates a RenderedImage instance of this image with width w, and
height h in pixels.

Gets the height in user coordinate space.

Gets the minimum X coordinate of the rendering-independent image data.

Gets the minimum Y coordinate of the rendering-independent image data.

Gets a property from the property set of this image.

Returns a list of names recognized by getProperty.

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage.

Gets the width in user coordinate space.

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results.

============ FIELD DETAIL ===========

- Field Detail

- HINTS_OBSERVED

```java
static final
String
HINTS_OBSERVED
```

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods. If such a property exists,
the value of the property will be a RenderingHints object
specifying which hints were observed in creating the rendering.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getSources

```java
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Returns:** a (possibly empty) Vector of RenderableImages, or null.

- getProperty

```java
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

- getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** a list of property names.

- isDynamic

```java
boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

- getWidth

```java
float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Returns:** the width of the image in user coordinates.

- getHeight

```java
float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Returns:** the height of the image in user coordinates.

- getMinX

```java
float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Returns:** the minimum X coordinate of the rendering-independent image
data.

- getMinY

```java
float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Returns:** the minimum Y coordinate of the rendering-independent image
data.

- createScaledRendering

```java
RenderedImage
createScaledRendering​(int w,
int h,

RenderingHints
hints)
```

Creates a RenderedImage instance of this image with width w, and
height h in pixels. The RenderContext is built automatically
with an appropriate usr2dev transform and an area of interest
of the full image. All the rendering hints come from hints
passed in.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

- createDefaultRendering

```java
RenderedImage
createDefaultRendering()
```

Returns a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. The rendering hints are
empty. createDefaultRendering may make use of a stored
rendering for speed.

**Returns:** a RenderedImage containing the rendered data.

- createRendering

```java
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext. This is the most general way to obtain a
rendering of a RenderableImage.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** renderContext

- the RenderContext to use to produce the rendering.
**Returns:** a RenderedImage containing the rendered data.

Field Detail

- HINTS_OBSERVED

```java
static final
String
HINTS_OBSERVED
```

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods. If such a property exists,
the value of the property will be a RenderingHints object
specifying which hints were observed in creating the rendering.

**See Also:** Constant Field Values

---

#### Field Detail

HINTS_OBSERVED

```java
static final
String
HINTS_OBSERVED
```

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods. If such a property exists,
the value of the property will be a RenderingHints object
specifying which hints were observed in creating the rendering.

**See Also:** Constant Field Values

---

#### HINTS_OBSERVED

static final

String

HINTS_OBSERVED

String constant that can be used to identify a property on
a RenderedImage obtained via the createRendering or
createScaledRendering methods. If such a property exists,
the value of the property will be a RenderingHints object
specifying which hints were observed in creating the rendering.

Method Detail

- getSources

```java
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Returns:** a (possibly empty) Vector of RenderableImages, or null.

- getProperty

```java
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

- getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** a list of property names.

- isDynamic

```java
boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

- getWidth

```java
float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Returns:** the width of the image in user coordinates.

- getHeight

```java
float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Returns:** the height of the image in user coordinates.

- getMinX

```java
float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Returns:** the minimum X coordinate of the rendering-independent image
data.

- getMinY

```java
float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Returns:** the minimum Y coordinate of the rendering-independent image
data.

- createScaledRendering

```java
RenderedImage
createScaledRendering​(int w,
int h,

RenderingHints
hints)
```

Creates a RenderedImage instance of this image with width w, and
height h in pixels. The RenderContext is built automatically
with an appropriate usr2dev transform and an area of interest
of the full image. All the rendering hints come from hints
passed in.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

- createDefaultRendering

```java
RenderedImage
createDefaultRendering()
```

Returns a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. The rendering hints are
empty. createDefaultRendering may make use of a stored
rendering for speed.

**Returns:** a RenderedImage containing the rendered data.

- createRendering

```java
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext. This is the most general way to obtain a
rendering of a RenderableImage.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** renderContext

- the RenderContext to use to produce the rendering.
**Returns:** a RenderedImage containing the rendered data.

---

#### Method Detail

getSources

```java
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Returns:** a (possibly empty) Vector of RenderableImages, or null.

---

#### getSources

Vector

<

RenderableImage

> getSources()

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

getProperty

```java
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

---

#### getProperty

Object

getProperty​(

String

name)

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** a list of property names.

---

#### getPropertyNames

String

[] getPropertyNames()

Returns a list of names recognized by getProperty.

isDynamic

```java
boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

---

#### isDynamic

boolean isDynamic()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

getWidth

```java
float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Returns:** the width of the image in user coordinates.

---

#### getWidth

float getWidth()

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

getHeight

```java
float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Returns:** the height of the image in user coordinates.

---

#### getHeight

float getHeight()

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

getMinX

```java
float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Returns:** the minimum X coordinate of the rendering-independent image
data.

---

#### getMinX

float getMinX()

Gets the minimum X coordinate of the rendering-independent image data.

getMinY

```java
float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Returns:** the minimum Y coordinate of the rendering-independent image
data.

---

#### getMinY

float getMinY()

Gets the minimum Y coordinate of the rendering-independent image data.

createScaledRendering

```java
RenderedImage
createScaledRendering​(int w,
int h,

RenderingHints
hints)
```

Creates a RenderedImage instance of this image with width w, and
height h in pixels. The RenderContext is built automatically
with an appropriate usr2dev transform and an area of interest
of the full image. All the rendering hints come from hints
passed in.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

---

#### createScaledRendering

RenderedImage

createScaledRendering​(int w,
int h,

RenderingHints

hints)

Creates a RenderedImage instance of this image with width w, and
height h in pixels. The RenderContext is built automatically
with an appropriate usr2dev transform and an area of interest
of the full image. All the rendering hints come from hints
passed in.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

If w == 0, it will be taken to equal
Math.round(h*(getWidth()/getHeight())).
Similarly, if h == 0, it will be taken to equal
Math.round(w*(getHeight()/getWidth())). One of
w or h must be non-zero or else an IllegalArgumentException
will be thrown.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
were used to create the image. In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

createDefaultRendering

```java
RenderedImage
createDefaultRendering()
```

Returns a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. The rendering hints are
empty. createDefaultRendering may make use of a stored
rendering for speed.

**Returns:** a RenderedImage containing the rendered data.

---

#### createDefaultRendering

RenderedImage

createDefaultRendering()

Returns a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. The rendering hints are
empty. createDefaultRendering may make use of a stored
rendering for speed.

createRendering

```java
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext. This is the most general way to obtain a
rendering of a RenderableImage.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Parameters:** renderContext

- the RenderContext to use to produce the rendering.
**Returns:** a RenderedImage containing the rendered data.

---

#### createRendering

RenderedImage

createRendering​(

RenderContext

renderContext)

Creates a RenderedImage that represented a rendering of this image
using a given RenderContext. This is the most general way to obtain a
rendering of a RenderableImage.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

---

