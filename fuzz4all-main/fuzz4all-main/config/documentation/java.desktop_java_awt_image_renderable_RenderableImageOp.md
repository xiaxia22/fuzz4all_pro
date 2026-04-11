# Class RenderableImageOp

**Source:** `java.desktop\java\awt\image\renderable\RenderableImageOp.html`

### Class Description

```java
public class
RenderableImageOp

extends
Object

implements
RenderableImage
```

This class handles the renderable aspects of an operation with help
from its associated instance of a ContextualRenderedImageFactory.

**All Implemented Interfaces:** RenderableImage

---

### Field Details

*No entries found.*

### Constructor Details

#### public RenderableImageOp​(
ContextualRenderedImageFactory
CRIF,

ParameterBlock
paramBlock)

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters. Any RenderedImage sources referenced by the
ParameterBlock will be ignored.

**Parameters:**
- CRIF

- a ContextualRenderedImageFactory object
- paramBlock

- a ParameterBlock containing this operation's source
images and other parameters necessary for the operation
to run.

---

### Method Details

#### public
Vector
<
RenderableImage
> getSources()

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Specified by:**
- getSources

in interface

RenderableImage

**Returns:**
- a (possibly empty) Vector of RenderableImages, or null.

---

#### public
Object
getProperty​(
String
name)

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Specified by:**
- getProperty

in interface

RenderableImage

**Parameters:**
- name

- the name of the property to get, as a String.

**Returns:**
- a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

---

#### public
String
[] getPropertyNames()

Return a list of names recognized by getProperty.

**Specified by:**
- getPropertyNames

in interface

RenderableImage

**Returns:**
- a list of property names.

---

#### public boolean isDynamic()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. The CRIF's isDynamic method will be called.

**Specified by:**
- isDynamic

in interface

RenderableImage

**Returns:**
- true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

---

#### public float getWidth()

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Specified by:**
- getWidth

in interface

RenderableImage

**Returns:**
- the width of the image in user coordinates.

---

#### public float getHeight()

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Specified by:**
- getHeight

in interface

RenderableImage

**Returns:**
- the height of the image in user coordinates.

---

#### public float getMinX()

Gets the minimum X coordinate of the rendering-independent image data.

**Specified by:**
- getMinX

in interface

RenderableImage

**Returns:**
- the minimum X coordinate of the rendering-independent image
data.

---

#### public float getMinY()

Gets the minimum Y coordinate of the rendering-independent image data.

**Specified by:**
- getMinY

in interface

RenderableImage

**Returns:**
- the minimum Y coordinate of the rendering-independent image
data.

---

#### public
ParameterBlock
setParameterBlock​(
ParameterBlock
paramBlock)

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains. The effects of such a
change will be visible when a new rendering is created from
this RenderableImageOp or any dependent RenderableImageOp.

**Parameters:**
- paramBlock

- the new ParameterBlock.

**Returns:**
- the old ParameterBlock.

**See Also:**
- getParameterBlock()

---

#### public
ParameterBlock
getParameterBlock()

Returns a reference to the current parameter block.

**Returns:**
- the

ParameterBlock

of this

RenderableImageOp

.

**See Also:**
- setParameterBlock(ParameterBlock)

---

#### public
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

**Specified by:**
- createScaledRendering

in interface

RenderableImage

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

#### public
RenderedImage
createDefaultRendering()

Gets a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. All the rendering hints come
from hints passed in. Implementors of this interface must be
sure that there is a defined default width and height.

**Specified by:**
- createDefaultRendering

in interface

RenderableImage

**Returns:**
- a RenderedImage containing the rendered data.

---

#### public
RenderedImage
createRendering​(
RenderContext
renderContext)

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Specified by:**
- createRendering

in interface

RenderableImage

**Parameters:**
- renderContext

- The RenderContext to use to perform the rendering.

**Returns:**
- a RenderedImage containing the desired output image.

---

### Additional Sections

#### Class RenderableImageOp

java.lang.Object

