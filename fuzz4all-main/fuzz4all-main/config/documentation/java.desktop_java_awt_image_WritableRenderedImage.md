# Interface WritableRenderedImage

**Source:** `java.desktop\java\awt\image\WritableRenderedImage.html`

### Class Description

```java
public interface
WritableRenderedImage

extends
RenderedImage
```

WritableRenderedImage is a common interface for objects which
contain or can produce image data in the form of Rasters and
which can be modified and/or written over. The image
data may be stored/produced as a single tile or a regular array
of tiles.

WritableRenderedImage provides notification to other interested
objects when a tile is checked out for writing (via the
getWritableTile method) and when the last writer of a particular
tile relinquishes its access (via a call to releaseWritableTile).
Additionally, it allows any caller to determine whether any tiles
are currently checked out (via hasTileWriters), and to obtain a
list of such tiles (via getWritableTileIndices, in the form of a Vector
of Point objects).

Objects wishing to be notified of changes in tile writability must
implement the TileObserver interface, and are added by a
call to addTileObserver. Multiple calls to
addTileObserver for the same object will result in multiple
notifications. An existing observer may reduce its notifications
by calling removeTileObserver; if the observer had no
notifications the operation is a no-op.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

**All Superinterfaces:** RenderedImage

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addTileObserver​(
TileObserver
to)

Adds an observer. If the observer is already present,
it will receive multiple notifications.

**Parameters:**
- to

- the specified

TileObserver

---

#### void removeTileObserver​(
TileObserver
to)

Removes an observer. If the observer was not registered,
nothing happens. If the observer was registered for multiple
notifications, it will now be registered for one fewer.

**Parameters:**
- to

- the specified

TileObserver

---

#### WritableRaster
getWritableTile​(int tileX,
int tileY)

Checks out a tile for writing.

The WritableRenderedImage is responsible for notifying all
of its TileObservers when a tile goes from having
no writers to having one writer.

**Parameters:**
- tileX

- the X index of the tile.
- tileY

- the Y index of the tile.

**Returns:**
- a writable tile.

---

#### void releaseWritableTile​(int tileX,
int tileY)

Relinquishes the right to write to a tile. If the caller
continues to write to the tile, the results are undefined.
Calls to this method should only appear in matching pairs
with calls to getWritableTile; any other use will lead
to undefined results.

The WritableRenderedImage is responsible for notifying all of
its TileObservers when a tile goes from having one writer
to having no writers.

**Parameters:**
- tileX

- the X index of the tile.
- tileY

- the Y index of the tile.

---

#### boolean isTileWritable​(int tileX,
int tileY)

Returns whether a tile is currently checked out for writing.

**Parameters:**
- tileX

- the X index of the tile.
- tileY

- the Y index of the tile.

**Returns:**
- true

if specified tile is checked out
for writing;

false

otherwise.

---

#### Point
[] getWritableTileIndices()

Returns an array of Point objects indicating which tiles
are checked out for writing. Returns null if none are
checked out.

**Returns:**
- an array containing the locations of tiles that are
checked out for writing.

---

#### boolean hasTileWriters()

Returns whether any tile is checked out for writing.
Semantically equivalent to (getWritableTileIndices() != null).

**Returns:**
- true

if any tiles are checked out for
writing;

false

otherwise.

---

#### void setData​(
Raster
r)

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.
The operation is clipped to the bounds of the WritableRenderedImage.

**Parameters:**
- r

- the specified

Raster

---

### Additional Sections

#### Interface WritableRenderedImage

**All Superinterfaces:** RenderedImage

**All Known Implementing Classes:** BufferedImage

```java
public interface
WritableRenderedImage

extends
RenderedImage
```

WritableRenderedImage is a common interface for objects which
contain or can produce image data in the form of Rasters and
which can be modified and/or written over. The image
data may be stored/produced as a single tile or a regular array
of tiles.

WritableRenderedImage provides notification to other interested
objects when a tile is checked out for writing (via the
getWritableTile method) and when the last writer of a particular
tile relinquishes its access (via a call to releaseWritableTile).
Additionally, it allows any caller to determine whether any tiles
are currently checked out (via hasTileWriters), and to obtain a
list of such tiles (via getWritableTileIndices, in the form of a Vector
of Point objects).

