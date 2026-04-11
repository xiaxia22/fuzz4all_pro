# Interface LSProgressEvent

**Source:** `java.xml\org\w3c\dom\ls\LSProgressEvent.html`

### Class Description

```java
public interface
LSProgressEvent

extends
Event
```

This interface represents a progress event object that notifies the
application about progress as a document is parsed. It extends the

Event

interface defined in [

DOM Level 3 Events

]
.

The units used for the attributes

position

and

totalSize

are not specified and can be implementation and
input dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**All Superinterfaces:** Event

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### LSInput
getInput()

The input source that is being parsed.

---

#### int getPosition()

The current position in the input source, including all external
entities and other resources that have been read.

---

#### int getTotalSize()

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen. A value of

0

is
returned if the total size cannot be determined or estimated.

---

### Additional Sections

#### Interface LSProgressEvent

**All Superinterfaces:** Event

```java
public interface
LSProgressEvent

extends
Event
```

This interface represents a progress event object that notifies the
application about progress as a document is parsed. It extends the

Event

interface defined in [

DOM Level 3 Events

]
.

The units used for the attributes

position

and

totalSize

are not specified and can be implementation and
input dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5

public interface

LSProgressEvent

extends

Event

This interface represents a progress event object that notifies the
application about progress as a document is parsed. It extends the

Event

interface defined in [

DOM Level 3 Events

]
.

The units used for the attributes

position

and

totalSize

are not specified and can be implementation and
input dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

The units used for the attributes

position

and

totalSize

are not specified and can be implementation and
input dependent.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

LSInput

getInput

()

The input source that is being parsed.

int

getPosition

()

The current position in the input source, including all external
entities and other resources that have been read.

int

getTotalSize

()

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen.

- Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

Field Summary

- Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

---

#### Field Summary

Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

---

#### Fields declared in interface org.w3c.dom.events. Event

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

LSInput

getInput

()

The input source that is being parsed.

int

getPosition

()

The current position in the input source, including all external
entities and other resources that have been read.

int

getTotalSize

()

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen.

- Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

---

#### Method Summary

The input source that is being parsed.

The current position in the input source, including all external
entities and other resources that have been read.

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen.

Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

---

#### Methods declared in interface org.w3c.dom.events. Event

============ METHOD DETAIL ==========

- Method Detail

- getInput

```java
LSInput
getInput()
```

The input source that is being parsed.

- getPosition

```java
int getPosition()
```

The current position in the input source, including all external
entities and other resources that have been read.

- getTotalSize

```java
int getTotalSize()
```

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen. A value of

0

is
returned if the total size cannot be determined or estimated.

Method Detail

- getInput

```java
LSInput
getInput()
```

The input source that is being parsed.

- getPosition

```java
int getPosition()
```

The current position in the input source, including all external
entities and other resources that have been read.

- getTotalSize

```java
int getTotalSize()
```

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen. A value of

0

is
returned if the total size cannot be determined or estimated.

---

#### Method Detail

getInput

```java
LSInput
getInput()
```

The input source that is being parsed.

---

#### getInput

LSInput

getInput()

The input source that is being parsed.

getPosition

```java
int getPosition()
```

The current position in the input source, including all external
entities and other resources that have been read.

---

#### getPosition

int getPosition()

The current position in the input source, including all external
entities and other resources that have been read.

getTotalSize

```java
int getTotalSize()
```

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen. A value of

0

is
returned if the total size cannot be determined or estimated.

---

#### getTotalSize

int getTotalSize()

The total size of the document including all external resources, this
number might change as a document is being parsed if references to
more external resources are seen. A value of

0

is
returned if the total size cannot be determined or estimated.

---

