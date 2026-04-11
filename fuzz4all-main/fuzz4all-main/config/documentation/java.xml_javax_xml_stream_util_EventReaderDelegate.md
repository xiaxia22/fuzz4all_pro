# Class EventReaderDelegate

**Source:** `java.xml\javax\xml\stream\util\EventReaderDelegate.html`

### Class Description

```java
public class
EventReaderDelegate

extends
Object

implements
XMLEventReader
```

This is the base class for deriving an XMLEventReader
filter.

This class is designed to sit between an XMLEventReader and an
application's XMLEventReader. By default each method
does nothing but call the corresponding method on the
parent interface.

**All Implemented Interfaces:** Iterator

<

Object

>

,

XMLEventReader

---

### Field Details

*No entries found.*

### Constructor Details

#### public EventReaderDelegate()

Construct an empty filter with no parent.

---

#### public EventReaderDelegate​(
XMLEventReader
reader)

Construct an filter with the specified parent.

**Parameters:**
- reader

- the parent

---

### Method Details

#### public void setParent​(
XMLEventReader
reader)

Set the parent of this instance.

**Parameters:**
- reader

- the new parent

---

#### public
XMLEventReader
getParent()

Get the parent of this instance.

**Returns:**
- the parent or null if none is set

---

### Additional Sections

#### Class EventReaderDelegate

java.lang.Object

- javax.xml.stream.util.EventReaderDelegate

javax.xml.stream.util.EventReaderDelegate

**All Implemented Interfaces:** Iterator

<

Object

>

,

XMLEventReader

```java
public class
EventReaderDelegate

extends
Object

implements
XMLEventReader
```

This is the base class for deriving an XMLEventReader
filter.

This class is designed to sit between an XMLEventReader and an
application's XMLEventReader. By default each method
does nothing but call the corresponding method on the
parent interface.

**Since:** 1.6
**See Also:** XMLEventReader

,

StreamReaderDelegate

public class

EventReaderDelegate

extends

Object

implements

XMLEventReader

This is the base class for deriving an XMLEventReader
filter.

This class is designed to sit between an XMLEventReader and an
application's XMLEventReader. By default each method
does nothing but call the corresponding method on the
parent interface.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EventReaderDelegate

()

Construct an empty filter with no parent.

EventReaderDelegate

​(

XMLEventReader

reader)

Construct an filter with the specified parent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLEventReader

getParent

()

Get the parent of this instance.

void

setParent

​(

XMLEventReader

reader)

Set the parent of this instance.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

- Methods declared in interface javax.xml.stream.

XMLEventReader

close

,

getElementText

,

getProperty

,

hasNext

,

nextEvent

,

nextTag

,

peek

Constructor Summary

Constructors

Constructor

Description

EventReaderDelegate

()

Construct an empty filter with no parent.

EventReaderDelegate

​(

XMLEventReader

reader)

Construct an filter with the specified parent.

---

#### Constructor Summary

Construct an empty filter with no parent.

Construct an filter with the specified parent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLEventReader

getParent

()

Get the parent of this instance.

void

setParent

​(

XMLEventReader

reader)

Set the parent of this instance.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

- Methods declared in interface javax.xml.stream.

XMLEventReader

close

,

getElementText

,

getProperty

,

hasNext

,

nextEvent

,

nextTag

,

peek

---

#### Method Summary

Get the parent of this instance.

Set the parent of this instance.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

---

#### Methods declared in interface java.util. Iterator

Methods declared in interface javax.xml.stream.

XMLEventReader

close

,

getElementText

,

getProperty

,

hasNext

,

nextEvent

,

nextTag

,

peek

---

#### Methods declared in interface javax.xml.stream. XMLEventReader

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EventReaderDelegate

```java
public EventReaderDelegate()
```

Construct an empty filter with no parent.

- EventReaderDelegate

```java
public EventReaderDelegate​(
XMLEventReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
XMLEventReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

- getParent

```java
public
XMLEventReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

Constructor Detail

- EventReaderDelegate

```java
public EventReaderDelegate()
```

Construct an empty filter with no parent.

- EventReaderDelegate

```java
public EventReaderDelegate​(
XMLEventReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

---

#### Constructor Detail

EventReaderDelegate

```java
public EventReaderDelegate()
```

Construct an empty filter with no parent.

---

#### EventReaderDelegate

public EventReaderDelegate()

Construct an empty filter with no parent.

EventReaderDelegate

```java
public EventReaderDelegate​(
XMLEventReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

---

#### EventReaderDelegate

public EventReaderDelegate​(

XMLEventReader

reader)

Construct an filter with the specified parent.

Method Detail

- setParent

```java
public void setParent​(
XMLEventReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

- getParent

```java
public
XMLEventReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

---

#### Method Detail

setParent

```java
public void setParent​(
XMLEventReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

---

#### setParent

public void setParent​(

XMLEventReader

reader)

Set the parent of this instance.

getParent

```java
public
XMLEventReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

---

#### getParent

public

XMLEventReader

getParent()

Get the parent of this instance.

---

