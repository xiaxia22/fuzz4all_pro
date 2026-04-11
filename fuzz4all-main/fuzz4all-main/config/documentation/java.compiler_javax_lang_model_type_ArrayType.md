# Interface ArrayType

**Source:** `java.compiler\javax\lang\model\type\ArrayType.html`

### Class Description

```java
public interface
ArrayType

extends
ReferenceType
```

Represents an array type.
A multidimensional array type is represented as an array type
whose component type is also an array type.

**All Superinterfaces:** AnnotatedConstruct

,

ReferenceType

,

TypeMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeMirror
getComponentType()

Returns the component type of this array type.

**Returns:**
- the component type of this array type

---

### Additional Sections

#### Interface ArrayType

**All Superinterfaces:** AnnotatedConstruct

,

ReferenceType

,

TypeMirror

```java
public interface
ArrayType

extends
ReferenceType
```

Represents an array type.
A multidimensional array type is represented as an array type
whose component type is also an array type.

**Since:** 1.6

public interface

ArrayType

extends

ReferenceType

Represents an array type.
A multidimensional array type is represented as an array type
whose component type is also an array type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeMirror

getComponentType

()

Returns the component type of this array type.

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

getComponentType

()

Returns the component type of this array type.

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

Returns the component type of this array type.

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

- getComponentType

```java
TypeMirror
getComponentType()
```

Returns the component type of this array type.

**Returns:** the component type of this array type

Method Detail

- getComponentType

```java
TypeMirror
getComponentType()
```

Returns the component type of this array type.

**Returns:** the component type of this array type

---

#### Method Detail

getComponentType

```java
TypeMirror
getComponentType()
```

Returns the component type of this array type.

**Returns:** the component type of this array type

---

#### getComponentType

TypeMirror

getComponentType()

Returns the component type of this array type.

---

