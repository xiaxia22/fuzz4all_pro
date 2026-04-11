# Interface IIOWriteProgressListener

**Source:** `java.desktop\javax\imageio\event\IIOWriteProgressListener.html`

### Class Description

```java
public interface
IIOWriteProgressListener

extends
EventListener
```

An interface used by

ImageWriter

implementations to notify
callers of their image writing methods of progress.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void imageStarted​(
ImageWriter
source,
int imageIndex)

Reports that an image write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning an image write
operation.

**Parameters:**
- source

- the

ImageWriter

object calling this
method.
- imageIndex

- the index of the image being written within
its containing input file or stream.

---

#### void imageProgress​(
ImageWriter
source,
float percentageDone)

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:**
- source

- the

ImageWriter

object calling this method.
- percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### void imageComplete​(
ImageWriter
source)

Reports that the image write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each image write
operation.

**Parameters:**
- source

- the

ImageWriter

object calling this method.

---

#### void thumbnailStarted​(
ImageWriter
source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning a thumbnail write
operation.

**Parameters:**
- source

- the

ImageWrite

object calling this method.
- imageIndex

- the index of the image being written within its
containing input file or stream.
- thumbnailIndex

- the index of the thumbnail being written.

---

#### void thumbnailProgress​(
ImageWriter
source,
float percentageDone)

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.
The semantics are identical to those of

imageProgress

.

**Parameters:**
- source

- the

ImageWriter

object calling this
method.
- percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### void thumbnailComplete​(
ImageWriter
source)

Reports that a thumbnail write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each thumbnail
write operation.

**Parameters:**
- source

- the

ImageWriter

object calling this
method.

---

#### void writeAborted​(
ImageWriter
source)

Reports that a write has been aborted via the writer's

abort

method. No further notifications will be
given.

**Parameters:**
- source

- the

ImageWriter

object calling this
method.

---

### Additional Sections

#### Interface IIOWriteProgressListener

**All Superinterfaces:** EventListener

```java
public interface
IIOWriteProgressListener

extends
EventListener
```

An interface used by

ImageWriter

implementations to notify
callers of their image writing methods of progress.

**See Also:** ImageWriter.write(javax.imageio.metadata.IIOMetadata, javax.imageio.IIOImage, javax.imageio.ImageWriteParam)

public interface

IIOWriteProgressListener

extends

EventListener

An interface used by

ImageWriter

implementations to notify
callers of their image writing methods of progress.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageComplete

​(

ImageWriter

source)

Reports that the image write operation has completed.

void

imageProgress

​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

void

imageStarted

​(

ImageWriter

source,
int imageIndex)

Reports that an image write operation is beginning.

void

thumbnailComplete

​(

ImageWriter

source)

Reports that a thumbnail write operation has completed.

void

thumbnailProgress

​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.

void

thumbnailStarted

