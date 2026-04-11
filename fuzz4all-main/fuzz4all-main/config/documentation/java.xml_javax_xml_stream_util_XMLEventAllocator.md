# Interface XMLEventAllocator

**Source:** `java.xml\javax\xml\stream\util\XMLEventAllocator.html`

### Class Description

```java
public interface
XMLEventAllocator
```

This interface defines a class that allows a user to register
a way to allocate events given an XMLStreamReader. An implementation
is not required to use the XMLEventFactory implementation but this
is recommended. The XMLEventAllocator can be set on an XMLInputFactory
using the property "javax.xml.stream.allocator"

**Since:** 1.6
**See Also:** XMLInputFactory

,

XMLEventFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XMLEventAllocator
newInstance()

This method creates an instance of the XMLEventAllocator. This
allows the XMLInputFactory to allocate a new instance per reader.

---

#### XMLEvent
allocate​(
XMLStreamReader
reader)
throws
XMLStreamException

This method allocates an event given the current
state of the XMLStreamReader. If this XMLEventAllocator
does not have a one-to-one mapping between reader states
and events this method will return null. This method
must not modify the state of the XMLStreamReader.

**Parameters:**
- reader

- The XMLStreamReader to allocate from

**Returns:**
- the event corresponding to the current reader state

**Throws:**
- XMLStreamException

---

#### void allocate​(
XMLStreamReader
reader,

XMLEventConsumer
consumer)
throws
XMLStreamException

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in. This method can be used
to expand or contract reader states into event states.
This method may modify the state of the XMLStreamReader.

**Parameters:**
- reader

- The XMLStreamReader to allocate from
- consumer

- The XMLEventConsumer to add to.

**Throws:**
- XMLStreamException

---

### Additional Sections

#### Interface XMLEventAllocator

```java
public interface
XMLEventAllocator
```

This interface defines a class that allows a user to register
a way to allocate events given an XMLStreamReader. An implementation
is not required to use the XMLEventFactory implementation but this
is recommended. The XMLEventAllocator can be set on an XMLInputFactory
using the property "javax.xml.stream.allocator"

**Since:** 1.6
**See Also:** XMLInputFactory

,

XMLEventFactory

public interface

XMLEventAllocator

This interface defines a class that allows a user to register
a way to allocate events given an XMLStreamReader. An implementation
is not required to use the XMLEventFactory implementation but this
is recommended. The XMLEventAllocator can be set on an XMLInputFactory
using the property "javax.xml.stream.allocator"

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XMLEvent

allocate

​(

XMLStreamReader

reader)

This method allocates an event given the current
state of the XMLStreamReader.

void

allocate

​(

XMLStreamReader

reader,

XMLEventConsumer

consumer)

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in.

XMLEventAllocator

newInstance

()

This method creates an instance of the XMLEventAllocator.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XMLEvent

allocate

​(

XMLStreamReader

reader)

This method allocates an event given the current
state of the XMLStreamReader.

void

allocate

​(

XMLStreamReader

reader,

XMLEventConsumer

consumer)

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in.

XMLEventAllocator

newInstance

()

This method creates an instance of the XMLEventAllocator.

---

#### Method Summary

This method allocates an event given the current
state of the XMLStreamReader.

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in.

This method creates an instance of the XMLEventAllocator.

============ METHOD DETAIL ==========

- Method Detail

- newInstance

```java
XMLEventAllocator
newInstance()
```

This method creates an instance of the XMLEventAllocator. This
allows the XMLInputFactory to allocate a new instance per reader.

- allocate

```java
XMLEvent
allocate​(
XMLStreamReader
reader)
throws
XMLStreamException
```

This method allocates an event given the current
state of the XMLStreamReader. If this XMLEventAllocator
does not have a one-to-one mapping between reader states
and events this method will return null. This method
must not modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Returns:** the event corresponding to the current reader state
**Throws:** XMLStreamException

- allocate

```java
void allocate​(
XMLStreamReader
reader,

XMLEventConsumer
consumer)
throws
XMLStreamException
```

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in. This method can be used
to expand or contract reader states into event states.
This method may modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Parameters:** consumer

- The XMLEventConsumer to add to.
**Throws:** XMLStreamException

Method Detail

- newInstance

```java
XMLEventAllocator
newInstance()
```

This method creates an instance of the XMLEventAllocator. This
allows the XMLInputFactory to allocate a new instance per reader.

- allocate

```java
XMLEvent
allocate​(
XMLStreamReader
reader)
throws
XMLStreamException
```

This method allocates an event given the current
state of the XMLStreamReader. If this XMLEventAllocator
does not have a one-to-one mapping between reader states
and events this method will return null. This method
must not modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Returns:** the event corresponding to the current reader state
**Throws:** XMLStreamException

- allocate

```java
void allocate​(
XMLStreamReader
reader,

XMLEventConsumer
consumer)
throws
XMLStreamException
```

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in. This method can be used
to expand or contract reader states into event states.
This method may modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Parameters:** consumer

- The XMLEventConsumer to add to.
**Throws:** XMLStreamException

---

#### Method Detail

newInstance

```java
XMLEventAllocator
newInstance()
```

This method creates an instance of the XMLEventAllocator. This
allows the XMLInputFactory to allocate a new instance per reader.

---

#### newInstance

XMLEventAllocator

newInstance()

This method creates an instance of the XMLEventAllocator. This
allows the XMLInputFactory to allocate a new instance per reader.

allocate

```java
XMLEvent
allocate​(
XMLStreamReader
reader)
throws
XMLStreamException
```

This method allocates an event given the current
state of the XMLStreamReader. If this XMLEventAllocator
does not have a one-to-one mapping between reader states
and events this method will return null. This method
must not modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Returns:** the event corresponding to the current reader state
**Throws:** XMLStreamException

---

#### allocate

XMLEvent

allocate​(

XMLStreamReader

reader)
throws

XMLStreamException

This method allocates an event given the current
state of the XMLStreamReader. If this XMLEventAllocator
does not have a one-to-one mapping between reader states
and events this method will return null. This method
must not modify the state of the XMLStreamReader.

allocate

```java
void allocate​(
XMLStreamReader
reader,

XMLEventConsumer
consumer)
throws
XMLStreamException
```

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in. This method can be used
to expand or contract reader states into event states.
This method may modify the state of the XMLStreamReader.

**Parameters:** reader

- The XMLStreamReader to allocate from
**Parameters:** consumer

- The XMLEventConsumer to add to.
**Throws:** XMLStreamException

---

#### allocate

void allocate​(

XMLStreamReader

reader,

XMLEventConsumer

consumer)
throws

XMLStreamException

This method allocates an event or set of events
given the current
state of the XMLStreamReader and adds the event
or set of events to the
consumer that was passed in. This method can be used
to expand or contract reader states into event states.
This method may modify the state of the XMLStreamReader.

---