- java.awt.image.renderable.RenderableImageOp

java.awt.image.renderable.RenderableImageOp

**All Implemented Interfaces:** RenderableImage

```java
public class
RenderableImageOp

extends
Object

implements
RenderableImage
```

This class handles the renderable aspects of an operation with help
from its associated instance of a ContextualRenderedImageFactory.

public class

RenderableImageOp

extends

Object

implements

RenderableImage

This class handles the renderable aspects of an operation with help
from its associated instance of a ContextualRenderedImageFactory.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.image.renderable.

RenderableImage

HINTS_OBSERVED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RenderableImageOp

​(

ContextualRenderedImageFactory

CRIF,

ParameterBlock

paramBlock)

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

RenderedImage

createDefaultRendering

()

Gets a RenderedImage instance of this image with a default
width and height in pixels.

RenderedImage

createRendering

​(

RenderContext

renderContext)

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

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

ParameterBlock

getParameterBlock

()

Returns a reference to the current parameter block.

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

Return a list of names recognized by getProperty.

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

ParameterBlock

setParameterBlock

​(

ParameterBlock

paramBlock)

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains.

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

- Fields declared in interface java.awt.image.renderable.

RenderableImage

HINTS_OBSERVED

---

#### Field Summary

Fields declared in interface java.awt.image.renderable.

RenderableImage

HINTS_OBSERVED

---

#### Fields declared in interface java.awt.image.renderable. RenderableImage

Constructor Summary

Constructors

Constructor

Description

RenderableImageOp

​(

ContextualRenderedImageFactory

CRIF,

ParameterBlock

paramBlock)

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters.

---

#### Constructor Summary

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

RenderedImage

createDefaultRendering

()

Gets a RenderedImage instance of this image with a default
width and height in pixels.

RenderedImage

createRendering

​(

RenderContext

renderContext)

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

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

ParameterBlock

getParameterBlock

()

Returns a reference to the current parameter block.

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

Return a list of names recognized by getProperty.

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

ParameterBlock

setParameterBlock

​(

ParameterBlock

paramBlock)

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains.

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

Gets a RenderedImage instance of this image with a default
width and height in pixels.

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

Creates a RenderedImage instance of this image with width w, and
height h in pixels.

Gets the height in user coordinate space.

Gets the minimum X coordinate of the rendering-independent image data.

Gets the minimum Y coordinate of the rendering-independent image data.

Returns a reference to the current parameter block.

Gets a property from the property set of this image.

Return a list of names recognized by getProperty.

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage.

Gets the width in user coordinate space.

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results.

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains.

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

- RenderableImageOp

```java
public RenderableImageOp​(
ContextualRenderedImageFactory
CRIF,

ParameterBlock
paramBlock)
```

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters. Any RenderedImage sources referenced by the
ParameterBlock will be ignored.

**Parameters:** CRIF

- a ContextualRenderedImageFactory object
**Parameters:** paramBlock

- a ParameterBlock containing this operation's source
images and other parameters necessary for the operation
to run.

============ METHOD DETAIL ==========

- Method Detail

- getSources

```java
public
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Specified by:** getSources

in interface

RenderableImage
**Returns:** a (possibly empty) Vector of RenderableImages, or null.

- getProperty

```java
public
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Specified by:** getProperty

in interface

RenderableImage
**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

- getPropertyNames

```java
public
String
[] getPropertyNames()
```

Return a list of names recognized by getProperty.

**Specified by:** getPropertyNames

in interface

RenderableImage
**Returns:** a list of property names.

- isDynamic

```java
public boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. The CRIF's isDynamic method will be called.

**Specified by:** isDynamic

in interface

RenderableImage
**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

- getWidth

```java
public float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Specified by:** getWidth

in interface

RenderableImage
**Returns:** the width of the image in user coordinates.

- getHeight

```java
public float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Specified by:** getHeight

in interface

RenderableImage
**Returns:** the height of the image in user coordinates.

- getMinX

```java
public float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Specified by:** getMinX