Objects wishing to be notified of changes in tile writability must
implement the TileObserver interface, and are added by a
call to addTileObserver. Multiple calls to
addTileObserver for the same object will result in multiple
notifications. An existing observer may reduce its notifications
by calling removeTileObserver; if the observer had no
notifications the operation is a no-op.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

public interface

WritableRenderedImage

extends

RenderedImage

WritableRenderedImage is a common interface for objects which
contain or can produce image data in the form of Rasters and
which can be modified and/or written over. The image
data may be stored/produced as a single tile or a regular array
of tiles.

WritableRenderedImage provides notification to other interested
objects when a tile is checked out for writing (via the
getWritableTile method) and when the last writer of a particular
tile relinquishes its access (via a call to releaseWritableTile).
Additionally, it allows any caller to determine whether any tiles
are currently checked out (via hasTileWriters), and to obtain a
list of such tiles (via getWritableTileIndices, in the form of a Vector
of Point objects).

Objects wishing to be notified of changes in tile writability must
implement the TileObserver interface, and are added by a
call to addTileObserver. Multiple calls to
addTileObserver for the same object will result in multiple
notifications. An existing observer may reduce its notifications
by calling removeTileObserver; if the observer had no
notifications the operation is a no-op.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

WritableRenderedImage provides notification to other interested
objects when a tile is checked out for writing (via the
getWritableTile method) and when the last writer of a particular
tile relinquishes its access (via a call to releaseWritableTile).
Additionally, it allows any caller to determine whether any tiles
are currently checked out (via hasTileWriters), and to obtain a
list of such tiles (via getWritableTileIndices, in the form of a Vector
of Point objects).

Objects wishing to be notified of changes in tile writability must
implement the TileObserver interface, and are added by a
call to addTileObserver. Multiple calls to
addTileObserver for the same object will result in multiple
notifications. An existing observer may reduce its notifications
by calling removeTileObserver; if the observer had no
notifications the operation is a no-op.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

Objects wishing to be notified of changes in tile writability must
implement the TileObserver interface, and are added by a
call to addTileObserver. Multiple calls to
addTileObserver for the same object will result in multiple
notifications. An existing observer may reduce its notifications
by calling removeTileObserver; if the observer had no
notifications the operation is a no-op.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

It is necessary for a WritableRenderedImage to ensure that
notifications occur only when the first writer acquires a tile and
the last writer releases it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addTileObserver

​(

TileObserver

to)

Adds an observer.

WritableRaster

getWritableTile

​(int tileX,
int tileY)

Checks out a tile for writing.

Point

[]

getWritableTileIndices

()

Returns an array of Point objects indicating which tiles
are checked out for writing.

boolean

hasTileWriters

()

Returns whether any tile is checked out for writing.

boolean

isTileWritable

​(int tileX,
int tileY)

Returns whether a tile is currently checked out for writing.

void

releaseWritableTile

​(int tileX,
int tileY)

Relinquishes the right to write to a tile.

void

removeTileObserver

​(

TileObserver

to)

Removes an observer.

void

setData

​(

Raster

r)

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.

- Methods declared in interface java.awt.image.

RenderedImage

copyData

,

getColorModel

,

getData

,

getData

,

getHeight

,

getMinTileX

,

getMinTileY

,

getMinX

,

getMinY

,

getNumXTiles

,

getNumYTiles

,

getProperty

,

getPropertyNames

,

getSampleModel

,

getSources

,

getTile

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getWidth

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addTileObserver

​(

TileObserver

to)

Adds an observer.

WritableRaster

getWritableTile

​(int tileX,
int tileY)

Checks out a tile for writing.

Point

[]

getWritableTileIndices

()

Returns an array of Point objects indicating which tiles
are checked out for writing.

boolean

hasTileWriters

()

Returns whether any tile is checked out for writing.

boolean

isTileWritable

​(int tileX,
int tileY)

Returns whether a tile is currently checked out for writing.

void

releaseWritableTile

​(int tileX,
int tileY)

Relinquishes the right to write to a tile.

void

removeTileObserver

​(

TileObserver

to)

Removes an observer.

void

setData

​(

Raster

r)

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.

- Methods declared in interface java.awt.image.

RenderedImage

copyData

,

getColorModel

,

getData

,

getData

,

getHeight

,

getMinTileX

,

getMinTileY

,

getMinX

,

getMinY

,

getNumXTiles

,

getNumYTiles

,

getProperty

,

getPropertyNames

,

getSampleModel

,

getSources

,

getTile

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getWidth

---

#### Method Summary

