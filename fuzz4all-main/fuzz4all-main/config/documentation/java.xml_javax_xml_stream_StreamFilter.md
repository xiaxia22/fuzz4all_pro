# Interface StreamFilter

**Source:** `java.xml\javax\xml\stream\StreamFilter.html`

### Class Description

```java
public interface
StreamFilter
```

This interface declares a simple filter interface that one can
create to filter XMLStreamReaders

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean accept​(
XMLStreamReader
reader)

Tests whether the current state is part of this stream. This method
will return true if this filter accepts this event and false otherwise.

The method should not change the state of the reader when accepting
a state.

**Parameters:**
- reader

- the event to test

**Returns:**
- true if this filter accepts this event, false otherwise

---

### Additional Sections

#### Interface StreamFilter

```java
public interface
StreamFilter
```

This interface declares a simple filter interface that one can
create to filter XMLStreamReaders

**Since:** 1.6

public interface

StreamFilter

This interface declares a simple filter interface that one can
create to filter XMLStreamReaders

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

XMLStreamReader

reader)

Tests whether the current state is part of this stream.

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

XMLStreamReader

reader)

Tests whether the current state is part of this stream.

---

#### Method Summary

Tests whether the current state is part of this stream.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
boolean accept​(
XMLStreamReader
reader)
```

Tests whether the current state is part of this stream. This method
will return true if this filter accepts this event and false otherwise.

The method should not change the state of the reader when accepting
a state.

**Parameters:** reader

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

Method Detail

- accept

```java
boolean accept​(
XMLStreamReader
reader)
```

Tests whether the current state is part of this stream. This method
will return true if this filter accepts this event and false otherwise.

The method should not change the state of the reader when accepting
a state.

**Parameters:** reader

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

---

#### Method Detail

accept

```java
boolean accept​(
XMLStreamReader
reader)
```

Tests whether the current state is part of this stream. This method
will return true if this filter accepts this event and false otherwise.

The method should not change the state of the reader when accepting
a state.

**Parameters:** reader

- the event to test
**Returns:** true if this filter accepts this event, false otherwise

---

#### accept

boolean accept​(

XMLStreamReader

reader)

Tests whether the current state is part of this stream. This method
will return true if this filter accepts this event and false otherwise.

The method should not change the state of the reader when accepting
a state.

---

