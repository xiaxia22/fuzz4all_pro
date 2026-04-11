# Interface XMLEventReader

**Source:** `java.xml\javax\xml\stream\XMLEventReader.html`

### Class Description

```java
public interface
XMLEventReader

extends
Iterator
<
Object
>
```

This is the top level interface for parsing XML Events. It provides
the ability to peek at the next event and returns configuration
information through the property interface.

**All Superinterfaces:** Iterator

<

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XMLEvent
nextEvent()
throws
XMLStreamException

Gets the next XMLEvent. The initial event is

StartDocument

.

**Returns:**
- the next XMLEvent

**Throws:**
- XMLStreamException

- if there is an error with the underlying XML.
- NoSuchElementException

- iteration has no more elements.

**See Also:**
- XMLEvent

---

#### boolean hasNext()

Check if there are more events.
Returns true if there are more events and false otherwise.

**Specified by:**
- hasNext

in interface

Iterator

<

Object

>

**Returns:**
- true if the event reader has more events, false otherwise

---

#### XMLEvent
peek()
throws
XMLStreamException

Check the next XMLEvent without reading it from the stream.
Returns null if the stream is at EOF or has no more XMLEvents.
A call to peek() will be equal to the next return of next().

**Returns:**
- the next XMLEvent

**Throws:**
- XMLStreamException

**See Also:**
- XMLEvent

---

#### String
getElementText()
throws
XMLStreamException

Reads the content of a text-only element. Precondition:
the current event is START_ELEMENT. Postcondition:
The current event is the corresponding END_ELEMENT.

**Returns:**
- the text of the element

**Throws:**
- XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

---

#### XMLEvent
nextTag()
throws
XMLStreamException

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached. If anything other than space characters are
encountered, an exception is thrown. This method should
be used when processing element-only content because
the parser is not able to recognize ignorable whitespace if
the DTD is missing or not interpreted.

**Returns:**
- a START_ELEMENT or END_ELEMENT

**Throws:**
- XMLStreamException

- if anything other than space characters are encountered

---

#### Object
getProperty​(
String
name)
throws
IllegalArgumentException

Get the value of a feature/property from the underlying implementation

**Parameters:**
- name

- The name of the property

**Returns:**
- The value of the property

**Throws:**
- IllegalArgumentException

- if the property is not supported

---

#### void close()
throws
XMLStreamException

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:**
- XMLStreamException

- if there are errors freeing associated resources

---

### Additional Sections

#### Interface XMLEventReader

**All Superinterfaces:** Iterator

<

Object

>

**All Known Implementing Classes:** EventReaderDelegate

```java
public interface
XMLEventReader

extends
Iterator
<
Object
>
```

This is the top level interface for parsing XML Events. It provides
the ability to peek at the next event and returns configuration
information through the property interface.

**Since:** 1.6
**See Also:** XMLInputFactory

,

XMLEventWriter

public interface

XMLEventReader

extends

Iterator

<

Object

>

This is the top level interface for parsing XML Events. It provides
the ability to peek at the next event and returns configuration
information through the property interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Frees any resources associated with this Reader.

String

getElementText

()

Reads the content of a text-only element.

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

boolean

hasNext

()

Check if there are more events.

XMLEvent

nextEvent

()

Gets the next XMLEvent.

XMLEvent

nextTag

()

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached.

XMLEvent

peek

()

Check the next XMLEvent without reading it from the stream.

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Frees any resources associated with this Reader.

String

getElementText

()

Reads the content of a text-only element.

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

boolean

hasNext

()

Check if there are more events.

XMLEvent

nextEvent

()

Gets the next XMLEvent.

XMLEvent

nextTag

()

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached.

XMLEvent

peek

()

Check the next XMLEvent without reading it from the stream.

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

---

#### Method Summary

Frees any resources associated with this Reader.

Reads the content of a text-only element.

Get the value of a feature/property from the underlying implementation

Check if there are more events.

Gets the next XMLEvent.

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached.

Check the next XMLEvent without reading it from the stream.

Methods declared in interface java.util.

Iterator

forEachRemaining

,

next

,

remove

---

#### Methods declared in interface java.util. Iterator

============ METHOD DETAIL ==========

- Method Detail

- nextEvent

```java
XMLEvent
nextEvent()
throws
XMLStreamException
```

Gets the next XMLEvent. The initial event is

StartDocument

.

**Returns:** the next XMLEvent
**Throws:** XMLStreamException

- if there is an error with the underlying XML.
**Throws:** NoSuchElementException

- iteration has no more elements.
**See Also:** XMLEvent

- hasNext

```java
boolean hasNext()
```

Check if there are more events.
Returns true if there are more events and false otherwise.

**Specified by:** hasNext

in interface

Iterator

<

Object

>
**Returns:** true if the event reader has more events, false otherwise

- peek

```java
XMLEvent
peek()
throws
XMLStreamException
```

Check the next XMLEvent without reading it from the stream.
Returns null if the stream is at EOF or has no more XMLEvents.
A call to peek() will be equal to the next return of next().