Adds an observer.

Checks out a tile for writing.

Returns an array of Point objects indicating which tiles
are checked out for writing.

Returns whether any tile is checked out for writing.

Returns whether a tile is currently checked out for writing.

Relinquishes the right to write to a tile.

Removes an observer.

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.

Methods declared in interface java.awt.image.

RenderedImage

copyData

,

getColorModel

,

getData

,

getData

,

getHeight

,

getMinTileX

,

getMinTileY

,

getMinX

,

getMinY

,

getNumXTiles

,

getNumYTiles

,

getProperty

,

getPropertyNames

,

getSampleModel

,

getSources

,

getTile

,

getTileGridXOffset

,

getTileGridYOffset

,

getTileHeight

,

getTileWidth

,

getWidth

---

#### Methods declared in interface java.awt.image. RenderedImage

============ METHOD DETAIL ==========

- Method Detail

- addTileObserver

```java
void addTileObserver​(
TileObserver
to)
```

Adds an observer. If the observer is already present,
it will receive multiple notifications.

**Parameters:** to

- the specified

TileObserver

- removeTileObserver

```java
void removeTileObserver​(
TileObserver
to)
```

Removes an observer. If the observer was not registered,
nothing happens. If the observer was registered for multiple
notifications, it will now be registered for one fewer.

**Parameters:** to

- the specified

TileObserver

- getWritableTile

```java
WritableRaster
getWritableTile​(int tileX,
int tileY)
```

Checks out a tile for writing.

The WritableRenderedImage is responsible for notifying all
of its TileObservers when a tile goes from having
no writers to having one writer.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** a writable tile.

- releaseWritableTile

```java
void releaseWritableTile​(int tileX,
int tileY)
```

Relinquishes the right to write to a tile. If the caller
continues to write to the tile, the results are undefined.
Calls to this method should only appear in matching pairs
with calls to getWritableTile; any other use will lead
to undefined results.

The WritableRenderedImage is responsible for notifying all of
its TileObservers when a tile goes from having one writer
to having no writers.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.

- isTileWritable

```java
boolean isTileWritable​(int tileX,
int tileY)
```

Returns whether a tile is currently checked out for writing.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** true

if specified tile is checked out
for writing;

false

otherwise.

- getWritableTileIndices

```java
Point
[] getWritableTileIndices()
```

Returns an array of Point objects indicating which tiles
are checked out for writing. Returns null if none are
checked out.

**Returns:** an array containing the locations of tiles that are
checked out for writing.

- hasTileWriters

```java
boolean hasTileWriters()
```

Returns whether any tile is checked out for writing.
Semantically equivalent to (getWritableTileIndices() != null).

**Returns:** true

if any tiles are checked out for
writing;

false

otherwise.

- setData

```java
void setData​(
Raster
r)
```

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.
The operation is clipped to the bounds of the WritableRenderedImage.

**Parameters:** r

- the specified

Raster

Method Detail

- addTileObserver

```java
void addTileObserver​(
TileObserver
to)
```

Adds an observer. If the observer is already present,
it will receive multiple notifications.

**Parameters:** to

- the specified

TileObserver

- removeTileObserver

```java
void removeTileObserver​(
TileObserver
to)
```

Removes an observer. If the observer was not registered,
nothing happens. If the observer was registered for multiple
notifications, it will now be registered for one fewer.

**Parameters:** to

- the specified

TileObserver

- getWritableTile

```java
WritableRaster
getWritableTile​(int tileX,
int tileY)
```

Checks out a tile for writing.

The WritableRenderedImage is responsible for notifying all
of its TileObservers when a tile goes from having
no writers to having one writer.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** a writable tile.

- releaseWritableTile

```java
void releaseWritableTile​(int tileX,
int tileY)
```

Relinquishes the right to write to a tile. If the caller
continues to write to the tile, the results are undefined.
Calls to this method should only appear in matching pairs
with calls to getWritableTile; any other use will lead
to undefined results.

The WritableRenderedImage is responsible for notifying all of
its TileObservers when a tile goes from having one writer
to having no writers.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.

- isTileWritable

```java
boolean isTileWritable​(int tileX,
int tileY)
```

Returns whether a tile is currently checked out for writing.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** true

if specified tile is checked out
for writing;

false

otherwise.

- getWritableTileIndices

```java
Point
[] getWritableTileIndices()
```

Returns an array of Point objects indicating which tiles
are checked out for writing. Returns null if none are
checked out.

