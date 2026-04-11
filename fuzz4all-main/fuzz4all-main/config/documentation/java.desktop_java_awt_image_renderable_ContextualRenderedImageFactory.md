# Interface ContextualRenderedImageFactory

**Source:** `java.desktop\java\awt\image\renderable\ContextualRenderedImageFactory.html`

### Class Description

```java
public interface
ContextualRenderedImageFactory

extends
RenderedImageFactory
```

ContextualRenderedImageFactory provides an interface for the
functionality that may differ between instances of
RenderableImageOp. Thus different operations on RenderableImages
may be performed by a single class such as RenderedImageOp through
the use of multiple instances of ContextualRenderedImageFactory.
The name ContextualRenderedImageFactory is commonly shortened to
"CRIF."

All operations that are to be used in a rendering-independent
chain must implement ContextualRenderedImageFactory.

Classes that implement this interface must provide a
constructor with no arguments.

**All Superinterfaces:** RenderedImageFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### RenderContext
mapRenderContext​(int i,

RenderContext
renderContext,

ParameterBlock
paramBlock,

RenderableImage
image)

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources. This is useful for
operations that can be expressed in whole or in part simply as
alterations in the RenderContext, such as an affine mapping, or
operations that wish to obtain lower quality renderings of
their sources in order to save processing effort or
transmission bandwidth. Some operations, such as blur, can also
use this mechanism to avoid obtaining sources of higher quality
than necessary.

**Parameters:**
- i

- the index of the source image.
- renderContext

- the RenderContext being applied to the operation.
- paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
- image

- the RenderableImage being rendered.

**Returns:**
- a

RenderContext

for
the source at the specified index of the parameters
Vector contained in the specified ParameterBlock.

---

#### RenderedImage
create​(
RenderContext
renderContext,

ParameterBlock
paramBlock)

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters. The output
is a RenderedImage that takes the RenderContext into account to
determine its dimensions and placement on the image plane.
This method houses the "intelligence" that allows a
rendering-independent operation to adapt to a specific
RenderContext.

**Parameters:**
- renderContext

- The RenderContext specifying the rendering
- paramBlock

- a ParameterBlock containing the operation's
sources and parameters

**Returns:**
- a

RenderedImage

from the sources and parameters
in the specified ParameterBlock and according to the
rendering instructions in the specified RenderContext.

---

#### Rectangle2D
getBounds2D​(
ParameterBlock
paramBlock)

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space. The bounds are returned as a Rectangle2D, that is, an
axis-aligned rectangle with floating-point corner coordinates.

**Parameters:**
- paramBlock

- a ParameterBlock containing the operation's
sources and parameters.

**Returns:**
- a Rectangle2D specifying the rendering-independent
bounding box of the output.

---

#### Object
getProperty​(
ParameterBlock
paramBlock,

String
name)

Gets the appropriate instance of the property specified by the name
parameter. This method must determine which instance of a property to
return when there are multiple sources that each specify the property.

**Parameters:**
- paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
- name

- a String naming the desired property.

**Returns:**
- an object reference to the value of the property requested.

---

#### String
[] getPropertyNames()

Returns a list of names recognized by getProperty.

**Returns:**
- the list of property names.

---

#### boolean isDynamic()

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
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

### Additional Sections

#### Interface ContextualRenderedImageFactory

**All Superinterfaces:** RenderedImageFactory

```java
public interface
ContextualRenderedImageFactory

extends
RenderedImageFactory
```

ContextualRenderedImageFactory provides an interface for the
functionality that may differ between instances of
RenderableImageOp. Thus different operations on RenderableImages
may be performed by a single class such as RenderedImageOp through
the use of multiple instances of ContextualRenderedImageFactory.
The name ContextualRenderedImageFactory is commonly shortened to
"CRIF."

All operations that are to be used in a rendering-independent
chain must implement ContextualRenderedImageFactory.

Classes that implement this interface must provide a
constructor with no arguments.

public interface

ContextualRenderedImageFactory

extends

RenderedImageFactory

ContextualRenderedImageFactory provides an interface for the
functionality that may differ between instances of
RenderableImageOp. Thus different operations on RenderableImages
may be performed by a single class such as RenderedImageOp through
the use of multiple instances of ContextualRenderedImageFactory.
The name ContextualRenderedImageFactory is commonly shortened to
"CRIF."

All operations that are to be used in a rendering-independent
chain must implement ContextualRenderedImageFactory.

Classes that implement this interface must provide a
constructor with no arguments.

All operations that are to be used in a rendering-independent
chain must implement ContextualRenderedImageFactory.

Classes that implement this interface must provide a
constructor with no arguments.

Classes that implement this interface must provide a
constructor with no arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

RenderedImage

create

​(

RenderContext

renderContext,

ParameterBlock

paramBlock)

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters.

Rectangle2D

getBounds2D

​(

ParameterBlock

paramBlock)

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space.

Object

