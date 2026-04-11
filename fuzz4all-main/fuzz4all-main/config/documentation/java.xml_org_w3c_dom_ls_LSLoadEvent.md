# Interface LSLoadEvent

**Source:** `java.xml\org\w3c\dom\ls\LSLoadEvent.html`

### Class Description

```java
public interface
LSLoadEvent

extends
Event
```

This interface represents a load event object that signals the completion
of a document load.

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

#### Document
getNewDocument()

The document that finished loading.

---

#### LSInput
getInput()

The input source that was parsed.

---

### Additional Sections

#### Interface LSLoadEvent

**All Superinterfaces:** Event

```java
public interface
LSLoadEvent

extends
Event
```

This interface represents a load event object that signals the completion
of a document load.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5

public interface

LSLoadEvent

extends

Event

This interface represents a load event object that signals the completion
of a document load.

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

The input source that was parsed.

Document

getNewDocument

()

The document that finished loading.

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

The input source that was parsed.

Document

getNewDocument

()

The document that finished loading.

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

The input source that was parsed.

The document that finished loading.

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

- getNewDocument

```java
Document
getNewDocument()
```

The document that finished loading.

- getInput

```java
LSInput
getInput()
```

The input source that was parsed.

Method Detail

- getNewDocument

```java
Document
getNewDocument()
```

The document that finished loading.

- getInput

```java
LSInput
getInput()
```

The input source that was parsed.

---

#### Method Detail

getNewDocument

```java
Document
getNewDocument()
```

The document that finished loading.

---

#### getNewDocument

Document

getNewDocument()

The document that finished loading.

getInput

```java
LSInput
getInput()
```

The input source that was parsed.

---

#### getInput

LSInput

getInput()

The input source that was parsed.

---

