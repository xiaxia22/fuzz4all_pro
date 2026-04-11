# Interface PrintJobAttributeListener

**Source:** `java.desktop\javax\print\event\PrintJobAttributeListener.html`

### Class Description

```java
public interface
PrintJobAttributeListener
```

Implementations of this interface are attached to a

DocPrintJob

to monitor the status of
attribute changes associated with the print job.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void attributeUpdate​(
PrintJobAttributeEvent
pjae)

Notifies the listener of a change in some print job attributes. One
example of an occurrence triggering this event is if the

JobState

attribute
changed from

PROCESSING

to

PROCESSING_STOPPED

.

**Parameters:**
- pjae

- the event being notified

---

### Additional Sections

#### Interface PrintJobAttributeListener

```java
public interface
PrintJobAttributeListener
```

Implementations of this interface are attached to a

DocPrintJob

to monitor the status of
attribute changes associated with the print job.

public interface

PrintJobAttributeListener

Implementations of this interface are attached to a

DocPrintJob

to monitor the status of
attribute changes associated with the print job.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

attributeUpdate

​(

PrintJobAttributeEvent

pjae)

Notifies the listener of a change in some print job attributes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

attributeUpdate

​(

PrintJobAttributeEvent

pjae)

Notifies the listener of a change in some print job attributes.

---

#### Method Summary

Notifies the listener of a change in some print job attributes.

============ METHOD DETAIL ==========

- Method Detail

- attributeUpdate

```java
void attributeUpdate​(
PrintJobAttributeEvent
pjae)
```

Notifies the listener of a change in some print job attributes. One
example of an occurrence triggering this event is if the

JobState

attribute
changed from

PROCESSING

to

PROCESSING_STOPPED

.

**Parameters:** pjae

- the event being notified

Method Detail

- attributeUpdate

```java
void attributeUpdate​(
PrintJobAttributeEvent
pjae)
```

Notifies the listener of a change in some print job attributes. One
example of an occurrence triggering this event is if the

JobState

attribute
changed from

PROCESSING

to

PROCESSING_STOPPED

.

**Parameters:** pjae

- the event being notified

---

#### Method Detail

attributeUpdate

```java
void attributeUpdate​(
PrintJobAttributeEvent
pjae)
```

Notifies the listener of a change in some print job attributes. One
example of an occurrence triggering this event is if the

JobState

attribute
changed from

PROCESSING

to

PROCESSING_STOPPED

.

**Parameters:** pjae

- the event being notified

---

#### attributeUpdate

void attributeUpdate​(

PrintJobAttributeEvent

pjae)

Notifies the listener of a change in some print job attributes. One
example of an occurrence triggering this event is if the

JobState

attribute
changed from

PROCESSING

to

PROCESSING_STOPPED

.

---

