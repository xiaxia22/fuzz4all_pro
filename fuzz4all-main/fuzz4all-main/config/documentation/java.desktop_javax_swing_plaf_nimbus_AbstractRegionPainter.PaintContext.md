# Class AbstractRegionPainter.PaintContext

**Source:** `java.desktop\javax\swing\plaf\nimbus\AbstractRegionPainter.PaintContext.html`

### Class Description

```java
protected static class
AbstractRegionPainter.PaintContext

extends
Object
```

A class encapsulating state useful when painting. Generally, instances of this
class are created once, and reused for each paint request without modification.
This class contains values useful when hinting the cache engine, and when decoding
control points and bezier curve anchors.

**Enclosing class:** AbstractRegionPainter

---

### Field Details

*No entries found.*

### Constructor Details

#### public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted)

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

**Parameters:**
- insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
- canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
- inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets

---

#### public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode
cacheMode,
double maxH,
double maxV)

Creates a new PaintContext.

**Parameters:**
- insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
- canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
- inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets
- cacheMode

- A hint as to which caching mode to use. If null, then set to no caching.
- maxH

- The maximum scale in the horizontal direction to use before punting and redrawing from scratch.
For example, if maxH is 2, then we will attempt to scale any cached images up to 2x the canvas
width before redrawing from scratch. Reasonable maxH values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.
- maxV

- The maximum scale in the vertical direction to use before punting and redrawing from scratch.
For example, if maxV is 2, then we will attempt to scale any cached images up to 2x the canvas
height before redrawing from scratch. Reasonable maxV values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AbstractRegionPainter.PaintContext

java.lang.Object

- javax.swing.plaf.nimbus.AbstractRegionPainter.PaintContext

javax.swing.plaf.nimbus.AbstractRegionPainter.PaintContext

**Enclosing class:** AbstractRegionPainter

```java
protected static class
AbstractRegionPainter.PaintContext

extends
Object
```

A class encapsulating state useful when painting. Generally, instances of this
class are created once, and reused for each paint request without modification.
This class contains values useful when hinting the cache engine, and when decoding
control points and bezier curve anchors.

protected static class

AbstractRegionPainter.PaintContext

extends

Object

A class encapsulating state useful when painting. Generally, instances of this
class are created once, and reused for each paint request without modification.
This class contains values useful when hinting the cache engine, and when decoding
control points and bezier curve anchors.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

AbstractRegionPainter.PaintContext.CacheMode

Cache mode.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PaintContext

​(

Insets

insets,

Dimension

canvasSize,
boolean inverted)

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

PaintContext

​(

Insets

insets,

Dimension

canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode

cacheMode,
double maxH,
double maxV)

Creates a new PaintContext.

========== METHOD SUMMARY ===========

- Method Summary

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

AbstractRegionPainter.PaintContext.CacheMode

Cache mode.

---

#### Nested Class Summary

Cache mode.

Constructor Summary

Constructors

Constructor

Description

PaintContext

​(

Insets

insets,

Dimension

canvasSize,
boolean inverted)

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

PaintContext

​(

Insets

insets,

Dimension

canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode

cacheMode,
double maxH,
double maxV)

Creates a new PaintContext.

---

#### Constructor Summary

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

Creates a new PaintContext.

Method Summary

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

- PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted)
```

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets

- PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode
cacheMode,
double maxH,
double maxV)
```

Creates a new PaintContext.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets
**Parameters:** cacheMode

- A hint as to which caching mode to use. If null, then set to no caching.
**Parameters:** maxH

- The maximum scale in the horizontal direction to use before punting and redrawing from scratch.
For example, if maxH is 2, then we will attempt to scale any cached images up to 2x the canvas
width before redrawing from scratch. Reasonable maxH values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.
**Parameters:** maxV

- The maximum scale in the vertical direction to use before punting and redrawing from scratch.
For example, if maxV is 2, then we will attempt to scale any cached images up to 2x the canvas
height before redrawing from scratch. Reasonable maxV values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.

Constructor Detail

- PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted)
```

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets

- PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode
cacheMode,
double maxH,
double maxV)
```

Creates a new PaintContext.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets
**Parameters:** cacheMode

- A hint as to which caching mode to use. If null, then set to no caching.
**Parameters:** maxH

- The maximum scale in the horizontal direction to use before punting and redrawing from scratch.
For example, if maxH is 2, then we will attempt to scale any cached images up to 2x the canvas
width before redrawing from scratch. Reasonable maxH values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.
**Parameters:** maxV

- The maximum scale in the vertical direction to use before punting and redrawing from scratch.
For example, if maxV is 2, then we will attempt to scale any cached images up to 2x the canvas
height before redrawing from scratch. Reasonable maxV values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.

---

#### Constructor Detail

PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted)
```

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets

---

#### PaintContext

public PaintContext​(

Insets

insets,

Dimension

canvasSize,
boolean inverted)

Creates a new PaintContext which does not attempt to cache or scale any cached
images.

PaintContext

```java
public PaintContext​(
Insets
insets,

Dimension
canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode
cacheMode,
double maxH,
double maxV)
```

Creates a new PaintContext.

**Parameters:** insets

- The stretching insets. May be null. If null, then assumed to be 0, 0, 0, 0.
**Parameters:** canvasSize

- The size of the canvas used when encoding the various x/y values. May be null.
If null, then it is assumed that there are no encoded values, and any calls
to one of the "decode" methods will return the passed in value.
**Parameters:** inverted

- Whether to "invert" the meaning of the 9-square grid and stretching insets
**Parameters:** cacheMode

- A hint as to which caching mode to use. If null, then set to no caching.
**Parameters:** maxH

- The maximum scale in the horizontal direction to use before punting and redrawing from scratch.
For example, if maxH is 2, then we will attempt to scale any cached images up to 2x the canvas
width before redrawing from scratch. Reasonable maxH values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.
**Parameters:** maxV

- The maximum scale in the vertical direction to use before punting and redrawing from scratch.
For example, if maxV is 2, then we will attempt to scale any cached images up to 2x the canvas
height before redrawing from scratch. Reasonable maxV values may improve painting performance.
If set too high, then you may get poor looking graphics at higher zoom levels. Must be >= 1.

---

#### PaintContext

public PaintContext​(

Insets

insets,

Dimension

canvasSize,
boolean inverted,

AbstractRegionPainter.PaintContext.CacheMode

cacheMode,
double maxH,
double maxV)

Creates a new PaintContext.

---

