# Interface ErrorType

**Source:** `java.compiler\javax\lang\model\type\ErrorType.html`

### Class Description

```java
public interface
ErrorType

extends
DeclaredType
```

Represents a class or interface type that cannot be properly modeled.
This may be the result of a processing error,
such as a missing class file or erroneous source code.
Most queries for
information derived from such a type (such as its members or its
supertype) will not, in general, return meaningful results.

**All Superinterfaces:** AnnotatedConstruct

,

DeclaredType

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

*No entries found.*

### Additional Sections

#### Interface ErrorType

**All Superinterfaces:** AnnotatedConstruct

,

DeclaredType

,

ReferenceType

,

TypeMirror

```java
public interface
ErrorType

extends
DeclaredType
```

Represents a class or interface type that cannot be properly modeled.
This may be the result of a processing error,
such as a missing class file or erroneous source code.
Most queries for
information derived from such a type (such as its members or its
supertype) will not, in general, return meaningful results.

**Since:** 1.6

public interface

ErrorType

extends

DeclaredType

Represents a class or interface type that cannot be properly modeled.
This may be the result of a processing error,
such as a missing class file or erroneous source code.
Most queries for
information derived from such a type (such as its members or its
supertype) will not, in general, return meaningful results.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

DeclaredType

asElement

,

getEnclosingType

,

getTypeArguments

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

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

DeclaredType

asElement

,

getEnclosingType

,

getTypeArguments

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

DeclaredType

asElement

,

getEnclosingType

,

getTypeArguments

---

#### Methods declared in interface javax.lang.model.type. DeclaredType

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