in interface

RenderableImage
**Returns:** the minimum X coordinate of the rendering-independent image
data.

- getMinY

```java
public float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Specified by:** getMinY

in interface

RenderableImage
**Returns:** the minimum Y coordinate of the rendering-independent image
data.

- setParameterBlock

```java
public
ParameterBlock
setParameterBlock​(
ParameterBlock
paramBlock)
```

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains. The effects of such a
change will be visible when a new rendering is created from
this RenderableImageOp or any dependent RenderableImageOp.

**Parameters:** paramBlock

- the new ParameterBlock.
**Returns:** the old ParameterBlock.
**See Also:** getParameterBlock()

- getParameterBlock

```java
public
ParameterBlock
getParameterBlock()
```

Returns a reference to the current parameter block.

**Returns:** the

ParameterBlock

of this

RenderableImageOp

.
**See Also:** setParameterBlock(ParameterBlock)

- createScaledRendering

```java
public
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

**Specified by:** createScaledRendering

in interface

RenderableImage
**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

- createDefaultRendering

```java
public
RenderedImage
createDefaultRendering()
```

Gets a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. All the rendering hints come
from hints passed in. Implementors of this interface must be
sure that there is a defined default width and height.

**Specified by:** createDefaultRendering

in interface

RenderableImage
**Returns:** a RenderedImage containing the rendered data.

- createRendering

```java
public
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Specified by:** createRendering

in interface

RenderableImage
**Parameters:** renderContext

- The RenderContext to use to perform the rendering.
**Returns:** a RenderedImage containing the desired output image.

Constructor Detail

- RenderableImageOp

```java
public RenderableImageOp​(
ContextualRenderedImageFactory
CRIF,

ParameterBlock
paramBlock)
```

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters. Any RenderedImage sources referenced by the
ParameterBlock will be ignored.

**Parameters:** CRIF

- a ContextualRenderedImageFactory object
**Parameters:** paramBlock

- a ParameterBlock containing this operation's source
images and other parameters necessary for the operation
to run.

---

#### Constructor Detail

RenderableImageOp

```java
public RenderableImageOp​(
ContextualRenderedImageFactory
CRIF,

ParameterBlock
paramBlock)
```

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters. Any RenderedImage sources referenced by the
ParameterBlock will be ignored.

**Parameters:** CRIF

- a ContextualRenderedImageFactory object
**Parameters:** paramBlock

- a ParameterBlock containing this operation's source
images and other parameters necessary for the operation
to run.

---

#### RenderableImageOp

public RenderableImageOp​(

ContextualRenderedImageFactory

CRIF,

ParameterBlock

paramBlock)

Constructs a RenderedImageOp given a
ContextualRenderedImageFactory object, and
a ParameterBlock containing RenderableImage sources and other
parameters. Any RenderedImage sources referenced by the
ParameterBlock will be ignored.

Method Detail

- getSources

```java
public
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Specified by:** getSources

in interface

RenderableImage
**Returns:** a (possibly empty) Vector of RenderableImages, or null.

- getProperty

```java
public
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Specified by:** getProperty

in interface

RenderableImage
**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

- getPropertyNames

```java
public
String
[] getPropertyNames()
```

Return a list of names recognized by getProperty.

**Specified by:** getPropertyNames

in interface

RenderableImage
**Returns:** a list of property names.

- isDynamic

```java
public boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. The CRIF's isDynamic method will be called.

**Specified by:** isDynamic

in interface

RenderableImage
**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

- getWidth

```java
public float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Specified by:** getWidth

in interface

RenderableImage
**Returns:** the width of the image in user coordinates.

- getHeight

```java
public float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Specified by:** getHeight

in interface

RenderableImage
**Returns:** the height of the image in user coordinates.

- getMinX

```java
public float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Specified by:** getMinX

in interface

RenderableImage
**Returns:** the minimum X coordinate of the rendering-independent image
data.

- getMinY

```java
public float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Specified by:** getMinY

