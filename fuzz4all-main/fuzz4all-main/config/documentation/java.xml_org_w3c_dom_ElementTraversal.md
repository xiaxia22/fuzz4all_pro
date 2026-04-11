# Interface ElementTraversal

**Source:** `java.xml\org\w3c\dom\ElementTraversal.html`

### Class Description

```java
public interface
ElementTraversal
```

The

ElementTraversal

interface is a set of read-only attributes
which allow an author to easily navigate between elements in a document.

In conforming implementations of Element Traversal, all objects that
implement

Element

must also implement the

ElementTraversal

interface. Four of the methods,

getFirstElementChild()

,

getLastElementChild()

,

getPreviousElementSibling()

, and

getNextElementSibling()

,
each provides a live reference to another element with the defined
relationship to the current element, if the related element exists. The
fifth method,

getChildElementCount()

, exposes the number of child
elements of an element, for preprocessing before navigation.

**Since:** 9
**See Also:** Element Traversal Specification

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Element
getFirstElementChild()

Returns a reference to the first child node of the element which is of
the

Element

type.

**Returns:**
- a reference to an element child,

null

if the element has
no child of the

Element

type.

---

#### Element
getLastElementChild()

Returns a reference to the last child node of the element which is of
the

Element

type.

**Returns:**
- a reference to an element child,

null

if the element has
no child of the

Element

type.

---

#### Element
getPreviousElementSibling()

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

**Returns:**
- a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes before this one.

---

#### Element
getNextElementSibling()

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

**Returns:**
- a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes after this one.

---

#### int getChildElementCount()

Returns the current number of child nodes of the element which are of
the

Element

type.

**Returns:**
- the number of element children, or

0

if the element has
no element children.

---

### Additional Sections

#### Interface ElementTraversal

```java
public interface
ElementTraversal
```

The

ElementTraversal

interface is a set of read-only attributes
which allow an author to easily navigate between elements in a document.

In conforming implementations of Element Traversal, all objects that
implement

Element

must also implement the

ElementTraversal

interface. Four of the methods,

getFirstElementChild()

,

getLastElementChild()

,

getPreviousElementSibling()

, and

getNextElementSibling()

,
each provides a live reference to another element with the defined
relationship to the current element, if the related element exists. The
fifth method,

getChildElementCount()

, exposes the number of child
elements of an element, for preprocessing before navigation.

**Since:** 9
**See Also:** Element Traversal Specification

public interface

ElementTraversal

The

ElementTraversal

interface is a set of read-only attributes
which allow an author to easily navigate between elements in a document.

In conforming implementations of Element Traversal, all objects that
implement

Element

must also implement the

ElementTraversal

interface. Four of the methods,

getFirstElementChild()

,

getLastElementChild()

,

getPreviousElementSibling()

, and

getNextElementSibling()

,
each provides a live reference to another element with the defined
relationship to the current element, if the related element exists. The
fifth method,

getChildElementCount()

, exposes the number of child
elements of an element, for preprocessing before navigation.

In conforming implementations of Element Traversal, all objects that
implement

Element

must also implement the

ElementTraversal

interface. Four of the methods,

getFirstElementChild()

,

getLastElementChild()

,

getPreviousElementSibling()

, and

getNextElementSibling()

,
each provides a live reference to another element with the defined
relationship to the current element, if the related element exists. The
fifth method,

getChildElementCount()

, exposes the number of child
elements of an element, for preprocessing before navigation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getChildElementCount

()

Returns the current number of child nodes of the element which are of
the

Element

type.

Element

getFirstElementChild

()

Returns a reference to the first child node of the element which is of
the

Element

type.

Element

getLastElementChild

()

Returns a reference to the last child node of the element which is of
the

Element

type.

Element

getNextElementSibling

()

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

Element

getPreviousElementSibling

()

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getChildElementCount

()

Returns the current number of child nodes of the element which are of
the

Element

type.

Element

getFirstElementChild

()

Returns a reference to the first child node of the element which is of
the

Element

type.

Element

getLastElementChild

()

Returns a reference to the last child node of the element which is of
the

Element

type.

Element

getNextElementSibling

()

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

Element

getPreviousElementSibling

()

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

---

#### Method Summary

Returns the current number of child nodes of the element which are of
the

Element

type.

Returns a reference to the first child node of the element which is of
the

Element

type.

Returns a reference to the last child node of the element which is of
the

Element

type.

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

============ METHOD DETAIL ==========

- Method Detail

- getFirstElementChild

```java
Element
getFirstElementChild()
```

Returns a reference to the first child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

- getLastElementChild

```java
Element
getLastElementChild()
```

Returns a reference to the last child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

- getPreviousElementSibling

```java
Element
getPreviousElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes before this one.

- getNextElementSibling

```java
Element
getNextElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes after this one.

- getChildElementCount

```java
int getChildElementCount()
```

Returns the current number of child nodes of the element which are of
the

Element

type.

**Returns:** the number of element children, or

0

if the element has
no element children.

Method Detail

- getFirstElementChild

```java
Element
getFirstElementChild()
```

Returns a reference to the first child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

- getLastElementChild

```java
Element
getLastElementChild()
```

Returns a reference to the last child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

- getPreviousElementSibling

```java
Element
getPreviousElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes before this one.

- getNextElementSibling

```java
Element
getNextElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes after this one.

- getChildElementCount

```java
int getChildElementCount()
```

Returns the current number of child nodes of the element which are of
the

Element

type.

**Returns:** the number of element children, or

0

if the element has
no element children.

---

#### Method Detail

getFirstElementChild

```java
Element
getFirstElementChild()
```

Returns a reference to the first child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

---

#### getFirstElementChild

Element

getFirstElementChild()

Returns a reference to the first child node of the element which is of
the

Element

type.

getLastElementChild

```java
Element
getLastElementChild()
```

Returns a reference to the last child node of the element which is of
the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no child of the

Element

type.

---

#### getLastElementChild

Element

getLastElementChild()

Returns a reference to the last child node of the element which is of
the

Element

type.

getPreviousElementSibling

```java
Element
getPreviousElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes before this one.

---

#### getPreviousElementSibling

Element

getPreviousElementSibling()

Returns a reference to the sibling node of the element which most immediately
precedes the element in document order, and which is of the

Element

type.

getNextElementSibling

```java
Element
getNextElementSibling()
```

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

**Returns:** a reference to an element child,

null

if the element has
no sibling node of the

Element

type that comes after this one.

---

#### getNextElementSibling

Element

getNextElementSibling()

Returns a reference to the sibling node of the element which most immediately
follows the element in document order, and which is of the

Element

type.

getChildElementCount

```java
int getChildElementCount()
```

Returns the current number of child nodes of the element which are of
the

Element

type.

**Returns:** the number of element children, or

0

if the element has
no element children.

---

#### getChildElementCount

int getChildElementCount()

Returns the current number of child nodes of the element which are of
the

Element

type.

---