​(

ImageWriter

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail write operation is beginning.

void

writeAborted

​(

ImageWriter

source)

Reports that a write has been aborted via the writer's

abort

method.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageComplete

​(

ImageWriter

source)

Reports that the image write operation has completed.

void

imageProgress

​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

void

imageStarted

​(

ImageWriter

source,
int imageIndex)

Reports that an image write operation is beginning.

void

thumbnailComplete

​(

ImageWriter

source)

Reports that a thumbnail write operation has completed.

void

thumbnailProgress

​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.

void

thumbnailStarted

​(

ImageWriter

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail write operation is beginning.

void

writeAborted

​(

ImageWriter

source)

Reports that a write has been aborted via the writer's

abort

method.

---

#### Method Summary

Reports that the image write operation has completed.

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

Reports that an image write operation is beginning.

Reports that a thumbnail write operation has completed.

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.

Reports that a thumbnail write operation is beginning.

Reports that a write has been aborted via the writer's

abort

method.

============ METHOD DETAIL ==========

- Method Detail

- imageStarted

```java
void imageStarted​(
ImageWriter
source,
int imageIndex)
```

Reports that an image write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning an image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** imageIndex

- the index of the image being written within
its containing input file or stream.

- imageProgress

```java
void imageProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- imageComplete

```java
void imageComplete​(
ImageWriter
source)
```

Reports that the image write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this method.

- thumbnailStarted

```java
void thumbnailStarted​(
ImageWriter
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning a thumbnail write
operation.

**Parameters:** source

- the

ImageWrite

object calling this method.
**Parameters:** imageIndex

- the index of the image being written within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being written.

- thumbnailProgress

```java
void thumbnailProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.
The semantics are identical to those of

imageProgress

.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- thumbnailComplete

```java
void thumbnailComplete​(
ImageWriter
source)
```

Reports that a thumbnail write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each thumbnail
write operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.

- writeAborted

```java
void writeAborted​(
ImageWriter
source)
```

Reports that a write has been aborted via the writer's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageWriter

object calling this
method.

Method Detail

- imageStarted

```java
void imageStarted​(
ImageWriter
source,
int imageIndex)
```

Reports that an image write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning an image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** imageIndex

- the index of the image being written within
its containing input file or stream.

- imageProgress

```java
void imageProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- imageComplete

```java
void imageComplete​(
ImageWriter
source)
```

Reports that the image write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this method.

- thumbnailStarted

```java
void thumbnailStarted​(
ImageWriter
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning a thumbnail write
operation.

**Parameters:** source

- the

ImageWrite

object calling this method.
**Parameters:** imageIndex

- the index of the image being written within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being written.

- thumbnailProgress

```java
void thumbnailProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.
The semantics are identical to those of

imageProgress

.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- thumbnailComplete

```java
void thumbnailComplete​(
ImageWriter
source)
```

Reports that a thumbnail write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each thumbnail
write operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.

- writeAborted

```java
void writeAborted​(
ImageWriter
source)
```

Reports that a write has been aborted via the writer's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageWriter

object calling this
method.

---

#### Method Detail

imageStarted

```java
void imageStarted​(
ImageWriter
source,
int imageIndex)
```

Reports that an image write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning an image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** imageIndex

- the index of the image being written within
its containing input file or stream.

---

#### imageStarted

void imageStarted​(

ImageWriter

source,
int imageIndex)

Reports that an image write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning an image write
operation.

imageProgress

```java
void imageProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### imageProgress

void imageProgress​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current

write

call within the associated

ImageWriter

.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

The degree of completion is expressed as an index
indicating which image is being written, and a percentage
varying from

0.0F

to

100.0F

indicating how much of the current image has been output. The
percentage should ideally be calculated in terms of the
remaining time to completion, but it is usually more practical
to use a more well-defined metric such as pixels decoded or
portion of input stream consumed. In any case, a sequence of
calls to this method during a given read operation should
supply a monotonically increasing sequence of percentage
values. It is not necessary to supply the exact values

0

and

100

, as these may be inferred
by the callee from other methods.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

Each particular

ImageWriter

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

imageComplete

```java
void imageComplete​(
ImageWriter
source)
```

Reports that the image write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each image write
operation.

**Parameters:** source

- the

ImageWriter

object calling this method.

---

#### imageComplete

void imageComplete​(

ImageWriter

source)

Reports that the image write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each image write
operation.

thumbnailStarted

```java
void thumbnailStarted​(
ImageWriter
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning a thumbnail write
operation.

**Parameters:** source

- the

ImageWrite

object calling this method.
**Parameters:** imageIndex

- the index of the image being written within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being written.

---

#### thumbnailStarted

void thumbnailStarted​(

ImageWriter

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail write operation is beginning. All

ImageWriter

implementations are required to call
this method exactly once when beginning a thumbnail write
operation.

thumbnailProgress

```java
void thumbnailProgress​(
ImageWriter
source,
float percentageDone)
```

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.
The semantics are identical to those of

imageProgress

.

**Parameters:** source

- the

ImageWriter

object calling this
method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### thumbnailProgress

void thumbnailProgress​(

ImageWriter

source,
float percentageDone)

Reports the approximate degree of completion of the current
thumbnail write within the associated

ImageWriter

.
The semantics are identical to those of

imageProgress

.

thumbnailComplete

```java
void thumbnailComplete​(
ImageWriter
source)
```

Reports that a thumbnail write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each thumbnail
write operation.

**Parameters:** source

- the

ImageWriter

object calling this
method.

---

#### thumbnailComplete

void thumbnailComplete​(

ImageWriter

source)

Reports that a thumbnail write operation has completed. All

ImageWriter

implementations are required to call
this method exactly once upon completion of each thumbnail
write operation.

writeAborted

```java
void writeAborted​(
ImageWriter
source)
```

Reports that a write has been aborted via the writer's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageWriter

object calling this
method.

---

#### writeAborted

void writeAborted​(

ImageWriter

source)

Reports that a write has been aborted via the writer's

abort

method. No further notifications will be
given.

---

