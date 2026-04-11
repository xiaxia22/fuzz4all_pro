# Interface XMLEventConsumer

**Source:** `java.xml\javax\xml\stream\util\XMLEventConsumer.html`

### Class Description

```java
public interface
XMLEventConsumer
```

This interface defines an event consumer interface. The contract of the
of a consumer is to accept the event. This interface can be used to
mark an object as able to receive events. Add may be called several
times in immediate succession so a consumer must be able to cache
events it hasn't processed yet.

**All Known Subinterfaces:** XMLEventWriter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void add​(
XMLEvent
event)
throws
XMLStreamException

This method adds an event to the consumer. Calling this method
invalidates the event parameter. The client application should
discard all references to this event upon calling add.
The behavior of an application that continues to use such references
is undefined.

**Parameters:**
- event

- the event to add, may not be null

**Throws:**
- XMLStreamException

---

### Additional Sections

#### Interface XMLEventConsumer

**All Known Subinterfaces:** XMLEventWriter

```java
public interface
XMLEventConsumer
```

This interface defines an event consumer interface. The contract of the
of a consumer is to accept the event. This interface can be used to
mark an object as able to receive events. Add may be called several
times in immediate succession so a consumer must be able to cache
events it hasn't processed yet.

**Since:** 1.6

public interface

XMLEventConsumer

This interface defines an event consumer interface. The contract of the
of a consumer is to accept the event. This interface can be used to
mark an object as able to receive events. Add may be called several
times in immediate succession so a consumer must be able to cache
events it hasn't processed yet.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

XMLEvent

event)

This method adds an event to the consumer.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

XMLEvent

event)

This method adds an event to the consumer.

---

#### Method Summary

This method adds an event to the consumer.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

This method adds an event to the consumer. Calling this method
invalidates the event parameter. The client application should
discard all references to this event upon calling add.
The behavior of an application that continues to use such references
is undefined.

**Parameters:** event

- the event to add, may not be null
**Throws:** XMLStreamException

Method Detail

- add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

This method adds an event to the consumer. Calling this method
invalidates the event parameter. The client application should
discard all references to this event upon calling add.
The behavior of an application that continues to use such references
is undefined.

**Parameters:** event

- the event to add, may not be null
**Throws:** XMLStreamException

---

#### Method Detail

add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

This method adds an event to the consumer. Calling this method
invalidates the event parameter. The client application should
discard all references to this event upon calling add.
The behavior of an application that continues to use such references
is undefined.

**Parameters:** event

- the event to add, may not be null
**Throws:** XMLStreamException

---

#### add

void add​(

XMLEvent

event)
throws

XMLStreamException

This method adds an event to the consumer. Calling this method
invalidates the event parameter. The client application should
discard all references to this event upon calling add.
The behavior of an application that continues to use such references
is undefined.

---