in interface

RenderableImage
**Returns:** the minimum Y coordinate of the rendering-independent image
data.

- setParameterBlock

```java
public
ParameterBlock
setParameterBlock​(
ParameterBlock
paramBlock)
```

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains. The effects of such a
change will be visible when a new rendering is created from
this RenderableImageOp or any dependent RenderableImageOp.

**Parameters:** paramBlock

- the new ParameterBlock.
**Returns:** the old ParameterBlock.
**See Also:** getParameterBlock()

- getParameterBlock

```java
public
ParameterBlock
getParameterBlock()
```

Returns a reference to the current parameter block.

**Returns:** the

ParameterBlock

of this

RenderableImageOp

.
**See Also:** setParameterBlock(ParameterBlock)

- createScaledRendering

```java
public
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

**Specified by:** createScaledRendering

in interface

RenderableImage
**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

- createDefaultRendering

```java
public
RenderedImage
createDefaultRendering()
```

Gets a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. All the rendering hints come
from hints passed in. Implementors of this interface must be
sure that there is a defined default width and height.

**Specified by:** createDefaultRendering

in interface

RenderableImage
**Returns:** a RenderedImage containing the rendered data.

- createRendering

```java
public
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Specified by:** createRendering

in interface

RenderableImage
**Parameters:** renderContext

- The RenderContext to use to perform the rendering.
**Returns:** a RenderedImage containing the desired output image.

---

#### Method Detail

getSources

```java
public
Vector
<
RenderableImage
> getSources()
```

Returns a vector of RenderableImages that are the sources of
image data for this RenderableImage. Note that this method may
return an empty vector, to indicate that the image has no sources,
or null, to indicate that no information is available.

**Specified by:** getSources

in interface

RenderableImage
**Returns:** a (possibly empty) Vector of RenderableImages, or null.

---

#### getSources

public

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
public
Object
getProperty​(
String
name)
```

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

**Specified by:** getProperty

in interface

RenderableImage
**Parameters:** name

- the name of the property to get, as a String.
**Returns:** a reference to the property Object, or the value
java.awt.Image.UndefinedProperty.

---

#### getProperty

public

Object

getProperty​(

String

name)

Gets a property from the property set of this image.
If the property name is not recognized, java.awt.Image.UndefinedProperty
will be returned.

getPropertyNames

```java
public
String
[] getPropertyNames()
```

Return a list of names recognized by getProperty.

**Specified by:** getPropertyNames

in interface

RenderableImage
**Returns:** a list of property names.

---

#### getPropertyNames

public

String

[] getPropertyNames()

Return a list of names recognized by getProperty.

isDynamic

```java
public boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. The CRIF's isDynamic method will be called.

**Specified by:** isDynamic

in interface

RenderableImage
**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

---

#### isDynamic

public boolean isDynamic()

Returns true if successive renderings (that is, calls to
createRendering() or createScaledRendering()) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. The CRIF's isDynamic method will be called.

getWidth

```java
public float getWidth()
```

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

**Specified by:** getWidth

in interface

RenderableImage
**Returns:** the width of the image in user coordinates.

---

#### getWidth

public float getWidth()

Gets the width in user coordinate space. By convention, the
usual width of a RenderableImage is equal to the image's aspect
ratio (width divided by height).

getHeight

```java
public float getHeight()
```

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

**Specified by:** getHeight

in interface

RenderableImage
**Returns:** the height of the image in user coordinates.

---

#### getHeight

public float getHeight()

Gets the height in user coordinate space. By convention, the
usual height of a RenderedImage is equal to 1.0F.

getMinX

```java
public float getMinX()
```

Gets the minimum X coordinate of the rendering-independent image data.

**Specified by:** getMinX

in interface

RenderableImage
**Returns:** the minimum X coordinate of the rendering-independent image
data.

---

#### getMinX

public float getMinX()

Gets the minimum X coordinate of the rendering-independent image data.

getMinY

```java
public float getMinY()
```

