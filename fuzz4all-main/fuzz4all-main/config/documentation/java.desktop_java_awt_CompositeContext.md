# Interface CompositeContext

**Source:** `java.desktop\java\awt\CompositeContext.html`

### Class Description

```java
public interface
CompositeContext
```

The

CompositeContext

interface defines the encapsulated
and optimized environment for a compositing operation.

CompositeContext

objects maintain state for
compositing operations. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Composite

object.

**See Also:** Composite

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dispose()

Releases resources allocated for a context.

---

#### void compose​(
Raster
src,

Raster
dstIn,

WritableRaster
dstOut)

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

. Note that the destination
can be the same object as either the first or second
source. Note that

dstIn

and

dstOut

must be compatible with the

dstColorModel

passed to the

createContext

method of the

Composite

interface.

**Parameters:**
- src

- the first source for the compositing operation
- dstIn

- the second source for the compositing operation
- dstOut

- the

WritableRaster

into which the
result of the operation is stored

**See Also:**
- Composite

---

### Additional Sections

#### Interface CompositeContext

```java
public interface
CompositeContext
```

The

CompositeContext

interface defines the encapsulated
and optimized environment for a compositing operation.

CompositeContext

objects maintain state for
compositing operations. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Composite

object.

**See Also:** Composite

public interface

CompositeContext

The

CompositeContext

interface defines the encapsulated
and optimized environment for a compositing operation.

CompositeContext

objects maintain state for
compositing operations. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Composite

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

compose

​(

Raster

src,

Raster

dstIn,

WritableRaster

dstOut)

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

.

void

dispose

()

Releases resources allocated for a context.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

compose

​(

Raster

src,

Raster

dstIn,

WritableRaster

dstOut)

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

.

void

dispose

()

Releases resources allocated for a context.

---

#### Method Summary

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

.

Releases resources allocated for a context.

============ METHOD DETAIL ==========

- Method Detail

- dispose

```java
void dispose()
```

Releases resources allocated for a context.

- compose

```java
void compose​(
Raster
src,

Raster
dstIn,

WritableRaster
dstOut)
```

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

. Note that the destination
can be the same object as either the first or second
source. Note that

dstIn

and

dstOut

must be compatible with the

dstColorModel

passed to the

createContext

method of the

Composite

interface.

**Parameters:** src

- the first source for the compositing operation
**Parameters:** dstIn

- the second source for the compositing operation
**Parameters:** dstOut

- the

WritableRaster

into which the
result of the operation is stored
**See Also:** Composite

Method Detail

- dispose

```java
void dispose()
```

Releases resources allocated for a context.

- compose

```java
void compose​(
Raster
src,

Raster
dstIn,

WritableRaster
dstOut)
```

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

. Note that the destination
can be the same object as either the first or second
source. Note that

dstIn

and

dstOut

must be compatible with the

dstColorModel

passed to the

createContext

method of the

Composite

interface.

**Parameters:** src

- the first source for the compositing operation
**Parameters:** dstIn

- the second source for the compositing operation
**Parameters:** dstOut

- the

WritableRaster

into which the
result of the operation is stored
**See Also:** Composite

---

#### Method Detail

dispose

```java
void dispose()
```

Releases resources allocated for a context.

---

#### dispose

void dispose()

Releases resources allocated for a context.

compose

```java
void compose​(
Raster
src,

Raster
dstIn,

WritableRaster
dstOut)
```

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

. Note that the destination
can be the same object as either the first or second
source. Note that

dstIn

and

dstOut

must be compatible with the

dstColorModel

passed to the

createContext

method of the

Composite

interface.

**Parameters:** src

- the first source for the compositing operation
**Parameters:** dstIn

- the second source for the compositing operation
**Parameters:** dstOut

- the

WritableRaster

into which the
result of the operation is stored
**See Also:** Composite

---

#### compose

void compose​(

Raster

src,

Raster

dstIn,

WritableRaster

dstOut)

Composes the two source

Raster

objects and
places the result in the destination

WritableRaster

. Note that the destination
can be the same object as either the first or second
source. Note that

dstIn

and

dstOut

must be compatible with the

dstColorModel

passed to the

createContext

method of the

Composite

interface.

---

