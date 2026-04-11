# Interface ThrowsTree

**Source:** `jdk.compiler\com\sun\source\doctree\ThrowsTree.html`

### Class Description

```java
public interface
ThrowsTree

extends
BlockTagTree
```

A tree node for an @exception or @throws block tag.
@exception is a synonym for @throws.

@exception class-name description

@throws class-name description

**All Superinterfaces:** BlockTagTree

,

DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ReferenceTree
getExceptionName()

Returns the name of the exception being documented.

**Returns:**
- the name of the exception

---

#### List
<? extends
DocTree
> getDescription()

Returns a description of the reasons why the
exception may be thrown.

**Returns:**
- the description

---

### Additional Sections

#### Interface ThrowsTree

**All Superinterfaces:** BlockTagTree

,

DocTree

```java
public interface
ThrowsTree

extends
BlockTagTree
```

A tree node for an @exception or @throws block tag.
@exception is a synonym for @throws.

@exception class-name description

@throws class-name description

**Since:** 1.8

public interface

ThrowsTree

extends

BlockTagTree

A tree node for an @exception or @throws block tag.
@exception is a synonym for @throws.

@exception class-name description

@throws class-name description

@exception class-name description

@throws class-name description

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

getDescription

()

Returns a description of the reasons why the
exception may be thrown.

ReferenceTree

getExceptionName

()

Returns the name of the exception being documented.

- Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

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

getDescription

()

Returns a description of the reasons why the
exception may be thrown.

ReferenceTree

getExceptionName

()

Returns the name of the exception being documented.

- Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns a description of the reasons why the
exception may be thrown.

Returns the name of the exception being documented.

Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

---

#### Methods declared in interface com.sun.source.doctree. BlockTagTree

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getExceptionName

```java
ReferenceTree
getExceptionName()
```

Returns the name of the exception being documented.

**Returns:** the name of the exception

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the reasons why the
exception may be thrown.

**Returns:** the description

Method Detail

- getExceptionName

```java
ReferenceTree
getExceptionName()
```

Returns the name of the exception being documented.

**Returns:** the name of the exception

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the reasons why the
exception may be thrown.

**Returns:** the description

---

#### Method Detail

getExceptionName

```java
ReferenceTree
getExceptionName()
```

Returns the name of the exception being documented.

**Returns:** the name of the exception

---

#### getExceptionName

ReferenceTree

getExceptionName()

Returns the name of the exception being documented.

getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the reasons why the
exception may be thrown.

**Returns:** the description

---

#### getDescription

List

<? extends

DocTree

> getDescription()

Returns a description of the reasons why the
exception may be thrown.

---

