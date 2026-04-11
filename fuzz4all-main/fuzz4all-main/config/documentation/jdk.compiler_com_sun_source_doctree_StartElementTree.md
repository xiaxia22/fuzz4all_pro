# Interface StartElementTree

**Source:** `jdk.compiler\com\sun\source\doctree\StartElementTree.html`

### Class Description

```java
public interface
StartElementTree

extends
DocTree
```

A tree node for the start of an HTML element.

< name [attributes] [/]>

**All Superinterfaces:** DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
getName()

Returns the name of the element.

**Returns:**
- the name

---

#### List
<? extends
DocTree
> getAttributes()

Returns any attributes defined by this element.

**Returns:**
- the attributes

---

#### boolean isSelfClosing()

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

**Returns:**
- true if this is a self-closing element

---

### Additional Sections

#### Interface StartElementTree

**All Superinterfaces:** DocTree

```java
public interface
StartElementTree

extends
DocTree
```

A tree node for the start of an HTML element.

< name [attributes] [/]>

**Since:** 1.8

public interface

StartElementTree

extends

DocTree

A tree node for the start of an HTML element.

< name [attributes] [/]>

< name [attributes] [/]>

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

DocTree

>

getAttributes

()

Returns any attributes defined by this element.

Name

getName

()

Returns the name of the element.

boolean

isSelfClosing

()

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.doctree. DocTree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

DocTree

>

getAttributes

()

Returns any attributes defined by this element.

Name

getName

()

Returns the name of the element.

boolean

isSelfClosing

()

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns any attributes defined by this element.

Returns the name of the element.

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
Name
getName()
```

Returns the name of the element.

**Returns:** the name

- getAttributes

```java
List
<? extends
DocTree
> getAttributes()
```

Returns any attributes defined by this element.

**Returns:** the attributes

- isSelfClosing

```java
boolean isSelfClosing()
```

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

**Returns:** true if this is a self-closing element

Method Detail

- getName

```java
Name
getName()
```

Returns the name of the element.

**Returns:** the name

- getAttributes

```java
List
<? extends
DocTree
> getAttributes()
```

Returns any attributes defined by this element.

**Returns:** the attributes

- isSelfClosing

```java
boolean isSelfClosing()
```

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

**Returns:** true if this is a self-closing element

---

#### Method Detail

getName

```java
Name
getName()
```

Returns the name of the element.

**Returns:** the name

---

#### getName

Name

getName()

Returns the name of the element.

getAttributes

```java
List
<? extends
DocTree
> getAttributes()
```

Returns any attributes defined by this element.

**Returns:** the attributes

---

#### getAttributes

List

<? extends

DocTree

> getAttributes()

Returns any attributes defined by this element.

isSelfClosing

```java
boolean isSelfClosing()
```

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

**Returns:** true if this is a self-closing element

---

#### isSelfClosing

boolean isSelfClosing()

Returns true if this is a self-closing element,
as indicated by a "/" before the closing ">".

---

