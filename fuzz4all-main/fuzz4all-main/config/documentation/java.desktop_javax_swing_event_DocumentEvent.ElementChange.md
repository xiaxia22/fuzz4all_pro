# Interface DocumentEvent.ElementChange

**Source:** `java.desktop\javax\swing\event\DocumentEvent.ElementChange.html`

### Class Description

```java
public static interface
DocumentEvent.ElementChange
```

Describes changes made to a specific element.

**All Known Implementing Classes:** AbstractDocument.ElementEdit

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Element
getElement()

Returns the element represented. This is the element
that was changed.

**Returns:**
- the element

---

#### int getIndex()

Fetches the index within the element represented.
This is the location that children were added
and/or removed.

**Returns:**
- the index >= 0

---

#### Element
[] getChildrenRemoved()

Gets the child elements that were removed from the
given parent element. The element array returned is
sorted in the order that the elements used to lie in
the document, and must be contiguous.

**Returns:**
- the child elements

---

#### Element
[] getChildrenAdded()

Gets the child elements that were added to the given
parent element. The element array returned is in the
order that the elements lie in the document, and must
be contiguous.

**Returns:**
- the child elements

---

### Additional Sections

#### Interface DocumentEvent.ElementChange

**All Known Implementing Classes:** AbstractDocument.ElementEdit

**Enclosing interface:** DocumentEvent

```java
public static interface
DocumentEvent.ElementChange
```

Describes changes made to a specific element.

public static interface

DocumentEvent.ElementChange

Describes changes made to a specific element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Element

[]

getChildrenAdded

()

Gets the child elements that were added to the given
parent element.

Element

[]

getChildrenRemoved

()

Gets the child elements that were removed from the
given parent element.

Element

getElement

()

Returns the element represented.

int

getIndex

()

Fetches the index within the element represented.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Element

[]

getChildrenAdded

()

Gets the child elements that were added to the given
parent element.

Element

[]

getChildrenRemoved

()

Gets the child elements that were removed from the
given parent element.

Element

getElement

()

Returns the element represented.

int

getIndex

()

Fetches the index within the element represented.

---

#### Method Summary

Gets the child elements that were added to the given
parent element.

Gets the child elements that were removed from the
given parent element.

Returns the element represented.

Fetches the index within the element represented.

============ METHOD DETAIL ==========

- Method Detail

- getElement

```java
Element
getElement()
```

Returns the element represented. This is the element
that was changed.

**Returns:** the element

- getIndex

```java
int getIndex()
```

Fetches the index within the element represented.
This is the location that children were added
and/or removed.

**Returns:** the index >= 0

- getChildrenRemoved

```java
Element
[] getChildrenRemoved()
```

Gets the child elements that were removed from the
given parent element. The element array returned is
sorted in the order that the elements used to lie in
the document, and must be contiguous.

**Returns:** the child elements

- getChildrenAdded

```java
Element
[] getChildrenAdded()
```

Gets the child elements that were added to the given
parent element. The element array returned is in the
order that the elements lie in the document, and must
be contiguous.

**Returns:** the child elements

Method Detail

- getElement

```java
Element
getElement()
```

Returns the element represented. This is the element
that was changed.

**Returns:** the element

- getIndex

```java
int getIndex()
```

Fetches the index within the element represented.
This is the location that children were added
and/or removed.

**Returns:** the index >= 0

- getChildrenRemoved

```java
Element
[] getChildrenRemoved()
```

Gets the child elements that were removed from the
given parent element. The element array returned is
sorted in the order that the elements used to lie in
the document, and must be contiguous.

**Returns:** the child elements

- getChildrenAdded

```java
Element
[] getChildrenAdded()
```

Gets the child elements that were added to the given
parent element. The element array returned is in the
order that the elements lie in the document, and must
be contiguous.

**Returns:** the child elements

---

#### Method Detail

getElement

```java
Element
getElement()
```

Returns the element represented. This is the element
that was changed.

**Returns:** the element

---

#### getElement

Element

getElement()

Returns the element represented. This is the element
that was changed.

getIndex

```java
int getIndex()
```

Fetches the index within the element represented.
This is the location that children were added
and/or removed.

**Returns:** the index >= 0

---

#### getIndex

int getIndex()

Fetches the index within the element represented.
This is the location that children were added
and/or removed.

getChildrenRemoved

```java
Element
[] getChildrenRemoved()
```

Gets the child elements that were removed from the
given parent element. The element array returned is
sorted in the order that the elements used to lie in
the document, and must be contiguous.

**Returns:** the child elements

---

#### getChildrenRemoved

Element

[] getChildrenRemoved()

Gets the child elements that were removed from the
given parent element. The element array returned is
sorted in the order that the elements used to lie in
the document, and must be contiguous.

getChildrenAdded

```java
Element
[] getChildrenAdded()
```

Gets the child elements that were added to the given
parent element. The element array returned is in the
order that the elements lie in the document, and must
be contiguous.

**Returns:** the child elements

---

#### getChildrenAdded

Element

[] getChildrenAdded()

Gets the child elements that were added to the given
parent element. The element array returned is in the
order that the elements lie in the document, and must
be contiguous.

---

