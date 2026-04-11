# Interface IIOReadProgressListener

**Source:** `java.desktop\javax\imageio\event\IIOReadProgressListener.html`

### Class Description

```java
public interface
IIOReadProgressListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
progress.

This interface receives general indications of decoding
progress (via the

imageProgress

and

thumbnailProgress

methods), and events indicating when
an entire image has been updated (via the

imageStarted

,

imageComplete

,

thumbnailStarted

and

thumbnailComplete

methods). Applications that wish to be informed of pixel updates
as they happen (for example, during progressive decoding), should
provide an

IIOReadUpdateListener

.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void sequenceStarted​(
ImageReader
source,
int minIndex)

Reports that a sequence of read operations is beginning.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- minIndex

- the index of the first image to be read.

---

#### void sequenceComplete​(
ImageReader
source)

Reports that a sequence of read operations has completed.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:**
- source

- the

ImageReader

object calling this method.

---

#### void imageStarted​(
ImageReader
source,
int imageIndex)

Reports that an image read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning an image read
operation.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- imageIndex

- the index of the image being read within its
containing input file or stream.

---

#### void imageProgress​(
ImageReader
source,
float percentageDone)

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### void imageComplete​(
ImageReader
source)

Reports that the current image read operation has completed.
All

ImageReader

implementations are required to
call this method exactly once upon completion of each image
read operation.

**Parameters:**
- source

- the

ImageReader

object calling this
method.

---

#### void thumbnailStarted​(
ImageReader
source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning a thumbnail read
operation.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- imageIndex

- the index of the image being read within its
containing input file or stream.
- thumbnailIndex

- the index of the thumbnail being read.

---

#### void thumbnailProgress​(
ImageReader
source,
float percentageDone)

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

. The semantics are identical to those
of

imageProgress

.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### void thumbnailComplete​(
ImageReader
source)

Reports that a thumbnail read operation has completed. All

ImageReader

implementations are required to call
this method exactly once upon completion of each thumbnail read
operation.

**Parameters:**
- source

- the

ImageReader

object calling this
method.

---

#### void readAborted​(
ImageReader
source)

Reports that a read has been aborted via the reader's

abort

method. No further notifications will be
given.

**Parameters:**
- source

- the

ImageReader

object calling this
method.

---

### Additional Sections

#### Interface IIOReadProgressListener

**All Superinterfaces:** EventListener

```java
public interface
IIOReadProgressListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
progress.

This interface receives general indications of decoding
progress (via the

imageProgress

and

thumbnailProgress

methods), and events indicating when
an entire image has been updated (via the

imageStarted

,

imageComplete

,

thumbnailStarted

and

thumbnailComplete

methods). Applications that wish to be informed of pixel updates
as they happen (for example, during progressive decoding), should
provide an

IIOReadUpdateListener

.

**See Also:** IIOReadUpdateListener

,

ImageReader.addIIOReadProgressListener(javax.imageio.event.IIOReadProgressListener)

,

ImageReader.removeIIOReadProgressListener(javax.imageio.event.IIOReadProgressListener)

public interface

IIOReadProgressListener

extends

EventListener

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
progress.

This interface receives general indications of decoding
progress (via the

imageProgress

and

thumbnailProgress

methods), and events indicating when
an entire image has been updated (via the

imageStarted

,

imageComplete

,

thumbnailStarted

and

thumbnailComplete

methods). Applications that wish to be informed of pixel updates
as they happen (for example, during progressive decoding), should
provide an

IIOReadUpdateListener

.

This interface receives general indications of decoding
progress (via the

imageProgress

and

thumbnailProgress

methods), and events indicating when
an entire image has been updated (via the

imageStarted

,

imageComplete

,

thumbnailStarted

and

thumbnailComplete

methods). Applications that wish to be informed of pixel updates
as they happen (for example, during progressive decoding), should
provide an

IIOReadUpdateListener

.

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

ImageReader

source)

Reports that the current image read operation has completed.

void

imageProgress

​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

void

imageStarted

​(

ImageReader

source,
int imageIndex)

