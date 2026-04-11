# Interface ParamTree

**Source:** `jdk.compiler\com\sun\source\doctree\ParamTree.html`

### Class Description

```java
public interface
ParamTree

extends
BlockTagTree
```

A tree node for an @param block tag.

@param parameter-name description

**All Superinterfaces:** BlockTagTree

,

DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isTypeParameter()

Returns true if this is documenting a type parameter.

**Returns:**
- true if this is documenting a type parameter

---

#### IdentifierTree
getName()

Returns the name of the parameter.

**Returns:**
- the name of the parameter

---

#### List
<? extends
DocTree
> getDescription()

Returns the description of the parameter.

**Returns:**
- the description

---

### Additional Sections

#### Interface ParamTree

**All Superinterfaces:** BlockTagTree

,

DocTree

```java
public interface
ParamTree

extends
BlockTagTree
```

A tree node for an @param block tag.

@param parameter-name description

**Since:** 1.8

public interface

ParamTree

extends

BlockTagTree

A tree node for an @param block tag.

@param parameter-name description

@param parameter-name description

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

Returns the description of the parameter.

IdentifierTree

getName

()

Returns the name of the parameter.

boolean

isTypeParameter

()

Returns true if this is documenting a type parameter.

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

Returns the description of the parameter.

IdentifierTree

getName

()

Returns the name of the parameter.

boolean

isTypeParameter

()

Returns true if this is documenting a type parameter.

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

Returns the description of the parameter.

Returns the name of the parameter.

Returns true if this is documenting a type parameter.

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

- isTypeParameter

```java
boolean isTypeParameter()
```

Returns true if this is documenting a type parameter.

**Returns:** true if this is documenting a type parameter

- getName

```java
IdentifierTree
getName()
```

Returns the name of the parameter.

**Returns:** the name of the parameter

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the parameter.

**Returns:** the description

Method Detail

- isTypeParameter

```java
boolean isTypeParameter()
```

Returns true if this is documenting a type parameter.

**Returns:** true if this is documenting a type parameter

- getName

```java
IdentifierTree
getName()
```

Returns the name of the parameter.

**Returns:** the name of the parameter

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the parameter.

**Returns:** the description

---

#### Method Detail

isTypeParameter

```java
boolean isTypeParameter()
```

Returns true if this is documenting a type parameter.

**Returns:** true if this is documenting a type parameter

---

#### isTypeParameter

boolean isTypeParameter()

Returns true if this is documenting a type parameter.

getName

```java
IdentifierTree
getName()
```

Returns the name of the parameter.

**Returns:** the name of the parameter

---

#### getName

IdentifierTree

getName()

Returns the name of the parameter.

getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the parameter.

**Returns:** the description

---

#### getDescription

List

<? extends

DocTree

> getDescription()

Returns the description of the parameter.

---

