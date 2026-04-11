# Interface NoType

**Source:** `java.compiler\javax\lang\model\type\NoType.html`

### Class Description

```java
public interface
NoType

extends
TypeMirror
```

A pseudo-type used where no actual type is appropriate.
The kinds of

NoType

are:

- VOID

- corresponds to the keyword

void

.

PACKAGE

- the pseudo-type of a package element.

MODULE

- the pseudo-type of a module element.

NONE

- used in other cases
where no actual type is appropriate; for example, the superclass
of

java.lang.Object

.

**All Superinterfaces:** AnnotatedConstruct

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

#### Interface NoType

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

```java
public interface
NoType

extends
TypeMirror
```

A pseudo-type used where no actual type is appropriate.
The kinds of

NoType

are:

- VOID

- corresponds to the keyword

void

.

PACKAGE

- the pseudo-type of a package element.

MODULE

- the pseudo-type of a module element.

NONE

- used in other cases
where no actual type is appropriate; for example, the superclass
of

java.lang.Object

.

**Since:** 1.6
**See Also:** ExecutableElement.getReturnType()

public interface

NoType

extends

TypeMirror

A pseudo-type used where no actual type is appropriate.
The kinds of

NoType

are:

- VOID

- corresponds to the keyword

void

.

PACKAGE

- the pseudo-type of a package element.

MODULE

- the pseudo-type of a module element.

NONE

- used in other cases
where no actual type is appropriate; for example, the superclass
of

java.lang.Object

.

VOID

- corresponds to the keyword

void

.

PACKAGE

- the pseudo-type of a package element.

MODULE

- the pseudo-type of a module element.

NONE

- used in other cases
where no actual type is appropriate; for example, the superclass
of

java.lang.Object

.

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