**Returns:** an array containing the locations of tiles that are
checked out for writing.

- hasTileWriters

```java
boolean hasTileWriters()
```

Returns whether any tile is checked out for writing.
Semantically equivalent to (getWritableTileIndices() != null).

**Returns:** true

if any tiles are checked out for
writing;

false

otherwise.

- setData

```java
void setData​(
Raster
r)
```

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.
The operation is clipped to the bounds of the WritableRenderedImage.

**Parameters:** r

- the specified

Raster

---

#### Method Detail

addTileObserver

```java
void addTileObserver​(
TileObserver
to)
```

Adds an observer. If the observer is already present,
it will receive multiple notifications.

**Parameters:** to

- the specified

TileObserver

---

#### addTileObserver

void addTileObserver​(

TileObserver

to)

Adds an observer. If the observer is already present,
it will receive multiple notifications.

removeTileObserver

```java
void removeTileObserver​(
TileObserver
to)
```

Removes an observer. If the observer was not registered,
nothing happens. If the observer was registered for multiple
notifications, it will now be registered for one fewer.

**Parameters:** to

- the specified

TileObserver

---

#### removeTileObserver

void removeTileObserver​(

TileObserver

to)

Removes an observer. If the observer was not registered,
nothing happens. If the observer was registered for multiple
notifications, it will now be registered for one fewer.

getWritableTile

```java
WritableRaster
getWritableTile​(int tileX,
int tileY)
```

Checks out a tile for writing.

The WritableRenderedImage is responsible for notifying all
of its TileObservers when a tile goes from having
no writers to having one writer.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** a writable tile.

---

#### getWritableTile

WritableRaster

getWritableTile​(int tileX,
int tileY)

Checks out a tile for writing.

The WritableRenderedImage is responsible for notifying all
of its TileObservers when a tile goes from having
no writers to having one writer.

releaseWritableTile

```java
void releaseWritableTile​(int tileX,
int tileY)
```

Relinquishes the right to write to a tile. If the caller
continues to write to the tile, the results are undefined.
Calls to this method should only appear in matching pairs
with calls to getWritableTile; any other use will lead
to undefined results.

The WritableRenderedImage is responsible for notifying all of
its TileObservers when a tile goes from having one writer
to having no writers.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.

---

#### releaseWritableTile

void releaseWritableTile​(int tileX,
int tileY)

Relinquishes the right to write to a tile. If the caller
continues to write to the tile, the results are undefined.
Calls to this method should only appear in matching pairs
with calls to getWritableTile; any other use will lead
to undefined results.

The WritableRenderedImage is responsible for notifying all of
its TileObservers when a tile goes from having one writer
to having no writers.

isTileWritable

```java
boolean isTileWritable​(int tileX,
int tileY)
```

Returns whether a tile is currently checked out for writing.

**Parameters:** tileX

- the X index of the tile.
**Parameters:** tileY

- the Y index of the tile.
**Returns:** true

if specified tile is checked out
for writing;

false

otherwise.

---

#### isTileWritable

boolean isTileWritable​(int tileX,
int tileY)

Returns whether a tile is currently checked out for writing.

getWritableTileIndices

```java
Point
[] getWritableTileIndices()
```

Returns an array of Point objects indicating which tiles
are checked out for writing. Returns null if none are
checked out.

**Returns:** an array containing the locations of tiles that are
checked out for writing.

---

#### getWritableTileIndices

Point

[] getWritableTileIndices()

Returns an array of Point objects indicating which tiles
are checked out for writing. Returns null if none are
checked out.

hasTileWriters

```java
boolean hasTileWriters()
```

Returns whether any tile is checked out for writing.
Semantically equivalent to (getWritableTileIndices() != null).

**Returns:** true

if any tiles are checked out for
writing;

false

otherwise.

---

#### hasTileWriters

boolean hasTileWriters()

Returns whether any tile is checked out for writing.
Semantically equivalent to (getWritableTileIndices() != null).

setData

```java
void setData​(
Raster
r)
```

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.
The operation is clipped to the bounds of the WritableRenderedImage.

**Parameters:** r

- the specified

Raster

---

#### setData

void setData​(

Raster

r)

Sets a rect of the image to the contents of the Raster r, which is
assumed to be in the same coordinate space as the WritableRenderedImage.
The operation is clipped to the bounds of the WritableRenderedImage.

---

