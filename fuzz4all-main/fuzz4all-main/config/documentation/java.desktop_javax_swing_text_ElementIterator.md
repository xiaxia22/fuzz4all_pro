# Class ElementIterator

**Source:** `java.desktop\javax\swing\text\ElementIterator.html`

### Class Description

```java
public class
ElementIterator

extends
Object

implements
Cloneable
```

ElementIterator, as the name suggests, iterates over the Element
tree. The constructor can be invoked with either Document or an Element
as an argument. If the constructor is invoked with a Document as an
argument then the root of the iteration is the return value of
document.getDefaultRootElement().

The iteration happens in a depth-first manner. In terms of how
boundary conditions are handled:
a) if next() is called before first() or current(), the
root will be returned.
b) next() returns null to indicate the end of the list.
c) previous() returns null when the current element is the root
or next() has returned null.

The ElementIterator does no locking of the Element tree. This means
that it does not track any changes. It is the responsibility of the
user of this class, to ensure that no changes happen during element
iteration.

Simple usage example:

public void iterate() {
ElementIterator it = new ElementIterator(root);
Element elem;
while (true) {
if ((elem = next()) != null) {
// process element
System.out.println("elem: " + elem.getName());
} else {
break;
}
}
}

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ElementIterator​(
Document
document)

Creates a new ElementIterator. The
root element is taken to get the
default root element of the document.

**Parameters:**
- document

- a Document.

---

#### public ElementIterator​(
Element
root)

Creates a new ElementIterator.

**Parameters:**
- root

- the root Element.

---

### Method Details

#### public
Object
clone()

Clones the ElementIterator.

**Overrides:**
- clone

in class

Object

**Returns:**
- a cloned ElementIterator Object.

**See Also:**
- Cloneable

---

#### public
Element
first()

Fetches the first element.

**Returns:**
- an Element.

---

#### public int depth()

Fetches the current depth of element tree.

**Returns:**
- the depth.

---

#### public
Element
current()

Fetches the current Element.

**Returns:**
- element on top of the stack or

null

if the root element is

null

---

#### public
Element
next()

Fetches the next Element. The strategy
used to locate the next element is
a depth-first search.

**Returns:**
- the next element or

null

at the end of the list.

---

#### public
Element
previous()

Fetches the previous Element. If however the current
element is the last element, or the current element
is null, then null is returned.

**Returns:**
- previous

Element

if available

---

### Additional Sections

#### Class ElementIterator

java.lang.Object

- javax.swing.text.ElementIterator

javax.swing.text.ElementIterator

**All Implemented Interfaces:** Cloneable

```java
public class
ElementIterator

extends
Object

implements
Cloneable
```

ElementIterator, as the name suggests, iterates over the Element
tree. The constructor can be invoked with either Document or an Element
as an argument. If the constructor is invoked with a Document as an
argument then the root of the iteration is the return value of
document.getDefaultRootElement().

The iteration happens in a depth-first manner. In terms of how
boundary conditions are handled:
a) if next() is called before first() or current(), the
root will be returned.
b) next() returns null to indicate the end of the list.
c) previous() returns null when the current element is the root
or next() has returned null.

The ElementIterator does no locking of the Element tree. This means
that it does not track any changes. It is the responsibility of the
user of this class, to ensure that no changes happen during element
iteration.

Simple usage example:

public void iterate() {
ElementIterator it = new ElementIterator(root);
Element elem;
while (true) {
if ((elem = next()) != null) {
// process element
System.out.println("elem: " + elem.getName());
} else {
break;
}
}
}

public class

ElementIterator

extends

Object

implements

Cloneable

ElementIterator, as the name suggests, iterates over the Element
tree. The constructor can be invoked with either Document or an Element
as an argument. If the constructor is invoked with a Document as an
argument then the root of the iteration is the return value of
document.getDefaultRootElement().

The iteration happens in a depth-first manner. In terms of how
boundary conditions are handled:
a) if next() is called before first() or current(), the
root will be returned.
b) next() returns null to indicate the end of the list.
c) previous() returns null when the current element is the root
or next() has returned null.

The ElementIterator does no locking of the Element tree. This means
that it does not track any changes. It is the responsibility of the
user of this class, to ensure that no changes happen during element
iteration.

Simple usage example:

public void iterate() {
ElementIterator it = new ElementIterator(root);
Element elem;
while (true) {
if ((elem = next()) != null) {
// process element
System.out.println("elem: " + elem.getName());
} else {
break;
}
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ElementIterator

​(

Document

document)

Creates a new ElementIterator.

ElementIterator

​(

Element

root)

Creates a new ElementIterator.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones the ElementIterator.

Element

current

()

Fetches the current Element.

int

depth

()

Fetches the current depth of element tree.

Element

first

()

Fetches the first element.

Element

next

()

Fetches the next Element.

Element

previous

()

Fetches the previous Element.

- Methods declared in class java.lang.

Object

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

Constructor Summary

Constructors

Constructor

Description

ElementIterator

​(

Document

document)

Creates a new ElementIterator.

ElementIterator

​(

Element

root)

Creates a new ElementIterator.

---

#### Constructor Summary

Creates a new ElementIterator.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clones the ElementIterator.

Element

current

()

Fetches the current Element.

int

depth

()

Fetches the current depth of element tree.

Element

first

()

Fetches the first element.

Element

next

()

Fetches the next Element.

Element

previous

()

Fetches the previous Element.

- Methods declared in class java.lang.

Object

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

#### Method Summary

Clones the ElementIterator.

Fetches the current Element.

Fetches the current depth of element tree.

Fetches the first element.

Fetches the next Element.

Fetches the previous Element.

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementIterator

```java
public ElementIterator​(
Document
document)
```

Creates a new ElementIterator. The
root element is taken to get the
default root element of the document.

**Parameters:** document

- a Document.

- ElementIterator

```java
public ElementIterator​(
Element
root)
```

Creates a new ElementIterator.

**Parameters:** root

- the root Element.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Clones the ElementIterator.

**Overrides:** clone

in class

Object
**Returns:** a cloned ElementIterator Object.
**See Also:** Cloneable

- first

```java
public
Element
first()
```

Fetches the first element.

**Returns:** an Element.

- depth

```java
public int depth()
```

Fetches the current depth of element tree.

**Returns:** the depth.

- current

```java
public
Element
current()
```

Fetches the current Element.

**Returns:** element on top of the stack or

null

if the root element is

null

- next

```java
public
Element
next()
```

Fetches the next Element. The strategy
used to locate the next element is
a depth-first search.

**Returns:** the next element or

null

at the end of the list.

- previous

```java
public
Element
previous()
```

Fetches the previous Element. If however the current
element is the last element, or the current element
is null, then null is returned.

**Returns:** previous

Element

if available

Constructor Detail

- ElementIterator

```java
public ElementIterator​(
Document
document)
```

Creates a new ElementIterator. The
root element is taken to get the
default root element of the document.

**Parameters:** document

- a Document.

- ElementIterator

```java
public ElementIterator​(
Element
root)
```

Creates a new ElementIterator.

**Parameters:** root

- the root Element.

---

#### Constructor Detail

ElementIterator

```java
public ElementIterator​(
Document
document)
```

Creates a new ElementIterator. The
root element is taken to get the
default root element of the document.

**Parameters:** document

- a Document.

---

#### ElementIterator

public ElementIterator​(

Document

document)

Creates a new ElementIterator. The
root element is taken to get the
default root element of the document.

ElementIterator

```java
public ElementIterator​(
Element
root)
```

Creates a new ElementIterator.

**Parameters:** root

- the root Element.

---

#### ElementIterator

public ElementIterator​(

Element

root)

Creates a new ElementIterator.

Method Detail

- clone

```java
public
Object
clone()
```

Clones the ElementIterator.

**Overrides:** clone

in class

Object
**Returns:** a cloned ElementIterator Object.
**See Also:** Cloneable

- first

```java
public
Element
first()
```

Fetches the first element.

**Returns:** an Element.

- depth

```java
public int depth()
```

Fetches the current depth of element tree.

**Returns:** the depth.

- current

```java
public
Element
current()
```

Fetches the current Element.

**Returns:** element on top of the stack or

null

if the root element is

null

- next

```java
public
Element
next()
```

Fetches the next Element. The strategy
used to locate the next element is
a depth-first search.

**Returns:** the next element or

null

at the end of the list.

- previous

```java
public
Element
previous()
```

Fetches the previous Element. If however the current
element is the last element, or the current element
is null, then null is returned.

**Returns:** previous

Element

if available

---

#### Method Detail

clone

```java
public
Object
clone()
```

Clones the ElementIterator.

**Overrides:** clone

in class

Object
**Returns:** a cloned ElementIterator Object.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clones the ElementIterator.

first

```java
public
Element
first()
```

Fetches the first element.

**Returns:** an Element.

---

#### first

public

Element

first()

Fetches the first element.

depth

```java
public int depth()
```

Fetches the current depth of element tree.

**Returns:** the depth.

---

#### depth

public int depth()

Fetches the current depth of element tree.

current

```java
public
Element
current()
```

Fetches the current Element.

**Returns:** element on top of the stack or

null

if the root element is

null

---

#### current

public

Element

current()

Fetches the current Element.

next

```java
public
Element
next()
```

Fetches the next Element. The strategy
used to locate the next element is
a depth-first search.

**Returns:** the next element or

null

at the end of the list.

---

#### next

public

Element

next()

Fetches the next Element. The strategy
used to locate the next element is
a depth-first search.

previous

```java
public
Element
previous()
```

Fetches the previous Element. If however the current
element is the last element, or the current element
is null, then null is returned.

**Returns:** previous

Element

if available

---

#### previous

public

Element

previous()

Fetches the previous Element. If however the current
element is the last element, or the current element
is null, then null is returned.

---

