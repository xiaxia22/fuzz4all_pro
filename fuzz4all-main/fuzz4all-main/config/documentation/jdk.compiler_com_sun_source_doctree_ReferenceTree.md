# Interface ReferenceTree

**Source:** `jdk.compiler\com\sun\source\doctree\ReferenceTree.html`

### Class Description

```java
public interface
ReferenceTree

extends
DocTree
```

A tree node for a reference to a Java language element.

package.class#field
package.class#method(

arg-types

)

**All Superinterfaces:** DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getSignature()

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

**Returns:**
- the signature.

---

### Additional Sections

#### Interface ReferenceTree

**All Superinterfaces:** DocTree

```java
public interface
ReferenceTree

extends
DocTree
```

A tree node for a reference to a Java language element.

package.class#field
package.class#method(

arg-types

)

**Since:** 1.8

public interface

ReferenceTree

extends

DocTree

A tree node for a reference to a Java language element.

package.class#field
package.class#method(

arg-types

)

package.class#field
package.class#method(

arg-types

)

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

String

getSignature

()

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

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

String

getSignature

()

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getSignature

```java
String
getSignature()
```

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

**Returns:** the signature.

Method Detail

- getSignature

```java
String
getSignature()
```

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

**Returns:** the signature.

---

#### Method Detail

getSignature

```java
String
getSignature()
```

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

**Returns:** the signature.

---

#### getSignature

String

getSignature()

Returns the signature of the Java language element being referenced,
as found in

@see

and similar nodes.

---