getProperty

​(

ParameterBlock

paramBlock,

String

name)

Gets the appropriate instance of the property specified by the name
parameter.

String

[]

getPropertyNames

()

Returns a list of names recognized by getProperty.

boolean

isDynamic

()

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results.

RenderContext

mapRenderContext

​(int i,

RenderContext

renderContext,

ParameterBlock

paramBlock,

RenderableImage

image)

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources.

- Methods declared in interface java.awt.image.renderable.

RenderedImageFactory

create

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

RenderedImage

create

​(

RenderContext

renderContext,

ParameterBlock

paramBlock)

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters.

Rectangle2D

getBounds2D

​(

ParameterBlock

paramBlock)

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space.

Object

getProperty

​(

ParameterBlock

paramBlock,

String

name)

Gets the appropriate instance of the property specified by the name
parameter.

String

[]

getPropertyNames

()

Returns a list of names recognized by getProperty.

boolean

isDynamic

()

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results.

RenderContext

mapRenderContext

​(int i,

RenderContext

renderContext,

ParameterBlock

paramBlock,

RenderableImage

image)

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources.

- Methods declared in interface java.awt.image.renderable.

RenderedImageFactory

create

---

#### Method Summary

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters.

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space.

Gets the appropriate instance of the property specified by the name
parameter.

Returns a list of names recognized by getProperty.

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results.

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources.

Methods declared in interface java.awt.image.renderable.

RenderedImageFactory

create

---

#### Methods declared in interface java.awt.image.renderable. RenderedImageFactory

============ METHOD DETAIL ==========

- Method Detail

- mapRenderContext

```java
RenderContext
mapRenderContext​(int i,

RenderContext
renderContext,

ParameterBlock
paramBlock,

RenderableImage
image)
```

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources. This is useful for
operations that can be expressed in whole or in part simply as
alterations in the RenderContext, such as an affine mapping, or
operations that wish to obtain lower quality renderings of
their sources in order to save processing effort or
transmission bandwidth. Some operations, such as blur, can also
use this mechanism to avoid obtaining sources of higher quality
than necessary.

**Parameters:** i

- the index of the source image.
**Parameters:** renderContext

- the RenderContext being applied to the operation.
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** image

- the RenderableImage being rendered.
**Returns:** a

RenderContext

for
the source at the specified index of the parameters
Vector contained in the specified ParameterBlock.

- create

```java
RenderedImage
create​(
RenderContext
renderContext,

ParameterBlock
paramBlock)
```

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters. The output
is a RenderedImage that takes the RenderContext into account to
determine its dimensions and placement on the image plane.
This method houses the "intelligence" that allows a
rendering-independent operation to adapt to a specific
RenderContext.

**Parameters:** renderContext

- The RenderContext specifying the rendering
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters
**Returns:** a

RenderedImage

from the sources and parameters
in the specified ParameterBlock and according to the
rendering instructions in the specified RenderContext.

- getBounds2D

```java
Rectangle2D
getBounds2D​(
ParameterBlock
paramBlock)
```

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space. The bounds are returned as a Rectangle2D, that is, an
axis-aligned rectangle with floating-point corner coordinates.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Returns:** a Rectangle2D specifying the rendering-independent
bounding box of the output.

- getProperty

```java
Object
getProperty​(
ParameterBlock
paramBlock,

String
name)
```

Gets the appropriate instance of the property specified by the name
parameter. This method must determine which instance of a property to
return when there are multiple sources that each specify the property.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** name

- a String naming the desired property.
**Returns:** an object reference to the value of the property requested.

- getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** the list of property names.

- isDynamic

