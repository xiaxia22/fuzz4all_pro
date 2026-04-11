# Interface WildcardType

**Source:** `java.compiler\javax\lang\model\type\WildcardType.html`

### Class Description

```java
public interface
WildcardType

extends
TypeMirror
```

Represents a wildcard type argument.
Examples include:

```java
?
? extends Number
? super T
```

A wildcard may have its upper bound explicitly set by an

extends

clause, its lower bound explicitly set by a

super

clause, or neither (but not both).

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeMirror
getExtendsBound()

Returns the upper bound of this wildcard.
If no upper bound is explicitly declared,

null

is returned.

**Returns:**
- the upper bound of this wildcard

---

#### TypeMirror
getSuperBound()

Returns the lower bound of this wildcard.
If no lower bound is explicitly declared,

null

is returned.

**Returns:**
- the lower bound of this wildcard

---

### Additional Sections

#### Interface WildcardType

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

```java
public interface
WildcardType

extends
TypeMirror
```

Represents a wildcard type argument.
Examples include:

```java
?
? extends Number
? super T
```

A wildcard may have its upper bound explicitly set by an

extends

clause, its lower bound explicitly set by a

super

clause, or neither (but not both).

**Since:** 1.6

public interface

WildcardType

extends

TypeMirror

Represents a wildcard type argument.
Examples include:

```java
?
? extends Number
? super T
```

A wildcard may have its upper bound explicitly set by an

extends

clause, its lower bound explicitly set by a

super

clause, or neither (but not both).

?
? extends Number
? super T

A wildcard may have its upper bound explicitly set by an

extends

clause, its lower bound explicitly set by a

super

clause, or neither (but not both).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeMirror

getExtendsBound

()

Returns the upper bound of this wildcard.

TypeMirror

getSuperBound

()

Returns the lower bound of this wildcard.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeMirror

getExtendsBound

()

Returns the upper bound of this wildcard.

TypeMirror

getSuperBound

()

Returns the lower bound of this wildcard.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Method Summary

Returns the upper bound of this wildcard.

Returns the lower bound of this wildcard.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Methods declared in interface javax.lang.model.type. TypeMirror

============ METHOD DETAIL ==========

- Method Detail

- getExtendsBound

```java
TypeMirror
getExtendsBound()
```

Returns the upper bound of this wildcard.
If no upper bound is explicitly declared,

null

is returned.

**Returns:** the upper bound of this wildcard

- getSuperBound

```java
TypeMirror
getSuperBound()
```

Returns the lower bound of this wildcard.
If no lower bound is explicitly declared,

null

is returned.

**Returns:** the lower bound of this wildcard

Method Detail

- getExtendsBound

```java
TypeMirror
getExtendsBound()
```

Returns the upper bound of this wildcard.
If no upper bound is explicitly declared,

null

is returned.

**Returns:** the upper bound of this wildcard

- getSuperBound

```java
TypeMirror
getSuperBound()
```

Returns the lower bound of this wildcard.
If no lower bound is explicitly declared,

null

is returned.

**Returns:** the lower bound of this wildcard

---

#### Method Detail

getExtendsBound

```java
TypeMirror
getExtendsBound()
```

Returns the upper bound of this wildcard.
If no upper bound is explicitly declared,

null

is returned.

**Returns:** the upper bound of this wildcard

---

#### getExtendsBound

TypeMirror

getExtendsBound()

Returns the upper bound of this wildcard.
If no upper bound is explicitly declared,

null

is returned.

getSuperBound

```java
TypeMirror
getSuperBound()
```

Returns the lower bound of this wildcard.
If no lower bound is explicitly declared,

null

is returned.

**Returns:** the lower bound of this wildcard

---

#### getSuperBound

TypeMirror

getSuperBound()

Returns the lower bound of this wildcard.
If no lower bound is explicitly declared,

null

is returned.

---

