# Interface DocumentEvent

**Source:** `java.desktop\javax\swing\event\DocumentEvent.html`

### Class Description

```java
public interface
DocumentEvent
```

Interface for document change notifications. This provides
detailed information to Document observers about how the
Document changed. It provides high level information such
as type of change and where it occurred, as well as the more
detailed structural changes (What Elements were inserted and
removed).

**All Known Implementing Classes:** AbstractDocument.DefaultDocumentEvent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getOffset()

Returns the offset within the document of the start
of the change.

**Returns:**
- the offset >= 0

---

#### int getLength()

Returns the length of the change.

**Returns:**
- the length >= 0

---

#### Document
getDocument()

Gets the document that sourced the change event.

**Returns:**
- the document

---

#### DocumentEvent.EventType
getType()

Gets the type of event.

**Returns:**
- the type

---

#### DocumentEvent.ElementChange
getChange​(
Element
elem)

Gets the change information for the given element.
The change information describes what elements were
added and removed and the location. If there were
no changes, null is returned.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

**Parameters:**
- elem

- the element

**Returns:**
- the change information, or null if the
element was not modified

---

### Additional Sections

#### Interface DocumentEvent

**All Known Implementing Classes:** AbstractDocument.DefaultDocumentEvent

```java
public interface
DocumentEvent
```

Interface for document change notifications. This provides
detailed information to Document observers about how the
Document changed. It provides high level information such
as type of change and where it occurred, as well as the more
detailed structural changes (What Elements were inserted and
removed).

**See Also:** Document

,

DocumentListener

public interface

DocumentEvent

Interface for document change notifications. This provides
detailed information to Document observers about how the
Document changed. It provides high level information such
as type of change and where it occurred, as well as the more
detailed structural changes (What Elements were inserted and
removed).

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

DocumentEvent.ElementChange

Describes changes made to a specific element.

static class

DocumentEvent.EventType

Enumeration for document event types

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocumentEvent.ElementChange

getChange

​(

Element

elem)

Gets the change information for the given element.

Document

getDocument

()

Gets the document that sourced the change event.

int

getLength

()

Returns the length of the change.

int

getOffset

()

Returns the offset within the document of the start
of the change.

DocumentEvent.EventType

getType

()

Gets the type of event.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

DocumentEvent.ElementChange

Describes changes made to a specific element.

static class

DocumentEvent.EventType

Enumeration for document event types

---

#### Nested Class Summary

Describes changes made to a specific element.

Enumeration for document event types

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DocumentEvent.ElementChange

getChange

​(

Element

elem)

Gets the change information for the given element.

Document

getDocument

()

Gets the document that sourced the change event.

int

getLength

()

Returns the length of the change.

int

getOffset

()

Returns the offset within the document of the start
of the change.

DocumentEvent.EventType

getType

()

Gets the type of event.

---

#### Method Summary

Gets the change information for the given element.

Gets the document that sourced the change event.

Returns the length of the change.

Returns the offset within the document of the start
of the change.

Gets the type of event.

============ METHOD DETAIL ==========

- Method Detail

- getOffset

```java
int getOffset()
```

Returns the offset within the document of the start
of the change.

**Returns:** the offset >= 0

- getLength

```java
int getLength()
```

Returns the length of the change.

**Returns:** the length >= 0

- getDocument

```java
Document
getDocument()
```

Gets the document that sourced the change event.

**Returns:** the document

- getType

```java
DocumentEvent.EventType
getType()
```

Gets the type of event.

**Returns:** the type

- getChange

```java
DocumentEvent.ElementChange
getChange​(
Element
elem)
```

Gets the change information for the given element.
The change information describes what elements were
added and removed and the location. If there were
no changes, null is returned.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

**Parameters:** elem

- the element
**Returns:** the change information, or null if the
element was not modified

Method Detail

- getOffset

```java
int getOffset()
```

Returns the offset within the document of the start
of the change.

**Returns:** the offset >= 0

- getLength

```java
int getLength()
```

Returns the length of the change.

**Returns:** the length >= 0

- getDocument

```java
Document
getDocument()
```

Gets the document that sourced the change event.

**Returns:** the document

- getType

```java
DocumentEvent.EventType
getType()
```

Gets the type of event.

**Returns:** the type

- getChange

```java
DocumentEvent.ElementChange
getChange​(
Element
elem)
```

Gets the change information for the given element.
The change information describes what elements were
added and removed and the location. If there were
no changes, null is returned.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

**Parameters:** elem

- the element
**Returns:** the change information, or null if the
element was not modified

---

#### Method Detail

getOffset

```java
int getOffset()
```

Returns the offset within the document of the start
of the change.

**Returns:** the offset >= 0

---

#### getOffset

int getOffset()

Returns the offset within the document of the start
of the change.

getLength

```java
int getLength()
```

Returns the length of the change.

**Returns:** the length >= 0

---

#### getLength

int getLength()

Returns the length of the change.

getDocument

```java
Document
getDocument()
```

Gets the document that sourced the change event.

**Returns:** the document

---

#### getDocument

Document

getDocument()

Gets the document that sourced the change event.

getType

```java
DocumentEvent.EventType
getType()
```

Gets the type of event.

**Returns:** the type

---

#### getType

DocumentEvent.EventType

getType()

Gets the type of event.

getChange

```java
DocumentEvent.ElementChange
getChange​(
Element
elem)
```

Gets the change information for the given element.
The change information describes what elements were
added and removed and the location. If there were
no changes, null is returned.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

**Parameters:** elem

- the element
**Returns:** the change information, or null if the
element was not modified

---

#### getChange

DocumentEvent.ElementChange

getChange​(

Element

elem)

Gets the change information for the given element.
The change information describes what elements were
added and removed and the location. If there were
no changes, null is returned.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

This method is for observers to discover the structural
changes that were made. This means that only elements
that existed prior to the mutation (and still exist after
the mutation) need to have ElementChange records.
The changes made available need not be recursive.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

For example, if the an element is removed from it's
parent, this method should report that the parent
changed and provide an ElementChange implementation
that describes the change to the parent. If the
child element removed had children, these elements
do not need to be reported as removed.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

If an child element is insert into a parent element,
the parent element should report a change. If the
child element also had elements inserted into it
(grandchildren to the parent) these elements need
not report change.

---

