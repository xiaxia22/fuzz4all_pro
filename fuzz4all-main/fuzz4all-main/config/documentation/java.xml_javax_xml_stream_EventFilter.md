# Interface EventFilter

**Source:** `java.xml\javax\xml\stream\EventFilter.html`

### Class Description

```java
public interface
EventFilter
```

This interface declares a simple filter interface that one can
create to filter XMLEventReaders

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean accept​(
XMLEvent
event)

Tests whether this event is part of this stream. This method
will return true if this filter accepts this event and false
otherwise.

**Parameters:**
- event

- the event to test

**Returns:**
- true if this filter accepts this event, false otherwise

---

### Additional Sections

#### Interface EventFilter

```java
public interface
EventFilter
```

This interface declares a simple filter interface that one can
create to filter XMLEventReaders

**Since:** 1.6

public interface

EventFilter

This interface declares a simple filter interface that one can
create to filter XMLEventReaders

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

accept

​(

XMLEvent

event)

Tests whether this event is part of this stream.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

accept

​(

XMLEvent

event)

Tests whether this event is part of this stream.

---

#### Method Summary

Tests whether this event is part of this stream.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
boolean accept​(
XMLEvent
event)
```

Tests whether this event is part of this stream. This method
will return true if this filter accepts this event and false
otherwise.

**Parameters:** event

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

Method Detail

- accept

```java
boolean accept​(
XMLEvent
event)
```

Tests whether this event is part of this stream. This method
will return true if this filter accepts this event and false
otherwise.

**Parameters:** event

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

---

#### Method Detail

accept

```java
boolean accept​(
XMLEvent
event)
```

Tests whether this event is part of this stream. This method
will return true if this filter accepts this event and false
otherwise.

**Parameters:** event

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

---

#### accept

boolean accept​(

XMLEvent

event)

Tests whether this event is part of this stream. This method
will return true if this filter accepts this event and false
otherwise.

---

