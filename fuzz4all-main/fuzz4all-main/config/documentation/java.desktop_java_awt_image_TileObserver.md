# Interface TileObserver

**Source:** `java.desktop\java\awt\image\TileObserver.html`

### Class Description

```java
public interface
TileObserver
```

An interface for objects that wish to be informed when tiles
of a WritableRenderedImage become modifiable by some writer via
a call to getWritableTile, and when they become unmodifiable via
the last call to releaseWritableTile.

**See Also:** WritableRenderedImage

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void tileUpdate​(
WritableRenderedImage
source,
int tileX,
int tileY,
boolean willBeWritable)

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

**Parameters:**
- source

- the image that owns the tile.
- tileX

- the X index of the tile that is being updated.
- tileY

- the Y index of the tile that is being updated.
- willBeWritable

- If true, the tile will be grabbed for writing;
otherwise it is being released.

---

### Additional Sections

#### Interface TileObserver

```java
public interface
TileObserver
```

An interface for objects that wish to be informed when tiles
of a WritableRenderedImage become modifiable by some writer via
a call to getWritableTile, and when they become unmodifiable via
the last call to releaseWritableTile.

**See Also:** WritableRenderedImage

public interface

TileObserver

An interface for objects that wish to be informed when tiles
of a WritableRenderedImage become modifiable by some writer via
a call to getWritableTile, and when they become unmodifiable via
the last call to releaseWritableTile.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

tileUpdate

​(

WritableRenderedImage

source,
int tileX,
int tileY,
boolean willBeWritable)

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

tileUpdate

​(

WritableRenderedImage

source,
int tileX,
int tileY,
boolean willBeWritable)

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

---

#### Method Summary

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

============ METHOD DETAIL ==========

- Method Detail

- tileUpdate

```java
void tileUpdate​(
WritableRenderedImage
source,
int tileX,
int tileY,
boolean willBeWritable)
```

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

**Parameters:** source

- the image that owns the tile.
**Parameters:** tileX

- the X index of the tile that is being updated.
**Parameters:** tileY

- the Y index of the tile that is being updated.
**Parameters:** willBeWritable

- If true, the tile will be grabbed for writing;
otherwise it is being released.

Method Detail

- tileUpdate

```java
void tileUpdate​(
WritableRenderedImage
source,
int tileX,
int tileY,
boolean willBeWritable)
```

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

**Parameters:** source

- the image that owns the tile.
**Parameters:** tileX

- the X index of the tile that is being updated.
**Parameters:** tileY

- the Y index of the tile that is being updated.
**Parameters:** willBeWritable

- If true, the tile will be grabbed for writing;
otherwise it is being released.

---

#### Method Detail

tileUpdate

```java
void tileUpdate​(
WritableRenderedImage
source,
int tileX,
int tileY,
boolean willBeWritable)
```

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

**Parameters:** source

- the image that owns the tile.
**Parameters:** tileX

- the X index of the tile that is being updated.
**Parameters:** tileY

- the Y index of the tile that is being updated.
**Parameters:** willBeWritable

- If true, the tile will be grabbed for writing;
otherwise it is being released.

---

#### tileUpdate

void tileUpdate​(

WritableRenderedImage

source,
int tileX,
int tileY,
boolean willBeWritable)

A tile is about to be updated (it is either about to be grabbed
for writing, or it is being released from writing).

---