Reports that an image read operation is beginning.

void

readAborted

​(

ImageReader

source)

Reports that a read has been aborted via the reader's

abort

method.

void

sequenceComplete

​(

ImageReader

source)

Reports that a sequence of read operations has completed.

void

sequenceStarted

​(

ImageReader

source,
int minIndex)

Reports that a sequence of read operations is beginning.

void

thumbnailComplete

​(

ImageReader

source)

Reports that a thumbnail read operation has completed.

void

thumbnailProgress

​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

.

void

thumbnailStarted

​(

ImageReader

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail read operation is beginning.

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

ImageReader

source)

Reports that the current image read operation has completed.

void

imageProgress

​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

void

imageStarted

​(

ImageReader

source,
int imageIndex)

Reports that an image read operation is beginning.

void

readAborted

​(

ImageReader

source)

Reports that a read has been aborted via the reader's

abort

method.

void

sequenceComplete

​(

ImageReader

source)

Reports that a sequence of read operations has completed.

void

sequenceStarted

​(

ImageReader

source,
int minIndex)

Reports that a sequence of read operations is beginning.

void

thumbnailComplete

​(

ImageReader

source)

Reports that a thumbnail read operation has completed.

void

thumbnailProgress

​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

.

void

thumbnailStarted

​(

ImageReader

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail read operation is beginning.

---

#### Method Summary

Reports that the current image read operation has completed.

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

Reports that an image read operation is beginning.

Reports that a read has been aborted via the reader's

abort

method.

Reports that a sequence of read operations has completed.

Reports that a sequence of read operations is beginning.

Reports that a thumbnail read operation has completed.

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

.

Reports that a thumbnail read operation is beginning.

============ METHOD DETAIL ==========

- Method Detail

- sequenceStarted

```java
void sequenceStarted​(
ImageReader
source,
int minIndex)
```

Reports that a sequence of read operations is beginning.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** minIndex

- the index of the first image to be read.

- sequenceComplete

```java
void sequenceComplete​(
ImageReader
source)
```

Reports that a sequence of read operations has completed.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.

- imageStarted

```java
void imageStarted​(
ImageReader
source,
int imageIndex)
```

Reports that an image read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning an image read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.

- imageProgress

```java
void imageProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- imageComplete

```java
void imageComplete​(
ImageReader
source)
```

Reports that the current image read operation has completed.
All

ImageReader

implementations are required to
call this method exactly once upon completion of each image
read operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

- thumbnailStarted

```java
void thumbnailStarted​(
ImageReader
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning a thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being read.

- thumbnailProgress

```java
void thumbnailProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

. The semantics are identical to those
of

imageProgress

.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- thumbnailComplete

```java
void thumbnailComplete​(
ImageReader
source)
```

Reports that a thumbnail read operation has completed. All

ImageReader

implementations are required to call
this method exactly once upon completion of each thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

- readAborted

```java
void readAborted​(
ImageReader
source)
```

Reports that a read has been aborted via the reader's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageReader

object calling this
method.

Method Detail

- sequenceStarted

```java
void sequenceStarted​(
ImageReader
source,
int minIndex)
```

Reports that a sequence of read operations is beginning.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** minIndex

- the index of the first image to be read.

- sequenceComplete

```java
void sequenceComplete​(
ImageReader
source)
```

Reports that a sequence of read operations has completed.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.

- imageStarted

```java
void imageStarted​(
ImageReader
source,
int imageIndex)
```

Reports that an image read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning an image read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.

- imageProgress

```java
void imageProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- imageComplete

```java
void imageComplete​(
ImageReader
source)
```

Reports that the current image read operation has completed.
All

ImageReader

implementations are required to
call this method exactly once upon completion of each image
read operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

- thumbnailStarted

```java
void thumbnailStarted​(
ImageReader
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning a thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being read.

- thumbnailProgress

```java
void thumbnailProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

. The semantics are identical to those
of

imageProgress

.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

- thumbnailComplete

```java
void thumbnailComplete​(
ImageReader
source)
```

Reports that a thumbnail read operation has completed. All

ImageReader

implementations are required to call
this method exactly once upon completion of each thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

- readAborted

```java
void readAborted​(
ImageReader
source)
```

Reports that a read has been aborted via the reader's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageReader

object calling this
method.

---

#### Method Detail

sequenceStarted

```java
void sequenceStarted​(
ImageReader
source,
int minIndex)
```

Reports that a sequence of read operations is beginning.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** minIndex

- the index of the first image to be read.

---

#### sequenceStarted

void sequenceStarted​(

ImageReader

source,
int minIndex)

Reports that a sequence of read operations is beginning.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

sequenceComplete

```java
void sequenceComplete​(
ImageReader
source)
```

Reports that a sequence of read operations has completed.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

**Parameters:** source

- the

ImageReader

object calling this method.

---

#### sequenceComplete

void sequenceComplete​(

ImageReader

source)

Reports that a sequence of read operations has completed.

ImageReader

implementations are required to call
this method exactly once from their

readAll(Iterator)

method.

imageStarted

```java
void imageStarted​(
ImageReader
source,
int imageIndex)
```

Reports that an image read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning an image read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.

---

#### imageStarted

void imageStarted​(

ImageReader

source,
int imageIndex)

Reports that an image read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning an image read
operation.

imageProgress

```java
void imageProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### imageProgress

void imageProgress​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

read

call of the associated

ImageReader

.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

The degree of completion is expressed as a percentage
varying from

0.0F

to

100.0F

. The
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

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

Each particular

ImageReader

implementation may
call this method at whatever frequency it desires. A rule of
thumb is to call it around each 5 percent mark.

imageComplete

```java
void imageComplete​(
ImageReader
source)
```

Reports that the current image read operation has completed.
All

ImageReader

implementations are required to
call this method exactly once upon completion of each image
read operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

---

#### imageComplete

void imageComplete​(

ImageReader

source)

Reports that the current image read operation has completed.
All

ImageReader

implementations are required to
call this method exactly once upon completion of each image
read operation.

thumbnailStarted

```java
void thumbnailStarted​(
ImageReader
source,
int imageIndex,
int thumbnailIndex)
```

Reports that a thumbnail read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning a thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** imageIndex

- the index of the image being read within its
containing input file or stream.
**Parameters:** thumbnailIndex

- the index of the thumbnail being read.

---

#### thumbnailStarted

void thumbnailStarted​(

ImageReader

source,
int imageIndex,
int thumbnailIndex)

Reports that a thumbnail read operation is beginning. All

ImageReader

implementations are required to call
this method exactly once when beginning a thumbnail read
operation.

thumbnailProgress

```java
void thumbnailProgress​(
ImageReader
source,
float percentageDone)
```

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

. The semantics are identical to those
of

imageProgress

.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** percentageDone

- the approximate percentage of decoding that
has been completed.

---

#### thumbnailProgress

void thumbnailProgress​(

ImageReader

source,
float percentageDone)

Reports the approximate degree of completion of the current

getThumbnail

call within the associated

ImageReader

. The semantics are identical to those
of

imageProgress

.

thumbnailComplete

```java
void thumbnailComplete​(
ImageReader
source)
```

Reports that a thumbnail read operation has completed. All

ImageReader

implementations are required to call
this method exactly once upon completion of each thumbnail read
operation.

**Parameters:** source

- the

ImageReader

object calling this
method.

---

#### thumbnailComplete

void thumbnailComplete​(

ImageReader

source)

Reports that a thumbnail read operation has completed. All

ImageReader

implementations are required to call
this method exactly once upon completion of each thumbnail read
operation.

readAborted

```java
void readAborted​(
ImageReader
source)
```

Reports that a read has been aborted via the reader's

abort

method. No further notifications will be
given.

**Parameters:** source

- the

ImageReader

object calling this
method.

---

#### readAborted

void readAborted​(

ImageReader

source)

Reports that a read has been aborted via the reader's

abort

method. No further notifications will be
given.

---