```java
boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

Method Detail

- mapRenderContext

```java
RenderContext
mapRenderContext​(int i,

RenderContext
renderContext,

ParameterBlock
paramBlock,

RenderableImage
image)
```

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources. This is useful for
operations that can be expressed in whole or in part simply as
alterations in the RenderContext, such as an affine mapping, or
operations that wish to obtain lower quality renderings of
their sources in order to save processing effort or
transmission bandwidth. Some operations, such as blur, can also
use this mechanism to avoid obtaining sources of higher quality
than necessary.

**Parameters:** i

- the index of the source image.
**Parameters:** renderContext

- the RenderContext being applied to the operation.
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** image

- the RenderableImage being rendered.
**Returns:** a

RenderContext

for
the source at the specified index of the parameters
Vector contained in the specified ParameterBlock.

- create

```java
RenderedImage
create​(
RenderContext
renderContext,

ParameterBlock
paramBlock)
```

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters. The output
is a RenderedImage that takes the RenderContext into account to
determine its dimensions and placement on the image plane.
This method houses the "intelligence" that allows a
rendering-independent operation to adapt to a specific
RenderContext.

**Parameters:** renderContext

- The RenderContext specifying the rendering
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters
**Returns:** a

RenderedImage

from the sources and parameters
in the specified ParameterBlock and according to the
rendering instructions in the specified RenderContext.

- getBounds2D

```java
Rectangle2D
getBounds2D​(
ParameterBlock
paramBlock)
```

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space. The bounds are returned as a Rectangle2D, that is, an
axis-aligned rectangle with floating-point corner coordinates.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Returns:** a Rectangle2D specifying the rendering-independent
bounding box of the output.

- getProperty

```java
Object
getProperty​(
ParameterBlock
paramBlock,

String
name)
```

Gets the appropriate instance of the property specified by the name
parameter. This method must determine which instance of a property to
return when there are multiple sources that each specify the property.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** name

- a String naming the desired property.
**Returns:** an object reference to the value of the property requested.

- getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** the list of property names.

- isDynamic

```java
boolean isDynamic()
```

Returns true if successive renderings (that is, calls to
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

**Returns:** true

if successive renderings with the
same arguments might produce different results;

false

otherwise.

---

#### Method Detail

mapRenderContext

```java
RenderContext
mapRenderContext​(int i,

RenderContext
renderContext,

ParameterBlock
paramBlock,

RenderableImage
image)
```

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources. This is useful for
operations that can be expressed in whole or in part simply as
alterations in the RenderContext, such as an affine mapping, or
operations that wish to obtain lower quality renderings of
their sources in order to save processing effort or
transmission bandwidth. Some operations, such as blur, can also
use this mechanism to avoid obtaining sources of higher quality
than necessary.

**Parameters:** i

- the index of the source image.
**Parameters:** renderContext

- the RenderContext being applied to the operation.
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** image

- the RenderableImage being rendered.
**Returns:** a

RenderContext

for
the source at the specified index of the parameters
Vector contained in the specified ParameterBlock.

---

#### mapRenderContext

RenderContext

mapRenderContext​(int i,

RenderContext

renderContext,

ParameterBlock

paramBlock,

RenderableImage

image)

Maps the operation's output RenderContext into a RenderContext
for each of the operation's sources. This is useful for
operations that can be expressed in whole or in part simply as
alterations in the RenderContext, such as an affine mapping, or
operations that wish to obtain lower quality renderings of
their sources in order to save processing effort or
transmission bandwidth. Some operations, such as blur, can also
use this mechanism to avoid obtaining sources of higher quality
than necessary.

create

```java
RenderedImage
create​(
RenderContext
renderContext,

ParameterBlock
paramBlock)
```

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters. The output
is a RenderedImage that takes the RenderContext into account to
determine its dimensions and placement on the image plane.
This method houses the "intelligence" that allows a
rendering-independent operation to adapt to a specific
RenderContext.

**Parameters:** renderContext

- The RenderContext specifying the rendering
**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters
**Returns:** a

RenderedImage

from the sources and parameters
in the specified ParameterBlock and according to the
rendering instructions in the specified RenderContext.

---

#### create

RenderedImage

create​(

RenderContext

renderContext,

ParameterBlock

paramBlock)

Creates a rendering, given a RenderContext and a ParameterBlock
containing the operation's sources and parameters. The output
is a RenderedImage that takes the RenderContext into account to
determine its dimensions and placement on the image plane.
This method houses the "intelligence" that allows a
rendering-independent operation to adapt to a specific
RenderContext.

getBounds2D

```java
Rectangle2D
getBounds2D​(
ParameterBlock
paramBlock)
```

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space. The bounds are returned as a Rectangle2D, that is, an
axis-aligned rectangle with floating-point corner coordinates.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Returns:** a Rectangle2D specifying the rendering-independent
bounding box of the output.

---

#### getBounds2D

Rectangle2D

getBounds2D​(

ParameterBlock

paramBlock)

Returns the bounding box for the output of the operation,
performed on a given set of sources, in rendering-independent
space. The bounds are returned as a Rectangle2D, that is, an
axis-aligned rectangle with floating-point corner coordinates.

getProperty

```java
Object
getProperty​(
ParameterBlock
paramBlock,

String
name)
```

Gets the appropriate instance of the property specified by the name
parameter. This method must determine which instance of a property to
return when there are multiple sources that each specify the property.

**Parameters:** paramBlock

- a ParameterBlock containing the operation's
sources and parameters.
**Parameters:** name

- a String naming the desired property.
**Returns:** an object reference to the value of the property requested.

---

#### getProperty

Object

getProperty​(

ParameterBlock

paramBlock,

String

name)

Gets the appropriate instance of the property specified by the name
parameter. This method must determine which instance of a property to
return when there are multiple sources that each specify the property.

getPropertyNames

```java
String
[] getPropertyNames()
```

Returns a list of names recognized by getProperty.

**Returns:** the list of property names.

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
create(RenderContext, ParameterBlock)) with the same arguments
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
create(RenderContext, ParameterBlock)) with the same arguments
may produce different results. This method may be used to
determine whether an existing rendering may be cached and
reused. It is always safe to return true.

---