**Returns:** the next XMLEvent
**Throws:** XMLStreamException
**See Also:** XMLEvent

- getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element. Precondition:
the current event is START_ELEMENT. Postcondition:
The current event is the corresponding END_ELEMENT.

**Returns:** the text of the element
**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

- nextTag

```java
XMLEvent
nextTag()
throws
XMLStreamException
```

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached. If anything other than space characters are
encountered, an exception is thrown. This method should
be used when processing element-only content because
the parser is not able to recognize ignorable whitespace if
the DTD is missing or not interpreted.

**Returns:** a START_ELEMENT or END_ELEMENT
**Throws:** XMLStreamException

- if anything other than space characters are encountered

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

Method Detail

- nextEvent

```java
XMLEvent
nextEvent()
throws
XMLStreamException
```

Gets the next XMLEvent. The initial event is

StartDocument

.

**Returns:** the next XMLEvent
**Throws:** XMLStreamException

- if there is an error with the underlying XML.
**Throws:** NoSuchElementException

- iteration has no more elements.
**See Also:** XMLEvent

- hasNext

```java
boolean hasNext()
```

Check if there are more events.
Returns true if there are more events and false otherwise.

**Specified by:** hasNext

in interface

Iterator

<

Object

>
**Returns:** true if the event reader has more events, false otherwise

- peek

```java
XMLEvent
peek()
throws
XMLStreamException
```

Check the next XMLEvent without reading it from the stream.
Returns null if the stream is at EOF or has no more XMLEvents.
A call to peek() will be equal to the next return of next().

**Returns:** the next XMLEvent
**Throws:** XMLStreamException
**See Also:** XMLEvent

- getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element. Precondition:
the current event is START_ELEMENT. Postcondition:
The current event is the corresponding END_ELEMENT.

**Returns:** the text of the element
**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

- nextTag

```java
XMLEvent
nextTag()
throws
XMLStreamException
```

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached. If anything other than space characters are
encountered, an exception is thrown. This method should
be used when processing element-only content because
the parser is not able to recognize ignorable whitespace if
the DTD is missing or not interpreted.

**Returns:** a START_ELEMENT or END_ELEMENT
**Throws:** XMLStreamException

- if anything other than space characters are encountered

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

---

#### Method Detail

nextEvent

```java
XMLEvent
nextEvent()
throws
XMLStreamException
```

Gets the next XMLEvent. The initial event is

StartDocument

.

**Returns:** the next XMLEvent
**Throws:** XMLStreamException

- if there is an error with the underlying XML.
**Throws:** NoSuchElementException

- iteration has no more elements.
**See Also:** XMLEvent

---

#### nextEvent

XMLEvent

nextEvent()
throws

XMLStreamException

Gets the next XMLEvent. The initial event is

StartDocument

.

hasNext

```java
boolean hasNext()
```

Check if there are more events.
Returns true if there are more events and false otherwise.

**Specified by:** hasNext

in interface

Iterator

<

Object

>
**Returns:** true if the event reader has more events, false otherwise

---

#### hasNext

boolean hasNext()

Check if there are more events.
Returns true if there are more events and false otherwise.

peek

```java
XMLEvent
peek()
throws
XMLStreamException
```

Check the next XMLEvent without reading it from the stream.
Returns null if the stream is at EOF or has no more XMLEvents.
A call to peek() will be equal to the next return of next().

**Returns:** the next XMLEvent
**Throws:** XMLStreamException
**See Also:** XMLEvent

---

#### peek

XMLEvent

peek()
throws

XMLStreamException

Check the next XMLEvent without reading it from the stream.
Returns null if the stream is at EOF or has no more XMLEvents.
A call to peek() will be equal to the next return of next().

getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element. Precondition:
the current event is START_ELEMENT. Postcondition:
The current event is the corresponding END_ELEMENT.

**Returns:** the text of the element
**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

---

#### getElementText

String

getElementText()
throws

XMLStreamException

Reads the content of a text-only element. Precondition:
the current event is START_ELEMENT. Postcondition:
The current event is the corresponding END_ELEMENT.

nextTag

```java
XMLEvent
nextTag()
throws
XMLStreamException
```

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached. If anything other than space characters are
encountered, an exception is thrown. This method should
be used when processing element-only content because
the parser is not able to recognize ignorable whitespace if
the DTD is missing or not interpreted.

**Returns:** a START_ELEMENT or END_ELEMENT
**Throws:** XMLStreamException

- if anything other than space characters are encountered

---

#### nextTag

XMLEvent

nextTag()
throws

XMLStreamException

Skips any insignificant space events until a START_ELEMENT or
END_ELEMENT is reached. If anything other than space characters are
encountered, an exception is thrown. This method should
be used when processing element-only content because
the parser is not able to recognize ignorable whitespace if
the DTD is missing or not interpreted.

getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

---

#### getProperty

Object

getProperty​(

String

name)
throws

IllegalArgumentException

Get the value of a feature/property from the underlying implementation

close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

---

#### close

void close()
throws

XMLStreamException

Frees any resources associated with this Reader. This method does not close the
underlying input source.

---