Gets the minimum Y coordinate of the rendering-independent image data.

**Specified by:** getMinY

in interface

RenderableImage
**Returns:** the minimum Y coordinate of the rendering-independent image
data.

---

#### getMinY

public float getMinY()

Gets the minimum Y coordinate of the rendering-independent image data.

setParameterBlock

```java
public
ParameterBlock
setParameterBlock​(
ParameterBlock
paramBlock)
```

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains. The effects of such a
change will be visible when a new rendering is created from
this RenderableImageOp or any dependent RenderableImageOp.

**Parameters:** paramBlock

- the new ParameterBlock.
**Returns:** the old ParameterBlock.
**See Also:** getParameterBlock()

---

#### setParameterBlock

public

ParameterBlock

setParameterBlock​(

ParameterBlock

paramBlock)

Change the current ParameterBlock of the operation, allowing
editing of image rendering chains. The effects of such a
change will be visible when a new rendering is created from
this RenderableImageOp or any dependent RenderableImageOp.

getParameterBlock

```java
public
ParameterBlock
getParameterBlock()
```

Returns a reference to the current parameter block.

**Returns:** the

ParameterBlock

of this

RenderableImageOp

.
**See Also:** setParameterBlock(ParameterBlock)

---

#### getParameterBlock

public

ParameterBlock

getParameterBlock()

Returns a reference to the current parameter block.

createScaledRendering

```java
public
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

**Specified by:** createScaledRendering

in interface

RenderableImage
**Parameters:** w

- the width of rendered image in pixels, or 0.
**Parameters:** h

- the height of rendered image in pixels, or 0.
**Parameters:** hints

- a RenderingHints object containing hints.
**Returns:** a RenderedImage containing the rendered data.

---

#### createScaledRendering

public

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
public
RenderedImage
createDefaultRendering()
```

Gets a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. All the rendering hints come
from hints passed in. Implementors of this interface must be
sure that there is a defined default width and height.

**Specified by:** createDefaultRendering

in interface

RenderableImage
**Returns:** a RenderedImage containing the rendered data.

---

#### createDefaultRendering

public

RenderedImage

createDefaultRendering()

Gets a RenderedImage instance of this image with a default
width and height in pixels. The RenderContext is built
automatically with an appropriate usr2dev transform and an area
of interest of the full image. All the rendering hints come
from hints passed in. Implementors of this interface must be
sure that there is a defined default width and height.

createRendering

```java
public
RenderedImage
createRendering​(
RenderContext
renderContext)
```

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

**Specified by:** createRendering

in interface

RenderableImage
**Parameters:** renderContext

- The RenderContext to use to perform the rendering.
**Returns:** a RenderedImage containing the desired output image.

---

#### createRendering

public

RenderedImage

createRendering​(

RenderContext

renderContext)

Creates a RenderedImage which represents this
RenderableImageOp (including its Renderable sources) rendered
according to the given RenderContext.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

This method supports chaining of either Renderable or
RenderedImage operations. If sources in
the ParameterBlock used to construct the RenderableImageOp are
RenderableImages, then a three step process is followed:

- mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

The created RenderedImage may have a property identified
by the String HINTS_OBSERVED to indicate which RenderingHints
(from the RenderContext) were used to create the image.
In addition any RenderedImages
that are obtained via the getSources() method on the created
RenderedImage may have such a property.

mapRenderContext() is called on the associated CRIF for
each RenderableImage source;

createRendering() is called on each of the RenderableImage sources
using the backwards-mapped RenderContexts obtained in step 1,
resulting in a rendering of each source;

ContextualRenderedImageFactory.create() is called
with a new ParameterBlock containing the parameters of
the RenderableImageOp and the RenderedImages that were created by the
createRendering() calls.

If the elements of the source Vector of
the ParameterBlock used to construct the RenderableImageOp are
instances of RenderedImage, then the CRIF.create() method is
called immediately using the original ParameterBlock.
This provides a basis case for the recursion.

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

